import pandas as pd
import streamlit as st
#from pathlib import Path
from streamlit_pdf_viewer import pdf_viewer
# Function to read the content of a markdown file
import base64
import os


direc = os.getcwd()

# Display PDF with custom zoom, alignment, and separators
pdf_viewer(
    f"{direc}/pages/appdata/Privacy_Policy_Final.pdf",
    width=700,
    height=1000,
    zoom_level=1.2,                    # 120% zoom
    viewer_align="center",             # Center alignment
    show_page_separator=True           # Show separators between pages
)

logofile = f'{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png'
st.logo(logofile, size="medium", link='https://alphaledgr.com/',
        icon_image=logofile)
url_stripe = "https://buy.stripe.com/6oU28t21Y2NmbfjdkK0480h"
url_stripe_2 = "https://buy.stripe.com/dR64iacsh6bx9zi5kk"
st.sidebar.image(logofile, use_container_width=True)
st.sidebar.link_button("Access/day!", url_stripe, type="primary",
                       disabled=False, use_container_width=True)
st.sidebar.link_button("Become a Patron!", url_stripe_2, type="primary",
                       disabled=False, use_container_width=True)
st.write("  ---------------------------------------------------------------  ")
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")

