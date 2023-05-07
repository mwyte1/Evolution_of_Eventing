import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from PIL import Image

st.title("Eventing through the Ages")

data = pd.read_excel('Final_Spreadsheet.xlsx')

tab1, tab2, tab3, tab4 = st.tabs(['Scoring Correlations', 'Dressage Multiplier', 'What is Eventing?', 'Different Classifications of Horse'])

with tab1:
    filter_by = st.selectbox("Filter By:", options=["Country", "Classification", "Breed", "Age"])
    mathematical_calculation = st.selectbox("What value would you like to compare?", options=["Average", "Maximum Value", "Minimum Value"])
    if mathematical_calculation == "Average":
        chart_1 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='mean(Final Score)', 
                                                color=filter_by)
        chart_2 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='mean(Dressage Score)', 
                                                color=filter_by)
        chart_3 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='mean(Cross-Country Penalties)', 
                                                color=filter_by)
        chart_4 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='mean(Stadium Jumping Penalties)', 
                                                color=filter_by)
        chart_12 = alt.concat(chart_1, chart_2)
        chart_34 = alt.concat(chart_3, chart_4)
        st.altair_chart(chart_12, use_container_width=True)
        st.altair_chart(chart_34, use_container_width=True)
    elif mathematical_calculation == "Maximum Value":
        chart_1 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='max(Final Score)', 
                                                color=filter_by)
        chart_2 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='max(Dressage Score)', 
                                                color=filter_by)
        chart_3 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='max(Cross-Country Penalties)', 
                                                color=filter_by)
        chart_4 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='max(Stadium Jumping Penalties)', 
                                                color=filter_by)
        chart_12 = alt.concat(chart_1, chart_2)
        chart_34 = alt.concat(chart_3, chart_4)
        st.altair_chart(chart_12, use_container_width=True)
        st.altair_chart(chart_34, use_container_width=True)
    else:
        chart_1 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='min(Final Score)', 
                                                color=filter_by)
        chart_2 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='min(Dressage Score)', 
                                                color=filter_by)
        chart_3 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='min(Cross-Country Penalties)', 
                                                color=filter_by)
        chart_4 = alt.Chart(data).mark_line().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='min(Stadium Jumping Penalties)', 
                                                color=filter_by)
        chart_12 = alt.concat(chart_1, chart_2)
        chart_34 = alt.concat(chart_3, chart_4)
        st.altair_chart(chart_12, use_container_width=True)
        st.altair_chart(chart_34, use_container_width=True)

with tab2:
    st.write("Before 2018, the penalty score given after the dressage test was multiplied by a coefficient of 1.5. This was to emphasive the importance of this phase of the competition.")
    st.write("The dressage multiplier did what it was designed to do; it made competitors spend more time on flat work with their horses. Unfortunately, it became the sole focus for a lot of riders. They began to neglect the other phases of competition when practicing at home which led to more refusals, time faults and knocked rails.")
    st.write("In 2018, the Fédération Equestre Internationale (FEI) unveiled that they were going to be removing the dressage multiplier from competition results. They stated that they wanted to start promoting the importance of cross country. After all, it is the heart of the sport.")
    st.write(" ")
    dressage_multiplier = st.checkbox("With Dressage Multiplier (Old Scoring)", value=True)
    if dressage_multiplier:
        chart_1 = alt.Chart(data).mark_point().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='Final with Multiplier', 
                                                color=filter_by)
        chart_2 = alt.Chart(data).mark_point().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='Dressage Score with Multiplier', 
                                                color=filter_by)
        chart_12 = alt.concat(chart_1, chart_2)
        st.altair_chart(chart_12, use_container_width=True)
    else:
        chart_1 = alt.Chart(data).mark_point().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='Final Score', 
                                                color=filter_by)
        chart_2 = alt.Chart(data).mark_point().encode(alt.X('Year', scale=alt.Scale(domain=[1999, 2023])),
                                                y='Dressage Score', 
                                                color=filter_by)
        chart_12 = alt.concat(chart_1, chart_2)
        st.altair_chart(chart_12, use_container_width=True)

with tab3:
    st.write('The sport of Eventing is one of the oldest sports dating back to World War I. It was originally used to test soldiers and their mounts before going into battle. The sport has since evolved into 3 different phases.')
    st.write(' ')
    
    st.subheader('Phase 1: Dressage')
    st.write("Dressage is always the first phase at an event because it is the key indicator that the horse and rider are in sync. If the horse and rider are not harmonious during their dressage test, they obviously won't be safe on course when they are running at stationary objects.")
    st.write("In Dressage, the rider is given a test to memorize and perform. A panel of judges then scores the ride, and the average score percentage is subtracted from 100 to give a baseline 'penalty' score for the rest of the competition.")
    dressage = Image.open('dressage.png')
    st.image(dressage)
    st.write(" ")

    st.subheader('Phase 2: Cross Country')
    st.write("Cross country is where a rider is given a course of between 12 and 20 jumps through the woods/fields. They are expected to complete the course within a certain time frame. This is referred to as 'optimum time'.")
    st.write("For every second you go over optimum time, you receive 0.4 penalty points. If your horse refuses a fence on course, 20 penalty points is added to your overall score.  If your horse refuses the same obstacle 2 times, you receive 40 penalty points. The third refusal at that same obstacle results in elimination from the competition. If your horses refuses 3 separate fences, you would receive 20 penalties per fence (aka 60 penalties). Four total refusals at separate fences results in elimination.")
    st.write("The time and jump penalties are then added to your dressage penalty score.")
    xc = Image.open('xc.png')
    st.image(xc)
    st.write(" ")

    st.subheader('Phase 3: Stadium Jumping')
    st.write("For stadium jumping, the rider is given a course that is set up in an arena. The rider has to memorize the course, complete it within a certain time limit, and knock down as few rails as possible.")
    st.write("For every second over the optimum time, you have 0.4 penalty points added to your score. Each rail that you knock down, and each time your horse refuses a fence, you will have 4 penalty points added to your score.")
    st.write("In the upper levels of eventing, you are eliminated after you have 2 refusals. Your total penalties are then added to the calculated score from after Phase 2 to give your the final penalty score. The person with the lowest score places first.")
    stadium = Image.open('stadium.png')
    st.image(stadium)

with tab4:
    st.write("As the equestrian world continued to evolve throughout time, the demand for more athletic and intelligent horses grew. Competitors from around the world began to breed different kinds of horses to find that 'perfect' mixture that would bring them to the winners circle.")
    st.write("Although there are over 400 breeds of horse throughout the world today, they can all be categorized into different classifications based on their temperament. 3 of these classifications describe horse breeds commonly used in eventing.")
    st.write(" ")
    
    st.subheader('Hot-Blooded Horses (aka Thoroughbreds)')
    st.write("Thoroughbreds are very high-spirited horses that are well-known for their astounding agility and amazing speed.  Having a lot of energy is a great advantage in eventing because you need it to last through all 3 phases, but too much spirit comes with a price.")
    st.write("Thoroughbreds are more likely to scare or hurt themselves because they have a harder time focusing on the task at hand.")
    tb = Image.open('tb.png')
    st.image(tb)
    st.write(" ")

    st.subheader('Warmbloods')
    st.write("Next, you have Warmbloods which are crosses between cold-blooded horse (like draft horses and Quarter Horses) and hot-bloods (like the Thoroughbred).")
    st.write("There is a very large number of horse breeds that fall into this category. This category of horse is commonly known for inheriting the same athletic agility as Thoroughbreds while maintaining the same trainable mindset as a cold-blood.")
    st.write("Warmbloods are well known for being eager to learn, and they always strive to please their rider. The calm nature can also be a detriment when it comes to clearing Stadium courses and making the optimum time in cross country.")
    wb = Image.open('wb.png')
    st.image(wb)
    st.write(" ")

    st.subheader('Sport Horses')
    st.write("Lastly, we have Sport Horses. Sport horses are becoming more common as years pass because the equestrian industry as a whole is trying to find that perfect combination of Thoroughbred speed/agility and Warmblood brains/trainability.")
    st.write("There is a lot of variability in this classification. Some Sport Horses may only have 1 or 2 throughbreds in their lineage whereas other may only have 1 or 2 warmbloods.")
    sport = Image.open('sport.png')
    st.image(sport)
