import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

alt.data_transformers.enable('default', max_rows=None)

def line_plot1(df):
    data_1 = df.loc[:, ['year', 'cpi2010']].groupby('year').mean().reset_index()

    scatter1 = alt.Chart(data_1).mark_line().encode(
        x = 'year:N',
        y = alt.Y('cpi2010:Q', title = 'Average Global CPI')
    ).properties(
        width = 400,
        height = 200
    )

    return scatter1

def line_plot2(df):
    scatter2 = alt.Chart(df.loc[:, ['year','prop']].groupby(['year']).mean().reset_index()).mark_line().encode(
        x = 'year:N',
        y = alt.Y('prop:Q', title = 'Avg Prop. of Kids that completed grades 1-9',scale = alt.Scale(zero = False))
    ).properties(
        width = 400,
        height = 200
    )
    return scatter2

def line_plot3(df):
    scatter3 = alt.Chart(df.loc[:, ['year','prop','sex']].groupby(['year', 'sex']).mean().reset_index()).mark_line().encode(
        x = 'year:N',
        y = alt.Y('prop:Q', title = 'Avg Prop. of Kids that completed grades 1-9',scale = alt.Scale(zero = False))
    ).properties(
        width = 400,
        height = 200
    ).facet(
        column = 'sex'
    )
    return scatter3

def line_plot4(df):
    scatter4 = alt.Chart(df.loc[:, ['year','prop','location']].groupby(['year', 'location']).mean().reset_index()).mark_line().encode(
        x = 'year:N',
        y = alt.Y('prop:Q', title = 'Avg Prop. of Kids that completed grades 1-9',scale = alt.Scale(zero = False))
    ).properties(
        width = 400,
        height = 200
    ).facet(
        column = 'location'
    )
    return scatter4
