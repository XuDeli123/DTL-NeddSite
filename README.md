# DTL-NeddSite
DTL-NeddSite: Deep Transfer Learning Based Architecture for Lysine Neddylation Sites Prediction
# Abstract
Neddylation, as a reversible post-translational modification (PTM), plays a role in various cellular processes. Defects in neddylation are related to human diseases. Detecting neddylation sites is necessary for revealing the mechanisms of protein neddylation. As identifying such sites through experimental methods is expensive and time-consuming, it is essential to develop in silico methods to predict neddylation sites. In this study, we constructed a few classifiers integrating various algorithms and encoding features. However, they gave low performances (AUC≈0.767) due mainly to the limited number (~1000) of identified neddylation sites. The large number (>100,000) of other lysine PTM sites inspired us to employ a deep-transfer learning (DTL) strategy for performance improvement. We constructed the predictor dubbed DTL-NeddSite, which adopted the DTL-based convolution neural network with the One-Hot encoding approach. Specifically, the massive lysine PTM sites were used to build the source model, followed by fine-tuning as the target model using neddylation sites. DTL-NeddSite compared favourably to the corresponding model without the DTL strategy in cross-validation and independent test. For instance, the AUC value increased to 0.818. Contrary to a general DTL model that combines frozen and unfrozen layers, all the layers in DTL-NeddSite were unfrozen to re-train. We expect the DTL strategy to be widely used in newly discovered modification types with limited known sites. 
# Dataset Description
We collected 1715 experimentally verified lysine neddylation sites on 934 human proteins[1,2,3]. After the CD-HIT clustering with a sequence identity of 40%, we obtained 715 protein clusters which contained 1236 neddylation sites as positives and 25,442 lysine non-modified sites. From these non-modified sites, we randomly selected 1236 sites as the negatives. All the positives and negatives are stored in the folder "Data".    
  
References:  
[1]A. M. Vogl et al., "Global site-specific neddylation profiling reveals that NEDDylated cofilin regulates actin dynamics," Nat Struct Mol Biol, vol. 27, no. 2, pp. 210-220, Feb 2020.  
[2]	S. Lobato-Gil et al., "Proteome-wide identification of NEDD8 modification sites reveals distinct proteomes for canonical and atypical NEDDylation," Cell Rep, vol. 34, no. 3, p. 108635, Jan 2021.  
[3]	A. S. Yavuz, N. B. Sözer, and O. U. Sezerman, "Prediction of neddylation sites from protein sequences and sequence-derived properties," BMC Bioinformatics, vol. 16, no. 18, p. S9, Dec 2015.
# Programming language
Python 3.8 and above
# Environment configuration information
The python package names with version numbers are stored in tensorflow.yaml.
# Usage
Step 1: Locate the /Prediction/Scripts/predict.py file and set the working directory to its parent directory "Scripts".  
Step 2: Specify the fasta file and execute the predict.py file for making predictions. Example command: python predict.py --file test.fasta  
Step 3: Once the execution is complete, the prediction results will be output to the folder "Results".
# Contact
Please contact us if you need any help: lileime@hotmail.com
