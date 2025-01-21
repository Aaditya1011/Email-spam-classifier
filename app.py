import streamlit as st
import string
import pickle
import nltk 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# loading pickle files.
tfidf = pickle.load(open('models/vectorizer.pkl','rb'))
model = pickle.load(open('models/model.pkl','rb'))
ps = PorterStemmer()

# streamlit app title.
st.title('Email Spam Classifier')

# preprocessing function.
def transform_text(text):

    text = text.lower()             # lowercase.
    text = nltk.word_tokenize(text) # tokenization

    # removing special characters.
    ans = []
    for i in text:
        if i.isalnum():
            ans.append(i)
    
    # storing in text.
    text = ans[:]
    ans.clear()
    
    # removing stopwords and punctuations.
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            ans.append(i)
            
    text = ans[:]
    ans.clear()
    # stemming.
    for i in text:
        ans.append(ps.stem(i))
        
    return ' '.join(ans)


# receiving input.
input_msg = st.text_area('Enter The Message')

if st.button('Predict'):
        
    # preprocessing.
    transform_msg = transform_text(input_msg)

    # vectorization.
    vector_input = tfidf.transform([transform_msg])

    # prediction.
    result = model.predict(vector_input)[0]

    if result == 1:
        st.header('Spam')
    else:
        st.header('Not Spam')
