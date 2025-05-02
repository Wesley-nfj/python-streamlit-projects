import streamlit as st

st.markdown(
    """
  <style>
    .stApp{
        background-image : url("https://i.pinimg.com/736x/43/33/8b/43338b13db1a7f9ab3c9e110621604a3.jpg");
        background-attachment : fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-size: contain;
    }   
  </style>                    
     """,
unsafe_allow_html=True
)
st.title("Calculator🧮")
num1= st.number_input("Enter first number", min_value=0)
num2= st.number_input("Enter second number", min_value=0)
operation=st.selectbox("Choose operator",["+", "-","*","/"])
if st.button("Calculate"):
    if num1 is not None and num2 is not None and operation:
      if operation =="+":
        result =num1 + num2
      elif operation =="-":
        result=num1-num2
      elif operation =="*":
        result=num1*num2
      elif operation =="/":
        if num2!=0:
          result= num1/num2
        else:
          result="Error, cannot divide by zero"
      st.success(f"Result:{result}")
else:
  st.error("Please enter both numbers and an operator!")
        
       
