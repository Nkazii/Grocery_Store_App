import streamlit as st
from projects_dao import get_all_products  
st.title("Welcome To Your Online Grocery Store")

# Add a button to trigger fetching data
if st.button('Get Products'):
    products = get_all_products()  # Call the function from database.py
    
    if products:
        # Display results in a table format
        st.write("Products:")
        st.table(products)
    else:
        st.write("No products found or error occurred.")

if st.button('Select Products'):
    products = get_all_products()  # Call the function from database.py
    product_names = [product['name'] for product in products]
    selected_products = st.multiselect('Select one or more products', product_names)

#   Display details for each selected product
    if selected_products:
        st.write("Selected Product Details:")
        for product_name in selected_products:
            selected_details = next((product for product in products if product['Name'] == product_name), None)
            st.write(f"Details for {product_name}:")
            st.json(selected_details)
