import streamlit as st
import time

# Set a background image using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("assets/background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


properties = [
    {
        'type': '1 BHK',
        'sqft': 500,
        'price': 3500000,
        'location': 'Virar, Gokul Township',
        'images': [
            'assets/image1.jpeg',  
            'assets/2 bhk 1.jpeg',
            'assets/2bhk2.jpeg'
        ]
    },
    {
        'type': '2 BHK',
        'sqft': 750,
        'price': 3000000,
        'location': 'Virar, YK Nagar',
        'images': [
            'assets/2bhk3.jpeg',
            'assets/2bhk4.jpeg',
            'assets/2bhk5.jpeg'
        ]
    },
    {
        'type': '3 BHK',
        'sqft': 1200,
        'price': 4000000,
        'location': 'Virar, Mhada',
        'images': [
            'assets/3bhk1.jpeg',
            'assets/3bhk2.jpeg',
            'assets/3bhk3.jpeg',
            'assets/3bhk4.jpeg',
            'assets/3bhk5.jpeg'
        ]
    },
    {
        'type': '3BHK',
        'sqft': 350,
        'price': 3800000,
        'location': 'Virar, Global City',
        'images': [
            'assets/3bhk6.jpeg',
            'assets/3bhk7.jpeg',
            'assets/3bhk8.jpeg',
            'assets/3bhk9.jpeg',
            'assets/3bhk10.jpeg'
        ]
    },
    {
        'type': '4 BHK',
        'sqft': 1500,
        'price': 5500000,
        'location': 'Virar, Bachraj',
        'images': [
            'assets/4bhk1.jpeg',
            'assets/4bhk2.jpeg',
            'assets/4bhk3.jpeg',
            'assets/4bhk4.jpeg',
            'assets/4bhk5.jpeg',
            'assets/4bhk6.jpeg'
        ]
    },
    {
        'type': 'Penthouse',
        'sqft': 2500,
        'price': 5000000,
        'location': 'Vatar, RJ Beach',
        'images': [
            'assets/pent1.jpeg',
            'assets/pent2.jpeg',
            'assets/pent3.jpeg'
        ]
    },
    {
        'type': '2 BHK',
        'sqft': 850,
        'price': 3000000,
        'location': 'Virar, Bolinj',
        'images': [
            'assets/2bhk10.jpeg',
            'assets/2bhk11.jpeg',
            'assets/2bhk12.jpeg',
            'assets/2bhk13.jpeg'
        ]
    }
]

# Title and heading
st.title("Real Estate Property Listings 🏡")
st.write("Browse through our available properties below:")

# Loop through the properties and display them
for prop in properties:
    st.subheader(f"{prop['type']} - {prop['location']}")

    # Show property images in an automatic slideshow
    for i in range(len(prop['images'])):
        st.image(prop['images'][i], width=500)
        time.sleep(2)

    # Display property details
    st.write(f"**Price**: Rs {prop['price']:,.2f}")
    st.write(f"**Size**: {prop['sqft']} sqft")
    st.write(f"**Location**: {prop['location']}")
    st.markdown("---")
