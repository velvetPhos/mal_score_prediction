import pandas as pd
import xgboost as xgb
from bayes_opt import BayesianOptimization
from sklearn.model_selection import train_test_split

def predict_score(rounds):
    train_df = pd.read_csv('data/train.csv')
    test_df = pd.read_csv('data/test.csv')

    train_X = train_df.drop('Unnamed: 0', axis=1).drop('name', axis=1).drop('score', axis=1)
    train_Y = train_df['score']

    test_X = test_df.drop('Unnamed: 0', axis=1).drop('name', axis=1).drop('score', axis=1)

    X_train, X_test, y_train, y_test = train_test_split(train_X, train_Y)
    dtrain = xgb.DMatrix(X_train, label=y_train)
    del(X_train)
    dtest = xgb.DMatrix(X_test)
    del(X_test)

    def xgb_evaluate(max_depth, gamma, colsample_bytree):
        params = {'nthread': 1,
                  'eval_metric': 'rmse',
                  'max_depth': int(max_depth),
                  'subsample': 0.8,
                  'eta': 0.1,
                  'gamma': gamma,
                  'colsample_bytree': colsample_bytree
                  #'min_child_weight': min_child_weight,
                  }
        # Used around 1000 boosting rounds in the full model
        cv_result = xgb.cv(params, dtrain, num_boost_round=1000, nfold=5)

        # Bayesian optimization only knows how to maximize, not minimize, so return the negative RMSE
        return -1.0 * cv_result['test-rmse-mean'].iloc[-1]



    xgb_bo = BayesianOptimization(xgb_evaluate, {'max_depth': (3, 7),
                                                 'gamma': (0, 1),
                                                 'colsample_bytree': (0.3, 0.9)
                                                 #'min_child_weight': (5, 30),
                                                 #'eta': (0.1, 1.0)
                                                 })

    for n in range(rounds):

        try:
            temp_df = pd.read_csv('data/params/params{}.csv'.format(n))
            params = {}

            for k in temp_df['keys'].values:
                temp = temp_df.loc[temp_df['keys'] == k]
                print(temp['keys'].values[0])
                params[temp['keys'].values[0]] = temp['values'].values[0]

            params['max_depth'] = int(params['max_depth'])
        except:
            # Use the expected improvement acquisition function to handle negative numbers
            # Optimally needs quite a few more initiation points and number of iterations
            xgb_bo.maximize(init_points=3, n_iter=5, acq='ei')

            params = xgb_bo.res['max']['max_params']
            params['max_depth'] = int(params['max_depth'])

            df = pd.DataFrame(data={'keys':list(params.keys()), 'values':list(params.values())})

            df.to_csv('data/params{}.csv'.format(n))

        feature_columns = train_X.columns.values

        dmatrix = xgb.DMatrix(train_X.values,
                             train_Y.values,
                             feature_names=train_X.columns.values)

        clf = xgb.train(params, dmatrix)

        dmatrixtest = xgb.DMatrix(test_X.values,
                             feature_names=test_X.columns.values)

        res = clf.predict(dmatrixtest)

        res = pd.DataFrame(res, columns=['prediction'])

        final_res = pd.concat([test_df['name'], res], axis=1)

        final_res = final_res.sort_values(by=['prediction'], ascending=False)

        final_res.to_csv('data/result{}.csv'.format(n))


        fscores = pd.DataFrame({'X': list(clf.get_fscore().keys()), 'Y': list(clf.get_fscore().values())})
        fscores = fscores.sort_values(by=['Y'], ascending=False)
        fscores.to_csv('data/fscores{}.csv'.format(n))

    print('Finished score prediction')
