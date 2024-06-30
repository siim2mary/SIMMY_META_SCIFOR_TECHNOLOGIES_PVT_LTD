import streamlit as st

def main():
    page = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])
    
    if page == "Home":
        st.title("Home Page")
        st.write("Welcome to the Home page!")
        
    elif page == "About":
        st.title("About Page")
        st.write("This is the About page. Learn more about us here.")
        
    elif page == "Contact":
        st.title("Contact Page")
        st.write("Contact us at contact@example.com.")

if __name__ == "__main__":
    main()
