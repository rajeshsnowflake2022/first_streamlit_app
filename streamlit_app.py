
import streamlit

streamlit.title("🥣New Workshop");

streamlit.header("Lerning");

streamlit.text("Snowflake");

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)


