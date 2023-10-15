# fake-profile

## Features
The functions to extract features are in the features/word_parser file for word level features amd in the features/keystroke_features file for KHT amd KIT features

## Verifiers
Template Generator: helpers to process our compact csv file of keystroke data
Verifier.py: A base class for all verifier implementations to inherit from
Each verifier has their own python implementation file, however, verifiers_library.py is the recommended way to use them
as it has all of the verifier algorithms implemented as class methods for ease of use

## Fusion
Score Level Fusion: We implement several score level fusion algorithms
- Mean 
- Median
- Min
- Max
The fusion matrix is calculated by iterating each triplet of the ITAD, Absolute, and Similarity matrices and applying the fusion algorithm to chose a final score. This matrix of fusion scores is used as input to calculate the top_k_accuracy_score from k=1 to k=5
Decision Level Fusion: We calculate score level fusion by using empirically determined thresholds for the particular verifier. If the score meets or exceeds the threshold, the profile is considered Genuine and we return False, otherwise we return True. Using the number of occurrences of False and True, if count(False) is greater than count(True), we say that the profile is genuine. If the probe id, matches the enrollment id, we also say that the profile is genuine. If both our verdict and the actual designation match we consider that a correct classification. 