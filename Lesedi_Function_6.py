def word_splitter(df):   
    """Splits and lowercases sentences in a dataframe's column into a list of seperate words.
       Created lists will be placed in a column named 'Split Tweets' in the
       original dataframe.Also known as tokenization
       
       Arguments : Takes in a pandas dataframe as an input
       Returns: returns a modified dataframe""" 
       
    dframe = pd.DataFrame(df,columns =['Tweets','Date','Split Tweets'])
    dframe['Date'] = dates
    dframe['Split Tweets']= dframe['Tweets'].str.lower()
    dframe['Split Tweets']= dframe['Split Tweets'].str.split()  
    return dframe
