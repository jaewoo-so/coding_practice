import numpy as np
import pandas as pd
import datetime

def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here


    '''
    output = [ [df1 , df2]  , [df1 , df2] ]

    df1.columns = ['date {YYYY-MM-DD}' , 'vol {vol of that day}'] # highest vol
    df2.columns = ['date {YYYY-MM-DD}' , 'close {close of that day}'] # highest closing prices in year 

    # 같은 값이면 날짜이면 다 포함 


    '''

    def get_max_dt_each(dfgrp, max_vl, trg_col):
        res = []
        for yr in dfgrp.groups.keys():
            max_vl_yr = max_vl.loc[max_vl.index == yr]
            df_yr = dfgrp.get_group(yr)
            df_sel = df_yr.loc[df_yr[trg_col] == float(max_vl_yr[trg_col])]
            res.append(df_sel)
        return pd.concat(res , ignore_index  = True)

    def to_dt(date):
        try:
            return pd.to_datetime(date)
        except Exception as e:
            print(e)
            return pd.Nat


    # load data to df 
    
    res_list = []
    for path in files:
        df_raw = pd.read_csv(path)

        # extract year
        try:
            df_raw['dt'] = pd.to_datetime(df_raw['date'].apply(lambda x : str(x).strip()), errors='coerce') 
        except: 
            dt_res = []
            for sdt in df_raw['date']:
                dt_temp = datetime.datetime.strptime( sdt, '%Y-%m-%d %H:%M:%S').strftime("%Y-%m-%d")
                dt_res.append(dt_temp)
            df_raw['dt'] = dt_res
        df_raw['year'] = df_raw['dt'].dt.year

        # get vol , get close 
        df_vol = df_raw[['year','date','vol']]
        df_cls = df_raw[['year','date','close']]


        # group by year 
        dfgrp_vol = df_vol.groupby('year')
        dfgrp_cls = df_cls.groupby('year')

        # get max of each year
        max_vol = dfgrp_vol.max()
        max_cls = dfgrp_cls.max()

        # get date == max
        max_vol_dates = get_max_dt_each(dfgrp_vol,max_vol,'vol')[['date','vol']] 
        max_cls_dates = get_max_dt_each(dfgrp_cls,max_cls,'close')[['date','close']]

        res_list.append([max_vol_dates,max_cls_dates])


    return res_list


