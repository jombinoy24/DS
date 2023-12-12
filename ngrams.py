def gen_ngrams(text,WordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words)-WordsToCombine+1):
        output.append(words[i:i+WordsToCombine])
    return output
print("SJC22MCA-2027 : Georgekutty Biju\nS3MCA")
x=gen_ngrams(
    text='The data set given satisfies the requirement for model generation., This is used in Data Science Lab',
    WordsToCombine=3
)
print(x)