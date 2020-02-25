# Example set-up for a text classification project

This little example set-up is supposed to help you get started with your own project. Please note that this is just an example and that there are many better, more explicit and more efficient ways of writing code. However, it illustrates the main principles we would like you to follow when setting up your project:

* modularity: Make sure your project consists of smaller 'building blocks' which you can use individually or in combination with each other. Make sure to set it up in such a way that adding additional 'modules' is easy.
* avoid repetition: Functions should be defined once and reused whenever possible.
* transparent structure: Use clear directory and script names to structure your code.
* essential documentation: Please provide information on how to run your code including details about filepaths which need to be changed, where to store your original data set, etc.

This project is supposed to provide an example of how you can set up a larger classification project.


## Data
The data for this project can be found in the directory data/.

data/ contains:
  - raw_data : contains a toy set of positive and negative files of a text classification dataset
  - data_split: new train/validation and test splits which are created in this project
  - extracted_features: directory in which the features for classification are stored


## Running the code

To run the system, please consider the scripts in scripts/:

scripts/ contains:
- preprocess.py: creates training, validation and test split of the dataset and stores the splits in data/data_split/
- feature_extraction.py: extracts features from the training, validation and test set and stores each set in a csv file in data/extracted_features/ (e.g.data/extracted_features/test_set.csv)
- create_model.py: creates a positive and a negative model based on the features in data/extracted_features/train_set.csv
- classify.py: not implemented yet
- evaluate.py: not implemented yet
- visualize.py: not implemented yet
- main.py: runs all implemented steps in the correct sequence

To run the program, please execute the scripts in the order shown above or run the main.py script.

## Other directories
In addition, this project contains the following directories:

- results/: contains a dummy file (should contain the predictions of a model)
- graphs/: contains a dummy file (should contain graphs visualizing interesting results or feature distributions)


If you have any questions, please contact me via this email address: pia.sommerauer@vu.nl. 
