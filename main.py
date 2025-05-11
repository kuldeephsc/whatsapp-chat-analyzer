from flask import Flask, render_template
import streamlit as st
from io import BytesIO
import preprocessor,helper
import matplotlib.pyplot as plt
#Creating a sidebar with below name
st.sidebar.title("What's App Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocess(data)

    #fetch unique users and convert it to list
    user_list=df['user'].unique().tolist()
    user_list.remove('group-notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show Analysis wrt",user_list)
    st.dataframe(df)
    if(st.sidebar.button("Show Analysis")):
        num_messages,words,num_media_messages,num_of_links=helper.fetch_stats(selected_user,df)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header('Totel Messages')
            st.title(num_messages)
        with col2:
            st.header('Total Words')
            st.title(words)
        with col3:
            st.header('Media Messages')
            st.title(num_media_messages)
        with col4:
            st.header('Media Links')
            st.title(num_of_links)
    #finding bussiest user in the group
    if(selected_user=='Overall'):
        st.title('Most Busy Users')
        x,new_df=helper.most_busy_user(df)
        fig,ax=plt.subplots()
        col1 ,col2 =st.columns(2)
        with col1:
            ax.bar(x.index,x.values,color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.dataframe(new_df)
    st.title("Word Cloud")
    ##word cloud
    wc_df=helper.create_wordcloud(selected_user,df)
    fig,ax=plt.subplots()
    ax.imshow(wc_df)
    st.pyplot(fig)
    #most common word
    most_common_df=helper.most_common_word(selected_user,df)
    fig,ax=plt.subplots()
    ax.bar(most_common_df[0],most_common_df[1],color='red')
    plt.xticks(rotation='vertical')
    st.title('Most Common Word')
    st.pyplot(fig)
    #st.dataframe(most_common_df)

    #Emoji Analysis
    emoji_df=helper.emoji_helper(selected_user,df)
    st.title('Emoji Analysis')
    col1,col2=st.columns(2)
    with col1:
        st.dataframe(emoji_df)
    with col2:
        fig,ax=plt.subplots()
        ax.pie(emoji_df[1],labels=emoji_df[0],autopct='%0.2f')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)



    


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")