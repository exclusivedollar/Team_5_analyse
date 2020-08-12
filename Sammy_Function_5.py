def number_of_tweets_per_day(df):
    
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df1 = df.groupby('Date').count()



    return df1
