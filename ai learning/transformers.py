from transformers import pipeline
model=pipeline("sentiment-analysis")
a=input()
result=model(a)
print(result)