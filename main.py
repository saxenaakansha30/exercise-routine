import streamlit as st
import time
import database as db

st.sidebar.title("Exercise Routine")

# Do 2 exercises
# 1 for 45 seconds showing name, purpose and an image with 45 seconds counter.
# Then show 15 seconds Rest with a timer
# Repeat for the next exercie.

group_placeholder = st.sidebar.empty()
timer_placeholder = st.sidebar.empty()

name_placeholder = st.empty()
benefit_placeholder = st.empty()
image_placeholder = st.empty()

for exercie in db.exercise_list:
  group_placeholder.subheader(exercie['group'])
  name_placeholder.subheader(exercie['name'])
  benefit_placeholder.write("Benefit: " + exercie['benefit'])
  image_placeholder.image(exercie['image'], caption=exercie['name'])
  for sec in range(45):
    timer_placeholder.header(f"Time Left: {45 - sec} seconds")
    time.sleep(1)

  # Rest
  group_placeholder.header("Rest")
  benefit_placeholder.write("Rest is important.")
  name_placeholder.subheader("Rest")
  image_placeholder.image('images/rest.png', "Green Rest")
  for sec in range(15):
    timer_placeholder.header(f"Time Left: {15 - sec} seconds")
    time.sleep(1)

name_placeholder.header("Routine Complete, Well Done!!")
image_placeholder.video('images/well-done.jpeg')

group_placeholder.empty()
timer_placeholder.empty()
name_placeholder.empty()
benefit_placeholder.empty()
image_placeholder.empty()
