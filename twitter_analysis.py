import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
## json object or tweets are store in tweetData

#iterate list of tweet_small
    #for each tweet access the text. use the text field tweet. tweet.text
    #print polarity

for tweet in tweetData:
    #print(tweet["text"])

    b= TextBlob(tweet["text"])
    print(b.polarity)
# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)
