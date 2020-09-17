class analyze:
    '''
    To start keep it simple
    then consider an exhaustive grid search
    '''
    def __init__:
        from sklearn.linear_model import LinearRegression

    def lr_analy();
    '''
    Preform a set of standard linear regression analysis
    using the sklearn.linearmodel.linear regression
    '''

    def grid_search():
        '''
        preform a grid search based on these parameters i have found to work the best
        
        '''

    def class_metrics(TP, TN, FP, FN):
        '''
        This function was written by Reggie DePiero from GA DSI 824
        It calculates the values from a given confusion matrix into
        metrics: accuracy, misclassification, senstivity, specificity,
        precision
        '''
        acc = (TP + TN) / (TP + FP + TN + FN)
        mis = 1 - acc
        sen = TP / (TP + FN)
        spec = TN / (TN + FP)
        prec = TP / (TP + FP)
        results = [acc, mis, sen, spec, prec]
        ## create dictionary for easy display of results
        names = ['accuracy', 'misclassification', 'sensitivity', 'specificity', 'precision']
        res_dict = dict(zip(names, results))
    return res_dict