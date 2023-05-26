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

# def PlotData(features):
#     fig2 = plt.figure(figsize= (20, 10))    
#     pltNum = 1
#     for mem in features:
#         plt.subplot(1, 2 , pltNum)
#         plt.style.use('seaborn-whitegrid')
#         plt.grid(True)
#         plt.title('Regplot Plot for '+ str(mem))
#         sns.regplot(data = data, x = mem, y = 'Likes' , color = 'green')
#         pltNum += 1
#         # st.pyplot(fig2) 
#         st.pyplot(plt.gcf())   
    

# # def true_values():
# #     predictions = gbr.predict(xTest)
# #     plt.scatter(yTest, predictions)
# #     plt.style.use('seaborn-whitegrid')
# #     plt.xlabel('true values')
# #     plt.ylabel('predicted values')
# #     plt.title('GradientRegressor')
# #     plt.plot(np.arange(0,0.4, 0.01), np.arange(0, 0.4, 0.01), color = 'green')
# #     plt.grid(True)

# #     # render the plot in Streamlit
# #     st.pyplot()


# # def PredictionsWithConstantFollowers(model, followerCount, scaller, maxVal):
# #     followers = followerCount * np.ones(24)
# #     hours = np.arange(1, 25)
    
# #     # defining vector 
# #     featureVector = np.zeros((24, 2))
# #     featureVector[:, 0] = followers
# #     featureVector [:, 1] = hours
    
# #     # doing scalling
# #     featureVector = scaller.transform(featureVector)
# #     predictions = model.predict(featureVector)
# #     predictions = (maxValLikes * predictions).astype('int')
    
# #     plt.figure(figsize= (10, 10))
# #     plt.plot(hours, predictions)
# #     plt.style.use('seaborn-whitegrid')
# #     plt.scatter(hours, predictions, color = 'g')
# #     plt.grid(True)
# #     plt.xlabel('hours since posted')
# #     plt.ylabel('Likes')
# #     plt.title('Likes progression with ' + str(followerCount) +' followers')
# #     st.pyplot()


# # define the true_values function
# def true_values(gbr, xTest, yTest):
#     predictions = gbr.predict(xTest)
#     plt.scatter(yTest, predictions)
#     plt.style.use('seaborn-whitegrid')
#     plt.xlabel('true values')
#     plt.ylabel('predicted values')
#     plt.title('GradientRegressor')
#     plt.plot(np.arange(0, 0.4, 0.01), np.arange(0, 0.4, 0.01), color='green')
#     plt.grid(True)
#     # render the plot in Streamlit
#     st.pyplot()

# # define the PredictionsWithConstantFollowers function
# def PredictionsWithConstantFollowers(model, followerCount, scaller, maxValLikes):
#     followers = followerCount * np.ones(24)
#     hours = np.arange(1, 25)
#     # defining vector featureVector
#     featureVector = np.zeros((24, 2))
#     featureVector[:, 0] = followers
#     featureVector[:, 1] = hours
#     # doing scaling
#     featureVector = scaller.transform(featureVector)
#     predictions = model.predict(featureVector)
#     predictions = (maxValLikes * predictions).astype('int')
#     plt.figure(figsize=(10, 10))
#     plt.plot(hours, predictions)
#     plt.style.use('seaborn-whitegrid')
#     plt.scatter(hours, predictions, color='g')
#     plt.grid(True)
#     plt.xlabel('hours since posted')
#     plt.ylabel('Likes')
#     plt.title('Likes progression with ' + str(followerCount) + ' followers')
#     # render the plot in Streamlit
#     st.pyplot()


# Create Streamlit app
def show_explore_page():
    # Add title and subtitle to app
    st.title("Instagram Reach Word Cloud")
    st.subheader("The most commonly used words.")

    WordCloudPlotter('Caption')

    st.subheader("The most commonly used hastags.")

    WordCloudPlotter('Hashtags')

    st.subheader("Regplot for Followers vs Likes")
    PlotData(['Followers', 'Time since posted'])


    st.subheader("Regplot for Followers vs Likes")

    true_values()
    
    # PredictionsWithConstantFollowers(gbr, 100, stdSc, maxValLikes)

    