import os
import streamlit as st
from factorial import cal_factorial
from user import UserList

def login_page():
    """
    page using for login by typing username and password
    """
    
    #get user list from file "user.txt"
    link_user_file = "user.txt"
    if os.path.exists(link_user_file):
        user_list = UserList(link_user_file)
    else:
        st.warning("Error while getting user file")
    
    st.title("LOGIN")
    
    #create text_input used for typing username and password
    username = st.text_input(
        "Username", 
        placeholder="Enter username",
        label_visibility="collapsed"
    )
    password = st.text_input(
        "Password",
        placeholder="Enter password", 
        label_visibility="collapsed",
        type="password"
    )
    
    #check if given user is valid or not
    check, infor = user_list.check_login(username, password)
    
    #if user is valid, switch to factorial page, otherwise warn user
    if st.button("Login"):
        if check:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.warning(infor)

def factorial_page():
    """
    page using for calculate factorial of a number
    """
    
    #show basic information
    st.title("Factorial Calculator")
    
    st.write(f"Welcome {st.session_state.username}")
    
    #create logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
        
    st.divider()

    #calculate factorial of a number
    n = st.number_input("Enter a number: ", min_value=0, max_value=999)

    if st.button("Calculate"):
        result = cal_factorial(n)
        st.write(f"Factorial of {n} is {result}")
    
        
def main():
    """
    navigate page depends on session
    """
    
    #init session_state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
        
    if st.session_state.logged_in:
        factorial_page()
    else:
        login_page()
        
if __name__ == "__main__":
    main()