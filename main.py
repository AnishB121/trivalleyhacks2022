import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def recommend(data,names,choice):
 tfidf = TfidfVectorizer(stop_words='english')
 tfidf_matrix = tfidf.fit_transform(data)
 #finds fetaures in the text
 tfidf.get_feature_names_out()[5000:5010]
 #finds cosine similarity between features
 cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
 def get_recommendations(title, cosine_sim=cosine_sim):
      duf = names.index(title)
      jow = cosine_sim[duf]
      ans =[]
      jow = list(jow)
      for i in jow:
         if i > 0:
             joa = jow.index(i)
             ans.append(names[joa])
      ans.remove(title)
      #incase no similarty is found
      if ans == []:
           print(random.choice(names))
      else:
           print(ans[0])
           
 get_recommendations(choice)
dat =["Long-running drive-through offering milk, cheese, ice cream & other dairy products, plus fast fare.","Caribbean & South American shared plates offered in bright surrounds with palms & paintings.","Spacious, colorful brewpub offering a lineup of its own beers, a bar food menu & regular live music.","Upscale bistro serving modern Spanish-Californian cuisine & drinks in a sleek space with 2 patios.","This bakery known for its unique wedding cake designs also offers pastries, tarts & other treats."]
name = ['meadowlark dairy','oyo','main street brewery','sabio on main','primrose bakery']
choose = random.choice(name)
recommend(dat,name,choose)
