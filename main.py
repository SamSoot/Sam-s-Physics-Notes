import streamlit as st
st.title("Sam's Online Physics Notes")
st.markdown("---")
st.header("Classical Mechanics")
col1, col2 = st.beta_columns([4, 6])
with col1:
    st.subheader("Resources")
    st.markdown("- [Feynman Lectures on Physics Vol. 1](https://www.feynmanlectures.caltech.edu/)\n- [David Tong's Lecture Notes](http://www.damtp.cam.ac.uk/user/tong/teaching.html)"
                + "\n- David Morin, 'Introduction to Classical Mechanics'"
                + "\n- John Taylor, 'Classical Mechanics'")
with col2:
    st.subheader("My Notes")
    st.write("- [Classical Mechanics](https://www.dropbox.com/sh/6zr2ho3szfvzz5v/AADpdKWCGRx9VF6NWSppbRmWa?dl=0)")

