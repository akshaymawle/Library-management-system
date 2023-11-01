import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.title("LIBRARY MANAGEMENT SYSTEM")
st.sidebar.image("https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/HOW-DO-YOU-DESIGN-A-LIBRARY-MANAGEMENT-SYSTEM-min.png")
choice=st.sidebar.selectbox("MENU",("HOME","STUDENT","ADMIN","REGISTRATION"))
if(choice=="HOME"):
    st.image("https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/WHAT-IS-THE-PURPOSE-OF-A-LIBRARY-MANAGEMENT-SYSTEM-min.png")
elif(choice=="STUDENT"):
    uid=st.text_input("Enter User ID")
    pwd=st.text_input("Enter User Password")
    if "login" not in st.session_state:
        st.session_state['login']=False
    btn=st.button("LOGIN")
    if btn:        
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
        c=mydb.cursor()
        c.execute("select * from users")
        for row in c:                         #maintain data during different part of apps in streamlit.
            if(row[0]==uid and row[1]==pwd):  # saves useer data across app interaction.
                st.session_state['login']=True #object in streamlit library.cretes and stores variables
                break
        if(not st.session_state['login']):
            st.header("Incorrect ID or Password ")
    if(st.session_state['login']):
        st.header("Login Successfull")
        choice2=st.selectbox("Features",("None","View All Books","Issue Books"))
        df=0
        if(choice2=="View All Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
            c=mydb.cursor()
            c.execute("select * from books")
            mydata=[]
            mycolumns=c.column_names            
            for row in c:
                mydata.append(row)
            st.session_state['df']=pd.DataFrame(data=mydata,columns=mycolumns)
            st.dataframe(st.session_state['df'])
        elif(choice2=="Issue Books"):
            df=0
            bid=st.selectbox("Choose Book ID",st.session_state['df']['book_id'])
            usid=st.text_input("Enter your User ID")
            btn3=st.button("Issue Book")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
                c=mydb.cursor()
                iid=str(datetime.datetime.now())
                c.execute("insert into issue values(%s,%s,%s)",(iid,bid,usid))
                mydb.commit()
                st.header("Book Issued Successfully")
        btn2=st.button("LOGOUT")
        if btn2:
            st.session_state['login']=False
            st.experimental_rerun()
elif(choice=="ADMIN"):
    aid=st.text_input("Enter Admin ID")
    pwd=st.text_input("Enter Admin Password")
    if "alogin" not in st.session_state:
        st.session_state['alogin']=False
    btn=st.button("LOGIN")
    if btn:        
        mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
        c=mydb.cursor()
        c.execute("select * from admins")
        for row in c:
            if(row[0]==aid and row[1]==pwd):
                st.session_state['alogin']=True
                break
        if(not st.session_state['alogin']):
            st.header("Incorrect ID or Password ")
    if(st.session_state['alogin']):
        st.header("Login Successfull")
        choice2=st.selectbox("Features",("None","View Issue Books","Add New Books","Delete Book"))
        if(choice2=="View Issue Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
            c=mydb.cursor()
            c.execute("select * from issue")
            mydata=[]
            mycolumns=c.column_names            
            for row in c:
                mydata.append(row)
            df=pd.DataFrame(data=mydata,columns=mycolumns)
            st.dataframe(df)
        elif(choice2=="Add New Books"):
            bid=st.text_input("Enter Book ID")
            bname=st.text_input("Enter Book Name")
            aname=st.text_input("Enter Author Name")
            btn3=st.button("Add Book")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
                c=mydb.cursor()                
                c.execute("insert into books values(%s,%s,%s)",(bid,bname,aname))
                mydb.commit()
                st.header("Book Added Successfully")
        elif(choice2=="Delete Book"):
            bid=st.selectbox("Choose Book ID",st.session_state['df']['book_id'])
            btn3=st.button("Delete Book")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
                c=mydb.cursor()                
                c.execute("delete from books where book_id=%s",(bid,))
                mydb.commit()
                st.header("Book Removed Successfully")
        btn2=st.button("LOGOUT")
        if btn2:
            st.session_state['login']=False
            st.experimental_rerun()
elif(choice=="REGISTRATION"):
    uid=st.text_input("Enter User ID")
    pwd=st.text_input("Enter Password")
    btn=st.button("Register")
    if btn:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="lms",auth_plugin="mysql_native_password")
            c=mydb.cursor()                
            c.execute("insert into users values(%s,%s)",(uid,pwd))
            mydb.commit()
            st.header("User Added Successfully")
        except Exception as e:
            st.header(e)






