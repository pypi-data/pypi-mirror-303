import sys

import scipy.stats as st
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_percentage_error
from tqdm import tqdm
import pandas as pd
from itertools import product
import matplotlib.pyplot as plt
import numpy as np


class SARIMAX:
    def __init__(self):
        self.result_table = None
        self.parameters_list = None
        self.param_mini = None
        self.param_seasonal_mini = None
        self.model_results = None
        self.best_model = None

    def sarima_grid_search(self, y, seasonal_period):
        p = d = q = range(0, 2)
        # d = q = range(0, 3)
        # p = range(0, 10)
        pdq = list(product(p, d, q))
        seasonal_pdq = [(x[0], x[1], x[2], seasonal_period) for x in list(product(p, d, q))]

        mini = float('+inf')

        for param in pdq:
            for param_seasonal in seasonal_pdq:
                try:
                    mod = sm.tsa.statespace.SARIMAX(y,
                                                    order=param,
                                                    seasonal_order=param_seasonal,
                                                    enforce_stationarity=False,
                                                    enforce_invertibility=False)

                    results = mod.fit()

                    if results.aic < mini:
                        mini = results.aic
                        param_mini = param
                        param_seasonal_mini = param_seasonal
                # print('SARIMA{}x{} - AIC:{}'.format(param, param_seasonal, results.aic))
                except:
                    print(param, param_seasonal, "Unexpected error:", sys.exc_info()[1])
        print('The set of parameters with the minimum AIC is: SARIMA{}x{} - AIC:{}'.format(param_mini,
                                                                                           param_seasonal_mini, mini))
        self.param_mini = param_mini
        self.param_seasonal_mini = param_seasonal_mini
        return param_mini, param_seasonal_mini

    def fit(self, data):
        # best_model = sm.tsa.statespace.SARIMAX(data, order=self.param_mini,
        #                                        seasonal_order=self.param_seasonal_mini,
        #                                        enforce_stationarity=True,
        #                                        enforce_invertibility=False
        #                                        ).fit(disp=-1)
        best_model = sm.tsa.statespace.SARIMAX(data,
                                               order=(1, 1, 1),
                                               seasonal_order=(1, 1, 1, 30),
                                               enforce_stationarity=True,
                                               enforce_invertibility=False
                                               ).fit(disp=-1)
        # self.model_results = best_model.fit()
        self.best_model = best_model
        print('best_model', best_model.summary)
        print(best_model.summary().tables[1])
        return best_model

    def plot_result(self):
        self.best_model.plot_diagnostics(figsize=(16, 8))
        plt.show()

    def plot_model(self, y_test, y, seasonal_period, pred_start_time, pred_end_time, plot_anomalies=False):
        # A better representation of our true predictive power can be obtained using dynamic forecasts.
        # In this case, we only use information from the time series up to a certain point,
        # and after that, forecasts are generated using values from previous forecasted time points.
        pred = self.best_model.get_prediction(start=pred_start_time,
                                              dynamic=False)

        pred_ci = pred.conf_int(alpha=0.1)
        y_forecasted = pred.predicted_mean
        print(y_forecasted)
        print('y_test', y_test)
        y_fc = self.best_model.fittedvalues
        # mape_dynamic = mean_absolute_percentage_error(y_test.values, y_fc_dynamic.values[-len(y_test.values):])
        mape = mean_absolute_percentage_error(y_test, y_forecasted)
        mse = ((y_forecasted - y_test) ** 2).mean()

        print(
            f'The MSE Error of SARIMA with season_length={seasonal_period} {mse}')
        plt.figure(figsize=(14, 7))
        plt.plot(y, label='actual')
        plt.plot(y_forecasted, label='Forecast', color='green')
        # plt.plot(y_fc_dynamic, label='model')
        plt.plot(pred_ci.index, pred_ci.iloc[:, 0], "r--", alpha=0.5, label="Up/Low confidence")
        plt.plot(pred_ci.index, pred_ci.iloc[:, 1], "r--", alpha=0.5)
        if plot_anomalies:
            anomalies = np.array([np.nan] * len(y_test))
            anomalies[y_test < pred_ci.iloc[:, 0]] = y_test[y_test < pred_ci.iloc[:, 0]]
            anomalies[y_test > pred_ci.iloc[:, 1]] = y_test[y_test > pred_ci.iloc[:, 1]]
            plt.plot(pred_ci.index, anomalies, "o", markersize=10, label="Anomalies")

        plt.title(f'The MSE={round(mse,2)} error of SARIMA with season_length={seasonal_period}')
        plt.xlabel("Date")
        plt.ylabel("Temperature, С")
        plt.grid(True)
        plt.legend()
        plt.show()

    def forecast(self, predict_steps, y):
        pred_uc = self.best_model.get_forecast(steps=predict_steps)

        # SARIMAXResults.conf_int, can change alpha,the default alpha = .05 returns a 95% confidence interval.
        pred_ci = pred_uc.conf_int(alpha=0.1)

        plt.figure(figsize=(14, 7))
        plt.plot(y, label='actual')
        #     print(pred_uc.predicted_mean)
        plt.plot(pred_uc.predicted_mean, label='Prediction', color='green')
        # ax.fill_between(pred_ci.index,
        #                 pred_ci.iloc[:, 0],
        #                 pred_ci.iloc[:, 1], color='k', alpha=.25, label='Conf.Interval')
        plt.plot(pred_ci.index, pred_ci.iloc[:, 0], "r--", alpha=0.5, label="Up/Low confidence")
        plt.plot(pred_ci.index, pred_ci.iloc[:, 1], "r--", alpha=0.5)
        plt.xlabel("Date")
        plt.ylabel("Temperature, С")
        plt.grid(True)
        plt.title(f'Model forecast for next {predict_steps} steps with CI')
        plt.legend()
        plt.show()

        # Produce the forcasted tables
        pm = pred_uc.predicted_mean.reset_index()
        pm.columns = ['Date', 'Predicted_Mean']
        pci = pred_ci.reset_index()
        pci.columns = ['Date', 'Lower Bound', 'Upper Bound']
        final_table = pm.join(pci.set_index('Date'), on='Date')

        return final_table
