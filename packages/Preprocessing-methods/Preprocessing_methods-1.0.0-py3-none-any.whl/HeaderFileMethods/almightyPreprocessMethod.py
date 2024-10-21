import os
import nltk
import spacy

nlp=spacy.load('en_core_web_sm')



def almightyPreprocessMethod(anything):
  if isinstance(anything,str):
    if anything.endswith('.txt'):
      #text file as param
      with open(anything) as f:
        text=f.readlines()

      proper_text = ' '.join(text)

      final_string=complete_preprocess(proper_text)
      return final_string


    else:
      #string as param
      final_string=completePreprocessMethod(anything)
      return final_string

  elif isinstance(anything,list):
    #list/array as param
    tokenized_string=' '.join(anything)

    final_string=completePreprocessMethod(tokenized_string)
    return final_string

  else:
    return "Invalid param passed"
