def stop_words_remover(df): #takes in a pandas dataframe as input
    """function to remove english stop words"""

    new_df = pd.DataFrame([]) #creat new dataframe
    tokenised_list = [] # tokenised sentence
    
    for row in df['Tweets']:
        no_stops = [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
        tokenised_list.append(no_stops) # adds words that are not in stop word dictionary into tokenised_list
    
    new_df['Tweets'] = df['Tweets'] #creats copy of tweets column
    new_df['Date'] = df['Date']# creates copy of column Date
    
    new_df['Without Stop Words'] = tokenised_list # creates column "Without stop words" containing tokenised list
    
    return new_df
### END FUNCTION
