import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from scipy.stats import linregress
from scipy.stats import beta
import random
from sklearn.neighbors import LocalOutlierFactor


class TrendChange:
    def __init__(self):
        self.trends_df: pd.DataFrame = None
        self.trends_dict: dict = None
        self.anomalies_df: pd.DataFrame = None

    def __regularizer(self, x):
        """Penalize an alghorithm for choosing a trend breaking point so that so that x is the ratio of the dataset got in right of left part.

        Used in in anomeda.__find_trend_breaking_point method. The more the value of the regularizer, the less the probabilty to choose a given point as a breaking point is."""
        return beta.pdf(x, 0.3, 0.6)

    def __find_trend_breaking_point(self,
                                    x: 'numpy.ndarray[int]',
                                    y: 'numpy.ndarray[float]',
                                    sample_frac: 'float' = 1
                                    ):
        metric_vals = []
        points_candidates = x[2:-1]
        points_candidates_ind = list(range(len(x))[2:-1])
        #
        if sample_frac == 1:
            points_candidates_ind = list(range(len(x))[2:-1])
        elif 0 <= sample_frac < 1:
            points_candidates_ind = np.random.choice(list(range(len(x))[2:-1]),
                                                     size=int(len(points_candidates) * sample_frac))
        else:
            raise ValueError('"sample_frac" must be between 0 and 1')

        if len(points_candidates) == 0:
            return None

        for dt in points_candidates_ind:
            y_true1 = y[:dt]
            x1 = np.arange(len(y_true1))

            y_true2 = y[dt:]
            x2 = np.arange(len(y_true2))

            linreg_fitted1 = linregress(x1, y_true1)
            y_pred1 = linreg_fitted1.slope * x1 + linreg_fitted1.intercept

            linreg_fitted2 = linregress(x2, y_true2)
            y_pred2 = linreg_fitted2.slope * x2 + linreg_fitted2.intercept

            ratio1 = len(y_true1) / (len(y_true1) + len(y_true2))
            ratio2 = len(y_true2) / (len(y_true1) + len(y_true2))

            metric = self.__regularizer(ratio1) * np.var(np.abs(y_pred1 - y_true1)) * np.quantile(
                np.abs(y_pred1 - y_true1),
                0.9) \
                     + self.__regularizer(ratio2) * np.var(np.abs(y_pred2 - y_true2)) * np.quantile(
                np.abs(y_pred2 - y_true2),
                0.9)

            metric_vals.append(metric)

        return points_candidates[np.argmin(metric_vals)]

    def __extract_trends(self,
                         x: 'numpy.ndarray[int] | pandas.DatetimeIndex',
                         y: 'numpy.ndarray[float]',
                         max_trends: "int | 'auto'" = 'auto',
                         min_var_reduction: 'float[0, 1] | None' = 0.5,
                         verbose: 'bool' = False
                         ):
        if max_trends == 'auto' or max_trends is None:
            if min_var_reduction is None:
                raise ValueError(
                    "Either max_trends or min_var_reduction parameters must be set. max_trends='auto' and min_var_reduction=None at the same time is not permitted.")
            max_trends = np.inf

        if min_var_reduction is None:
            min_var_reduction = np.inf

        x_scaled = x - x.min()

        linreg_fitted = linregress(x_scaled, y)
        y_fitted = linreg_fitted.slope * x_scaled + linreg_fitted.intercept
        error_var = np.var(np.abs(y_fitted - y))

        trends = {
            0: (
                x[0], x[-1] + 1,
                (linreg_fitted.slope, linreg_fitted.intercept),
                (y.shape[0], np.mean(y), error_var, np.sum(y))
            )
        }

        best_vars = [error_var]
        reducted_variance = 0  # that much of variance we explained

        n = len(trends.keys())
        while n < max_trends and reducted_variance < min_var_reduction:

            min_metric_diff = 0
            best_id = None
            best_dt = None
            best_params = None
            best_var = None
            for i in trends.keys():
                xmin, xmax, (a, b), _ = trends[i]

                index_mask = (x >= xmin) & (x < xmax)
                if len(x[index_mask]) <= 300:
                    sample_frac = 1
                elif len(x[index_mask]) <= 500:
                    sample_frac = -0.001 * len(x[index_mask]) + 1.3
                else:
                    sample_frac = 0.8

                dt = self.__find_trend_breaking_point(x[index_mask], y[index_mask], sample_frac=sample_frac)

                if dt is None:
                    continue

                y_true1 = y[(x >= xmin) & (x < dt)]
                x1 = x[(x >= xmin) & (x < dt)]

                y_true2 = y[(x >= dt) & (x < xmax)]
                x2 = x[(x >= dt) & (x < xmax)]

                linreg_fitted1 = linregress(x1 - x1.min(), y_true1)
                y_pred1 = linreg_fitted1.slope * (x1 - x1.min()) + linreg_fitted1.intercept

                linreg_fitted2 = linregress(x2 - x2.min(), y_true2)
                y_pred2 = linreg_fitted2.slope * (x2 - x2.min()) + linreg_fitted2.intercept

                y_base_diffs = []
                y_new_diffs = []
                for trend_id in trends.keys():
                    trend_xmin, trend_xmax, (trend_a, trend_b), _ = trends[trend_id]
                    y_trend_true = y[trend_xmin: trend_xmax]
                    # print('y_trend_true', y_trend_true)
                    y_trend_predicted = trend_a * np.arange(len(y_trend_true)) + trend_b
                    y_trend_diff = y_trend_predicted - y_trend_true
                    # print('y_trend_diff', y_trend_diff)
                    y_base_diffs.append(y_trend_diff)

                    if trend_id == i:
                        y_new_diffs.append(y_pred1 - y_true1)
                        y_new_diffs.append(y_pred2 - y_true2)
                    else:
                        y_new_diffs.append(y_trend_diff)

                y_base_diffs = np.concatenate(y_base_diffs)
                y_new_diffs = np.concatenate(y_new_diffs)

                new_var = np.var(np.abs(y_new_diffs))
                new_metric = np.var(np.abs(y_new_diffs)) * np.quantile(np.abs(y_new_diffs), 0.9)
                old_var = np.var(np.abs(y_base_diffs))
                # print("y_base_diffs", y_base_diffs)
                old_metric = np.var(np.abs(y_base_diffs)) * np.quantile(np.abs(y_base_diffs), 0.9)
                metric_diff = new_metric - old_metric

                if metric_diff < min_metric_diff:
                    min_metric_diff = metric_diff
                    best_id = i
                    best_dt = dt
                    best_params = [(linreg_fitted1.slope, linreg_fitted1.intercept),
                                   (linreg_fitted2.slope, linreg_fitted2.intercept)]
                    best_var = new_var
                    best_aggs = [
                        (
                            y_true1.shape[0],
                            np.mean(y_true1),
                            np.var(np.abs(y_true1 - y_pred1)),
                            np.sum(y_true1)
                        ),
                        (
                            y_true2.shape[0],
                            np.mean(y_true2),
                            np.var(np.abs(y_true2 - y_pred2)),
                            np.sum(y_true2)
                        )
                    ]

            if best_id is not None:
                left_trend = (trends[best_id][0], best_dt, best_params[0], best_aggs[0])
                right_trend = (best_dt, trends[best_id][1], best_params[1], best_aggs[1])

                trends[best_id] = left_trend
                trends[max(trends.keys()) + 1] = right_trend
                best_vars.append(best_var)
            else:
                if verbose:
                    print(f'No more trends were found. Finish with {n + 1} trends.')
                break

            if max(best_vars) == 0:
                reducted_variance = 1
            else:
                reducted_variance = 1 - min(best_vars) / max(best_vars)  # that much of variance we explained

            if reducted_variance >= min_var_reduction:
                if verbose:
                    print(
                        f'Variance reduced by {reducted_variance} comparing to initial value,'
                        f' while the reduction of {min_var_reduction} is needed.'
                        f' Finish with {n + 1} trends'
                    )
                break

            n += 1
            continue
        return trends

    def fit_trends(self,
                   data: '(numpy.ndarray[int], numpy.ndarray[float])',
                   trend_fitting_conf: 'dict' = {'max_trends': 'auto', 'min_var_reduction': 0.75},
                   plot: 'bool' = False,  # пока не надо
                   df: 'bool' = True,
                   verbose: 'bool' = False
                   ):
        def resp_to_df(resp):
            flattened = []
            for t in trends:
                # print(t)
                x_min, x_max, (slope, intercept), (cnt, mean, mae_var, y_sum) = trends[t]
                flattened.append((x_min, x_max, slope, intercept, cnt, mean, mae_var, y_sum))
            resp_df = pd.DataFrame(flattened,
                                   columns=['trend_start_dt', 'trend_end_dt', 'slope', 'intercept', 'cnt', 'mean',
                                            'mae_var', 'sum'])
            # resp_df.sort_values(by='trend_start_dt', inplace=True)
            return resp_df

        x, y = data

        if len(y) == 0:
            return None

        sorted_indx = np.argsort(x)
        x = x[sorted_indx]
        y = y[sorted_indx]
        res_values = {}
        trends = self.__extract_trends(x, y,
                                       max_trends=trend_fitting_conf.get('max_trends'),
                                       min_var_reduction=trend_fitting_conf.get('min_var_reduction'),
                                       verbose=verbose
                                       )
        # res_values = trends.copy()
        self.trends_dict = trends
        res_values = resp_to_df(trends)
        if plot:
            self.plot_trends(res_values)
        if df:
            self.trends_df = res_values
            return res_values
        return trends  # зписать в атрибиты класса

    def plot_trends(self,
                    ax: 'matplotlib.axes.Axes' = None,
                    shading: bool = False):
        if ax is None:
            fig, ax = plt.subplots()
        df = self.trends_df.copy()
        df_tmp = df.sort_values(by='trend_start_dt')
        x_cluster = []
        y_trend_cluster = []
        trends_no = []
        legend = []

        for trend in df_tmp.iterrows():
            i, t = trend
            trends_no.append(i)
            x_axis = np.arange(t['trend_start_dt'], t['trend_end_dt'])
            x = np.arange(len(x_axis))
            y_trend = x * t['slope'] + t['intercept']
            x_cluster.append(x_axis)
            y_trend_cluster.append(y_trend)
            if shading:
                if t['slope'] >= 0:
                    plt.axvspan(x_axis[0], x_axis[-1], alpha=0.05, lw=0, color="green")
                else:
                    plt.axvspan(x_axis[0], x_axis[-1], alpha=0.05, lw=0, color="red")
            # x_cluster.append(x_axis[0])
            # x_cluster.append(x_axis[-1])
            # y_trend_cluster.append(x[0] * t['slope'] + t['intercept'])
            # y_trend_cluster.append(x[-1] * t['slope'] + t['intercept'])
            # ax.plot(x + t['trend_start_dt'], y_trend)
            # legend.append(f"{i},"
            #               f"(k={round(float(t['slope']),2)},"
            #               f"b={round(float(t['intercept']),2)})")
        x_cluster = np.concatenate(x_cluster)
        y_trend_cluster = np.concatenate(y_trend_cluster)
        ax.plot(x_cluster, y_trend_cluster, color='black', linewidth=0.8, label='Trend Line')
        # ax.xaxis.set_major_locator(ticker.AutoLocator())
        # ax.xaxis.set_major_locator(ticker.AutoLocator())
        # ax.xaxis.set_major_locator(ticker.MaxNLocator(20))
        # ax.xaxis.set_minor_locator(ticker.MaxNLocator(100))
        # plt.xticks(rotation=90)
        plt.grid(True)
        ax.legend()
        return ax

    def find_anomalies(self,
                       data: '(numpy.ndarray[int], numpy.ndarray[float])',
                       n_neighbors=3):
        yindex, ydata = data
        yindex_int = yindex
        y_fitted_list = []
        y_diff_list = []
        x_labels = []
        df_tmp = self.trends_df
        resp = []
        for trend in df_tmp.iterrows():
            i, t = trend
            xmin, xmax = t['trend_start_dt'], t['trend_end_dt']
            slope, intercept = t['slope'], t['intercept']
            index_mask = (yindex >= xmin) & (yindex < xmax)
            cluster_indx = yindex[index_mask]
            cluster_indx_int = np.arange(len(yindex_int[index_mask]))
            y_fitted = slope * cluster_indx_int + intercept
            y_diff_list.append(ydata[index_mask] - y_fitted)
            x_labels.append(cluster_indx)
            y_fitted_list.append(y_fitted)
        x_labels = np.concatenate(x_labels)
        y_diff = np.concatenate(y_diff_list)
        y_fitted = np.concatenate(y_fitted_list)

        sorted_ind = np.argsort(x_labels)
        y_diff = y_diff[sorted_ind]
        y_fitted = y_fitted[sorted_ind]

        if len(ydata) == 1:
            outliers = np.array([False])
        else:
            clusterizator = LocalOutlierFactor(n_neighbors=max(min(len(ydata) - 1, n_neighbors), 1), novelty=False)
            try:
                outliers = clusterizator.fit_predict(y_diff.reshape(-1, 1)) == -1
            except ValueError:
                raise ValueError(
                    "Something is wrong with the metric values. It may contain NaN or other values which caused errors while fitting trends.")

        # Remove inliers, i.e. isolated points not from the left or right tail of values range
        # We want to keep only the largest or the lowest differences
        # We also keep only % of anomalies defined by p_low and p_large
        indeces_sorted_by_y_diff = np.argsort(y_diff)  # Индексы отсортированы по убыванию (?) Y-Diff
        not_outliers_indeces = np.where(outliers[indeces_sorted_by_y_diff] == False)[
            0]  # Получаем индексы в которых outliers = Flase сортированные по Ydiff min to max
        outliers[indeces_sorted_by_y_diff[np.min(not_outliers_indeces): np.max(not_outliers_indeces)]] = False
        res_df = pd.DataFrame({
            'index': yindex,
            'metric_value': ydata,
            'fitted_trend_value': y_fitted,
            'anomaly': outliers
        })
        res_df['cluster'] = 'total'
        res_df = res_df[['cluster', 'index', 'metric_value', 'fitted_trend_value', 'anomaly']]
        resp.append(res_df)

        resp = pd.concat(resp).reset_index(drop=True)
        self.anomalies_df = resp[resp['anomaly']].reset_index(drop=True)
        return self.anomalies_df

    def plot_anomalies(self,
                       ax: 'matplotlib.axes.Axes' = None,
                       ):
        if ax is None:
            fig, ax = plt.subplots()
        df = self.anomalies_df.copy()
        x, y = df['index'], df['metric_value']
        ax.plot(x, y, 'o', c='red', label='Detected Anomalies')
        ax.legend()
        plt.grid(True)
        return ax
