from os import replace, wait
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Datarov")
st.write(
    "Datarov ile basit .csv uzantılı dosyaları modele uygulamaya uygun hale getirebilirsin.")


@st.cache()
def load_data():
    data_uploaded = st.file_uploader("Data path")
    data = pd.read_csv(data_uploaded)
    return data


data = load_data()

if data is not None:
    first_column = st.selectbox('Please select x axis', data.columns)
    second_column = st.selectbox('Please select y axis', data.columns)

    first_min = float(data[first_column].min())
    first_max = float(data[first_column].max())

    second_min = float(data[second_column].min())
    second_max = float(data[second_column].max())

    xmin_line = st.slider("X Min Axis", first_min*0.9,
                            first_max*1.1, first_min)
    xmax_line = st.slider("X Max Axis", first_min*0.9,
                            first_max*1.1, first_max)
    ymin_line = st.slider("Y Min Axis", second_min*0.9,
                            second_max*1.1, second_min)
    ymax_line = st.slider("Y Max Axis", second_min*0.9,
                            second_max*1.1, second_max)

    fig, ax = plt.subplots()

    plt.xlabel(first_column)
    plt.ylabel(second_column)
    plt.grid(linestyle=":")

    plt.hlines((ymin_line, ymax_line),
                first_min*0.9, first_max*1.1, color="b")
    plt.vlines((xmin_line, xmax_line),
                second_min*0.9, second_max*1.1, color="b")

    plt.fill_between(np.linspace(xmin_line, xmax_line),
                        ymin_line, ymax_line, color="g", alpha=0.3)

    data = data[
        (data[first_column] > xmin_line) &
        (data[first_column] < xmax_line) &
        (data[second_column] > ymin_line) &
        (data[second_column] < ymax_line)]

    ax.scatter(data[first_column], data[second_column])

    st.pyplot(fig)

    st.write(data.index)

    if st.button("Crop Data"):
        st.write("Data has been saved!")
