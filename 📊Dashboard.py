import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from streamlit_extras.app_logo import add_logo


def logo():
    add_logo("./images/logo.jpg", height=120)


logo()

with st.sidebar:
    st.markdown(
        f'<p style="color:red;">{"GAT Point data as of 1 SEP 2024"}<p>',
        unsafe_allow_html=True,
    )

df = pd.read_csv("./data/thai-go-all.csv")
thisyear = len(df[df["Dan Year"] == 2024])
beforethisyear = len(df) - thisyear
alldangrowth = thisyear / beforethisyear * 100
alldangrowth = f"{alldangrowth:.2f}%"

dfmale = df.loc[(df["Dan Year"] == 2024) & (df["Gender"] == "♂️")]
malethisyear = len(dfmale)
malebeforethisyear = len(df[df["Gender"] == "♂️"]) - malethisyear
maledangrowth = malethisyear / malebeforethisyear * 100
maledangrowth = f"{maledangrowth:.2f}%"

dffemale = df.loc[(df["Dan Year"] == 2024) & (df["Gender"] == "♀️")]
femalethisyear = len(dffemale)
femalebeforethisyear = len(df[df["Gender"] == "♀️"]) - femalethisyear
femaledangrowth = femalethisyear / femalebeforethisyear * 100
femaledangrowth = f"{femaledangrowth:.2f}%"

# malethisyear = len(df.loc[df["Dan Year"] == 2023 & df["Gender"] == "♂️"])
# print(malethisyear)

col1, col2, col3 = st.columns(3)
col1.metric("All Dan Players", len(df), alldangrowth)
col2.metric("Male Dan Players", len(df[df["Gender"] == "♂️"]), maledangrowth)
col3.metric("Female Dan Players", len(df[df["Gender"] == "♀️"]), femaledangrowth)

st.write("*Percentage of new Dan players compared to last year.*")
st.markdown("---")
c1, c2 = st.columns((1.3, 1.5), gap="large")

with c1:
    gen = px.data.tips()
    gen = df.groupby(by=["Gender"], as_index=False)["Gender"].count()
    gen.rename(columns={"Gender": "Number of Players"}, inplace=True)
    gen.insert(1, "Gender", ["Female", "Male"])
    fig = px.pie(
        gen,
        values="Number of Players",
        names="Gender",
        template="plotly_dark",
        title="Number of Players by Gender",
    )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    dia = df.groupby(by=["Diamond"], as_index=False)["Diamond"].count()
    dia.rename(columns={"Diamond": "Number of Players"}, inplace=True)
    dia.insert(1, "Diamond", ["Players with no 💎", "Players with 💎"])
    fig = px.pie(
        dia,
        values="Number of Players",
        names="Diamond",
        title="Number of Players by Diamond",
    )
    st.plotly_chart(fig, use_container_width=True)

c3, c4 = st.columns((1, 1), gap="medium")

with c3:
    gk = df.groupby(by=["Dan Level"], as_index=False)["Dan Level"].count()
    gk.rename(columns={"Dan Level": "Number of Players"}, inplace=True)
    gk.insert(1, "Dan Level", [1, 2, 3, 4, 5, 6, 7])
    fig = px.bar(
        gk,
        x="Dan Level",
        y="Number of Players",
        template="ggplot2",
        title="Number of Players in Each Dan Level",
    )
    st.plotly_chart(fig, use_container_width=True)

with c4:
    # dangrowth = df["Dan Year"].value_counts()
    # years = dangrowth.index
    # years = years.astype(int)
    # for year in range(1993, 2024):
    #     if year not in years:
    #         dangrowth[year] = 0
    # dangrowth = dangrowth.sort_index()
    # dangrowth = dangrowth.to_frame()
    # dangrowth.rename(columns={"count": "Number of New Dan Players"}, inplace=True)
    # dangrowth["Year"] = dangrowth.index
    # fig = px.line(
    #     dangrowth,
    #     x="Year",
    #     y="Number of New Dan Players",
    #     template="plotly",
    #     markers=True,
    #     title="Number of New Dan Players in Each Year",
    # )
    # st.plotly_chart(fig, use_container_width=True)

    years = range(1993, 2025)
    male = []
    female = []
    total = []
    for year in years:
        num1 = len(df.loc[(df["Dan Year"] == year) & (df["Gender"] == "♂️")])
        male.append(num1)
        num2 = len(df.loc[(df["Dan Year"] == year) & (df["Gender"] == "♀️")])
        female.append(num2)
        total.append(num1 + num2)
    t1 = go.Line(x=list(years), y=total, mode="lines+markers", name="All")
    t2 = go.Line(x=list(years), y=male, mode="lines+markers", name="Male")
    t3 = go.Line(x=list(years), y=female, mode="lines+markers", name="Female")
    fig = go.Figure([t1, t2, t3])
    fig.update_layout(
        title="Number of New Dan Players in Each Year",
        xaxis_title="Year",
        yaxis_title="Number of New Dan Players",
    )
    st.plotly_chart(fig, use_container_width=True)
