import pandas as pd
import streamlit as st
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("instagram_reach.csv")

# Set stopwords
stopwords = set(STOPWORDS)
stopwords.add('will')

# Define word cloud plotter function
def WordCloudPlotter(dfColumn):
    colData = data[dfColumn]
    textCloud = ''
    
    # Text processing converting colums to a single line of text
    for mem in colData:
        textCloud = textCloud + str(mem)
    
    # Plotting word cloud
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color='white',
        stopwords=stopwords,
        min_font_size=10
    ).generate(textCloud)
    
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    plt.style.use('seaborn-whitegrid')
    plt.imshow(wordcloud) 
    plt.rcParams.update({'font.size': 25})
    plt.axis("off") 
    plt.title('Word Cloud: ' + str(dfColumn))
    plt.tight_layout(pad=0)
  
    st.pyplot(fig)


# Create Streamlit app
def show_explore_page():
    # Add title and subtitle to app
    st.title("Instagram Reach Word Cloud")
    # st.subheader("The most commonly used words.")

    # WordCloudPlotter('Caption')

    # st.subheader("The most commonly used hastags.")

    # WordCloudPlotter('Hashtags')

    # st.subheader("Regplot for Followers vs Likes")
    # PlotData(['Followers', 'Time since posted'])


    # st.subheader("Regplot for Followers vs Likes")

    option = st.sidebar.selectbox("Explore Or Predict", ("Caption", "Hashtags"))

    if option == "Caption":
        st.subheader("The most commonly used words.")

        WordCloudPlotter('Caption')
    else:
        st.subheader("The most commonly used hastags.")

        WordCloudPlotter('Hashtags')
