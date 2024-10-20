import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
import holidays

vn_holiday = holidays.country_holidays('VN')


class ExtractTime:
    @staticmethod
    def sin_transformer(period):
        return FunctionTransformer(lambda x: np.sin(x / period * 2 * np.pi))

    @staticmethod
    def cos_transformer(period):
        return FunctionTransformer(lambda x: np.cos(x / period * 2 * np.pi))

    @staticmethod
    def trigonometric_features(data, dict_column: dict = None, merge_with_data: bool = True):
        # sin/cos transformation
        if dict_column is None:
            dict_column = {'month': 12, 'day': 30}
        sin_f = [(f'{i}_sin', ExtractTime.sin_transformer(v), [i]) for i, v in dict_column.items()]
        cos_f = [(f'{i}_cos', ExtractTime.cos_transformer(v), [i]) for i, v in dict_column.items()]
        ct = ColumnTransformer(transformers=sin_f + cos_f)
        col = [i[0] for i in sin_f + cos_f]
        df_trigonometric = pl.DataFrame(ct.fit_transform(data), schema=col)
        # export
        if merge_with_data:
            return pl.concat([data, df_trigonometric], how='horizontal')
        else:
            return df_trigonometric

    @staticmethod
    def date_time_features(df: pl.DataFrame, col: str = 'grass_date') -> pl.DataFrame:
        return (
            df
            .with_columns(
                pl.col(col).dt.year().alias('year').cast(pl.Int16),
                pl.col(col).dt.month().alias('month').cast(pl.Int8),
                pl.col(col).dt.day().alias('day').cast(pl.Int8),
                pl.col(col).dt.weekday().alias('weekday').cast(pl.Int8),
                pl.col(col).map_elements(lambda x: 1 if vn_holiday.get(x) else 0, return_dtype=pl.Int64).alias('holiday')
            )
            .with_columns(
                (pl.col('month') - pl.col('day')).alias('days_dif_spike')
            )
        )

    @staticmethod
    def trend(df: pl.DataFrame, col: list, index_column: str = 'grass_date', period: str = '3d') -> pl.DataFrame:
        return df.with_columns(
            pl.mean(i).rolling(index_column=index_column, period=period, closed='left').alias(f'trend_{period}_{i}')
            for i in col
        )

    @staticmethod
    def season(df: pl.DataFrame, col: list, period: str = '3d') -> pl.DataFrame:
        return df.with_columns(
            (pl.col(i) - pl.col(f'trend_{period}_{i}')).alias(f'season_{period}_{i}') for i in col
        )

    @staticmethod
    def lag(df: pl.DataFrame, col: list, window: int = 7) -> pl.DataFrame:
        return df.with_columns(
            pl.col(i).shift(window).alias(f'shift_{window}d_{i}') for i in col
        )


class EDA:
    @staticmethod
    def clean_check(data: pl.DataFrame, pct: bool = False, verbose: bool = False) -> dict:
        zero_check_dict = data.sum().to_dicts()[0].items()
        zero_check = {i: v for i, v in zero_check_dict if v == 0}

        null_check_dict = data.null_count().to_dicts()[0].items()
        null_check = {i: v for i, v in null_check_dict if v > 0}
        if pct:
            null_check = {i: round(v / data.shape[0], 2) for i, v in null_check_dict if v > 0}

        if verbose:
            print(f"- Null columns: {null_check}")
            print(f"- Zero columns: {zero_check}")
        dict_ = {
            'null': null_check,
            'zero': zero_check
        }
        return dict_


    @staticmethod
    def group_by_describe(col: str, percentiles: list = None) -> list:
        """
        Use in polars
        Ex: df.group_by(pl.col('date')).agg(*group_by_describe("a"), *group_by_describe("b"))
        :param col: 'a'
        :param percentiles: [.25, .5]
        :return: list of exp
        """
        if not percentiles:
            percentiles = [.25, .5, .75]
        lst = [
            pl.col(col).count().alias(f"{col}_count"),
            pl.col(col).is_null().sum().alias(f"{col}_null_count"),
            pl.col(col).mean().alias(f"{col}_mean"),
            pl.col(col).std().alias(f"{col}_std"),
            pl.col(col).min().alias(f"{col}_min"),
            pl.col(col).max().alias(f"{col}_max"),
        ]
        lst_quantile = [
            pl.col(col).quantile(i).alias(f"{col}_{int(i*100)}th") for i in percentiles
        ]
        return lst + lst_quantile

    @staticmethod
    def plot_correlation(data, figsize: tuple = (10, 6), save_path: Path = None):
        if isinstance(data, pl.DataFrame):
            data = data.to_pandas()
        fig, ax = plt.subplots(figsize=figsize)
        cmap = sns.diverging_palette(230, 20, as_cmap=True)
        sns.heatmap(data.corr(), cmap=cmap, annot=True, linewidths=.5, fmt=",.2f")
        fig.show()
        if save_path:
            fig.savefig(save_path)

    @staticmethod
    def value_count(data: pl.DataFrame, col: str):
        return (
            data[col]
            .value_counts(sort=True)
            .with_columns(
                (pl.col('count') / data.shape[0]).round(2).alias('pct')
            )
            .to_dict(as_series=False)
        )

    @staticmethod
    def convert_decimal(data: pl.DataFrame):
        col_decimal = [i for i, v in dict(data.schema).items() if isinstance(v, pl.Decimal)]
        return (data.with_columns(pl.col(i).cast(pl.Float64) for i in col_decimal))
