import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "centered")
st.title("Dashboard 2")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

df = pd.read_csv('./dataset/haeyang_dashboard_2.csv')
csv = convert_df(df)

st.subheader("가설 1. 월 평균 접속 세션 길이와 성취도 사이의 관계")

fig = px.bar(data_frame=df, x ='month', y ='session_duration' , barmode = 'group', color = 'label', text_auto = True)
st.plotly_chart(fig)

st.markdown('💡 Session Duration : Session End Time - Session Start Time')
st.markdown('➡️ 2021년 1학기의 Session duration을 같이보니 **저성과자의 경우, 접속숫자만 많았지 Session Duration 자체는 짧은 것을 확인할 수 있었다.**')
st.markdown('➡️ 이는 해당 시기의 수업들 중 장시간 접속해야 하는 과제에서 고성과자와 저성과자 사이에 차이가 드러난 것으로 보인다.')
st.markdown('➡️ 또한, 수업에 특성으로 인해서 세션 길이의 차이가 발생할 수 있으나, 대체적으로 저성과자의 경우, 고성과자보다 동일한 과제에 대해 session_time이 긴 것을 확인할 수 있었다.')



st.subheader('You can download the data used to create this  dashboard through the button below\n')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='haeyang_dashboard_2.csv',
    mime='text/csv',
)
