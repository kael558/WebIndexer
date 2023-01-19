import streamlit as st

from generation import construct_context, post
from helper import get_keys
import cohere
from index import get_closest_paragraphs, get_index, load_dataset

import matplotlib.pyplot as plt

cohere_key, ai21_key = get_keys()
co = cohere.Client(cohere_key)

st.title("Web Indexer")

dataset = st.selectbox('Select a dataset', ['Spring 3.2', 'Spring 4.3', 'Spring 5.2'])
question = st.text_input('Enter a question:', 'What is the difference between @Autowired and @Resource?')

df = load_dataset(f'data/{dataset}.csv')
index = get_index(co, df, f'{dataset}.ann')

if question != "":
    num_nearest = int(st.number_input('Number of paragraphs', min_value=10, max_value=1000, value=50))
    paragraphs = get_closest_paragraphs(co, df, index, question, num_nearest)

    min_distance = round(paragraphs['distance'].min(), 1)
    max_distance = round(paragraphs['distance'].max(), 1)

    fig, ax = plt.subplots()
    bins = round((max_distance-min_distance)*10)
    ax.hist(paragraphs["distance"], range=(min_distance, max_distance), bins=bins)
    ax.set_xlabel('Distance')
    ax.set_ylabel('Frequency')
    ax.axvline(x=st.session_state.get('threshold', 1.0), linewidth=3, color='r', label='threshold')
    st.pyplot(fig)

    threshold = st.slider('Threshold', min_value=min_distance, max_value=max_distance, value=1.0, step=0.1)
    if threshold != st.session_state.get('threshold', 1.0):
        st.session_state['threshold'] = threshold
        st.experimental_rerun()

    context = construct_context(paragraphs, threshold)
    answer = post(context, question, ai21_key)

    st.header('Answer')
    answer_placeholder = st.empty()
    answer_placeholder.write(answer)

    st.header('Context')
    context_placeholder = st.empty()
    context_placeholder.write(context)

    st.header('Top Links')
    links_placeholder = st.empty()
    links = paragraphs[paragraphs['distance'] < threshold]['links'].value_counts(normalize=True).nlargest(5).mul(100).round(1).astype(str) + '%'
    links_placeholder.write(links)

    st.write("To request a website to be indexed, send a friendly email to rahel.gunaratne@gmail.com")



