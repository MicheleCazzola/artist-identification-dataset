# mvlm-dataset
This repository contains the dataset used in the paper "Artist identification using deep multi-branch neural network".

## Authors
- [Michele Cazzola](https://github.com/MicheleCazzola)
- [Giuseppe Arbore](https://github.com/GiuseppeArbore)

## Dataset
The dataset contains 21220 RGB images and it is split in [artist dataset](./artist_dataset/) that contains 21,220 images and [ kaggle dataset](./kaggle_testset/) that contains 3960 images. 

## Split
The dataset is split in [training](./train.txt), [validation](./val.txt) and [test](./test.txt) set. The training set contains 14854 images, the validation set contains 3183 images and the test set contains 3183 images.

## Scripts
The [scripts](./scripts/) folder contains the scripts used to :
- [Modify the file name based on the full path](./scripts/script.py)
- [Generate the training, validation and test set](./scripts/split.py)
- [Check the split](./scripts/check.py)
