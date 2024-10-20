from sklearn.model_selection import cross_val_score
from sklearn.model_selection import TimeSeriesSplit
import scipy.stats as st
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt


def main_ci(model, x_train, y_train, scoring="neg_mean_absolute_error"):
    tscv = TimeSeriesSplit(n_splits=5)
    cv = cross_val_score(model, x_train, y_train,
                         cv=tscv,
                         scoring="neg_mean_absolute_error")

    mae = cv.mean() * (-1)
    deviation = cv.std()
    confidence_level = 1.96
    z = st.norm.ppf((1 + confidence_level) / 2)
    # scale = 1.96  # z-factor for 0.95  confidence level
    bound = (mae + z * deviation)
    return bound


def main2_ci(y, y_hat, confidence_level):
    # # Find the z-score for the confidence level
    # z = st.norm.ppf((1 + confidence_level) / 2)
    # # Find the margin of error
    # margin_of_error = z * sample_std / sample_size ** 0.5
    #
    # # estimate stdev of yhat
    # sum_errs = arraysum((y - yhat) ** 2)
    # stdev = sqrt(1 / (len(y) - 2) * sum_errs)
    # interval = z.stdev
    # return margin_of_error
    pass


def seasonal_decompose(y):
    decomposition = sm.tsa.seasonal_decompose(y, model='additive', extrapolate_trend='freq')
    fig = decomposition.plot()
    fig.set_size_inches(14, 7)
    plt.show()


def ADF_test(timeseries, dataDesc):
    print(' > Is the {} stationary ?'.format(dataDesc))
    dftest = adfuller(timeseries.dropna(), autolag='AIC')
    print('Test statistic = {:.3f}'.format(dftest[0]))
    print('P-value = {:.3f}'.format(dftest[1]))
    print('Critical values :')
    for k, v in dftest[4].items():
        print('\t{}: {} - The data is {} stationary with {}% confidence'.format(k, v, 'not' if v < dftest[0] else '',
                                                                                100 - int(k[:-1])))


def tsplot(y, lags=None, figsize=(12, 7), style="bmh"):
    """
        Plot time series, its ACF and PACF, calculate Dickey–Fuller test

        y - timeseries
        lags - how many lags to include in ACF, PACF calculation
    """
    if not isinstance(y, pd.Series):
        y = pd.Series(y)

    with plt.style.context(style):
        fig = plt.figure(figsize=figsize)
        layout = (2, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))

        ts_ax.plot(y)
        p_value = sm.tsa.stattools.adfuller(y)[1]
        ts_ax.set_title(
            "Time Series Analysis Plots\n Dickey-Fuller: p={0:.5f}".format(p_value)
        )
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax)
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax)
        plt.tight_layout()


def timeseries_train_test_split(X, y, test_size):
    """
        Perform train-test split with respect to time series structure
    """

    # считаем индекс в датафрейме, после которого начинается тестовый отрезок
    test_index = int(len(X) * (1 - test_size))

    # разбиваем весь датасет на тренировочную и тестовую выборку
    X_train = X.iloc[:test_index]
    y_train = y.iloc[:test_index]
    X_test = X.iloc[test_index:]
    y_test = y.iloc[test_index:]

    return X_train, X_test, y_train, y_test, test_index
