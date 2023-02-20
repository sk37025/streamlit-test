import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "centered")
st.title("Dashboard 1")


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

df = pd.read_csv('./dataset/haeyang_dashboard_1.csv')
csv = convert_df(df)

st.subheader("가설 1. 월 평균 접속과 성취도 사이의 관계")

year = st.selectbox("확인하고 싶은 연도 선택", ['2020','2021','2022'])

fig = px.bar(data_frame=df.loc[df.month.str.startswith(year),:], x ='month', y ='mau' , barmode = 'group', color = 'label', text_auto = True)
st.plotly_chart(fig)

st.markdown('💡 COURSE에 관심이 많은 학생일수록 보다 많은 접속을 할 것이며, 이는 결국 그 학생이 좋은 성과를 받는데 영향을 미칠 것이다')
st.markdown('➡️ 2021년 1학기를 제외하고는 대부분 **고성과자들이 저성과자에 비해 평균적으로 많이 접속하였다.**')

st.subheader('You can download the data used to create this  dashboard through the button below\n')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='haeyang_dashboard_1.csv',
    mime='text/csv',
)
