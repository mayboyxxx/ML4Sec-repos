# -*- coding:utf-8 -*-
#coding=utf-8
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.svm import SVR
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.DESCR)
print("new branch")