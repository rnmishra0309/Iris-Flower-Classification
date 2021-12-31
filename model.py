# This file is for making the model from the data
# Author: Rudra Narayan Mishra

# Importing Libraries

import numpy as np
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import joblib

# Data Fetching and Preprocessing

# Names of the columns
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Fetching Data
df = pd.read_csv('iris.data', header=None, names=columns)

# Data Splitting
X = df[columns[:-1]]    # Separating the training features
Y = df[columns[-1]]     # Separating the target column

# splitting in stratified manner so as to have nearly equal distribution of all labels
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, stratify=Y, random_state=0)

# Model Building

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# Model Saving

joblib.dump(model, 'model.sav')