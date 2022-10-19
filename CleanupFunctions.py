


# Converting all tweets to lowercase
def convert_to_lowercase(text):
 return text.lower()


# punc_clean ofzo
def punc_clean(text):
    punct = st.punctuation
    trantab = str.maketrans(punct, len(punct)*' ')  # Every punctuation symbol will be replaced by a space
    return text.translate(trantab)


def remove_stopword(text):
    stopword=nltk.corpus.stopwords.words('english')
    stopword.remove('not')
    a=[w for w in nltk.word_tokenize(text) if w not in stopword]
    return ' '.join(a)


    # Bron: https://datapeaker.com/big-data/integre-r-tableau-y-excel/
import nltk
import string as st
import re