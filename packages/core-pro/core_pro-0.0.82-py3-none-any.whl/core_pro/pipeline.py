import polars as pl
from pathlib import Path
import joblib
from sklearn.metrics import classification_report
from xgboost import XGBClassifier, XGBRegressor


def feature_importance(model_input, all_features: list) -> pl.DataFrame:
    return (
        pl.DataFrame({
            'feature': all_features,
            'contribution': model_input.feature_importances_
        })
        .sort('contribution', descending=True)
    )


class DataInput:
    def __init__(self, x_train, y_train, x_test, y_test, target_names: list = None, save_model: Path | str = None):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.target_names = target_names
        self.save_model = save_model
        self.rf_params = {
            'colsample_bynode': 0.8,
            'learning_rate': 1,
            'max_depth': 5,
            'num_parallel_tree': 100,
            'objective': 'binary:logistic',
            'subsample': 0.8,
            'tree_method': 'hist',
            'device': 'cuda',
        }


class PipelineClassification(DataInput):
    @staticmethod
    def report(y_test, y_pred, target_names: list = None, print_report: bool = True) -> pl.DataFrame:
        # print report
        if print_report:
            print(classification_report(y_test, y_pred))

        # export report to dataframe
        dict_report = classification_report(y_test, y_pred, output_dict=True, target_names=target_names)
        report_full = pl.DataFrame()
        for _ in dict_report.keys():
            if _ == 'accuracy':
                continue
            tmp = (
                pl.DataFrame(dict_report.get(_))
                .with_columns(pl.lit(_).alias('name'))
            )
            report_full = pl.concat([report_full, tmp])

        col = ['name', 'accuracy', 'f1-score', 'precision', 'recall', 'support']
        report_full = (
            report_full
            .with_columns(pl.lit(dict_report.get('accuracy')).alias('accuracy'))
            .select(col)
        )

        return report_full

    def xgb(
            self,
            report_output: bool = True,
            params: dict = None,
            use_rf: bool = None,
    ):
        # params
        if not params:
            params = {
                'objective': 'binary:logistic',
                'metric': 'auc',
                'random_state': 42,
                'device': 'cuda',
            }
        if use_rf:
            params = self.rf_params

        # train
        xgb_model = XGBClassifier(**params)
        xgb_model.fit(
            self.x_train, self.y_train,
            eval_set=[(self.x_test, self.y_test)],
        )
        # predict
        pred = xgb_model.predict(self.x_test)

        # save model
        if self.save_model:
            model_path = joblib.dump(xgb_model, self.save_model)
            print(f'Save model to {model_path}')

        # report
        report = None
        if report_output:
            report = self.report(self.y_test, pred, target_names=self.target_names)
        return xgb_model, report


class PipelineRegression(DataInput):
    def xgb(
            self,
            params: dict = None,
    ):
        # params
        if not params:
            params = {
                'metric': 'mse',
                'random_state': 42,
                'device': 'cuda',
            }
        # train
        xgb_model = XGBRegressor(**params)
        xgb_model.fit(
            self.x_train, self.y_train,
            eval_set=[(self.x_test, self.y_test)],
        )
        # predict
        pred = xgb_model.predict(self.x_test)
        return xgb_model
