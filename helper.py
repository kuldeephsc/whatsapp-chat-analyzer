from urlextract import URLExtract
import matplotlib as plt
extract=URLExtract()
from wordcloud import WordCloud
import pandas as pd
import emoji
from collections import Counter
def fetch_stats(selected_user,df):
    if(selected_user!='Overall'):
   
        df=df[df['user']==selected_user]
    #fetch number of messages
    num_messages=df.shape[0]
    #number of words
    word=[]
    for message in df['message']:
        word.extend(message.split())
    
    #fetch number of media messages
    num_media_messages=df[df['message']=='<Media omitted>\n'].shape[0]
    #fetch urls
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(word),num_media_messages,len(links)

##most busy user
def most_busy_user(df):
   
    x=df['user'].value_counts().head()
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'name':'Name','count':'percentage'})
    return x,df
def create_wordcloud(selected_user,df):
    if(selected_user!='Overall'):
        df=df[df['user']==selected_user]
    wc=WordCloud(width=500,height=500,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc
#most common word
def most_common_word(selected_user,df):
    f=f = open('C:\\Users\\KuldeepMaurya\\Desktop\\dataset\\stop_words_hinglish.txt', 'r')
    stop_words=f.read()
    if(selected_user!='Overall'):
        df=df[df['user']==selected_user]
    temp=df[df['user']!='group-notification']
    temp=temp[temp['message']!='<Media omitted>\n']
    words=[]
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df
def emoji_helper(selected_user,df):
    if(selected_user!='Overall'):
        df=df[df['user']==selected_user]
    emojies=[]
    for message in df['message']:
        emojies.extend([char for char in message if emoji.emoji_count(char) > 0])
    emoji_df=pd.DataFrame(Counter(emojies).most_common(len(Counter(emojies))))
    return emoji_df
    



    
   