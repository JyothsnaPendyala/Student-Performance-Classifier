import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocess import data_preprocess

def visualise_data():
    data, numerical_features, categorical_features = data_preprocess()
    # visualisation of categorical_features
    for categorical_column in categorical_features:
        fig, axs = plt.subplots(figsize=(5,5))
        sns.countplot(data=data, x=categorical_column)
        plt.show()
    #Distrubution of numerical features
    for numerical_feature in numerical_features:
        fig, axs = plt.subplots(figsize=(5,4))
        sns.distplot(data[numerical_feature])
        plt.xlabel(numerical_feature)
        plt.show()
    #finding outliers in numerical features
    for numerical_feature in numerical_features:
        fig, axs = plt.subplots(figsize=(5,4))
        sns.boxplot(data[numerical_feature])
        plt.xlabel(numerical_feature)
        plt.show()
    # Correlation matrix
    data_num = data[numerical_features]
    corr = data_num.corr()
    plt.figure(figsize = (12,12))
    mp = sns.heatmap(corr, linewidth = 1 ,  annot=True, cmap="coolwarm", fmt=".2f")
    plt.show()
    return data

visualise_data()
