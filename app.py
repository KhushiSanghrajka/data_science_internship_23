import streamlit as st
import pandas as pd
import numpy as np
import os
from matplotlib import image
import plotly.express as px

st.title(":red[Innomatics] Data Science 23 ")
st.header("Data App using streamlit")
st.snow()


st.title(":blue[Titanic Survival Analysis]")


data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
st.dataframe(data)

var=st.selectbox("Bar Chart",("Pclass","Sex","Embarked"))
df=data.groupby([var,"Survived"])[["Age"]].count().reset_index()
fig = px.bar(x=df[var], y=df["Age"], color=df["Survived"])
st.plotly_chart(fig)

var=st.selectbox("Histogram Chart",("Age","Fare"))
fig = px.histogram(data, x=var)
st.plotly_chart(fig)