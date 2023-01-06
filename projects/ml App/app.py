
import streamlit as st
import pandas as pd
import os
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report

from pycaret.classification import setup as setup1
from pycaret.classification import pull as pull1
from pycaret.classification import compare_models as compare_models1
from pycaret.classification import save_model as save_model1
# from pycaret.classification import plot_model as plot_model1
from pycaret.regression  import setup as setup2
from pycaret.regression  import pull as pull2
from pycaret.regression  import compare_models as compare_models2
from pycaret.regression  import save_model as save_model2


df = pd.DataFrame({})

with st.sidebar:
    st.image("https://miro.medium.com/max/1400/1*c_fiB-YgbnMl6nntYGBMHQ.jpeg")
    st.title("*Machine learning* :red[Tool] :sunglasses:")
    with st.container():
        choice = st.radio("Options",('upload','profiling','ML',"Download","predict"))
    st.info("Make **Automated** ML Apps 🎁", icon="ℹ️" )
    

if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv",index_col=None)


if choice == "upload":
    st.title("upload your :red[data] to make model")
    file = st.file_uploader("upload a file",help="upload dataset csv file",type=['csv'])
    if file:
        df = pd.read_csv(file)
        df.to_csv("data.csv",index=None)
        st.dataframe(df)
        
        
        
if choice == "profiling":
    if (not df.empty):
        st.title("explore Your :red[Data]")
        profile_report = df.profile_report()
        #profile_report
        st_profile_report(profile_report)
    else:
        st.warning("first import your data")
    
if choice == "ML":
    st.title("Build Your :red[Model]")
    choice = st.radio("Select problem type",('classification','Regression'))
    if (not df.empty):
        target = st.selectbox("select your target",df.columns)
        if choice == "classification":
            btn = st.button("train")
            if btn:
                setup1(df,target=target)
                setup_df = pull1()
                st.info("Ml experiment settings")
                st.dataframe(setup_df)
                best_model = compare_models1()
                compare_df = pull1()
                st.info("this is the best model")
                st.dataframe(compare_df)
                st.info("Results")
                st.write(best_model)
                save_model1(best_model,"best_model")
        
        if choice == "regression":
            btn = st.button("train")
            if btn:
                setup2(df,target=target)
                setup_df = pull2()
                st.info("Ml experiment settings")
                st.dataframe(setup_df)
                best_model = compare_models2()
                compare_df = pull2()
                st.info("this is the best model")
                st.dataframe(compare_df)
                st.info("Results")
                st.write(best_model)
                save_model2(best_model,"best_model")       
    else:
        st.warning("first import your data")       
       
    
    
if choice == 'Download':
    st.title("Download Your :red[Model]")
    if (not df.empty):
        if os.path.exists("best_model.pkl"):
            with open("best_model.pkl","rb") as f:
                st.download_button("download model",f,"best_model.pkl")
        else:
            st.warning("train the model first")
    else:
        st.warning("first import your data")

if choice == "predict":
    pass