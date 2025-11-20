# Required libraries
import tweepy
from collections import Counter
import re
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

# -----------------------------
# Twitter API Settings
# -----------------------------
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"

client = tweepy.Client(bearer_token=bearer_token)

# -----------------------------
# Fetch Tweets
# -----------------------------
query = "Python -is:retweet lang:en"  # English tweets, excluding retweets
tweets = client.search_recent_tweets(query=query, max_results=100)

tweet_texts = [tweet.text for tweet in tweets.data]
print("Sample tweets:")
for t in tweet_texts[:5]:
    print("-", t)

# -----------------------------
# Text cleaning and keyword analysis
# -----------------------------
stop_words = set(stopwords.words('english'))
words = []

for tweet in tweet_texts:
    tweet = tweet.lower()  # Convert to lowercase
    tweet = re.sub(r'[^\w\s]', '', tweet)  # Remove punctuation
    words.extend([word for word in tweet.split() if word not in stop_words])

word_counts = Counter(words)
most_common = word_counts.most_common(10)
print("\nTop 10 Keywords:")
for word, count in most_common:
    print(word, ":", count)

# -----------------------------
# Bar chart of top keywords
# -----------------------------
words, counts = zip(*most_common)
plt.figure(figsize=(10,5))
plt.bar(words, counts, color='skyblue')
plt.title("Top 10 Keywords in Tweets about Python")
plt.show()

# -----------------------------
# Word cloud visualization
# -----------------------------
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
