import os
import pandas as pd
from cytoolz.curried import groupby


def load_user_config():
    user_config = groupby(
        'name'
        , pd.read_csv(
            filepath_or_buffer=os.path.join(os.getcwd(), '..', '..', 'gillescommon', 'gillescommon', "config", "user_config.csv")
            , encoding="gbk"
        ).query(
            "account == account and account not in ('', r'/')"
        ).to_dict("records")
    )
    return user_config
