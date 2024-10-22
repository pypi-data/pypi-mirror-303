import os
import nltk
import spacy

nlp=spacy.load('en_core_web_sm')

print("======== You have summoned the Almighty Preprocess Method ========")





def completePreprocessMethod(str):



  #Tokenization
  #==================
  token_doc=nlp(str.lower())
  token_array=[]

  for token in token_doc:
    token_array.append(token.text)
    token_string=' '.join(token_array)

  print("\n After Tokenization-------->\n",token_string)


  #remove stopwords and punct and lemmatize
  #==================
  from spacy.lang.en.stop_words import STOP_WORDS

  stoppunclemma_doc=nlp(token_string)
  stoppunclemma_array=[]

  for token in stoppunclemma_doc:

    if not (token.is_stop or token.is_punct):
      stoppunclemma_array.append(token.lemma_)

  stoppunclemma_string=' '.join(stoppunclemma_array)

  print("\n After removing stopwords and punctuations and lemmatizing-------->\n",stoppunclemma_string)




  #stemming
  #==================
  words=stoppunclemma_array
  from nltk.stem import PorterStemmer
  stemmer=PorterStemmer()
  stemmArray=[]

  for i in words:
    stemmArray.append(stemmer.stem(i))

  string_stemm = ' '.join(stemmArray)
  print("\nAfter stemming-------->\n",string_stemm)




  '''
  #lemma
  #==================
  lemma_doc=nlp(string_stemm)

  lemmaArray=[]

  for i in lemma_doc:
    lemmaArray.append(i.lemma_)

  string_lemma = ' '.join(lemmaArray)
  print("\nafter lemmatization-------->\n",string_lemma)

  '''


  final_string=string_stemm

  print("Final string\n")

  return final_string


#YOU are calling this method
#This is the main method to call.

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
  


