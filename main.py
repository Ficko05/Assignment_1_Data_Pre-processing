import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets, svm, tree, preprocessing, metrics
import explore_the_data as etd
import outliers_detectors as od

# pip install openpyxl "in terminal"

# Assignment 1: Data Pre-processing
if __name__ == '__main__':
    # nr 1
    pd.set_option('display.width', 400)
    pd.set_option('display.max_columns', 20)
    red_wine = "C:/Users/filip/Desktop/SOFT/sem-2-soft/Data-Science/soft2022spring-DS-main/soft2022spring-DS-new/Data/winequality-red.xlsx"
    white_wine = "C:/Users/filip/Desktop/SOFT/sem-2-soft/Data-Science/soft2022spring-DS-main/soft2022spring-DS-new/Data/winequality-white.xlsx"
    df_red = pd.read_excel(red_wine,skiprows=1)
    df_red["wine_type"] = "red" # making a new column called wine_type and setting values to red
    df_white = pd.read_excel(white_wine, skiprows=1)
    df_white["wine_type"] = "white" # making a new column called wine_type and setting values to whit

    # print(df_red.columns)
    # print(df_red)
    # print(df_white.columns)
    # print(df_white)
    #nr 2
    df_wine = pd.DataFrame() # creates a empty dataframe variable
    df_wine = pd.concat([df_red, df_white])  # This "merges" 2 csv/Excel files together
    df_wine.reset_index(drop=True, inplace=True)  # this resets the indexes of the 2 merged files, important step
    #nr 3
    etd.explore(df_wine)
    # nr 4
    etd.plots(df_wine)  # wines plot in IDE
    #etd.profiling(df_wine) # html file with all basic plots
    #nr 5
    etd.subsets(df_wine)
    # nr 6
    etd.correlation(df_wine)

    #nr 7
    etd.data_preparation(df_wine)
    check_zero = (df_wine == 0).sum()
    print("check zero", check_zero)

    #nr 8
    print(df_wine.shape)
    df_wine = od.outliers_detector(df_wine)

    # nr 9
    # Identify the attribute with the lowest correlation to the wine quality and remove it.
    etd.lowest_corr(df_wine)

# nr 10
#Finally, transform categorical data into numeric and print out the start and the end of the preprocessed data frame.
    print("last task")
    etd.transform_to_numeric(df_wine)








# plt.hist(gaussian_numbers)
# plt.title("Gaussian Histogram")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

