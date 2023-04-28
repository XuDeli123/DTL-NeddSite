# DTL-NeddSite
DTL-NeddSite: Deep Transfer Learning Based Architecture for Lysine Neddylation Sites Prediction
# Datasets Description
We collected 1715 experimentally verified lysine neddylation sites on 934 human proteins from the literature. After the CD-HIT clustering with a sequence identity of 40%, we obtained 715 protein clusters which contained 1236 neddylation sites as positives and 25,442 lysine non-modified sites. From these non-modified sites, we randomly selected 1236 sites as the negatives.
# Programming language
Python 3.8 and above
# Environment configuration information
All python packages and their corresponding version numbers required by the project are stored in tensorflow.yaml
# Using DTL-NeddSite to predict neddylation sites
Step 1: Locate the predict.py file and set the working directory to its parent directory.  
Step 2: Specify the fasta file and execute the predict.py file for making predictions. Example command: `python predict.py --file test.fasta`  
Step 3: Once the execution is complete, the prediction results will be saved in the Results folder.
# Contact
Please contact us if you need any help: lileime@hotmail.com
