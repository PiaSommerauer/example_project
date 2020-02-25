import csv
from collections import defaultdict

def create_model(label, feature_list):
    """
    Calculate average values of a given list of features for a particular class.
    """

    with open(f'../data/extracted_features/train_set.csv') as infile:
        feature_dict_list = [dict(feature_dict) for feature_dict in csv.DictReader(infile, delimiter = ',')]


    average_feature_values_dict = defaultdict(list)
    for feature_dict in feature_dict_list:
        label_gold = feature_dict['gold_label']
        if label_gold == label:
            for feature in feature_list:
                value = feature_dict[feature]
                average_feature_values_dict[feature].append(float(value))

    average_values = []
    for feature, values_list in average_feature_values_dict.items():
        average_feature_value = sum(values_list)/len(values_list)
        average_values.append(average_feature_value)
    return average_values


def main():

    model_list_pos = create_model('pos', ['number_characters'])
    print(model_list_pos)

if __name__ == '__main__':
    main()
