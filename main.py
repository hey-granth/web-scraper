import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

st.title('AI Web Scraper')
url = st.text_input('Enter a website URL:')

if st.button("Scrape Site"):
    st.write(f"Scraping {url}...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)
    st.session_state.dom_content = clean_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", value=clean_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area('Describe what you wanna parse?')
    if st.button("Parse Content"):
        st.write(f"Parsing {parse_description}...")
        dom_chunks = split_dom_content(st.session_state.dom_content)
