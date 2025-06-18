from transformers import pipeline
model=pipeline("sentiment-analysis")
result=model("i hate you!")
print(result)