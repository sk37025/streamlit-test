import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "centered")
st.title("Dashboard 3")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

df = pd.read_csv('./dataset/haeyang_dashboard_3.csv')
df = df.groupby(['encrypted_course_id','encrypted_user_id','case']).mean().reset_index()
csv = convert_df(df)

st.subheader("가설 2. 접속 기간과 페이지 조회수 사이의 관계")

course_id = st.selectbox("확인하고 싶은 암호화된 COURSE_ID 선택", df['encrypted_course_id'].unique())

fig = px.scatter(data_frame=df.loc[df['encrypted_course_id'] == course_id,:], x ='session_duration', y ='FORUM_SCORE' , color = 'case')
st.plotly_chart(fig)

st.markdown('💡 히트가 많을수록 고객의 행동은 많아질 수 있으며, 이는 학생으로 하여금 접속 duration을 연장시킬 수 있을 것이라고 생각한다.')

st.markdown('➡️ **접속 duration과 페이지 hit의 상관관계는 샘플 수가 너무 적어 확인이 불가능하다**')
st.markdown('➡️ 접속 duration과 FORUM의 score 역시 상관관계는 없으며 FORUM의 score는 전체 성적에 아주 적은 비율이 반영되기에 저성과자가 FORUM에서 점수를 많이 잃었다고 결론을 내릴 수 없음.')


st.subheader('You can download the data used to create this  dashboard through the button below\n')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='haeyang_dashboard_3.csv',
    mime='text/csv',)