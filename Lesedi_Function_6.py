def word_splitter(df):   
    """Splits and lowercases sentences in a dataframe's column into a list of seperate words.
       Created lists will be placed in a column named 'Split Tweets' in the
       original dataframe.Also known as tokenization
       
       Arguments : Takes in a pandas dataframe as an input
       Returns: returns a modified dataframe""" 
    #Creates a new Dataframe using the given one
    dframe = pd.DataFrame(df,columns =['Tweets','Date','Split Tweets'])

    #Creates a column called 'Date' and assign given dates to it         
    dframe['Date'] = dates

    #Modifies the 'Split Tweets' column by making every character lowercase and splits
    dframe['Split Tweets']= dframe['Tweets'].str.lower()
    dframe['Split Tweets']= dframe['Split Tweets'].str.split()

    #Returns the modifies Dataframe  
    return dframe
