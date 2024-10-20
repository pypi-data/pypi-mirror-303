import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler


class LinearRegressLags:
    def __init__(self):
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.tscv = TimeSeriesSplit(n_splits=5)
        self.X_train_scaled = None
        self.X_test_scaled = None

    def timeseries_train_test_split(self, X, y, test_size):
        test_index = int(len(X) * (1 - test_size))
        # разбиваем весь датасет на тренировочную и тестовую выборку
        self.X_train = X.iloc[:test_index]
        self.y_train = y.iloc[:test_index]
        self.X_test = X.iloc[test_index:]
        self.y_test = y.iloc[test_index:]
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        self.model.fit(self.X_train_scaled, self.y_train)

        return self.X_train, self.X_test, self.y_train, self.y_test

    def mean_absolute_percentage_error(self, y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    def code_mean(self, data, cat_feature, real_feature):
        """
        Возвращает словарь, где ключами являются уникальные категории признака cat_feature,
        а значениями - средние по real_feature
        """
        return dict(data.groupby(cat_feature)[real_feature].mean())

    def plot_model_results(self, plot_intervals=False, plot_anomalies=False):
        prediction = self.model.predict(self.X_test_scaled)
        plt.figure(figsize=(15, 7))
        plt.plot(prediction, "g", label="prediction", linewidth=2.0)
        plt.plot(self.y_test.values, label="actual", linewidth=2.0)

        if plot_intervals:
            cv = cross_val_score(self.model, self.X_train_scaled, self.y_train,
                                 cv=self.tscv,
                                 scoring="neg_mean_absolute_error")
            mae = cv.mean() * (-1)
            deviation = cv.std()

            scale = 1.96
            lower = prediction - (mae + scale * deviation)
            upper = prediction + (mae + scale * deviation)

            plt.plot(lower, "r--", label="upper bond / lower bond", alpha=0.5)
            plt.plot(upper, "r--", alpha=0.5)
            if plot_anomalies:
                anomalies = np.array([np.nan] * len(self.y_test))
                anomalies[self.y_test < lower] = self.y_test[self.y_test < lower]
                anomalies[self.y_test > upper] = self.y_test[self.y_test > upper]
                plt.plot(anomalies, "o", markersize=10, label="Anomalies")

        error = self.mean_absolute_percentage_error(y_true=prediction, y_pred=self.y_test)
        plt.title("Mean absolute percentage error {0:.2f}%".format(error))
        plt.legend(loc="best")
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    def plot_coefficients(self):
        coefs = pd.DataFrame(self.model.coef_, self.X_train.columns)
        coefs.columns = ["coef"]
        coefs["abs"] = coefs.coef.apply(np.abs)
        coefs = coefs.sort_values(by="abs", ascending=False).drop(["abs"], axis=1)
        plt.figure(figsize=(15, 7))
        coefs.coef.plot(kind='bar')
        plt.grid(True, axis='y')
        plt.hlines(y=0, xmin=0, xmax=len(coefs), linestyles='dashed')
        plt.show()

    def get_coefficients(self):
        coefs = pd.DataFrame(self.model.coef_, self.X_train.columns)
        coefs.columns = ["coef"]
        coefs["abs"] = coefs.coef.apply(np.abs)
        coefs = coefs.sort_values(by="abs", ascending=False).drop(["abs"], axis=1)
        return coefs

    def get_anomalies(self):
        prediction = self.model.predict(self.X_test_scaled)
        cv = cross_val_score(self.model, self.X_train_scaled, self.y_train,
                             cv=self.tscv,
                             scoring="neg_mean_absolute_error")
        mae = cv.mean() * (-1)
        deviation = cv.std()
        scale = 1.96
        lower = prediction - (mae + scale * deviation)
        upper = prediction + (mae + scale * deviation)
        anomalies = np.array([np.nan] * len(self.y_test))
        anomalies = self.y_test[self.y_test < lower]
        anomalies = self.y_test[self.y_test > upper]
        return anomalies

    def prepare_data(self, series, lag_start, lag_end, test_size, target_encoding=False):
        # Создадим копию исходного датафрейма, чтобы можно было выполнять различные преобразования
        data = pd.DataFrame(series.copy())
        data.columns = ["y"]

        # Добавляем лаги целевой переменной
        for i in range(lag_start, lag_end):
            data["lag_{}".format(i)] = data.y.shift(i)

        # Добавляем данные по часу, дню недели и выходным
        # нужно выделить в отдельные методы - class.add_feature('weekday'), class.add_feature('is_weekend')
        data.index = pd.to_datetime(data.index)
        # data["hour"] = data.index.hour
        data["weekday"] = data.index.weekday
        data['is_weekend'] = data.weekday.isin([5, 6]) * 1

        if target_encoding:
            # считаем средние только по тренировочной части, чтобы избежать лика
            test_index = int(len(data.dropna()) * (1 - test_size))
            data['weekday_average'] = list(map(self.code_mean(data[:test_index], 'weekday', "y").get, data.weekday))
            # data["hour_average"] = list(map(code_mean(data[:test_index], 'hour', "y").get, data.hour))

            # выкидываем закодированные средними признаки
            data.drop(["weekday"], axis=1, inplace=True)

        # Делим на тренировочную и тестовую
        y = data.dropna().y
        X = data.dropna().drop(['y'], axis=1)
        self.X_train, self.X_test, self.y_train, self.y_test = self.timeseries_train_test_split(X, y,
                                                                                                test_size=test_size)

        return self.X_train, self.X_test, self.y_train, self.y_test
