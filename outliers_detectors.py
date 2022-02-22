import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# import pandas_profiling # must be commented out for ide to show plots
import tkinter
import seaborn as sns
from sklearn import datasets, svm, tree, preprocessing, metrics


def outliers_detector(df_data):
    # shows box plots to see outliers
    sns.boxplot(df_data['residual sugar'])
    plt.show()
    # df_data['residual sugar'].plot.box()
    # plt.show()

    index_list = []
    #outliers(df_data, 'residual sugar')  # calls function to find outliers
    for item in ['residual sugar']:
        index_list.extend(outliers(df_data, item))
    print("index_list", index_list)
    df_data = outliers_remover(df_data, index_list)  # removes all outliers for data-form
    sns.boxplot(df_data['residual sugar'])
    plt.show()
    return df_data

# this function finds the index of outliers
def outliers(df_data, ft):
    max_threshold = df_data[ft].quantile(0.75)  # quantile is a way to see average of 75% data below
    min_threshold = df_data[ft].quantile(0.05)  # quantile is a way to see average of 05% data below

    print("max_threshold", max_threshold)
    print("min_threshold", min_threshold)
    # df_data = df_data[(df_data['residual sugar']<max_threshold) & (df_data['residual sugar']>min_threshold)] # data that is in between min and max threshold

    IQR = max_threshold - min_threshold  # inter quartile range
    lower_bound = min_threshold - 1.5 * IQR
    upper_bound = max_threshold + 1.5 * IQR
    ls = df_data.index[(df_data[ft] < lower_bound) | (df_data[ft] > upper_bound)]  # extract index of outliers
    return ls


def outliers_remover(df_data, ls):
    ls = sorted(set(ls))  # sorting the list of indexes

    df_data = df_data.drop(ls)
    print("the clean shape ", df_data.shape)
    return df_data
