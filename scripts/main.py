from preprocess import split_data
from feature_extraction import extract_features
from model_creation import create_model

# split original data set into training, testing and validation
# results are written to '../data/data_split'

print('Splitting the original data set into a train, test and validation set')
split_data('pos')
split_data('neg')


# extract features
print('extracting features from all sets')
set_names = ['train_set', 'validation_set', 'test_set']
for set_name in set_names:
    extract_features(set_name)

# create model ...
# Features to be included:
feature_list = ['number_characters']
print('creating models including the following features:')
print(feature_list)
model_pos = create_model('pos', feature_list)
model_neg = create_model('neg', feature_list)

print('the following models were created:')
print('pos: ', model_pos)
print('neg: ', model_neg)

# classify texts ...

# evaluate predictions ...

# create graphs ...
