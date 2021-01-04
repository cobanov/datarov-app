import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("engine/datasets/iris.csv")

st.title("Datarov")
st.write("Datarov ile basit .csv uzantılı dosyaları modele uygulamaya uygun hale getirebilirsin.")

first_column = st.selectbox('Please select x axis', data.columns)
second_column = st.selectbox('Please select y axis', data.columns)

first_min = float(data[first_column].min())
first_max = float(data[first_column].max()+1)

second_min = float(data[second_column].min())
second_max = float(data[second_column].max()+1)

xmin_line = st.slider("X Min Axis", first_min, first_max)
xmax_line = st.slider("X Max Axis", first_min, first_max)
ymin_line = st.slider("Y Min Axis", second_min, second_max)
ymax_line = st.slider("Y Max Axis", second_min, second_max)

fig, ax = plt.subplots()
ax.scatter(data[first_column], data[second_column])

plt.xlabel(first_column)
plt.ylabel(second_column)

plt.hlines((ymin_line, ymax_line), first_min, first_max, color="b")
plt.vlines((xmin_line, xmax_line), second_min, second_max, color="b")

plt.fill_between(np.linspace(xmin_line, xmax_line), ymin_line, ymax_line, color="g", alpha=0.3)

st.pyplot(fig)

if st.button("Crop Data"):
    pass