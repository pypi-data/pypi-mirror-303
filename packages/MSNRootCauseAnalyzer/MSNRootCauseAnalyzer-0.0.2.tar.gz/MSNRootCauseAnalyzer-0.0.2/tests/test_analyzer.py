import os, sys
# set sys.path to import the src module
current_path = os.path.dirname(__file__)
print(f"current path: {current_path}")
print(f"add path: {os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))}")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import numpy as np
import pandas as pd
from pprint import pprint

from src.root_cause_analyzer import get_analyzer
from src.root_cause_analyzer.algorithms.adtributor import Adtributor, RecursiveAdtributor

class TestRootCauseAnalyzer(unittest.TestCase):
    def test_algorithm_a(self):
        analyzer = get_analyzer('adtributor', top_n_factors=5, verbose=0)
        result = analyzer.analyze(data={})
        self.assertEqual(result, "Result from Adtributor")

    def test_algorithm_b(self):
        analyzer = get_analyzer('r_adtributor', top_n_factors=5, verbose=0)
        result = analyzer.analyze(data={})
        self.assertEqual(result, "Result from RecursiveAdtributor")

def test_Adtributor():
    df0 = pd.read_csv("C:\\Users\\yankunwang\\OneDrive - Microsoft\\MS Work\\git\\CSAnalysisAndExperiment\\ContentServiceExpApi\\tests\\data\\Test_mCFV_breakdown.csv")
    df_t = df0[df0["Group"] == "Treatment"]
    df_c = df0[df0["Group"] == "Control"]
    df = pd.merge(df_c, df_t, on=["Canvas", "Browser", "PageType", "Product", "PageName", "PageVertical"], how="outer", suffixes=["_c", "_t"]).fillna(0)
    df.rename(columns={"mCFV_c": "predict", "mCFV_t": "real"}, inplace=True)
    pprint(df.head())
    analyzer = Adtributor(top_n_factors=5,
                          max_item_num=3,
                          TEEP=0.05, 
                          TEP=1,
                          min_surprise=5e-04, 
                          need_negative_ep_factor=False,
                          verbose=1)

    res = analyzer.analyze(data=df, dimension_cols=["Canvas", "Browser","PageName", "PageVertical"], treatment_col="real", control_col="predict")
    print("\n\nfinal RCA Result:")
    pprint(res)


def test_RecursiveAdtributor():
    df0 = pd.read_csv("C:\\Users\\yankunwang\\OneDrive - Microsoft\\MS Work\\git\\CSAnalysisAndExperiment\\ContentServiceExpApi\\tests\\data\\Test_mCFV_breakdown.csv")
    df_t = df0[df0["Group"] == "Treatment"]
    df_c = df0[df0["Group"] == "Control"]
    df = pd.merge(df_c, df_t, on=["Canvas", "Browser", "PageType", "Product", "PageName", "PageVertical"], how="outer", suffixes=["_c", "_t"]).fillna(0)
    df.rename(columns={"mCFV_c": "predict", "mCFV_t": "real"}, inplace=True)
    pprint(df.head())

    analyzer = RecursiveAdtributor(top_n_factors=5,
                          max_item_num=3,
                          max_dimension_num=3,
                          max_depth=3,
                          TEEP=0.08, 
                          TEP=1,
                          min_surprise=5e-04, 
                          need_negative_ep_factor=False,
                          need_prune = True,
                          verbose=0)
    
    res = analyzer.analyze(data=df, dimension_cols=["Canvas", "Browser", "Product", "PageName", "PageVertical"], treatment_col="real", control_col="predict")
    print("\n\nfinal RCA Result:")
    print(res)
    # C:\Users\yankunwang\OneDrive - Microsoft\MS Work\000-Analysis\000-Auto Analysis
    res.to_csv("C:\\Users\\yankunwang\\OneDrive - Microsoft\\MS Work\\000-Analysis\\000-Auto Analysis\\tests\\RCA_result.csv", index=False)

if __name__ == '__main__':
    unittest.main()
    # test_Adtributor()
    # test_RecursiveAdtributor()
