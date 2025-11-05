import streamlit as st 
from PIL import Image

from data import get_passangers_count_by_pclass
from ini import ini

def get_ui():
    image = Image.open('./favicon.png')
    st.image(image)
    st.title("Данные пассажиров титаника")  
    st.write("Для просмотра данных только по определённому классу обслуживания, выберите соответствующее значение!")    

    input_pclass = st.slider("Введите класс обслуживания:", min_value=1, max_value=3, value=1) 
    st.write(f"Вы выбрали класс обслуживания: {input_pclass}.") 

    if st.button('Запустить анализ'): 
        with st.spinner('Анализируем данные...'): 
            titanic_df = ini() 
            result_df = get_passangers_count_by_pclass(titanic_df=titanic_df, pclass_value=input_pclass)
            st.success('Анализ завершен!') 

        st.subheader("Результат выборки:") 
        st.dataframe(result_df)