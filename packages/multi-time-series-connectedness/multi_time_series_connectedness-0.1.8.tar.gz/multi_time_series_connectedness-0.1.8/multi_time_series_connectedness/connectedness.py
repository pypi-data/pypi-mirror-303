"""
     1    2    3
1    a    b    c

2

3

b means volatility of 2 cause volatility of 1

"""
import numpy as np
import pandas as pd
from multi_time_series_connectedness import coef as f_coef


def var_p_to_var_1(ai_list):
    """
    :param ai_list: the Coef calculated
    :return: the coef of VAR1
    """
    ar1_coef = np.zeros((len(ai_list[0]), 1)) # You should change the number 7 to the number of variables. I mean, why it is 7?
    for coef_i in ai_list:
        ar1_coef = np.column_stack((ar1_coef, coef_i))
    ar1_coef = np.delete(ar1_coef, 0, 1)
    nrow = ar1_coef.shape[0]
    lag = len(ai_list)
    n = nrow * lag
    ar1_coef_down = np.identity(n)
    ar1_coef_down = np.delete(ar1_coef_down, np.s_[(n-nrow):n], 0)
    ar1_coef = np.vstack((ar1_coef, ar1_coef_down))
    return ar1_coef


def ar1_coef_to_psi(coef, h=5):
    """
    :param coef: the coef estimated
    :param h: the period of predicted future from now
    :return: The mechanism of periods to periods
    """
    n = coef.shape[0]
    lag = coef.shape[1]/n
    i_k = np.identity(n)
    zeros = np.zeros((n, coef.shape[1]-n))
    j = np.column_stack((i_k, zeros))
    ai_list = []
    for i in range(1, int(lag) + 1):
        ai_list.append(coef[:, 0:n])
        coef = np.delete(coef, np.s_[0:7], 1)
    ar1_coef = var_p_to_var_1(ai_list)
    psi = []
    psi.append(i_k)
    big_i = np.identity(ar1_coef.shape[1])
    for i in range(2, h+2):
        big_i = np.dot(big_i, ar1_coef)
        psi.append(np.dot(np.dot(j, big_i), j.transpose()))
    return psi


def theta(coef, sigma_hat, h=5):
    p = np.linalg.cholesky(sigma_hat)
    n = coef.shape[0]
    matrix = np.zeros(shape=(n, n))
    row, col = np.diag_indices(matrix.shape[0])
    matrix[row, col] = np.diagonal(p)
    inv = np.linalg.inv(matrix).transpose()
    psi = ar1_coef_to_psi(coef, h)
    theta_unit = []
    theta_std = []
    for i in range(0, (h+1)):  # must use append
        theta_std.append(np.dot(psi[i], p))
        theta_unit.append(np.dot(np.dot(psi[i], p), inv))
    return theta_unit, theta_std


def generalized_variance_decomp(m, coef, sigma_hat, h=5):
    n = coef.shape[0]
    i_k = np.identity(n)
    m_i = i_k[:, (m-1)]
    psi = ar1_coef_to_psi(coef, h)
    theta_value = theta(coef, sigma_hat, h)[1]
    diag = np.diagonal(sigma_hat)
    inv_sigma2 = 1/diag
    # i = 0
    den = []
    num = []
    decomp = []
    den_fill = (np.linalg.
                multi_dot((m_i, theta_value[0], theta_value[0].T,
                          m_i[np.newaxis].T)))
    den.append(den_fill)
    num_fill = np.square(np.linalg.multi_dot((m_i, psi[0], sigma_hat)))
    num.append(num_fill)
    decomp.append(num_fill * inv_sigma2 / den_fill)
    for l in range(1, h):
        den_fill = den[l-1] + (np.linalg.
                               multi_dot((m_i, theta_value[l], theta_value[l].T,
                                          m_i[np.newaxis].T)))
        den.append(den_fill)
        num_fill = (np.square(np.linalg.multi_dot((m_i, psi[l], sigma_hat))) +
                    num[l-1])
        num.append(num_fill)
        decomp.append(num_fill*inv_sigma2/den_fill)
    return decomp


class Connectedness:
    def __init__(self, volatilities, forecast_at_next_period=1):
        self.forecast_at_next_period = forecast_at_next_period
        self.start_at = volatilities["time"].iloc[0]
        self.end_at = volatilities["time"].iloc[-1]
        self.Coef, self.Sigma_hat = self.calculate_coef(volatilities)
        self.volatilities = volatilities

        # return the Full_Connectedness
        self.full_connectedness = None
        # restructure into flat shape
        self.restructure_connectedness = None

    def calculate_coef(self, volatilities):
        coef = f_coef.Coef(volatilities.dropna(), 20)
        coef.f_ols_coef()
        ols_coef = coef.OLS_coef
        ols_sigma = coef.OLS_sigma
        return ols_coef, ols_sigma

    def calculate_full_connectedness(self):

        # input required variable
        coef = self.Coef
        sigma_hat = self.Sigma_hat

        # the number of time series data
        n = coef.shape[0]

        # start to calculate connectedness
        connectedness = []

        # obtain the generalized variance decomposition after 5 periods
        # each variable fluctuates one time
        for i in range(1, (n + 1)):
            GVD = generalized_variance_decomp(i, coef, sigma_hat, self.forecast_at_next_period)[self.forecast_at_next_period - 1]
            connectedness.append(GVD)

        # transpose
        connectedness = np.array(connectedness).T

        # rescale each row to summation of 1
        for i in range(len(connectedness)):
            connectedness[i] = connectedness[i]/np.sum(connectedness[i])

        # calculate from_other
        from_other = []
        for i in range(0, len(connectedness)):
            connectedness_value = connectedness[i]
            from_other_value = 1 - connectedness_value[i]
            from_other.append(from_other_value)

        # calculated to_other
        to_other = []
        connectedness_tran = np.array(connectedness).T
        for i in range(0, len(connectedness)):
            connectedness_value = connectedness_tran[i]
            to_other_value = np.sum(connectedness_value) - connectedness_value[i]
            to_other.append(to_other_value)

        # spill over index (total connectedness)
        spill_over = np.sum(from_other) / n
        np.matrix(from_other).transpose()
        up = np.concatenate((np.matrix(connectedness), np.matrix(from_other).transpose()), axis=1)
        down = np.concatenate((np.matrix(to_other), np.matrix(spill_over)), axis=1)
        connectedness_table = np.concatenate((up, down), axis=0)

        self.full_connectedness = pd.DataFrame(connectedness_table)

    def rename_table(self, names):
        full_connectedness = self.full_connectedness
        full_connectedness.columns = names
        full_connectedness.rename(index=dict(
                                  zip(full_connectedness.index, names)),
                                  inplace=True)

    def flatten_connectedness(self):

        connectedness = self.full_connectedness

        # get the names specify the direction of a connectedness
        col_names = list(connectedness.columns.values)
        row_names = list(connectedness.index)

        name_list = []
        for col_name in col_names:
            for row_name in row_names:
                name = col_name + "_->_" + row_name
                name_list.append(name)

        # get the restructure connectedness value ##
        # array
        flat_connectedness = np.array(connectedness).T.flatten()
        # dataframe
        flat_connectedness = pd.DataFrame(flat_connectedness).transpose()
        # name
        flat_connectedness.columns = name_list

        flat_connectedness['start_at'] = self.start_at
        flat_connectedness['end_at'] = self.end_at
        flat_connectedness['forecast_at_next_period'] = self.forecast_at_next_period

        self.restructure_connectedness = flat_connectedness

    def calculate(self):
        # get the variable names
        names = list(self.volatilities.columns[1:])

        self.calculate_full_connectedness()
        self.rename_table(names + ["all"])
        table = self.full_connectedness
        return table
        # conn.table_restructure()
