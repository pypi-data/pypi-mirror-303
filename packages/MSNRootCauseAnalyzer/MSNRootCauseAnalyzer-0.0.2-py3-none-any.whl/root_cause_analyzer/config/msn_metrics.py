
from .base_metric_config import BaseMetricConfig


class mCFVConfig(BaseMetricConfig):
    def __init__(self):
        super().__init__()
        self.metric_name = "mCFV"

        # TODO: Only multiplication is supported.
        self.Metrics_Breakdown = {
            "mCFV" : ["mCFV/UU", "UU"],
            "mCFV/UU" : ["CPV/UU", "mCFV/CPV"]
        }

        # should be aligned with TITAN definition
        self.Metric_Query = {
            "mCFV" : "SUM(mCFV_FY24)",  # TODO: will change every FY
            "CPV" : "SUM(IF(UserAction = 'View', IsCorePV, 0))",
            "UU" : "COUNT(DISTINCT UserMUIDHash)"
        }

        self.Metric_Expression = {
            "mCFV": "variable['mCFV/UU'] * variable['UU']",
            "mCFV/UU": "variable['CPV/UU'] * variable['mCFV/CPV']",
            "CPV": "variable['CPV/UU'] * variable['UU']"
        }

        self.Titan_Query_Dimension_Template = {
            "Canvas": """CASE WHEN Canvas IN ('Anaheim DHP', 'Anaheim NTP', 'EnterpriseNews NTP') THEN 'All-Up Anaheim'
            WHEN Canvas IN ('WindowsShell Taskbar', 'WindowsP2Shell', 'Enterprise WindowsP2Shell') THEN 'Prong1&2'
            WHEN Canvas IN ('Win 10 Prime', 'Downlevel Prime') THEN 'msn.com'
            WHEN Canvas IN ('AndroidApp', 'IOSApp') THEN 'SuperApp'
            ELSE 'Others' END AS Canvas_""",  # add suffix to avoid conflict with other columns
            
            "Browser": """CASE WHEN lower(Browser) LIKE '%edg%' THEN 'Edge'
            ELSE 'Others' END AS Browser_""",
            
            "PageType": """CASE WHEN lower(PageVertical) == 'homepage' THEN 'Homepage' 
            WHEN lower(PageType) IN ('article', 'gallery', 'video', 'watch') THEN 'Consumption'
            WHEN lower(PageType) NOT IN ('article', 'gallery', 'video', 'watch') 
            AND lower(PageVertical) IN ('sports', 'weather', 'traffic', 'finance', 'casualgames', 'shopping', 'autos') 
            THEN 'Verticals'
            ELSE 'Others' END AS PageType_""",

            "Product": """CASE WHEN Product IN ('anaheim', 'entnews') THEN Product
            WHEN Product IN ('windowsshell', 'windowsdash', 'entwindowsdash', 'windows') THEN Product
            WHEN Product IN ('SuperAppHP', 'SuperAppNews', 'SuperAppBing') THEN Product
            ELSE 'Others' END AS Product_"""
        }


        self.Titan_Query_Dimension_Value_Template = {
            "Canvas": {
                "All-Up Anaheim": "Canvas IN ('Anaheim DHP', 'Anaheim NTP', 'EnterpriseNews NTP')",
                "Prong1&2": "Canvas IN ('WindowsShell Taskbar', 'WindowsP2Shell', 'Enterprise WindowsP2Shell')",
                "msn.com": "Canvas IN ('Win 10 Prime', 'Downlevel Prime')",
                "SuperApp": "Canvas IN ('AndroidApp', 'IOSApp')"
            },
            "Browser": {
                "Edge": "lower(Browser) LIKE '%edg%'"
            },
            "PageType": {
                "Homepage": "lower(PageVertical) == 'homepage'",
                "Consumption": "lower(PageType) IN ('article', 'gallery', 'video', 'watch')",
                "Verticals": """lower(PageType) NOT IN ('article', 'gallery', 'video', 'watch') 
                                AND lower(PageVertical) IN ('sports', 'weather', 'traffic', 'finance', 'casualgames', 'shopping', 'autos')"""
            },
            "Product": {
            }
        }