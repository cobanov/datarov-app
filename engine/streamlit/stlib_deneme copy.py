from os import wait
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(data_uploaded):
    data = pd.read_csv(data_uploaded)
    return data


def select_data(data):
    global first_column, second_column, xmin_line, xmax_line, ymin_line, ymax_line, first_min, first_max, second_min, second_max

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


st.cache(allow_output_mutation=False)


def plot_data(data):
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

    ax.scatter(data[first_column], data[second_column])

    return fig, ax


@st.cache
def crop_data(data):
    data = data[
        (data[first_column] > xmin_line) &
        (data[first_column] < xmax_line) &
        (data[second_column] > ymin_line) &
        (data[second_column] < ymax_line)]
    return data


def make_cmap(data):
    correlation_map = data.corr()
    st.dataframe(correlation_map)

    fig = plt.figure()
    sns.heatmap(correlation_map, annot=True)
    return fig


def show_plot(data):
    fig, ax = plot_data(data)
    st.pyplot(fig)


def main():
    st.title("Datarov")
    st.write(
        "Datarov ile basit .csv uzantılı dosyaları modele uygulamaya uygun hale getirebilirsin.")

    sidebar = st.sidebar.radio(
        "Sidebar", ["Crop Data", "Correlation Map", "Dist Plots"])

    data_uploaded = st.file_uploader("Data path")

    try:
        data = load_data(data_uploaded)
        if sidebar == "Crop Data":

            st.subheader("Head")
            st.dataframe(data.head())
            st.subheader("Tail")
            st.dataframe(data.tail())

            st.subheader("Describe")
            st.dataframe(data.describe().T)

            select_data(data)
            show_plot(data)

            if st.button("Crop Data"):
                data = crop_data(data)
                fig, ax = plot_data(data)
                st.pyplot(fig)

        st.write(data.shape)

        # Correlation Map
        if sidebar == "Correlation Map":
            st.header("Correlation Map")
            fig = make_cmap(data)
            st.pyplot(fig)

        # Dist Plots
        if sidebar == "Dist Plots":
            st.header("Distribution Plots")
            column_name = st.multiselect("Select a column", data.columns)

            fig = plt.figure()
            for col in column_name:
                sns.distplot(data[[col]])
            st.pyplot(fig)
    except ValueError:
        pass


if __name__ == "__main__":
    main()
