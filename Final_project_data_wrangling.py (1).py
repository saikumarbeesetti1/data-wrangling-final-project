# # Title: Problem for Covid - 19 Data Analysis Project using Python


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



URL = "https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"


# # 1. Import the dataset using Pandas from above mentioned url.



df = pd.read_csv(URL)


df.head()


# # 2. High Level Data Understanding:

# ## 1.Find no. of rows & columns in the dataset
# ## 2.Data types of columns.
# ## 3.Info & describe of data in dataframe.



df.shape



print(f"No of rows : {df.shape[0]}")




print(f"No of columns : {df.shape[1]}")





df.dtypes




df.info()



df.describe()


# # 3. Low Level Data Understanding :


# ## 1.Find count of unique values in location column.


df["location"].nunique()


# ## 2.Find which continent has maximum frequency using values counts.


df["continent"].value_counts()


# ## 3.Find maximum & mean value in 'total_cases'.


df["total_cases"].max()


df["total_cases"].min()



df["total_cases"].mean()


# ## 4.Find 25%,50% & 75% quartile value in 'total_deaths'.


df["total_deaths"].quantile(0.25)



df["total_deaths"].quantile(0.5)



df["total_deaths"].quantile(0.75)


# ## 5.Find which continent has maximum 'human_development_index'.



df.iloc[df["human_development_index"].idxmax()]["continent"]


# ## 6.Find which continent has minimum 'gdp_per_capita'.


df.iloc[df["gdp_per_capita"].idxmin()]["continent"]


# # 4. Filter the dataframe with only this columns ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'] and update the data frame.



df = df[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]


df.head()


# # 5. Data Cleaning
 

# ## a. Remove all duplicates observations




df.drop_duplicates(inplace=True)




df.shape


# # b. Find missing values in all columns



df.isnull().sum()


# # c. Remove all observations where continent column value is missing



df.dropna(subset="continent",inplace= True)




df.shape


# # d. Fill all missing values with 0




df.fillna(value=0,inplace=True)


# # 6. Date time format :


# ## a. Convert date column in datetime format using pandas.to_datetime



pd.to_datetime(df["date"])


# ## b. Create new column month after extracting month data from date column.



df["month"] = pd.to_datetime(df["date"]).dt.month




df.head()


# # 7. Data Aggregation:


# ## a. Find max value in all columns using groupby function on 'continent' column



df.groupby("continent").max().reset_index()


# # b. Store the result in a new dataframe named 'df_groupby'



df_groupby = df.groupby("continent").max().reset_index()




df_groupby.head()


# # 8. Feature Engineering :


# ## a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'



df_groupby["total_deaths"]/df_groupby["total_cases"]




df_groupby["total_deaths_to_total_cases"] = df_groupby["total_deaths"]/df_groupby["total_cases"]




df_groupby


# ## (Use df_groupby dataframe for all further analysis)


# # 9. Data Visualization :


# ## a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.



sns.set_theme()




sns.distplot(df_groupby["gdp_per_capita"],bins=6,rug=True)


# ## b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'



sns.scatterplot(data=df_groupby,x="total_cases",y="gdp_per_capita",hue="continent",legend=False)


# ## c. Plot Pairplot on df_groupby dataset.



sns.pairplot(df_groupby,diag_kind="kde")


# ## d. Plot a bar plot of 'continent' column with 'total_cases' .


sns.catplot(data=df_groupby,x="continent",y="total_cases",kind="bar",palette="coolwarm")


# # 10.Save the df_groupby dataframe in your local drive using pandas.to_csv function .



df_groupby.to_csv("Data_groupby")








# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




