import glob
import os


def features_to_file(feature_dict_list, name_set):
    """Write a list of feature dicts to a csv file"""

    # get names of columns by taking the first dict from the list
    column_names = sorted(feature_dict_list[0].keys())

    with open(f'../data/extracted_features/{name_set}.csv', 'w') as outfile:
        outfile.write(','.join(column_names)+'\n')

        for feature_dict in feature_dict_list:
            line = []
            for column_name in column_names:
                line.append(str(feature_dict[column_name]))
            line_str = ','.join(line)
            outfile.write(line_str+'\n')



def extract_features(name_set):
    """Extract text, features and gold label of all files in a set
    and return a list of dictionaries containing this information"""

    feature_dict_list = []

    # load splits



    with open('../data/data_set_splits.csv') as infile:
        lines = infile.read().strip().split('\n')

    files = []
    for line in lines:
        line_list = line.split(',')
        set_name = line_list[0]
        f = line_list[1]
        if set_name == name_set:
            files.append(f)

    #files = glob.glob(f'../data/data_split/{name_set}/*.txt')

    for f in files:
        instance_dict = dict()
        with open(f) as infile:
            text = infile.read()
        label = os.path.basename(f).split('.')[0][:3]

        instance_dict['filename'] = f
        instance_dict['text'] = text
        instance_dict['gold_label'] = label
        instance_dict['number_characters'] = len(text)
        feature_dict_list.append(instance_dict)

    features_to_file(feature_dict_list, name_set)


# only execute the function calls if this script is called
def main():
    feature_dict_list_train = extract_features('train_set')
    feature_dict_list_train = extract_features('validation_set')
    feature_dict_list_train = extract_features('test_set')

if __name__ == '__main__':
    main()
