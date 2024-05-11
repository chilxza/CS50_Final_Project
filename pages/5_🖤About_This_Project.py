import streamlit as st
import pandas as pd
from streamlit_extras.app_logo import add_logo


def logo():
    add_logo("./images/logo.jpg", height=150)


logo()

st.markdown(
    "<b><h2 style='text-align: center; color: LightCoral;'>About This Project</h2><b>",
    unsafe_allow_html=True,
)

# st.write(
#   "Go is a mind sport where two players aim to surround more territory than the opponent. The game was invented in China more than 4,500 years ago, and it is believed to be the oldest board game still being played today."
# )

st.write(
    "This project involves developing an information system related to processing and analyzing GAT Point scores, as well as displaying statistics of various Go players. Including gender, rank level, individual GAT Point score history, and ranking the skill levels of players. The information is displayed in an easy-to-understand format using Interactive Graphs (Data Visualization)."
)

st.write(
    "โครงการนี้เป็นการพัฒนาระบบสารสนเทศเกี่ยวกับการประมวลผล วิเคราะห์ (Data Analysis) คะแนน GAT Point และ แสดงค่าสถิติของผู้เล่นหมากล้อมต่างๆ เช่น เพศ ระดับดั้ง ประวัติคะแนน GAT Point รายบุคคล และจัดอันดับระดับฝีมือของนักกีฬาในรูปแบบที่เข้าใจง่าย โดยใช้ Interactive Graph (Data Visualization)"
)
st.markdown(
    "<p><i>This project is developed by Waranphat B.</i></p>",
    unsafe_allow_html=True,
)


# st.markdown(
#    "<b><h2 style='text-align: center; color: LightCoral;'>About Me</h2><b>",
#   unsafe_allow_html=True,
# )

# col1, col2 = st.columns((1, 1.5), gap="Medium")

# with col1:
#   st.image("./images/me.jpg")

# with col2:
#    st.write(
#        "I've been playing Go since I was a little young girl. Go has helped me develop many life skills, such as calculation, memory, and creativity. From there, I developed this web application to visualize GAT Point of Go players in Thailand. GAT Point web will let Go players know their status, progress, and ranking in Thailand. Last, I hope this web application will inspire Go players to continuously improve their Go capabilities and benefit the Thailand Go community.🖤🤍"
#    )

st.markdown(
    "###### [GAT-Point Data](https://drive.google.com/file/d/14SMzCtmljfmfT2OpVxmrN0XrBb1P4hCU/view)",
)
