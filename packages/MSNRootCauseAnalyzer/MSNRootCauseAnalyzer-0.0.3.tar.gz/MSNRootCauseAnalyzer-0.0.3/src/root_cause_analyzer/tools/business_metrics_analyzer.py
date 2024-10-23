import numpy as np
import pandas as pd
import requests
from datetime import datetime
from msal import PublicClientApplication
from pprint import pprint

from ..algorithms.adtributor import Adtributor, RecursiveAdtributor
from ..utils import safe_div
from ..titan.titan_api import TitanApi
from ..config.msn_metrics import mCFVConfig

# TODO:1. titan api error, need a cache and retry mechanism from break point

REPORT_METRIC_FUNCTION = 0
REPORT_DIMENSION = 1
REPORT_DIMENSION_ADTRIBUTION = 2

class MSNBusinessMetricsAnalyzer:

    def __init__(self, alias_account, metric, verbose=0):
        """
        alias_account: string, alias account
        metric: string, metric name
        """
        self.alias_account = alias_account
        self.titan_api = TitanApi(alias_account)
        self.verbose = verbose

        # init metric config
        self.metric = metric
        self._initial_metric_config()
        if not self.metric_config:
            print(f"Error: metric {metric} is not supported.")
            return
        self.metric_set, self.metric_query_str = self._get_metric_function(metric)
        
        self.top_n_factor = 10  # TODO: move to config

        # init algorithm map
        self.algorithms = {
            'adtributor': self._run_adtributor,
            'r_adtributor': self._run_r_adtributor
        }
        
        # init dataframes
        self.df_metric_comparison = pd.DataFrame()
        self.df_metric_breakdown = pd.DataFrame()
        self.df_attribution_result = pd.DataFrame()

        # init report dataframes
        self.report_total = pd.DataFrame()  # report by metric breakdown
        self.report_dimension = pd.DataFrame()  # report by dimension breakdown
        self.report_attribution = pd.DataFrame()  # report by adtribution analysis
        print("AutoAnalysis initialized.")        

    # ======================== public methods ========================   
    # run analysis step by step
    def run_analysis(self, treatment_date, control_date, filter_str, 
                     step=-1,
                     attribution_dimensions = [], 
                     algorithm_name = "adtributor",
                     **attribution_args):
        
        # set query parameters
        self.treatment_date = treatment_date
        self.control_date = control_date
        # set Adtributor parameters
        # self.attribution_args = attribution_args

        """step1. get metric comparison"""
        if step == 1 or step == -1:
            self._run_metric_breakdown(filter_str)

        """step2. get metric comparison by dimension (optional)"""
        if step == 2:
            self._run_dimension_breakdown(filter_str)     

        """step3. get metric comparison by customized dimension"""
        if step == 3 or step == -1:
            self._run_attribution_analysis(filter_str, 
                                           attribution_dimensions, 
                                           algorithm_name,
                                           **attribution_args)
        
        return

    
    # ======================== private methods ========================
    # init metric config
    def _initial_metric_config(self):
        if self.metric == "mCFV":
            self.metric_config = mCFVConfig()

    def _calculate_contribution_by_factor(self, metric, variable):
        """
        calculate contribution by factor
        """
        if variable is None:
            return
        try:
            expression = self.metric_config.Metric_Expression.get(metric, "")  # "variable['mCFV/UU'] * variable['UU']" 
            res = eval(expression)
            return res
        except Exception as e:
            print(e)
            return

    def _call_calculate_contribution_by_factor(self, row, metric, sub_metric, sub_metrics):
        variable = {sub_metric: row[f"delta_{sub_metric}"]}
        remain_metrics = [m for m in sub_metrics if m != sub_metric]
        for k in remain_metrics:
            variable[k] = row[f'{k}_ctrl']
        return self._calculate_contribution_by_factor(metric, variable)

    def _get_filter_str_by_dimension(self, df, columns):
        filter_list = []
        for col in df.columns:
            if col not in columns:
                continue
            dimension_filter_list = []
            dimension_values = df[col].value_counts().index.tolist()
            if 'Others' in dimension_values:
                continue
            for value in dimension_values:
                q = self.metric_config.Titan_Query_Dimension_Value_Template.get(col, {}).get(value, "")
                if not q:
                    break
                dimension_filter_query = f"{q}"
                dimension_filter_list.append(dimension_filter_query)
            
            if not dimension_filter_list:
                continue
            dimension_filter_str = " OR ".join(dimension_filter_list)
            filter_list.append(f"({dimension_filter_str})")
        filter_str = " AND ".join(filter_list)
        return filter_str
    
    def _get_metric_function(self, metric):
        """
        get metric decomposition function from config
        """
        # get all the sub-metrics of the metric
        metric_list = [metric]
        metric_set = set()
        while metric_list:
            m = metric_list.pop(0)
            metric_set.add(m)
            metric_list += self.metric_config.Metrics_Breakdown.get(m, [])

        # build query string for each metric
        metric_query_list = []
        for m in metric_set:
            if "/" in m:
                numerator, denominator = m.split("/")
                numerator_query = self.metric_config.Metric_Query.get(numerator, "")
                denominator_query = self.metric_config.Metric_Query.get(denominator, "")
                if numerator_query and denominator_query:
                    metric_query_list.append(f"{numerator_query} / {denominator_query} AS `{m}`")
            else:
                query = self.metric_config.Metric_Query.get(m, "")
                if query:
                    metric_query_list.append(f"{query} AS {m}")
        return metric_set, ", ".join(metric_query_list)

    def _cast_metric_dtype(self, df):  
        print(self.metric_set)
        for col in df.columns:
            if col in self.metric_set:
                df[col] = df[col].astype(float)


    def _get_metric_comparison(self, filter_str):
        """
        get metric comparison from ClickHouse
        treatment_date: string, yyyy-mm-dd
        control_date: string, yyyy-mm-dd
        """
        # TODO: Change Table and Sample Table
        sql = f"""SELECT IF(EventDate = toDate('{self.treatment_date}'), 'Treatment', 'Control') AS Group
                , {self.metric_query_str}
                FROM MSNAnalytics_Sample
                WHERE EventDate IN (toDate('{self.treatment_date}'), toDate('{self.control_date}'))
                    AND IsNotExcludedStandard_FY24 = 1
                    AND ({filter_str})
                GROUP BY Group""" 
        print(f"sql:\n{sql}")
        data = self.titan_api.query_clickhouse(sql, "MSNAnalytics_Sample")
        if not data:
            print("No data found.")
            return pd.DataFrame()
        return pd.DataFrame(data)

    def _get_metric_comparison_by_dimension(self, filter_str):
        """
        get metric comparison by dimension from ClickHouse
        """
        dimension_query_list = [
            self.metric_config.Titan_Query_Dimension_Template.get("Canvas", "'AllUp' AS Canvas_"),
            self.metric_config.Titan_Query_Dimension_Template.get("Browser", "'AllUp' AS Browser_"),
            self.metric_config.Titan_Query_Dimension_Template.get("PageType", "'AllUp' AS PageType_"),
            self.metric_config.Titan_Query_Dimension_Template.get("Product", "'AllUp' AS Product_")
        ]

        dimension_query_str = ", ".join([d for d in dimension_query_list if d])
        filter_str = f" AND ({filter_str})" if filter_str else ""

        # TODO: Dimension template
        sql = f"""SELECT 
            Group
            , Canvas_ AS Canvas, Browser_ AS Browser, PageType_ AS PageType, Product_ AS Product
            , SUM(mCFV) AS mCFV
            , SUM(CPV) AS CPV
            , COUNT(1) AS UU
            , mCFV / UU AS `mCFV/UU`
            , CPV / UU AS `CPV/UU`
            , mCFV / CPV AS `mCFV/CPV`
        FROM
        (
            SELECT IF(EventDate = toDate('{self.treatment_date}'), 'Treatment', 'Control') AS Group
            , {dimension_query_str}
            , UserMUIDHash
            , SUM(mCFV_FY24)AS mCFV
            , SUM(IF(UserAction = 'View', IsCorePV, 0)) AS CPV
            FROM MSNAnalytics_Sample
            WHERE EventDate IN (toDate('{self.treatment_date}'), toDate('{self.control_date}'))
                AND IsNotExcludedStandard_FY24 = 1
                {filter_str}
            GROUP BY Group, Canvas_, Browser_, PageType_, Product_, UserMUIDHash
        ) t
        GROUP BY Group, Canvas, Browser, PageType, Product
        """
        print(f"sql:\n{sql}")
        data = self.titan_api.query_clickhouse(sql, "MSNAnalytics_Sample")
        if not data:
            print("No data found.")
            return pd.DataFrame()
        return pd.DataFrame(data)
    

    def _get_metric_comparison_by_customized_dimension(self, filter_str, dimension_list):
        # TODO: remove treatment_date, control_date
        """
        get metric comparison from ClickHouse
        treatment_date: string, yyyy-mm-dd
        control_date: string, yyyy-mm-dd
        """
        if len(dimension_list) == 0:
            print("Error: dimension_list is empty.")
            return pd.DataFrame()
        dimensions_str = ",".join(dimension_list)
        sql = f"""SELECT IF(EventDate = toDate('{self.treatment_date}'), 'Treatment', 'Control') AS Group
                , {dimensions_str}
                , {self.metric_query_str}
                FROM MSNAnalytics_Sample
                WHERE EventDate IN (toDate('{self.treatment_date}'), toDate('{self.control_date}'))
                    AND IsNotExcludedStandard_FY24 = 1
                    AND ({filter_str})
                GROUP BY Group, {dimensions_str}""" 
        print(f"sql:\n{sql}")
        data = self.titan_api.query_clickhouse(sql, "MSNAnalytics_Sample")
        if not data:
            print("No data found.")
            return pd.DataFrame()

        return pd.DataFrame(data)


    # 计算子 metric 对整体 metric 的贡献度
    def _calculate_contribution_by_submetric(self, df, metric):
        # layer0: calculate delta
        df[f'delta_{metric}'] = df[f'{metric}_treat'] - df[f'{metric}_ctrl']
        df[f'delta%_{metric}'] = df.apply(lambda x: safe_div(x[f'delta_{metric}'], x[f'{metric}_ctrl']), axis=1)
        # calculate every group's mCFV delta / total mCFV delta
        # df_merge[f'{metric}_Contribution%'] = df_merge[f'delta_{metric}'] / df_merge[f'delta_{metric}'].sum()
        sub_metrics = self.metric_config.Metrics_Breakdown.get(metric, [])
        if not sub_metrics:
            print(f"There is no sub-metrics for {metric}")
            return
        print(f"metric:{metric}, sub_metrics:{sub_metrics}")
        
        for sub_metric in sub_metrics:
            df[f'delta_{sub_metric}'] = df[f'{sub_metric}_treat'] - df[f'{sub_metric}_ctrl']

        df["total_contribution"] = 0
        for sub_metric in sub_metrics:
            df[f'{sub_metric}_Contribution'] = df.apply(
                lambda x: self._call_calculate_contribution_by_factor(x, metric, sub_metric, sub_metrics), axis=1)
            df["total_contribution"] = df["total_contribution"] + df[f'{sub_metric}_Contribution']

        for sub_metric in sub_metrics:
            df[f'{sub_metric}_Contribution%'] = df[f'{sub_metric}_Contribution'] / df["total_contribution"]
        return

    def _level_traverse_calculate_contribution(self, df):
            # get all the sub-metrics of the metric
            metric_list = [self.metric]
            while metric_list:
                m = metric_list.pop(0)
                self._calculate_contribution_by_submetric(df, m)
                # get next level sub-metrics
                metric_list += self.metric_config.Metrics_Breakdown.get(m, [])



    def _run_metric_breakdown(self, filter_str):
        """
        Get metric comparison by metric breakdown
        Metric breakdown function is predefined in the config file.
        """
        # 1-1. get metric comparison
        df = self._get_metric_comparison(filter_str)
        # if df is empty or df didnt contains Treatment or Control, raise exception
        if df.empty or not df["Group"].isin(["Treatment", "Control"]).all():
            raise Exception("No data found. Please check the Titan query.")
        self._cast_metric_dtype(df)
        if self.verbose:
            print(f"{__class__.__name__} get data by dimension: {df.shape}")

        # 1-2. merge two dataframes
        df["key"] = 1
        df_treat = df[df["Group"] == "Treatment"]
        df_ctrl = df[df["Group"] == "Control"]
        self.df_metric_comparison = pd.merge(df_treat, df_ctrl, on=['key'], suffixes=('_treat', '_ctrl'))
        # pprint(self.df_metric_comparison.head())

        # 1-3. calculate contribution
        self._level_traverse_calculate_contribution(self.df_metric_comparison)
        pprint(self.df_metric_comparison.head())

        # 1-4. report by metric function
        self.report_total = self._format_report(REPORT_METRIC_FUNCTION)


    def _run_dimension_breakdown(self, filter_str):
        """
        Get metric comparison by dimension
        Dimensions include Canvas, Browser, PageType, Product, which are predefined in the config file.
        """
        # 2-1. get metric comparison by dimension
        df = self._get_metric_comparison_by_dimension(filter_str)
        if df.empty or not df["Group"].isin(["Treatment", "Control"]).all():
            raise Exception("No data found. Please check the Titan query.")
        self.cast_metric_dtype(df)
        if self.verbose:
            print(f"{__class__.__name__} get data by dimension: {df.shape}")

        # 2-2. merge two dataframes
        df_treat = df[df["Group"] == "Treatment"]
        df_ctrl = df[df["Group"] == "Control"]
        self.df_metric_breakdown = pd.merge(df_treat, df_ctrl, 
                                            on=['Canvas', 'Browser', 'PageType', 'Product'],
                                            suffixes=('_treat', '_ctrl'))
        
        # calculate every group's metric delta / total metric delta
        self.df_metric_breakdown[f'delta_{self.metric}'] = self.df_metric_breakdown[f'{self.metric}_treat'] - self.df_metric_breakdown[f'{self.metric}_ctrl']
        self.df_metric_breakdown[f'delta%_{self.metric}'] = self.df_metric_breakdown.apply(
            lambda x: safe_div(x[f'delta_{self.metric}'], x[f'{self.metric}_ctrl']), axis=1)

        # calculate every group's mCFV delta / total mCFV delta
        self.df_metric_breakdown[f'{self.metric}_Contribution%'] = self.df_metric_breakdown[f'delta_{self.metric}'] / self.df_metric_breakdown[f'delta_{self.metric}'].sum()

        self.level_traverse_calculate_contribution(self.df_metric_breakdown)
        # sort by contribution
        self.df_metric_breakdown.sort_values(f'{self.metric}_Contribution%', ascending=False, inplace=True)
        # pprint(self.df_metric_breakdown.head())

        # 2-4. report by dimension contribution
        self.report_dimension = self.format_report(REPORT_DIMENSION)   


    def _run_attribution_analysis(self, filter_str: str, 
                                  attribution_dimensions: list, 
                                  algorithm_name: str, 
                                  **kwargs):

        if algorithm_name not in self.algorithms:
            raise Exception(f"Algorithm {algorithm_name} is not supported. Now only support {list(self.algorithms.keys())}")

        if len(attribution_dimensions) == 0:
            raise Exception("Error: attribution_dimensions is at least one dimension.")

        # 3-1. get metric comparison by customized dimension
        df = self._get_metric_comparison_by_customized_dimension(filter_str, attribution_dimensions)
        
        if df.empty or not df["Group"].isin(["Treatment", "Control"]).all():
            raise Exception("No data found. Please check the Titan query.")
        
        self._cast_metric_dtype(df)
        
        if self.verbose:
            print(f"{__class__.__name__} get data by dimension: {df.shape}")

        # refactor the dataframe
        df_t = df[df["Group"] == "Treatment"]
        df_c = df[df["Group"] == "Control"]
        df = pd.merge(df_c, df_t, on = attribution_dimensions, how="outer", suffixes=["_c", "_t"]).fillna(0)
        df.rename(columns={f"{self.metric}_c": "Control", f"{self.metric}_t": "Treatment"}, inplace=True)

        # # TODO: create a test dataframe
        # df = pd.DataFrame({
        #     "Canvas": ["Canvas1", "Canvas2", "Canvas3", "Canvas4", "Canvas5"],
        #     "Browser": ["Browser1", "Browser2", "Browser3", "Browser4", "Browser5"],
        #     "PageType": ["PageType1", "PageType2", "PageType3", "PageType4", "PageType5"],
        #     "Product": ["Product1", "Product2", "Product3", "Product4", "Product5"],
        #     "Control": [100, 200, 300, 400, 500],
        #     "Treatment": [110, 220, 330, 440, 550]
        # })

        if self.verbose:
            print(f"{__class__.__name__} Input data for adtribution analysis:")
            pprint(df.head())
        
        # 3-2. Call the adtributor_analysis
        algorithm_func = self.algorithms[algorithm_name]
        algorithm_func(df, attribution_dimensions, "Treatment", "Control", **kwargs)  # self.df_attribution_result will be updated.

        # 3-3. report by adtribution result
        self.report_attribution = self._format_report(REPORT_DIMENSION_ADTRIBUTION)

    
    def _run_adtributor(self, df: pd.DataFrame,
                        dimension_cols: list,
                        treatment_col: str,
                        control_col: str,
                        top_n_factors = 10,
                        TEEP = 0.05,
                        TEP = 1,
                        min_surprise = 0.0005,
                        max_item_num = 10,
                        need_negative_ep_factor = False,
                        verbose = 0):
        """
        TEEP: Minimum detectable EP value
        TEP: EP cumulative threshold
        dimension_cols must be found in data
        treatment_col and control_col must be found in data
        """
        # check if the columns are in the dataframe
        if not set(dimension_cols + [treatment_col, control_col]).issubset(set(df.columns)):
            raise Exception(f"Columns:{dimension_cols + [treatment_col, control_col]} not found in the dataframe.")
                
        analyzer = Adtributor(top_n_factors = top_n_factors,
                        TEEP = TEEP, 
                        TEP = TEP,
                        min_surprise = min_surprise, 
                        max_item_num = max_item_num,
                        need_negative_ep_factor = need_negative_ep_factor,
                        verbose = verbose)

        self.df_attribution_result = analyzer.analyze(
            data = df, 
            dimension_cols = dimension_cols, 
            treatment_col = treatment_col, 
            control_col = control_col)
        
        return

    def _run_r_adtributor(self, df: pd.DataFrame,
                        dimension_cols: list,
                        treatment_col: str,
                        control_col: str,
                        top_n_factors = 10,
                        TEEP = 0.05,
                        TEP = 1,
                        min_surprise = 0.0005,
                        max_item_num = 3,
                        max_dimension_num = 3,
                        max_depth = 3,
                        need_negative_ep_factor = False,
                        need_prune = True,
                        verbose = 0):
        """
        TEEP: Minimum detectable EP value
        TEP: EP cumulative threshold
        dimension_cols must be found in data
        treatment_col and control_col must be found in data
        """
        # check if the columns are in the dataframe
        if not set(dimension_cols + [treatment_col, control_col]).issubset(set(df.columns)):
            raise Exception(f"Columns:{dimension_cols + [treatment_col, control_col]} not found in the dataframe.")

        analyzer = RecursiveAdtributor(top_n_factors = top_n_factors,
                        TEEP = TEEP, 
                        TEP = TEP,
                        min_surprise = min_surprise, 
                        max_item_num = max_item_num,
                        max_dimension_num = max_dimension_num,
                        max_depth = max_depth,
                        need_negative_ep_factor = need_negative_ep_factor,
                        need_prune = need_prune,
                        verbose = verbose)

        self.df_attribution_result = analyzer.analyze(
            data = df, 
            dimension_cols = dimension_cols, 
            treatment_col = treatment_col, 
            control_col = control_col)
        
        return        


    def _format_report(self, mode):
        if mode == REPORT_METRIC_FUNCTION:
            df = self.df_metric_comparison
            report = []
            metric_list = [(self.metric, 0)]
            parent_metric_map = {}
            while metric_list:
                m, layer = metric_list.pop(0)
                record = {}
                record["layer"] = layer
                record["metric"] = m
                record["delta"] = df[f"delta_{m}"].sum() if f"delta_{m}" in df.columns else np.nan
                record["delta%"] = df[f"delta%_{m}"].sum() if f"delta%_{m}" in df.columns else np.nan
                record["contribution%"] = df[f"{m}_Contribution%"].sum() if f"{m}_Contribution%" in df.columns else 1
                record["parent_metric"] = parent_metric_map.get(m, "")
                report.append(record)
                sub_metrics = self.metric_config.Metrics_Breakdown.get(m, [])
                for sub_m in sub_metrics:
                    if sub_m not in parent_metric_map:
                        parent_metric_map[sub_m] = m
                        metric_list.append((sub_m, layer+1))
            # df.style.format({"delta": "{:,.4f}", "delta%": "{:.2%}", "contribution%": "{:.2%}"})        
            return pd.DataFrame(report)

        elif mode == REPORT_DIMENSION:
            df = self.df_metric_breakdown.head(self.top_n_factor)
            needed_cols = ["Canvas", "Browser", "PageType", "Product", f"delta_{self.metric}", f"delta%_{self.metric}", f"{self.metric}_Contribution%"]
            for sub_metric in self.metric_set:
                if sub_metric == self.metric:
                    continue
                needed_cols += [f"delta%_{sub_metric}", f"{sub_metric}_Contribution%"]
            df = df[needed_cols]
            # df.style.format({f"delta_{self.metric}": "{:,.4f}", f"delta%_{self.metric}": "{:.2%}", f"{self.metric}_Contribution%": "{:.2%}"})
            return df

        elif mode == REPORT_DIMENSION_ADTRIBUTION:
            df = self.df_attribution_result
            # df = self.df_attribution_result[self.df_attribution_result["Surprise"] >= self.min_surprice].head(self.top_n_atribution_factor)
            return df
        else:
            return pd.DataFrame()
    