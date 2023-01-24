import os
from math import floor, ceil

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from generation import construct_context, post
from index import get_closest_paragraphs, get_index, load_dataset


@st.cache
def cached_wrapper(func, *args):
    return func(*args)


st.title("Web Indexer")


def get_files():
    files = []
    for file in os.listdir("data"):
        if file.endswith(".csv"):
            files.append(file[:-4])
    files.sort(reverse=True)
    return files


dataset = st.selectbox('Select a website', get_files())
question = st.text_input('Enter a question:', 'What is the difference between @Autowired and @Resource?')

df = cached_wrapper(load_dataset, f'{dataset}.csv')
index = get_index(df, f'{dataset}.ann')

if question != "":
    num_nearest = int(st.number_input('Number of paragraphs', min_value=10, max_value=1000, value=50))
    paragraphs = get_closest_paragraphs(df, index, question, num_nearest)

    min_distance = floor(paragraphs['distance'].min() * 10) / 10
    max_distance = ceil(paragraphs['distance'].max() * 10) / 10
    fig, ax = plt.subplots()
    bins = round((max_distance - min_distance) * 10)
    ax.hist(paragraphs["distance"], range=(min_distance, max_distance), bins=bins)
    ax.set_title("Distribution of Distances")
    ax.set_xticks(np.arange(min_distance, max_distance + 0.001, 0.1))
    ax.set_xlabel('Distance')
    ax.set_ylabel('Frequency')
    ax.axvline(x=st.session_state.get('threshold', min_distance + 0.1), linewidth=3, color='r', label='threshold')
    st.pyplot(fig)

    threshold = st.slider('Threshold', min_value=min_distance, max_value=max_distance, value=float(min_distance + 0.1),
                          step=0.1)
    if threshold != st.session_state.get('threshold', min_distance + 0.1):
        st.session_state['threshold'] = threshold
        st.experimental_rerun()

    context = cached_wrapper(construct_context, paragraphs, threshold)
    answer = cached_wrapper(post, context, question)

    st.subheader('Answer')
    answer_placeholder = st.empty()
    answer_placeholder.write(answer if answer else 'I don\'t know given the current information.')

    links = paragraphs[paragraphs['distance'] < threshold]['links'].value_counts(normalize=True).nlargest(5).mul(
        100).round(1).astype(str) + '%'

    if links.any():
        st.subheader('Top Links')
        links_placeholder = st.empty()
        links_placeholder.write(links)

    if context:
        st.subheader('Context')
        context_placeholder = st.empty()
        context_placeholder.write(context)

    st.subheader("Contact")
    st.write("To request a website to be indexed, send a friendly email to rahel.gunaratne@gmail.com")
