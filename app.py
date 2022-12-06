import streamlit as st
st.write("TDS Week 8 Assignment")
a=st.number_input("Enter first number")
b=st.number_input("Enter second number") 
if (b == 0):
  st.write("Division not possible.")
else:
  c=a/b
  st.write("Division of the Two numbers is: ",c)
st.write("By Puneet 21f3002005")
