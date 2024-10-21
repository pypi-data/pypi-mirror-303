""" 
IMPORTS
"""
import pandas as pd
import re
import tqdm
from tqdm import tqdm
import spacy as sp
import spacy_cleaner as spc
from spacy_cleaner.processing import mutators, removers

language_model = sp.load('en_core_web_trf')

# %%
def lowercase(series):
    """ 
    INPUT    --> Series
                 
    FUNCTION --> lower cases the texts in the given Series and,
                 puts them in a list
    
    OUTPUT   --> list
    """
    lowercased = list()
    
    for item in tqdm(series, desc='Lowercasing in progress'):
        lowercased.append(item.lower())
    
    return lowercased

# %%
def clean(list_of_docs):
    """ 
    INPUT    --> list
                 
    FUNCTION --> removes the stopwords, numbers, urls, eamils, punctuations
                 of the documents in the list
                 
    OUTPUT   --> list
    """
    
    remover_pipeline = spc.Cleaner(language_model,
                                   removers.remove_stopword_token,
                                   removers.remove_number_token,
                                   removers.remove_punctuation_token,
                                   removers.remove_email_token,
                                   removers.remove_url_token
                                   )
    
    length = len(list_of_docs)
        
    cleaned_docs = list()


    for doc in tqdm(list_of_docs, desc='Cleaning in progress'):
        cleaned_docs.append(remover_pipeline.clean([doc])[0])
        
       
    clean_docs = []
    
    for doc in tqdm(cleaned_docs, desc='Cleaning in progress'):
    
        cleaned_text = ""
        
        for token in language_model(doc):
            # Combine conditions more robustly
            if token.like_url or \
                    token.like_email or \
                    token.is_currency or \
                    token.is_punct or \
                    token.is_space or \
                    token.is_stop or \
                    token.like_num :  
                
                continue
            
            # Add the cleaned token to the text
            if token.is_alpha and \
                token.pos_ in {"NOUN", "VERB", "ADJ", "ADV", "PROPN", "INTJ"}:
                cleaned_text += (token.text + ' ')
        
        # Trim and append the cleaned text
        clean_docs.append(cleaned_text.strip())


    return clean_docs    

# %%
def lemmatize(list_of_docs):
    """ 
    INPUT    --> list
                 
    FUNCTION --> lemmatizes the documents in the list
    
    OUTPUT   --> list
    """
    
    lemma_pipeline = spc.Cleaner(language_model, 
                                 mutators.mutate_lemma_token)
    

    lemma_docs_list = list()
    for doc in tqdm(list_of_docs, desc='lemmatization in progress'):
        lemma_docs_list.append(lemma_pipeline.clean([doc])[0])
        

    return lemma_docs_list

# %%
def tokenize_document(document):
    """ 
    INPUT    --> string(document)
                 
    FUNCTION --> tokenizes the document with spacy
    
    OUTPUT   --> document format of spacy
    """
    
    tokenized_document = language_model(document)
        
    return tokenized_document

# %%
def tokenize_documents(documents_list):
    """ 
    INPUT    --> strings list
                 
    FUNCTION --> tokenizes the documents in the list with spacy
    
    OUTPUT   --> list
    """
    
    tokenized_documents_list =[]
    
    for i in range(0, len(documents_list)):
        tokenized_documents_list.append(
            tokenize_document(
                documents_list[i]
                ))
        
    return tokenized_documents_list

# %%
def extract_unique_words(documents_list):
    """ 
    INPUT    --> documents list
                 
    FUNCTION --> extracts the unique words from the documents in the given list
                 and returns the in a set
                 
    OUTPUT   --> set
    """
    
    unique_words_set = set()
    for i in tqdm(range(0, len(documents_list))):
        doc = language_model(documents_list[i])
        for token in doc:
            # Add the lemmatized form of the token to the set
            unique_words_set.add(token.lemma_)

    return unique_words_set


# %%
def wordscount(documents_list):  
    """ 
    INPUT    --> documents list
                 
    FUNCTION --> extracts the unique words from the documents in the given list
                 and their amount then puts them in a dictionary in below format
                 dict = {
                     keys --> words 
                     values --> amount
                     }
    
    OUTPUT   --> unique word count dictionary
    """
    
    words_count_dict = dict()

    for Doc in tqdm(documents_list, desc= 'Word Counting'):
        for token in Doc:
            if token.text in words_count_dict.keys():
                words_count_dict[token.text] += 1
            else:
                words_count_dict[token.text] = 1
 
    for key in list(words_count_dict.keys()):
        if      words_count_dict[key] <= 10 or \
                key =='[' or \
                key == ']' or \
                key == '$' or \
                key == "'" or \
                key == "'s" or \
                key == '+' or \
                key == '=' or \
                key == '=)' or \
                key == 'a&m' or \
                key == 'a.' :
                    
            del words_count_dict[key]

    return words_count_dict

# %%
