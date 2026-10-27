import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    st.title("Used Car Seling Price Prediction")

    img = Image.open('cars.jpg')
    st.image(img)

    st.header(
            ''' 
            Planning on Selling Your Car? Check How Much Your Car Worth Here!
            '''
        )

    data = pd.read_csv('cardekho.csv')


    st.header('Dataset Overview')

    st.write(
        '''
        The dataset contains information about used cars,
        including vehicle year, kilometers driven, fuel type,
        transmission, engine capacity, mileage, maximum power,
        number of seats, and selling price.
        '''
    )

# Display data
    st.dataframe(
        data.head(20),
        use_container_width=True
    )

    st.subheader('Dataset Information')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            'Number of Rows',
            data.shape[0]
        )

    with col2:
        st.metric(
            'Number of Columns',
            data.shape[1]
        )

    with col3:
        st.metric(
            'Missing Values',
            data.isnull().sum().sum()
        )

# Desvcriptive stat
    st.subheader('Descriptive Statistics')

    st.dataframe(
        data.describe(),
        use_container_width=True
    )


    # -----------------------------------------------------
    # SELLING PRICE DISTRIBUTION
    # -----------------------------------------------------

    st.header('Exploratory Data Analysis')

    st.subheader(
        'Distribution of Selling Price'
    )

    fig = plt.figure(figsize=(10, 5))

    sns.histplot(
        data=data,
        x='selling_price',
        bins=30,
        kde=True
    )

    plt.xlabel('Selling Price')
    plt.ylabel('Frequency')
    plt.title(
        'Distribution of Used Car Selling Price'
    )

    st.pyplot(fig)

    st.write(
        '''
        This visualization shows the distribution of selling
        prices in the dataset. It can be used to identify the
        most common price range and the presence of vehicles
        with relatively high selling prices.
        '''
    )

# Top car brand
    st.subheader('Top Car Brands')

    brand = (
        data['name']
        .str.split()
        .str[0]
    )

    top_brands = (
        brand
        .value_counts()
        .head(10)
    )

    fig = plt.figure(figsize=(10, 5))

    sns.barplot(
        x=top_brands.values,
        y=top_brands.index
    )

    plt.xlabel('Number of Cars')
    plt.ylabel('Brand')
    plt.title(
        'Top 10 Car Brands in Dataset'
    )

    st.pyplot(fig)



if __name__ == '__main__':
    run()