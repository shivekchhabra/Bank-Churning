from ricebowl.processing import data_preproc
from ricebowl import plotting
import matplotlib.pyplot as plt
import seaborn as sns


# General function to get all the basic stats of the data
def basic_stats(data, file=None):
    s = ''
    s = s + '------------Unique values:-----------------\n'
    s = s + str(data.nunique())
    s = s + '\n\n------------Null values:-----------------\n'
    s = s + str(data.isnull().sum())
    s = s + '\n\n------------Dtypes:-----------------\n'
    s = s + str(data.dtypes)
    temp = data.drop_duplicates()
    duplicates = data.shape[0] - temp.shape[0]
    s = s + '\n\n------------Duplicate values:-----------------\n'
    s = s + str(duplicates)
    if file == None:
        print(s)
    else:
        f = open(file, 'w')
        f.write(s)
        f.close()
        print('Written in file: {}'.format(file))


# Specific function for checking various graphs
def graphs(df):
    # plotting.box(df)
    plotting.plot(df['gender'], df['exited'])


# General function for plotting a pie chart
def pie_chart(data, column_name, title='Title', labels=['None'], convert=False):
    if title == 'Title':
        title = column_name.capitalize()
    if convert == True:
        labels = list(data[column_name].unique())
        data, le = data_preproc.label_encode(data, c1=column_name)

    uniques = list(data[column_name].unique())
    if labels == ['None']:
        labels = labels * len(uniques)

    values = []
    for i in uniques:
        values = values + [data[column_name][data[column_name] == i].count()]
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.pie(values, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title(title, size=20)
    plt.show()


# Specific function for categorical comparison of data
def categorical_comparisons(df):
    fig, axarr = plt.subplots(2, 2, figsize=(20, 12))
    sns.countplot(x='geography', hue='exited', data=df, ax=axarr[0][0])
    sns.countplot(x='gender', hue='exited', data=df, ax=axarr[0][1])
    sns.countplot(x='hascrcard', hue='exited', data=df, ax=axarr[1][0])
    sns.countplot(x='isactivemember', hue='exited', data=df, ax=axarr[1][1])
    plt.show()


if __name__ == '__main__':
    data = data_preproc.read_csv('./bank_churn.csv')
    # basic_stats(data, 'stats.txt')
    data = data_preproc.reformat_col_headers(data)
    # pie_chart(data, 'gender', convert=True)
    categorical_comparisons(data)
    exit(1)
    data.drop(columns={'rownumber', 'surname', 'customerid'}, inplace=True)
    data, le = data_preproc.label_encode(data, c1='gender', c2='geography')
    # print(data.head())
    corr = data_preproc.find_corr(data)

    # exit(1)
    # data = data_preproc.normalization(data, list(data.columns))
    # graphs(data)
