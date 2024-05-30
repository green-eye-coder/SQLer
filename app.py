from dotenv import load_dotenv
# load all the environmenty variable
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import sqlite3

# configure APT key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load google gemini model
# provide sql query as defination

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    
    return response.text

# to retrieve query from sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)

    return rows


# defining prompt

prompt=[
    """
    you are an expert in converting english question to sql query!
    the sql database has the name STUDENT and has following columns  USN varchar2(20),NAME varchar(30), DEPARTMENT varchar2(25), SEMISISTER varchar2(10),SECTION varchar2(10),MARKS \n\n
    for example ,\nexample 1 - how many entries of records are present then sql command willb somthing like SELECT COUNT(*) FROM STUDENT;\n
    Example 2: Tell me all the students studying in computer applications ?, the sql command will be something like SELECT * FROME STUDENT WHERE DEPARTMENT="computer applicationa";
    also the sql code should not have ``` in begining or end and sql word in the output

    """
]

# create stramlet application

st.set_page_config(page_title="SQLer - Text to SQL query")
st.header("SQLer")
st.markdown('''
    :rainbow[Ask for any SQL queryes] \n:green[I can retrieve Any sql query]''')

question=st.text_input("Ask me: ",key="input")

submit=st.button("Submit")

if submit:
    response=get_gemini_response(question=question,prompt=prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.text(f"you can use the query : {response}")
    st.subheader("the response is")   
    for row in data:
        print(row)
        st.text(row)
        