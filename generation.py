import streamlit as st

import requests

@st.cache
def construct_context(df, threshold):
    context = ""
    for index, row in df.iterrows():
        if row['distance'] < threshold:
            context += row['texts']
    return context

@st.cache
def post(context, question, key):
    response = requests.post("https://api.ai21.com/studio/v1/j1-grande/complete",
                             headers={"Authorization": f"Bearer {key}"},
                             json={
                                 "prompt": f"Context: {context}\nQuestion: {question}\nAnswer:",
                                 "numResults": 1,
                                 "maxTokens": 64,
                                 "temperature": 0,
                                 "topKReturn": 0,
                                 "topP": 1,
                                 "countPenalty": {
                                     "scale": 0,
                                     "applyToNumbers": False,
                                     "applyToPunctuations": False,
                                     "applyToStopwords": False,
                                     "applyToWhitespaces": False,
                                     "applyToEmojis": False
                                 },
                                 "frequencyPenalty": {
                                     "scale": 0,
                                     "applyToNumbers": False,
                                     "applyToPunctuations": False,
                                     "applyToStopwords": False,
                                     "applyToWhitespaces": False,
                                     "applyToEmojis": False
                                 },
                                 "presencePenalty": {
                                     "scale": 0,
                                     "applyToNumbers": False,
                                     "applyToPunctuations": False,
                                     "applyToStopwords": False,
                                     "applyToWhitespaces": False,
                                     "applyToEmojis": False
                                 },
                                 "stopSequences": ["↵"]
                             }
                             )

    response = response.json()
    if 'completions' not in response or response['completions'][0]['data']['text'] == '':
        return 'I don\'t know'

    return response['completions'][0]['data']['text'].strip()



def test():
    from helper import get_keys
    import cohere
    from index import get_closest_paragraphs, get_index, load_dataset

    cohere_key, ai21_key = get_keys()
    co = cohere.Client(cohere_key)

    df = load_dataset('data/spring3-2.csv')
    index = get_index(co, df, 'spring3-2.ann')
    while True:
        query = input("Enter a question: ")
        if query == 'x':
            break
        paragraphs = get_closest_paragraphs(co, df, index, query)
        context = construct_context(paragraphs, 1.0)
        answer = post(context, query, ai21_key)
        print(context)
        print(query)
        print(answer)


if __name__ == '__main__':
    test()
