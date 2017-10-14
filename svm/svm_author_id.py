#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
'''
### A smaller training set
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
'''
from sklearn import svm
clf = svm.SVC(C=10000., kernel='rbf') ### linear
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t1, 3), "s"
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print "accuracy:", accuracy
print "prediction for element 10:", pred[10]
print "prediction for element 26:", pred[26]
print "prediction for element 50:", pred[50]
print sum(pred), "Chris emails predicted"
#########################################################
#########################################################
### results (kernel='linear'):
### training time: 155.598 s
### predict time: 16.197 s
### accuracy: 0.984072810011
### A smaller training set results (kernel='linear'):
### training time: 0.088 s
### predict time: 0.942 s
### accuracy: 0.884527872582
### A smaller training set results (kernel='rbf'):
### training time: 0.096 s
### predict time: 1.043 s
### accuracy: 0.616040955631
### A smaller training set results (C=10.0, kernel='rbf'):
### training time: 0.096 s
### predict time: 1.05 s
### accuracy: 0.616040955631
### A smaller training set results (C=100., kernel='rbf'):
### training time: 0.109 s
### predict time: 1.06 s
### accuracy: 0.616040955631
### A smaller training set results (C=1000., kernel='rbf'):
### training time: 0.095 s
### predict time: 1.016 s
### accuracy: 0.821387940842
### A smaller training set results (C=10000., kernel='rbf'):
### training time: 0.089 s
### predict time: 0.829 s
### accuracy: 0.892491467577
### Full training set results (C=10000., kernel='rbf'):
### training time: 99.914 s
### predict time: 10.134 s
### accuracy: 0.990898748578
### prediction for element 10: 1
### prediction for element 26: 0
### prediction for element 50: 1
### 877 Chris emails predicted