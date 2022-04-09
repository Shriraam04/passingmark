import streamlit as st
y = 50
st.header("Exam Passing Rate Calculator")


readme = st.checkbox("Readme")

if readme:

    st.write("""
        This is a Exam Passing Rate Calculator. If interested, do get the codes from github (https://github.com/Shriraam04/passingrate)
        """)

    st.write ("For more info, please contact:")

    st.write("[Shriraam Asokumar](https://www.linkedin.com/in/shriraamasokumar/)")
    
         
mark = st.text_input('Enter your mark here', '50')
        
         
try:
    val = float(mark)
            
    if (val > 100 or val < 0):
        st.write("\nPlease enter a valid mark.\n")
                
    elif val >= y:
        st.write("\nYou passed your exam. Keep it up!\n")
       
    else:
        st.write("\nYou failed this time. Keep your head up, failure is the key to success. Each mistake teaches us something!\n")

            
except ValueError:
    st.write("\nPlease enter a number.\n")
