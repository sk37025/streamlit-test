import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "centered")
st.title("Dashboard 4")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

df = pd.read_csv("./dataset/haeyang_dashboard_4.csv")
csv = convert_df(df)

st.subheader("가설 3. 과제 점수와 성과 사이의 관계")

fig = px.bar(data_frame=df.groupby(['GRADE']).mean()[['normalized_score']].reset_index(), x ='GRADE', y ='normalized_score' , color = 'GRADE', text_auto = True,
             labels = ['A+','A','B+','B','C+','C','D+','D','F'])
st.plotly_chart(fig)


st.markdown('💡 저성과자와 고성과자는 Report를 작성할 때, 태도에 차이가 있을 것이며, 이는 곧 Report 점수 사이에 차이를 만들 것이기에 최종적으로는 성과에 차이를 줄 것')

st.markdown('➡️ 고성과자와 저성과자를 묶는 기준이 현재는 C+이기 때문에, 급간이 평균적으로 넓은 B+와 B가 본 분석에서 방해가 될 것으로 생각하고 해당 분석에서는 Final Grade를 통해 더 명확하게 구분 짓기를 도모함.')
st.markdown('➡️ 하지만 COURSE 별로 A+, A, B+, B, C+, C, D+, D, F의 배분이 일정하지가 않아서 Report 점수를 통한 저성과자와 고성과자의 분류가 방해가 되는 것을 볼 수 있으며 상관관계가 없는 것을 확인')
st.markdown('➡️ COURSE의 최고점과 차이가 5% 밖에 나지 않았음에도 저성과자로 분류가 된 것으로 보아, Report 점수의 신뢰성이 없음을 확인할 수 있음. 이는 추후 학습 동력을 떨어뜨리는 요인이 될 수 있다고 사료됨')




st.subheader('You can download the data used to create this  dashboard through the button below\n')
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='haeyang_dashboard_4.csv',
    mime='text/csv',)