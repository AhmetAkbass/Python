import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()
df.shape

df.columns

df.index

df.describe().T

df.isnull().values.any()

df.isnull().sum()

def check_df(dataframe, head=5):
    print("#####Shape####")
    print(dataframe.shape)
    print("#####Types#####")
    print(dataframe.dtypes)
    print("#####Head#####")
    print(dataframe.head(head))
    print("#####Tail#####")
    print(dataframe.tail(head))
    print("#####NA#####")
    print(dataframe.isnull().sum())
    print("#####Quantiles#####")
    print(dataframe.describe([0,0.05,0.5,0.95,0.99,1]).T)



df = sns.load_dataset("tips")


check_df(df)


###########################################################################################


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()



df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and str(df[col].dtypes) in ["int64","float32"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]

df["survived"].value_counts()

100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe ,col_name):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio":100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#############################################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df,col)

###########################################################################################


def cat_summary(dataframe ,col_name , plot = False):
    print(pd.DataFrame({col_name:dataframe[col_name].value_counts(),
                        "Ratio":100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#############################################################")

    if plot:
        sns.countplot(x = dataframe[col_name],data=dataframe)
        plt.show(block = True)


cat_summary(df,"sex",plot = True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("it is bool")
    else:
        cat_summary(df,col,plot = True)


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df,col,plot = True)

#############################################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

df[["age","fare"]].describe().T


num_cols = [col for col in df.columns if df[col].dtypes in ["int64","float32"]]

num_cols = [col for col in df.columns if col not in cat_cols]


def num_summary(dataframe, numerical_col):
    quantiles = [0.05 , 0.10 ,0.20 , 0.30 ,0.40 ,0.50 , 0.60 , 0.70 , 0.80 ,0.90 , 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)

def num_summary(dataframe, numerical_col,plot= False):
    quantiles = [0.05 , 0.10 ,0.20 , 0.30 ,0.40 ,0.50 , 0.60 , 0.70 , 0.80 ,0.90 , 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)

num_summary(df,"age",plot = True)


for col in num_cols:
    num_summary(df,col,plot=True)

###########################################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()
df.info()


def grab_col_names(dataframe,cat_th = 10, car_th =20):
    """

    Parameters
    ----------
    Fonksiyonun ne görev yapacağı hakkında bilgi vermektedir.
    dataframe:dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th:int ,float
        numerik fakat kategorik değişkenler için sınıf eşik değeri
    car_th: int ,float
        kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------

    """

def target_summary_with_cat(dataframe,target,categorical_col):
    print(pd.DataFrame({"TARGET_MEAN":dataframe.groupby(categorical_col)[target].mean()}))

target_summary_with_cat(df,"age","survived")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)