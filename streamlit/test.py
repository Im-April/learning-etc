import streamlit as st
import pandas as pd

#  Streamlit에서 텍스트나 다양한 콘텐츠를 웹페이지에 표시하는 함수
st.write('''
# My First app
         Hello *world!*
''')


df = pd.read_csv('my_data.csv') # 'my_data.csv' 파일을 읽어 DataFrame으로 변환
st.line_chart(df) # 데이터를 선 그래프로 시각화

# Pick a color
color = st.color_picker('Pick a color')

# pick number
number = st.slider('Pick a number', 0, 100)

# bar chart
st.bar_chart(df,x='category',y='sales')

# Pick a pet
pets = ['Dog','Cat','Bird']
pet = st.radio('Pick a pet',pets)

# Pick a date
date = st.date_input('Pick a date')