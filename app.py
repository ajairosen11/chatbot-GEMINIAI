from dotenv import load_dotenv
load_dotenv()   ##Load all the env variables


import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configure our API Key
genai.configure(api_key=os.getenv("google_api_key"))

# Function to Load Google Gemini model and provide Sql query as a response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to Retrieve queyr from the Sql Database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Important
#Define Your Prompt

prompt=[
    """
    You are an expert in converting English Questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS< SECTION and MARKS \n\nFor example,\nExample 1- How many entries of records
    are present ?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in Mech class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="Mech";
    also the sql code should not have ``` in the beginning or the end and sql word in the output
    """
]

##Streamlit App
st.set_page_config(page_title="I can retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

#if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)