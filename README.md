# DTL-NeddSite
DTL-NeddSite: Deep Transfer Learning Based Architecture for Lysine Neddylation Sites Prediction
# Datasets Description
We collected 1715 experimentally verified lysine neddylation sites on 934 human proteins[1,2,3]. After the CD-HIT clustering with a sequence identity of 40%, we obtained 715 protein clusters which contained 1236 neddylation sites as positives and 25,442 lysine non-modified sites. From these non-modified sites, we randomly selected 1236 sites as the negatives. All the positives and negatives are stored in the folder "Data".  
[1]A. M. Vogl et al., "Global site-specific neddylation profiling reveals that NEDDylated cofilin regulates actin dynamics," Nat Struct Mol Biol, vol. 27, no. 2, pp. 210-220, Feb 2020.  
[2]	S. Lobato-Gil et al., "Proteome-wide identification of NEDD8 modification sites reveals distinct proteomes for canonical and atypical NEDDylation," Cell Rep, vol. 34, no. 3, p. 108635, Jan 19 2021.  
[3]	A. S. Yavuz, N. B. Sözer, and O. U. Sezerman, "Prediction of neddylation sites from protein sequences and sequence-derived properties," BMC Bioinformatics, vol. 16, no. 18, p. S9, 2015/12/09 2015.
# Programming language
Python 3.8 and above
# Environment configuration information
The python package names with version numbers are stored in tensorflow.yaml.
# Using DTL-NeddSite to predict neddylation sites
Step 1: Locate the /Predict/Scripts/predict.py file and set the working directory to its parent directory "Scripts".  
Step 2: Specify the fasta file and execute the predict.py file for making predictions. Example command: python predict.py --file test.fasta  
Step 3: Once the execution is complete, the prediction results will be output to the folder "Results".
# Contact
Please contact us if you need any help: lileime@hotmail.com
