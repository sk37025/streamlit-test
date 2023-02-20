import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout = "centered")
st.title("Dashboard 5")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

df = pd.read_csv("./dataset/haeyang_dashboard_5.csv")
csv = convert_df(df)

st.subheader("가설 4. etest 여정 추이와 학업 최종 성과 사이의 관계")

image = Image.open('./dataset/img1.png')
st.image(image, caption = 'Course별 8일간 여정 그래프')

st.markdown('- 모든 학생을 대상으로 했을 때, 가장 많이 보인 여정은 아래와 같음 (오른쪽으로 갈수록 최근에 본 시험)')
st.markdown('- 최고점과의 차이가 점점 좁혀지다가 마지막에 급격히 꺾이는 것을 확인할 수 있음')

image = Image.open('./dataset/img2.png')
st.image(image, caption = '여정 clustering')

st.markdown('- 최고점과의 차이가 점점 좁혀지다가 마지막에 급격하게 꺾이는 것을 확인할 수 있음')
st.markdown('- 마지막 평가에서 급격하게 떨어지는 경우 (검정색 선)는 마지막에 0점인 경우인데 이는 데이터 수집 단계에서 잘못된 것으로 보이며, 이를 제외하고서 확인해보면 크게 2가지 여정으로 나뉘는 것을 확인이 가능함') 
st.markdown('- 다만, 이를 LM_STD_SCORE과 join했을 때, 공통된 COURSE_ID와 USER_ID가 없어서 최종 성과와 비교는 불가능했음')


st.subheader('You can download the data used to create this  dashboard through the button below\n')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='haeyang_dashboard_4.csv',
    mime='text/csv',)