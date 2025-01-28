import pandas as pd 
import numpy as np 
import re
from collections import Counter
import textdistance
from textdistance import jaccard
import logging

def load_vocablary():
    file1 = open("words.txt","r")
    text=file1.read().lower()
    text=re.findall(r'\w+',text)
    unique_words=set(text)
    word_freq=Counter(text)
    total=sum(word_freq.values())
    prb_dist={k:word_freq[k]/total for k in word_freq}
    return unique_words,word_freq,prb_dist

def calculate_jaccard_similarity(input_word,word_freq):
    input_word=input_word.lower()
    sim_score = [1 - jaccard(input_word, word) for word in word_freq.keys()]
    return sim_score

def my_autocorrect(input_paragraph,word_freq,unique_words,prb_dist,top_n=5):
    input_paragraph=input_paragraph.lower()
    words_in_para=re.findall(r'\w+',input_paragraph)
    incorrected_words=[]
    corrected_words=[]

    for word in words_in_para:
        if word not in unique_words:
            logging.info(word)
            logging.info(word_freq)
            similar_words=calculate_jaccard_similarity(input_word=word,word_freq=word_freq)
            df=pd.DataFrame.from_dict(prb_dist,orient='index').reset_index()
            df=df.rename(columns={'index':'Word',0:'Prob'})
            df['similarity']=similar_words
            output=df.sort_values(['similarity','Prob'],ascending=False).head(top_n)
            output=output[['Word','similarity','Prob']].reset_index(drop=True)
            output.index=output.index+1
            incorrected_words.append(word)
            corrected_words.append(output)

    return incorrected_words,corrected_words
