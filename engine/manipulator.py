import pandas as pd
import streamlit


class Data:
    def __init__(self, path):
        self.path = path
        self.raw_data = None
        self.columns = None

    def read_data(self):
        self.raw_data = pd.read_csv(self.path)
        self.columns = pd.Series(self.raw_data.columns)

    def select_columns(self):
        print("Please select two columns shown under below:")

        for idx, col in enumerate(self.columns):
            print(idx, col)
        self.first_column = int(input("Select first:"))
        self.second_column = int(input("Select second:"))

        print("Choosen columns are showing under below:")
        print(self.columns[[self.first_column, self.second_column]])

    def selected_data(self):
        data_to_visualize = self.raw_data.iloc[:, [self.first_column, self.second_column]]
        return data_to_visualize



data1 = Data("engine/datasets/iris.csv")
data1.read_data()
data1.select_columns()
data_to = data1.selected_data()


st.title("Datarov")
st.write("Datarov ile basit .csv uzantılı dosyaları modele uygulamaya uygun hale getirebilirsin.")

