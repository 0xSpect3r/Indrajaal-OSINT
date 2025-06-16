import streamlit as st
import snscrape.modules.twitter as sntwitter
import pandas as pd

def run():
    st.header("Twitter OSINT")
    username = st.text_input("Enter Twitter username (without @)")
    if username:
        st.info(f"Fetching tweets for @{username} ...")
        tweets = []
        try:
            for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
                if i > 10:
                    break
                tweets.append([tweet.date, tweet.content, tweet.replyCount, tweet.retweetCount, tweet.likeCount])
            df = pd.DataFrame(tweets, columns=["Date", "Content", "Replies", "Retweets", "Likes"])
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error fetching tweets: {e}")