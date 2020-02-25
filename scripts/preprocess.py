import glob
import os

def split_data(label):
    """
    Split the positive or negative (pos/neg) files in the original dataset
    into train, test and validationset.
    Write the files to new files in ../data/data_split/[label][name].txt
    """

    # create list of all files and make sure it is always in the same order
    full_set = sorted(list(glob.glob(f'../data/raw_data/{label}*.txt')))

    data_dict = dict()

    # Use a more sophisiticated way of splitting the data - this is just an example
    data_dict['train_set'] = full_set[:1]
    data_dict['validation_set'] = full_set[1:2]
    data_dict['test_set'] = full_set[2:]

    with open('../data/data_set_splits.csv', 'w') as outfile:
        for set_name, filepaths in data_dict.items():
            for filepath in filepaths:
                outfile.write(f'{set_name},{filepath}\n')




def main():
    split_data('pos')
    split_data('neg')



if __name__ == '__main__':
    main()
