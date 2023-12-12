from nltk import ngrams
sentence='I reside in Bengaluru'
n=3
unigrams=ngrams(sentence.split(),n)
print("SJC22MCA-2027 Georgekutty Biju\nS3MCA")
for grams in unigrams:
    print(grams)