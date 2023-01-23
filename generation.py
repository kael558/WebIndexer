
def construct_context(df, threshold):
    context = ""
    for index, row in df.iterrows():
        if row['distance'] < threshold:
            context += row['texts']
    return context


def post(context, question):
    import requests
    from helper import get_keys

    _, ai21_key = get_keys()

    response = requests.post("https://api.ai21.com/studio/v1/j1-grande/complete",
                             headers={"Authorization": f"Bearer {ai21_key}"},
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
    if 'completions' not in response or response['completions'][0]['data']['text'] == '' or \
            response['completions'][0]['data']['text'].isspace():
        return None

    return response['completions'][0]['data']['text'].strip()


def test():
    dataset = 'AI21'

    from index import get_closest_paragraphs, get_index, load_dataset

    df = load_dataset(f'{dataset}.csv')
    index = get_index(df, f'{dataset}.ann')
    while True:
        query = input("Enter a question: ")
        if query == 'x':
            break
        paragraphs = get_closest_paragraphs(df, index, query)
        context = construct_context(paragraphs, 1.0)
        answer = post(context, query)
        print(context)
        print(query)
        print(answer)


if __name__ == '__main__':
    test()
