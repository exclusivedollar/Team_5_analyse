def word_splitter(df):    
    dframe = pd.DataFrame(df,columns =['Tweets','Date','Split Tweets'])
    dframe['Date'] = dates
    dframe['Split Tweets']= dframe['Tweets'].str.lower()
    dframe['Split Tweets']= dframe['Split Tweets'].str.split()  
    return dframe