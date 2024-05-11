import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from streamlit_extras.app_logo import add_logo


def logo():
    add_logo("./images/logo.jpg", height=150)


logo()

df = pd.read_csv("./data/thai-go-all.csv")
st.markdown(
    "<h3 style='text-align: center; color: black;'>⚫️ Personal GAT Point ⚪️</h3>",
    unsafe_allow_html=True,
)
input = st.text_input("Enter player's name/surname (at least 3 characters in Thai): ")
input2 = input.strip()
sizeinput = len(input2)

selected_player = {}
if input2 != "":
    if sizeinput < 3:
        st.markdown(
            "<h6 style='text-align: left; color: black;'>Please enter at least 3 characters</h3>",
            unsafe_allow_html=True,
        )
    else:
        name = input2[0]
        surname = input2[1]
        ser1 = df["Name-Surname"]
        results = ser1[ser1.str.contains(input2)]
        player = st.radio(
            "Please select a player",
            results,
        )
        selected_player = df[df["Name-Surname"] == player]

col1, col2 = st.columns((2, 1), gap="Medium")
with col1:
    if len(selected_player):
        option = st.selectbox(
            "Select Year", ("All Years", "2567", "2566", "2565", "2564", "2563")
        )
        if option == "All Years":
            option = "25"
        gat_columns = selected_player.columns[
            selected_player.columns.str.contains(option)
        ]
        gat_hist = selected_player[gat_columns]
        x = gat_columns.values
        y = selected_player[gat_columns].values[0]
        x = [day[:2] + "-" + day[2:4] + "-" + day[4:] for day in x]
        x.reverse()
        y = [float(gat) for gat in y]
        y.reverse()
        mingat = min(y) - 100
        maxgat = max(y) + 100
        x = [str(name) for name in x]
        fig = go.Figure(
            data=go.Line(x=x, y=y, mode="lines+markers"),
            layout_yaxis_range=[mingat, maxgat],
        )
        fig.update_layout(
            title="GAT Point History", xaxis_title="Year", yaxis_title="GAT Point"
        )
        st.plotly_chart(fig, use_container_width=True)
with col2:
    if len(selected_player):
        if (selected_player["Gender"] == "♂️").any():
            st.image("./images/male.jpg")
        else:
            st.image("./images/female.jpg")
        name = selected_player["Name-Surname"].values[0]
        level = selected_player["Dan Level"].values[0]
        current_gat = df.columns[8]
        gp = selected_player[current_gat].values[0]
        did = selected_player["Dan-ID"].values[0]
        ddate = selected_player["Dan Date"].values[0]
        active = selected_player["Active"].values[0]
        if active == True:
            active = "Yes"
        else:
            active = "No"
        st.write("Name: ", name)
        st.write("Dan Level: ", level)
        st.write("GAT Point: ", gp)
        st.write("Dan-ID: ", did)
        st.write("Dan Date: ", ddate)
        st.write("Active Player?: ", active)
