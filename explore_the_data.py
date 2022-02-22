import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# import pandas_profiling # must be commented out for ide to show plots
import tkinter
import seaborn as sns
from sklearn import datasets, svm, tree, preprocessing, metrics


# crates a correlation heatMap
def correlation(df_data):
    # Use the function corr() to create a correlation matrix of all data and investigate it.
    # Can you tell which vine attribute has the biggest influence on the wine quality.
    # Do you get the same results when you analyze the red and white wine data sets separately?
    plt.matshow(df_data.corr())
    plt.show()

    print("___correlation---")
    corrmat = df_data.corr()
    print(corrmat)
    sns.heatmap(corrmat, annot=True)
    plt.show()
    # So depending on the data correlation, if we look at quality in the heatmap,
    # the closer you are to 1, the more correlation you have to it being "dependant" of the quality


# This function finds all the NaN values. and all this 0 as a value, and converts 0 the mean of the column
def data_preparation(df_data):
    print("---is null---")
    print(df_data.isnull().sum())  # finds null/NaN values
    print("--- has 0 value---")
    numb_zero_value = (df_data == 0).sum()  # finds alle 0 values
    print(numb_zero_value)
    # Replace 0 values with the mean of the column type.
    citric_acid_mean = df_data['citric acid'].mean()
    df_data['citric acid'] = df_data['citric acid'].replace(0, citric_acid_mean)  # replaces 0 values with the mean values of the column


# prints basic information about the data values.
def explore(df_data):
    # df_data.shape could also be used here to se rows and columns
    count_row = df_data.shape[0]  # Gives number of rows
    count_col = df_data.shape[1]  # Gives number of columns
    print(f"number of col {count_col} number of rows {count_row}")
    print(df_data.columns)
    print(df_data.dtypes)
    print(df_data.describe)  #
    # print(df_data.dtypes) # what each column type is
    print(df_data.describe())
    wines = df_data.groupby('wine_type').value_counts()
    print(wines)


# splits the data into different subsets using qcut.
def subsets(df_data):
    # Split the data into five subsets by binning the attribute pH. Identify the subset with the highest density?
    # What if you split the data in ten subsets?
    phdf = pd.qcut(df_data["pH"], q=5).value_counts()
    print("____Subset 5____")
    print(phdf)
    print("higest subset is from 3.08 to 3,17 with 5 subsets")
    print("____Subset 10____")
    phdf = pd.qcut(df_data["pH"], q=10).value_counts()
    print(phdf)
    print("higest subset is from 3.13 to 3,17 with 10 subsets")


# just prints out different plots
def plots(df_data):
    # matplotlib.use('TkAgg') # this is used when u want the plot in an external view
    df_data['wine_type'].value_counts().plot.pie()
    plt.show()
    # Plot diagrams that visualize the differences in red and white wines. What do your diagrams show
    wine_types = df_data.groupby('wine_type').mean()
    print(wine_types)
    wine_types["pH"].plot.bar()
    plt.show()
    wine_types["quality"].plot.bar()
    plt.show()
    wine_types["alcohol"].plot.bar()
    sns.barplot()
    plt.show()


# finds the corr of quality and drops fixed acidity, because its the lowest
def lowest_corr(df_data):
    #print("quality", df_data.groupby('quality').corr())
    pp = df_data[['quality']]
    # print(pp.corrwith(df_data['alcohol']))
    # print(pp.corrwith(df_data))
    print("corr stuff", "\n", df_data.corr()['quality'][:-1])  # Se the corr of quality with other columns. "[:-1]" excludes the same column
    print("corr stuff2", "\n", df_data.corr()['quality'])
    print("pH: seem to be the lowes value")
    df_data = df_data.drop(['pH'], axis=1)
    print("corr stuff3", "\n", df_data.corr()['quality'])


# transforms none numeric coulomb to numeric, fx wine_type to 0 & 2
def transform_to_numeric(df_data):
    # print(df_data.dtypes)
    processed_df = df_data.copy()
    le = preprocessing.LabelEncoder()
    processed_df['wine_type'] = le.fit_transform(df_data['wine_type'])
    print("processed ", "\n", processed_df['wine_type'])



# this is to make pandas_profiling make a html file that shows different plots.
# def profiling(df_data): # must be commented out for plots to show in IDE and not html
#     # prof = pandas_profiling.ProfileReport(df_data, minimal=True)
#     # prof.to_file('wine-data-visual.html')
