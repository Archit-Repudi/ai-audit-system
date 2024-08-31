import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the DataFrame
df = pd.read_csv('transaction_data_with_anomalies.csv')

# Verify that the 'Anomaly' column exists
if 'Anomaly' not in df.columns:
    st.error("The 'Anomaly' column is missing from the DataFrame.")
else:
    st.title('Anomaly Detection Dashboard')
    st.write('This dashboard shows anomalies detected in transaction data.')

    # Plot histogram
    st.subheader('Transaction Amount Distribution')
    fig, ax = plt.subplots()
    ax.hist(df['Amount'], bins=50, alpha=0.5, label='All Transactions')
    ax.hist(df[df['Anomaly'] == 1]['Amount'], bins=50, alpha=0.5, label='Anomalies')
    ax.legend()
    
    st.pyplot(fig)

    # Display detected anomalies
    st.subheader('Detected Anomalies')
    st.write(df[df['Anomaly'] == 1])
