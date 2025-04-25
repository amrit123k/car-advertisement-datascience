import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('cleaned_data.csv')

st.header('Vehicle Analysis')
filtered_df = df[df['model_year'] >= 1990]
df[['price', 'days_listed']] = df[['price', 'days_listed']].astype(float)
filtered_df[['price', 'days_listed']] = filtered_df[['price', 'days_listed']].astype(float)
# Fix unnamed columns
df.columns = [f'col_{i}' if col is None else col for i, col in enumerate(df.columns)]
filtered_df.columns = [f'col_{i}' if col is None else col for i, col in enumerate(filtered_df.columns)]

if st.checkbox("Include Model Years before 1990"):
    st.dataframe(df)
else:
    st.dataframe(filtered_df)

fig = px.histogram(df, x='type', title='Distribution of Vehicle Types')
st.plotly_chart(fig)

fig = px.scatter(df, x='odometer', y='price', color='condition',
                 title='Price vs Odometer by Condition',
                 labels={'odometer': 'Mileage', 'price': 'Price ($)'})
st.plotly_chart(fig)

df_price_year = df.groupby('model_year')['price'].mean().reset_index()
df_price_year = df_price_year[df_price_year['model_year']>=1974]
df_price_year = df_price_year.sort_values(by = 'model_year')
fig = px.line(df_price_year,
              x='model_year',
              y='price',
              title='Price Inflation Over the Years')
st.plotly_chart(fig)

df_transmission = df.groupby('model_year',)['transmission'].value_counts().reset_index()
df_transmission = df_transmission[df_transmission['model_year'] >= 1995]
fig = px.bar(df_transmission,
             x='model_year',
             y='count',
             color='transmission',
             title='Transmission Type Counts by Model Year',
             barmode='stack')
st.plotly_chart(fig)


