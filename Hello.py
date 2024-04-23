import streamlit as st
import requests
import pandas as pd

# Function to fetch data from MySwitzerland API
def fetch_data(location, category, max_distance, limit=10):
    api_key = 'sIc2qS2gs7jrSld9nhih5ambBIQRDRE1qYV3pPi0'
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    params = {
        'location': location,
        'category': category,
        'radius': max_distance,
        'limit': limit
    }
    url = 'https://api.myswitzerland.com/v3/businesses/search'  # This URL needs to be corrected based on actual API documentation
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Set up the Streamlit app
def main():
    st.title("Campus Eats")
    st.write("Discover the best food and drinks near your campus in Switzerland!")

    # User input for API parameters
    location = st.text_input("Enter a location (e.g., Zurich, Geneva)", "Zurich")
    max_distance = st.slider('Maximum Distance from Campus (meters)', 100, 5000, 1000)
    selected_category = st.selectbox('Type of Place', options=['', 'bars', 'restaurants'])

    # Fetch data when user updates input
    if st.button('Search'):
        raw_data = fetch_data(location, selected_category, max_distance)
        if raw_data and 'businesses' in raw_data:
            businesses = raw_data['businesses']
            df = pd.DataFrame.from_records(businesses)
            st.write(df[['name', 'location', 'rating']])
        else:
            st.error("Failed to fetch data from MySwitzerland API.")

if __name__ == "__main__":
    main()
