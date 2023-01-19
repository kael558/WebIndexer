import os

from annoy import AnnoyIndex

import numpy as np
import pandas as pd

import streamlit as st


@st.cache
def load_dataset(data_file) -> pd.DataFrame:
    df = pd.read_csv(data_file)[:1000]
    return df


def _build_index(co, df, index_filename) -> None:
    embeds = co.embed(texts=list(df['paragraphs']),
                      model='large',
                      truncate='left').embeddings

    embeds = np.array(embeds)

    # Create the search index, pass the size of embedding
    search_index = AnnoyIndex(embeds.shape[1], 'angular')
    # Add all the vectors to the search index
    for i in range(len(embeds)):
        search_index.add_item(i, embeds[i])
    search_index.build(50)  # 10 trees
    search_index.save(index_filename)

def get_index(co, df: pd.DataFrame, index_filename: str) -> AnnoyIndex:
    index_dir = 'indexes'

    if not os.path.isdir(index_dir):
        os.mkdir(index_dir)

    index_path = os.path.join(index_dir, index_filename)
    if not os.path.isfile(index_path):
        _build_index(co, df, index_path)

    index = AnnoyIndex(4096, 'angular')
    index.load(index_path)
    return index

def get_closest_paragraphs(co, df: pd.DataFrame, index: AnnoyIndex, query: str, n: int = 100) -> pd.DataFrame:
    query_embed = co.embed(texts=[query],
                           model='large',
                           truncate='left').embeddings
    query_embed = np.array(query_embed)

    # Retrieve nearest neighbors
    similar_item_ids = index.get_nns_by_vector(query_embed[0], n,
                                               include_distances=True)

    # Format and print the text and distances
    results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['paragraphs'],
                                 'links': df.iloc[similar_item_ids[0]]['link'],
                                 'distance': similar_item_ids[1]})

    #print(f"Question:'{query}'\nNearest neighbors:")
    #for i, row in results.iterrows():
    #    print(row['distance'], row['texts'])

    return results


def test():
    from helper import get_keys
    import cohere

    cohere_key, ai21_key = get_keys()
    co = cohere.Client(cohere_key)

    df = load_dataset('data/spring3-2.csv')
    index = get_index(co, df, 'spring3-2.ann')
    while True:
        query = input("Enter a question: ")
        if query == 'x':
            break
        get_closest_paragraphs(co, df, index, query)

if __name__ == '__main__':
    test()
