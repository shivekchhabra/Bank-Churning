from ricebowl.processing import data_preproc
from ricebowl.modeling import choose_model
from ricebowl import metrics


def reading_and_processing():
    data = data_preproc.read_csv('./bank_churn.csv')
    data = data_preproc.reformat_col_headers(data)
    data.drop(columns={'surname', 'rownumber', 'customerid'}, inplace=True)
    data, le = data_preproc.label_encode(data, c1='gender', c2='geography')
    target = data['exited']
    data = data.drop(columns='exited')
    xtrain, xtest, ytrain, ytest = data_preproc.split_data(data, target)
    return xtrain, xtest, ytrain, ytest


if __name__ == '__main__':
    xtrain, xtest, ytrain, ytest = reading_and_processing()
    print('------------Random Forest---------------')
    ypred = choose_model.random_forest_classifier(xtrain, ytrain, xtest)
    print(metrics.classifier_outputs(ytest, ypred))
    print('\n\n------------KNN---------------')
    ypred = choose_model.knn_classifier(xtrain, ytrain, xtest)
    print(metrics.classifier_outputs(ytest, ypred))
    print('\n\n------------SVM---------------')
    ypred = choose_model.svm_classifier(xtrain, ytrain, xtest)
    print(metrics.classifier_outputs(ytest, ypred))
