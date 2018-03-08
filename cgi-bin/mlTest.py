#!/usr/local/bin/python3

from cgitb import enable 
from createDict import *
enable()
import math
import numpy
import random
import scipy
import sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from code import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from collections import Counter
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

from sklearn.linear_model import LogisticRegression

from sklearn.cross_validation import StratifiedKFold, cross_val_score, train_test_split 

from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import add_dummy_feature

from sklearn.linear_model import LinearRegression

from mpl_toolkits.mplot3d import Axes3D




print('Content-Type: text/html')
print()

print('Hello World')
dic = getCleanDictionary('CancerMolar')

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names, dtype=None):
        self.attribute_names = attribute_names
        self.dtype = dtype
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X_selected = X[self.attribute_names]
        if self.dtype:
            return X_selected.astype(self.dtype).values
        return X_selected.values

def predictML(dic, array, length):
	
	#print(dict1)
	values = [] # Values are the values and their percentage decrease
	valuePairs = []
	for key in dic:
	    case = dic[key]
	    for i in range(1, len(case) -1):
	        if (case[i] not in [None, 0] and case[i+1]!= None and case[i] > case[i+1]):
	            if case[i] < 5000:
	                values += [(case[i], (case[i]-case[i+1])/case[i])]
	            
	                valuePairs += [(case[i], case[i+1])]

	val = [] #value
	pcDec = [] #percentage change
	value1 = []
	value2 = []

	for v in values:
	    val += [[v[0]]]
	    pcDec += [[v[1]]]

	for v in valuePairs:
	    value1 += [[v[0]]]
	    value2 += [[v[1]]]

	data = pd.DataFrame({'val1': [], 'val2': []})
	rows = []
	for values in valuePairs:
	    rows.append({'val1':  values[0], 'val2':  values[1]})
	 
	    

	data_frame = pd.DataFrame(rows)
	data = data.append(data_frame)

	data = data.take(np.random.permutation(len(data)))
	data.reset_index(drop = True, inplace = True)
	pipeline = Pipeline([("selector", DataFrameSelector(["val1"]))])

	linreg = LinearRegression()
	y = data["val2"].values
	X = pipeline.transform(data)
	linreg.fit(X, y)
	
	for i in range(len(array), length+1):
		mostRecentValue = array[i-1]
		value = linreg.predict(mostRecentValue)
		#value = 2**(value[0])
		#print(value)
		if value < 1:
			value = 0
		array += [int(value)]

	return(array)
	#return (linreg.predict(number))


#print(predictML(dic, 50))

def predicMLlogLoss(dic, array, length):
	logDic = {}
	for key in dic:
	    sample = dic[key]
	    sample = sample[removeFirstValue(sample):]
	    newSample = []
	    for i in sample:
	        if i != 0:
	            newSample += [math.log(i, 2)]
	        
	            
	    #print(key)
	    logDic[key] = newSample

	xVal = []
	yVal = []

	for key in logDic:
	    sample = logDic[key]
	    for i in range(len(sample)):
	        xVal += [i]
	        yVal += [sample[i]]
	        
	xVals = pd.Series(xVal)
	yVals = pd.Series(yVal)
	d = {'xVal' : xVals, 'yVal' : yVals}
	dfXY = pd.DataFrame(d)
	y= dfXY['yVal']
	X = dfXY.drop('yVal', axis = 1)
	lm = LinearRegression()
	lm.fit(X, y)

	for i in range(len(array), length+1):
		value = lm.predict(i)
		value = 2**(value[0])
		#print(value)
		if value < 1:
			value = 0
		array += [int(value)]

	return(array)

x = predicMLlogLoss(dic, [1000, 100], 20)
print(x)
y = predictML(dic, [10000, 9000], 20)
print(y)



