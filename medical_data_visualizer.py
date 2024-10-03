import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight'] / (df['height']/100) ** 2)>25).astype(int)
df.head()

# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['id', 'cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                        var_name='variable', value_name='total')


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'total']).size().reset_index(name='count')
    

    # 7
    sns.catplot(data=df_cat, x='variable', y='count', hue='total', col='cardio',
             kind='bar')


    # 8
    fig = sns.catplot(data=df_cat, x='variable', y='count', hue='total', col='cardio',
             kind='bar')


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['ap_lo'] <= df['ap_hi'])
        ]
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)





    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(data=corr, mask=mask, annot=True, fmt=".1f", square=True, cbar=False, ax=ax)


    fig = fig.figure
    # 16
    fig.savefig('heatmap.png')
    return fig
