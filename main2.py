import streamlit as st
import pandas as pd
import mysql.connector
import datetime
st.title ("LOAN APPLICATION FORM")
income=st.text_input("enter income")
amount=st.text_input("enter loan amount")
btn=st.button("submit application")
if btn:
    app_id=str(datetime.datetime.now())
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="bank",auth_plugin="mysql_native_password")
    c=mydb.cursor()
    c.execute("insert into loan_application values (%s,%s,'processing',%s)",(app_id,income,amount))
    mydb.commit()
    st.header("data saved successfully")
