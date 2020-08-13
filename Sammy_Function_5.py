    """
    The Function calculates the number of tweets that were posted per day.
    Takes in a pandas dataframe as input.
    It then returns a new dataframe, grouped by day, with the number of
    tweets for that day.
    The index of the new dataframe will be named Date, and the column of
    the new dataframe will be 'Tweets', corresponding to the date and number
    of tweets, respectively.
    The date will be formated as yyyy-mm-dd, and will be a datetime object.

    Parameter:
    df - A pandas dataframe
    Returns:
    df1 - A new dataframe grouped by day, with the number of tweets for
    that day, with date as an index and a new column 'Tweets' corresponding
    to the date and number of tweets.

    """

    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df1 = df.groupby('Date').count()

    return df1
