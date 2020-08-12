def number_of_tweets_per_day(df):
    """ The Function takes in a pandas dataframe as input.
        It then returns a new dataframe, grouped by day, with the number of tweets for that day. """
    
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df1 = df.groupby('Date').count()



    return df1
