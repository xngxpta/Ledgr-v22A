# Created on Mon Dec 12 00:34:13 2022
# Author: r_xngxpta; xngxpta@gmail.com
# !/usr/bin/env python310
# -*- coding: utf-8 -*-
# __author__ = 'R. Sengupta | r_xn'
# __copyright__ = 'Copyright 2023, Ledgr | www.alphaLedgr.com'
# __credits__ = ['r_xn, s.sengupta, adasgupta@gmail.com']
# __license__ = 'Ledgr | alphaledgr.com'
# __version__ = '01.02.04'
# __maintainer__ = 'r_xn@alphaledgr.com'
# __emails__ = 'r_xn@alphaledgr.com / response@alphaledgr.com'
# __status__ = 'In active development'

# Imports
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib as plt
from pypfopt.efficient_frontier import EfficientFrontier

# from pypfopt import objective_functions, plotting
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices
from pypfopt import HRPOpt
from pypfopt import CLA
from pypfopt import EfficientSemivariance
from pypfopt import EfficientCVaR

# import copy
import os
import datetime as dt
from pypfopt.expected_returns import mean_historical_return
from pypfopt import risk_models
from pypfopt.risk_models import CovarianceShrinkage
import yfinance as yf

# from ta.utils import dropna
from functools import reduce
import streamlit as st
import streamlit.components.v1 as components

GA_ID = "G-4MRDCEFGB4"

gtag_html = """
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
"""
# Embed the script
components.html(gtag_html, height=0)

st.set_page_config(page_title="Ledgr | Optimization Engine", layout="wide")

direc = os.getcwd()
# direc = f'{direc}/Documents/Ledgr'
# bpath = f'{direc}/pages'
logofile = f"{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png"
st.logo(logofile, size="medium", link='https://alphaledgr.com/',
        icon_image=logofile)

# #########################################
start_date = dt.datetime(2019, 1, 1)
end_date = dt.datetime.today()
pathtkr = f"{direc}/pages/appdata/tickerlist_y.csv"
ytube = f"{direc}/pages/appdata/imgs/ytube.svg"
fbook = f"{direc}/pages/appdata/imgs/fbook.svg"
insta = f"{direc}/pages/appdata/imgs/insta.svg"
linkedin = f"{direc}/pages/appdata/imgs/linkedin.svg"
ledgrblog = f"{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png"

tickerdb = pd.read_csv(pathtkr)
tickerlist = tickerdb["SYMBOL"]
# ###################### #######################################
url_ytube = "https://www.youtube.com/@LedgrInc"
url_fb = "https://www.facebook.com/share/1BnXaYvRzV/"
url_insta = "https://www.instagram.com/alphaledgr/"
url_blog = "https://www.alphaledgr.com/Blog"
url_linkedin = "https://www.linkedin.com/company/ledgrapp/"
#############################################################

##########################
st.sidebar.image(logofile)
st.sidebar.subheader("Efficient Investments buid an Efficient Economy.")
st.sidebar.caption(
    """These KPIs, Analyses impact living standards within
                   Ledgr's smaller Market in hand with their
                   Global Counterparts."""
)
# ################################################################
url_stripe = "https://buy.stripe.com/6oU28t21Y2NmbfjdkK0480h"
url_stripe_2 = "https://buy.stripe.com/dR64iacsh6bx9zi5kk"

# #############################################################
bc1, bc2 = st.columns(2)
with bc1:
    st.title(":InvestmentLab:")
    st.write("Maximize Returns.")
    st.write("Mitigate Risks.")
    st.info("Create Efficient Portfolios with Optimized Allocation.")
with bc2:
    st.video("https://youtu.be/wu0nDaMyIG4?si=f7Y0v_I_Am7JwGe6")


st.warning("Please Click the Access/Day @ INR 149.90/- to access the complete set of tools!!")
st.link_button("Access Pro for a day!", url_stripe, type="primary", disabled=False, use_container_width=True)
st.success("LedgrTeam would be elated if you Support us Monthly for a small price of INR 349/-")
st.link_button("Become a Patron!", url_stripe_2, type="secondary", disabled=False, use_container_width=True)


# ##################################################
st.stop()
# ################Pagework ####################################
x0, x1, x2, x3, x4, x5 = st.columns([2, 1, 1, 1, 1, 1])
with x0:
    st.header("Expected Returns", divider='rainbow')
with x1:
    st.metric("**Option - 1**", returns_df.iloc[-5])
    st.write("***MVAR***")
with x2:
    st.metric("**Option - 2**", returns_df.iloc[-4])
    st.write("***HRP***")
with x3:
    st.metric("**Option - 3**", returns_df.iloc[-3])
    st.write("***CLA***")
with x4:
    st.metric("**Option - 4**", returns_df.iloc[-2])
    st.write("***SVAR***")
with x5:
    st.metric("**Option - 5**", returns_df.iloc[-1])
    st.write("***CoVAR***")

st.write("  -------------  ")


st.header("Trends, Returns & Risk Exposure", divider='rainbow')
with st.container(border=True):
    st.plotly_chart(figRet, use_container_width=True)
    x7, x8, x9 = st.columns([2, 3, 2])
    with x7:
        st.plotly_chart(fig1, use_container_width=True)
    with x8:
        st.plotly_chart(fig_return_global, use_container_width=True)
    with x9:
        st.plotly_chart(figMU, use_container_width=True)
    g1, g2 = st.columns([3, 1])
    with g1:
        st.plotly_chart(figCov, use_container_width=True)
    with g2:
        st.subheader("Profiling Risks")
        st.info(
            "Covariance maps help investors understand how different assets in their portfolio might be correlated."
        )
        st.markdown(
            """This allows one to diversify their investments by including assets
that have a negative covariance, reducing overall portfolio risk."""
        )
st.info(
    "By visualizing the relationships between assets, investors can better assess the overall risk of their portfolio. "
)
st.write("  -------------  ")

with st.container(border=True):
    cbb1, cbb2, cbb3, cbb4 = st.columns([2, 1, 1, 1])
    with cbb1:
        st.subheader("Option - 1")
        st.caption("Mean Variance Optimization")
    with cbb2:
        st.metric("Returns Expected (%)", er)
    with cbb3:
        st.metric("Volatility (%) Exposure", vlt)
    with cbb4:
        st.metric("Sharpe Ratio", shrp.round(2))
    cn1, cn2 = st.columns([1, 4])
    with cn1:
        for n in allocation_mvar:
            st.metric(f"{n}", allocation_mvar[n])
        st.info("Funds remaining: INR {:.2f}".format(leftover_mvar))
    with cn2:
        st.plotly_chart(figMVAR)  # use_container_width=True)

    st.info(
        "Mean-variance optimization (MVO) is a fundamental concept in portfolio management, aiming to construct a portfolio that maximizes expected return for a given level of risk or minimizes risk for a given level of return. It's based on the principle that investors are risk-averse and prefer higher returns for the same level of risk or lower risk for the same level of return"
    )
st.write("  -------------  ")
with st.container(border=True):
    cbb4, cbb5, cbb6, cbb7 = st.columns([2, 1, 1, 1])
    with cbb4:
        st.subheader("Option - 2")
        st.caption("Hierarchical Risk Parity Algorithm")
    with cbb5:
        st.metric("Returns Expected (%)", er_hrp)
    with cbb6:
        st.metric("Volatility (%) Exposure", vlt_hrp)
    with cbb7:
        st.metric("Sharpe Ratio", shrp_hrp.round(2))
    cn3, cn4 = st.columns([1, 3])
    with cn3:
        for m in allocation_hrp:
            st.metric(f"{m}", allocation_hrp[m])
        st.info("Funds remaining (HRP): INR{:.2f}".format(leftover_hrp))
    with cn4:
        st.plotly_chart(figHRP)  # use_container_width=True)
    st.info(
        "Leverage on graph theory and machine learning to build diversified portfolios by clustering assets into hierarchical structures. Generate a portfolio where each asset's risk contribution to the overall portfolio is equal, similar to traditional risk parity, but with a hierarchical approach to asset clustering. HRP is designed to improve upon traditional risk parity methods by considering the hierarchical relationships between assets"
    )
st.write("  -------------  ")
with st.container(border=True):
    cbb7, cbb8, cbb9, cbb10 = st.columns([2, 1, 1, 1])
    with cbb7:
        st.subheader("Option - 3")
        st.caption("Critical Line Algorithm")
    with cbb8:
        st.metric("Returns Expected (%)", er_cla)
    with cbb9:
        st.metric("Volatility (%) Exposure", vlt_cla)
    with cbb10:
        st.metric("Sharpe Ratio", shrp_cla.round(2))
    cn5, cn6 = st.columns([1, 3])
    with cn5:
        for k in allocation_cla:
            st.metric(f"{k}", allocation_cla[k])
        st.info("Funds remaining (CLA): INR {:.2f}".format(leftover_cla))
    with cn6:
        st.plotly_chart(figCLA)  # use_container_width=True)

    st.info(
        "The algorithm works by iteratively finding critical values (turning points) on the efficient frontier. Starting with a portfolio where maximizing utility is equivalent to maximizing expected portfolio return. Then by adjusting a parameter related to the risk-aversion level, the algorithm traces out the entire efficient frontier."
    )  # st.plotly_chart(fig_cla)
st.write("  -------------  ")
with st.container(border=True):
    cbb11, cbb12, cbb13, cbb14 = st.columns([2, 1, 1, 1])
    with cbb11:
        st.subheader("Option - 4")
        st.caption("Efficient SemiVariance Optimization")
    with cbb12:
        st.metric("Returns Expected (%)", er_es)
    with cbb13:
        st.metric("Volatility (%) Exposure", vlt_es)
    with cbb14:
        st.metric("Sortino's Ratio", srtn_es.round(2))
    cn7, cn8 = st.columns([1, 3])
    with cn7:
        for j in allocation_es:
            st.metric(f"{j}", allocation_es[j])
        st.info("Funds remaining (ES): INR {:.2f}".format(leftover_es))
    with cn8:
        st.plotly_chart(figES)  # use_container_width=True)
    st.info(
        " A variation of portfolio optimization that considers only the negative deviations from a target return, unlike traditional mean-variance optimization which considers both positive and negative deviations, Efficient Semi Variance Optimization algortithm  focuses on finding portfolios that minimize downside risk, the risk of returns falling below a certain target, while maximizing returns. "
    )
st.write("  -------------  ")
with st.container(border=True):
    cbb77, cbb7a, cbb8a = st.columns(3)
    with cbb77:
        st.subheader("Option - 5")
        st.caption("Mean CoVaRiance Optimization")
    with cbb7a:
        st.metric("Annual Returns Expected (%)", er_ec)
    with cbb8a:
        st.metric("Conditional Value(%) at Risk", vlt_ec)
    cn9, cn10 = st.columns([1, 3])
    with cn9:
        for i in allocation_cvar:
            st.metric(f"{i}", allocation_cvar[i])
        st.info("Funds remaining: INR {:.2f}".format(leftover_cvar))
    with cn10:
        st.plotly_chart(figCVAR)  # use_container_width=True)

    st.info(
        """"This algorithm highlights the benefits of diversification
            in reducing portfolio risk, accounting in how each security,
            in unison or in combinations, affect the expected returns.
            By combining assets with low or negative correlations,
            one can potentially achieve a more efficient arbitrage."""
    )
    st.write("  -------------  ")
c0, column1, column2, column3, column4, column5, c0a = st.columns([1, 1, 1, 1, 1, 1, 1])
with c0:
    st.write(" ")
with column1:
    st.image(ytube, "[Ledgr's YouTube Channel](%s)" % url_ytube, width=60)
with column2:
    st.image(fbook, "[Our Meta Page ](%s)" % url_fb, width=60)
with column3:
    st.image(linkedin, "[Ledgr @ LinkedIn](%s)" % url_linkedin, width=60)
with column4:
    st.write(" ")
    st.image(ledgrblog, "[Ledgr's Blog ](%s)" % url_blog, width=85)
    st.write(" ")
with column5:
    st.image(insta, "[Ledgr @ Insta](%s)" % url_insta, width=60)
with c0a:
    st.write(" ")
# # ###################################################################
with st.container(border=True):
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")
