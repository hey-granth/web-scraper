import streamlit as st

st.title('AI Web Scraper')
url = st.text_input('Enter a website URL:')

if st.button("Scrape Site"):
    st.write(f"Scraping {url}...")
    # Scrape the website here
    st.write("Scraping complete!")