import streamlit as st
import pandas as pd
import csv

def read_data_from_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def search(keyword):
    data_from_scraped_data_csv = read_data_from_csv('flask-web-main/Project/scraped_data.csv')
    filtered_data = [row for row in data_from_scraped_data_csv if any(keyword.lower() in str(value).lower() for value in row.values())]
    return filtered_data

def main():
    st.title('Scraped Data')

    # Read scraped data from CSV
    data_from_scraped_data_csv = read_data_from_csv('flask-web-main/Project/scraped_data.csv')

    # Display the first 10 entries of scraped data in a table
    st.header('First 10 Entries of Scraped Data')
    df_first_10_entries = pd.DataFrame(data_from_scraped_data_csv[:10])
    st.write(df_first_10_entries)

    # Search functionality
    st.header('Search Data')
    keyword = st.text_input('Enter Keyword')
    if st.button('Search'):
        search_results = search(keyword)
        if search_results:
            st.write('Search Results:')
            for result in search_results:
                st.write(result)
        else:
            st.write('No results found.')

if __name__ == '__main__':
    main()
