
import streamlit
import pandas
import requests
import snowflake.connector

from urllib.error import URLError


streamlit.title("🥣New Workshop");

streamlit.header("Lerning");

streamlit.text("Snowflake");



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Grapes'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
     streamlit.error('Select the fruit')
   else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
        fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

add_myfruit = streamlit.text_input('What fruit would you like add?')

streamlit.write('Thanks for adding ', add_myfruit)


my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
