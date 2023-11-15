# import warnings
# warnings.filterwarnings("ignore")
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from data_preprocess import data_preprocess

# def visualise_data():
#     data, numerical_features, categorical_features = data_preprocess()
#     # visualisation of categorical_features
#     for categorical_column in categorical_features:
#         fig, axs = plt.subplots(figsize=(5,5))
#         sns.countplot(data=data, x=categorical_column)
#         plt.show()
#     #Distrubution of numerical features
#     for numerical_feature in numerical_features:
#         fig, axs = plt.subplots(figsize=(5,4))
#         sns.distplot(data[numerical_feature])
#         plt.xlabel(numerical_feature)
#         plt.show()
#     #finding outliers in numerical features
#     for numerical_feature in numerical_features:
#         fig, axs = plt.subplots(figsize=(5,4))
#         sns.boxplot(data[numerical_feature])
#         plt.xlabel(numerical_feature)
#         plt.show()
#     # Correlation matrix
#     data_num = data[numerical_features]
#     corr = data_num.corr()
#     plt.figure(figsize = (12,12))
#     mp = sns.heatmap(corr, linewidth = 1 ,  annot=True, cmap="coolwarm", fmt=".2f")
#     plt.show()
#     return data

# visualise_data()

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import plotly.express as px
from data_preprocess import data_preprocess
import plotly.figure_factory as ff
import plotly.graph_objects as go

def visualise_data():
    data, numerical_features, categorical_features = data_preprocess()
    # fig = ff.create_distplot([data[c] for c in numerical_features], numerical_features, bin_size=.25, show_rug=False)
    # fig.show()
    data_num = data[numerical_features]
    data_num_corr = data_num.corr()
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x = data_num_corr.columns,
            y = data_num_corr.index,
            z = np.array(data_num_corr),
            text=data_num_corr.values,
            texttemplate='%{text:.2f}',
            
        )
    )
    fig.update_layout(template='plotly_dark')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.show()
    for numerical_feature in numerical_features:
        fig = ff.create_distplot([data[numerical_feature]], [numerical_feature], show_rug=False)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(title_text=numerical_feature, showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()
    
    for numerical_feature in numerical_features:
        fig = px.box(data, y=numerical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False,zeroline=True,zerolinewidth=4)
        fig.show()
    
    for categorical_feature in categorical_features:
        fig = px.histogram(data, x=categorical_feature)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()

visualise_data()
