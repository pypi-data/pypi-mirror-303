# import required modules
import numpy as np
import math
from sklearn import linear_model
import operator
# ======================


def var_y(data, lag=1):
    """
    :param data: volatiltiies dataframe with Date
    :param lag: the lags of AR
    :return: for example, if lag = 4, then the first part of 4 periods would be
    # deleted because we cannot estimate them
    """
    y = data.drop("time", axis=1).drop(data.index[:lag]).values.transpose()
    return y


def shift_right(data, n_shift):
    """
    :param data: matrix without Date
    :param n_shift: the number of lags
    :return: shifted data (lag is the number of position to shift and filled
    # the blank with NA)
    """
    nrow = data.shape[0]
    ncol = data.shape[1]
    matrix_na = np.empty((nrow, n_shift,))
    matrix_na[:] = np.nan
    matrix_num = np.delete(data, [list(range(ncol - n_shift, ncol))], 1)
    result = np.concatenate((matrix_na, matrix_num), axis=1)
    return result


def var_x(data, lag=1):
    """
    :param data: volatiltiies dataframe with Date
    :param lag: the lag od AR
    :return: a matrix with stacked shifted past period data
    """
    y = data.drop("time", axis=1).values.transpose()
    x = y
    if lag > 1:
        for i in range(1, lag):
            x_down = shift_right(y, i)
            x = np.concatenate((x, x_down), 0)
        x = np.delete(x, range(lag - 1), 1)
    x = np.delete(x, x.shape[1] - 1, 1)
    return x


def ols(sy, sx):
    """
    :param sy: output of var_y
    :param sx: output of var_x
    :return: ols estimated coef
    """
    a = np.dot(sy, sx.transpose())
    b = np.linalg.inv(np.dot(sx, sx.transpose()))
    coef_result = np.dot(a, b)
    return coef_result


def mle_sigma(sy, sx, coef):
    t = sx.shape[1]
    std = sy - np.dot(coef, sx)
    mle_sigma_result = np.dot(std, std.transpose()) / t
    return mle_sigma_result


def aic(mle_sigma_estimates, coef, t):
    length = coef.shape[0] * coef.shape[1]
    eq_0 = np.count_nonzero(coef == 0)
    length = length - eq_0
    # if the size of data is too small, then the det may be 0, meaning it can not estimate it
    aic_result = math.log(np.linalg.det(mle_sigma_estimates)) + 2 / t * length
    return aic_result


def lag_chooser(data, max_lag):
    list_aic = []
    for i in range(1, max_lag + 1):
        sx = var_x(data, i)
        sy = var_y(data, i)
        t = sx.shape[1]
        reg = linear_model.LinearRegression(fit_intercept=False)
        reg.fit(sx.transpose(), sy.transpose())
        coef = reg.coef_
        mle_sigma_result = mle_sigma(sy, sx, coef)
        aic_result = aic(mle_sigma_result, coef, t)
        list_aic.append(aic_result)
    index, value = min(enumerate(list_aic), key=operator.itemgetter(1))
    return index + 1, value


class Coef:

    def __init__(self, data, max_lag):
        # The variables we need to launch this class
        # the lag chooses from lag_chooser
        self.lag = lag_chooser(data, max_lag)
        # the x and y to calculate coef
        self.x = var_x(data, self.lag[0])
        self.y = var_y(data, self.lag[0])

        # The place where to save calculated coef
        self.OLS_coef = None
        self.LASSO_coef = None
        self.LASSO_score = None
        self.LASSO_alpha = None

        # The place where to save calculated sigma
        self.OLS_sigma = None

        # accuracy
        self.accuracy = None

    def f_ols_coef(self):

        sx = self.x
        sy = self.y

        reg = linear_model.LinearRegression(fit_intercept=False)
        reg.fit(sx.transpose(), sy.transpose())
        self.accuracy = reg.score(sx.transpose(), sy.transpose())
        ols_coef_result = reg.coef_
        self.OLS_coef = ols_coef_result
        self.OLS_sigma = mle_sigma(sy, sx, self.OLS_coef)

    def f_lasso_coef(self, cv_value, max_iter):

        data = self.Data
        lag = self.Lag

        sx = self.var_x(data, lag[0])
        sy = self.var_y(data, lag[0])

        lasso_model = (linear_model.
                       MultiTaskLassoCV(cv=cv_value, fit_intercept=False,
                                        max_iter=max_iter).
                       fit(sx.transpose(), sy.transpose()))

        self.LASSO_alpha = lasso_model.alpha_

        clf = (linear_model.
               MultiTaskLasso(fit_intercept=False, alpha=self.LASSO_alpha,
                              max_iter=1000))

        clf.fit(sx.transpose(), sy.transpose())

        self.LASSO_score = clf.score(sx.transpose(), sy.transpose())
        self.LASSO_coef = clf.coef_

    """
    ## Ridge
# SX = VAR_X(stock_volatility, lag[0]) # 23 determined by lag_chooser in OLS
# SY = VAR_Y(stock_volatility, lag[0]) # 23 determined by lag_chooser in OLS
# n_alphas = 200
# alphas = np.logspace(-10, 1, n_alphas)
# Ridge_model = linear_model.RidgeCV(alphas=alphas, cv=10, fit_intercept=False).fit(SX.transpose(), SY.transpose())
# alpha = Ridge_model.alpha_
# clf = linear_model.Ridge(fit_intercept=False, alpha=alpha)
# clf.fit(SX.transpose(), SY.transpose())
# clf.score(SX.transpose(), SY.transpose())
 #coef_Ridge = clf.coef_ # get it

## Elastic net (combine LASSO and ridge, l = 1 for LASSO and l = 0 for Ridge)
# SX = VAR_X(stock_volatility, lag[0]) # 23 determined by lag_chooser in OLS
# SY = VAR_Y(stock_volatility, lag[0]) # 23 determined by lag_chooser in OLS
# n_alphas = 10
# alphas = np.logspace(-10, 1, n_alphas)
# ElasticNet_model = linear_model.MultiTaskElasticNetCV(alphas=alphas, cv=10, fit_intercept=False, l1_ratio=0.5, max_iter=10000).fit(SX.transpose(), SY.transpose())
 #alpha = ElasticNet_model.alpha_
# clf = linear_model.MultiTaskElasticNet(fit_intercept=False, alpha=alpha, max_iter=10000)
# clf.fit(SX.transpose(), SY.transpose())
# clf.score(SX.transpose(), SY.transpose())
# coef_ElasticNet = clf.coef_

# get the coefficients
# os.chdir("/Users/rucachen/Desktop/open_pycharm_virtualenv_3.6.4/financial_connectedness/coef")
# dict_coef = {}
# name = ["OLS", "LASSO", "Ridge", "ElasticNet"]
# list = [coef_OLS, coef_LASSO, coef_Ridge, coef_ElasticNet]
# for i in range(len(name)):
#     dict_coef[name[i]] = list[i]

# for i in range(len(name)):
#     Name = name[i] + "_" + "coef" + ".csv"
#     coef = pd.DataFrame(dict_coef[name[i]]).to_csv(Name)
    """
