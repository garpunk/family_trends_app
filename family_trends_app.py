'''
Author: Garrett Helms
File: family_trend.py
Date: May 15th 2024
Purpose: creating a user interface to 
interact with data from family trends project.

'''

import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt


pytrends = TrendReq(hl='en-US', tz=360)

def main():
    st.title('Family Trends')

    # Input box for the search term
    search_term = st.text_input('Enter a search term:', '')

    # Button to submit the search term
    if st.button('Get Trends'):
        if search_term:
            # Fetch the trends data
            fetch_trends(search_term)
        else:
            st.warning('Please enter a search term.')

def fetch_trends(term):
    # Build the payload for Pytrends
    pytrends.build_payload([term], cat=0, timeframe='today 12-m', geo='', gprop='')

    # Retrieve interest over time
    data = pytrends.interest_over_time()

    if not data.empty:
        # Plot the data
        st.write(f"Search trends for: {term}")

        # Drop the 'isPartial' column if it exists
        if 'isPartial' in data.columns:
            data = data.drop(columns=['isPartial'])

        st.line_chart(data)
    else:
        st.warning('No data available for the entered term.')

if __name__ == '__main__':
    main()
