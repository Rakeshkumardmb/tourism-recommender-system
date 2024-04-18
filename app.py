import streamlit as st
import pickle
import pandas as pd

# def recommend(tour):
#     tour_index = tour[tour['Name'] == tour].index[0]
#     distances = similarity[tour_index]
#     tour_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_tour = []
#     for i in tour_list:
#         recommended_tour.append(tour.iloc[i[0]].Name)
#     return recommended_tour

def recommend(selected_tour_name):
    tour_index = tour[tour['Name'] == selected_tour_name].index[0]
    distances = similarity[tour_index]
    tour_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_tour = []
    for i in tour_list:
        recommended_tour.append(tour.iloc[i[0]].Name)
    return recommended_tour

tour_dict = pickle.load(open('tour_dict.pkl','rb'))
tour = pd.DataFrame(tour_dict)

similarity = pickle.load((open('similarity.pkl','rb')))

st.title('Tourism Recommender System')

selected_tour_name = st.selectbox(
    'How would you like to be contacted?',
    tour['Name'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_tour_name)
    for i in recommendations:
        st.write(i)