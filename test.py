import datetime

from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.regression import LabeledPoint
from pyspark.ml.classification import DecisionTreeClassifier
import pandas as pd
import re
import warnings
import os
import datetime
import numpy as np
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.util import MLUtils
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithLBFGS, LogisticRegressionModel



import pandas as pd
from datetime import datetime




def run_with_spark():
    
  

    conf = SparkConf().set("spark.driver.maxResultSize", "6g")
    conf.setMaster('local')
    conf.setAppName('spark-basic')
    sc = SparkContext(conf=conf)
       
    df= sc.textFile("C:/Users/Khiem/Desktop/big_data/data/data2K.csv").map(lambda line: line.split(","))
    dataset  = df.map(lambda x: LabeledPoint(x[0], x[1:]))   
    (trainingData, testData) = dataset.randomSplit([0.7, 0.3])
    print (dataset.collect()[0])



    start = datetime.now()
    model = DecisionTree.trainClassifier(trainingData,  numClasses=20, categoricalFeaturesInfo={}, impurity='gini', maxDepth=8, maxBins=32)
# Evaluate model on test instances and compute test error
    predictions = model.predict(testData.map(lambda x: x.features))    
   # print(predictions.collect())
    end = datetime.now() -start
    print ('time Decision tree : ', end)
    
    labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)    
#    print(labelsAndPredictions.collect()[1]) 
    acc =0
    acc = (labelsAndPredictions.filter( lambda lp: lp[0] == lp[1]).count()) / float(testData.count())
    print('Test Error = ' + str(acc))
    
    
    

    
run_with_spark()
