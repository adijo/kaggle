# Imports.

import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import csv
import numpy as np 
import sklearn.preprocessing


CATEGORICAL_COLUMNS = set(['City', 'City Group', 'Type'])
NUMBER_JOBS = 3
LABEL_ENCODER = sklearn.preprocessing.LabelEncoder()

df = pd.read_csv('train.csv', sep = ',', dtype = 'unicode')

# remove unecesary columns.
df = df.drop('Id', 1)
df = df.drop('Open Date', 1)


def train_model(df):
	"""
	Trains and returns model
	"""
	columns = list(df.columns.values)
	for column in columns:
		if column in CATEGORICAL_COLUMNS:
			df[column] = LABEL_ENCODER.fit_transform(df[column])
	
	target = np.array(df.ix[:, len(columns) - 1])
	training = df.as_matrix()
	training = np.delete(training, (len(training[0]) - 1), axis = 1)
	forest = RandomForestClassifier(n_jobs = NUMBER_JOBS)
	forest.fit(training, target)
	return forest

test = pd.read_csv('test.csv', sep = ",", dtype = "unicode")
test = test.drop('Id', 1)
test = test.drop('Open Date', 1)

columns = list(test.columns.values)
for column in columns:
	if column in CATEGORICAL_COLUMNS:
		test[column] = LABEL_ENCODER.fit_transform(test[column])

test_matrix = test.as_matrix()

ctr = 0

forest = train_model(df)
for row in test_matrix:
	print ctr, forest.predict(row)[0]
	ctr += 1