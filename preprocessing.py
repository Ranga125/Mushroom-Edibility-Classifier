# -*- coding: utf-8 -*-
"""MLopsnew.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fvew7lATiVV1K5NFq0_4LOiZofj2ja40

# **MLops**
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

data = pd.read_csv("/content/sample_data/mushroom.csv")

data.head()

data.isnull().sum()

data=data.drop("gill_spacing",axis=1)
data=data.drop("stem_root",axis=1)
data=data.drop("stem_surface",axis=1)
data=data.drop("veil_type",axis=1)
data=data.drop("veil_color",axis=1)
data=data.drop("spore_print_color",axis=1)

data.isnull().sum()

data.head()

#labelencoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
cat_cols = ['class','cap_shape','cap_surface','cap_color','does_bruise_or_bleed','gill_attachment','gill_color','stem_color','has_ring','ring_type','habitat','season']
data[cat_cols]=data[cat_cols].apply(le.fit_transform)

data

from sklearn.impute import SimpleImputer
se= SimpleImputer(missing_values=np.nan,strategy = "mean")
se.fit(data[['cap_surface']])

data[['cap_surface']]=se.transform(data[['cap_surface']])

from sklearn.impute import SimpleImputer
se= SimpleImputer(missing_values=np.nan,strategy = "mean")
se.fit(data[['gill_attachment']])

data[['gill_attachment']]=se.transform(data[['gill_attachment']])

from sklearn.impute import SimpleImputer
se= SimpleImputer(missing_values=np.nan,strategy = "mean")
se.fit(data[['ring_type']])

data[['ring_type']]=se.transform(data[['ring_type']])

data.shape

data['class'].value_counts()

data.groupby('class').mean()

X = data.drop(columns = 'class', axis=1)
Y = data['class']

print(X)

# Import SVM module
from sklearn import svm
# Import other necessary modules
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

classifier = svm.SVC(kernel='linear')

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, Y_train)

#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)

# accuracy score
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy score of the training data : ', training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

input_data = (1,15.26,6,6,0,2,10,16.95,17.09,11,1,2,0,3)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('edible')
else:
  print('poisonous')

"""# **pickle**"""

import pickle as pk

pk_path = '/content/sample_data/pickle_file.pkl'

with open(pk_path, 'wb') as file:
  pk.dump(lm, file)