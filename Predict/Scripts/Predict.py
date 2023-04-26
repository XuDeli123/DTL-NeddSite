import os.path
import re
import sys
import time
import numpy as np
import tensorflow as tf
import argparse
from tensorflow.keras import layers, optimizers
import pandas as pd
from tensorflow.keras.models import Model
from Bio import SeqIO
from tensorflow.keras.models import load_model

def file_check(filename):
    if not os.path.exists(filename):
        print("file does not exist")
        sys.exit()
    else:
        with open(filename, "r") as handle:
            fasta = SeqIO.parse(handle, "fasta")
            return any(fasta)

def get_dataset(filepath):
    try:
        predict_id = []
        predict_seq = []
        for index, record in enumerate(SeqIO.parse(filepath, 'fasta')):
            re_search = re.search(r"\|[-A-Za-z0-9]+\|", record.name)
            if re_search:
                name = re_search.group()[1:-1]
            else:
                name = record.name
            sequences = 'X' * 20 + str(record.seq) + 'X' * 20
            for location, seq in enumerate(sequences):
                if seq == 'K':
                    predict_id.append(name + '*' + str(location + 1 - 20))
                    predict_seq.append(sequences[location - 20:location + 21])
        csvfile = pd.DataFrame({'Protein': predict_id, 'Sequence': predict_seq})

        return csvfile
    except:
        return pd.DataFrame()

def One_hot(dataframe):
    AA = 'ACDEFGHIKLMNPQRSTVWYX'
    encodings = []
    sequences = list(dataframe['Sequence'])
    for i in sequences:
        sequence = re.sub('[^ACDEFGHIKLMNPQRSTVWYX]', 'X', ''.join(i).upper())
        code = []
        for aa in sequence:
            singlecode = []
            for aa1 in AA:
                tag = 1 if aa == aa1 else 0
                singlecode.append(tag)
            code.append(singlecode)
        encodings.append(code)
    return np.array(encodings).astype(np.float64)

def predict(dataframe, model_path, save_path):
    x = One_hot(dataframe)
    sign = list(dataframe['Protein'])
    name = []
    position = []
    for s in sign:
        reversal = s[::-1]
        site = reversal.index('*')
        name.append(reversal[site + 1:][::-1])
        position.append(reversal[:site][::-1])
    folds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    predict_score = np.zeros((len(x), len(folds)))
    predict_result = []
    predict_confidence = []
    for fold in folds:
        modelName = 'model' + str(fold) + '.h5'
        modelPath = os.path.join(model_path, modelName)
        network = load_model(modelPath)
        predict_score[:, fold - 1:fold] = network.predict(x)

    predict_average_score = np.average(predict_score, axis=1)
    predict_average_score = np.around(predict_average_score, 3)
    for i in predict_average_score:
        if i >= 0.85:
            predict_result.append(1)
            predict_confidence.append('Very High confidence')
        elif i >= 0.7:
            predict_result.append(2)
            predict_confidence.append('High confidence')
        elif i >= 0.5:
            predict_result.append(3)
            predict_confidence.append('Medium confidence')
        else:
            predict_result.append(0)
            predict_confidence.append('No')
    saveCsv = pd.DataFrame({'Protein': name, 'Position': position, 'Sequence': dataframe['Sequence'],
                            'Prediction score': predict_average_score, 'Prediction category': predict_confidence})
    saveCsv.to_csv(save_path, index=None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.",
                                     description="ResSUMO: A Deep Learning Architecture Based on Residual Structure "
                                                 "for Lysine SUMOylation Sites Prediction")
    parser.add_argument("--file", required=True, help="input fasta format file")

    parent_dir = os.path.abspath(os.path.dirname(os.getcwd()))
    args = parser.parse_args()
    filecheck = file_check(args.file)
    if filecheck:
        dataset = get_dataset(args.file)
        net_path = os.path.join(parent_dir, 'Models')
        res_path = os.path.join(parent_dir, 'Results')
        result_path = os.path.join(res_path, str(time.time()).split('.')[0] + '.csv')
        predict(dataset, net_path, result_path)
    else:
        print("The input file format is incorrect, it must be in fasta format")
        sys.exit()
    print("The prediction results are stored in ", result_path)