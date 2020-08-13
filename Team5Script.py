def dictionary_of_metrics(items):

    """ This function creates a Metric Dictionary,
        it calculates the mean, median, variance, standard deviation, minimum
        and maximum of a list of items.
        It assumes the given list contains only numerical entries,
        and we will use numpy functions to do this.

        Parameter:

        items - list as an input

        Returns:

        dict - A dict with keys 'mean', 'median', 'std', 'var', 'min', and
        'max', corresponding to the mean, median, standard deviation, variance,
        minimum and maximum of the input list, respectively.

        Example:

        >>> dictionary_of_metrics(gauteng)
        {'mean': 26244.42,
         'median': 24403.5,
         'var': 108160153.17,
         'std': 10400.01,
         'min': 8842.0,
         'max': 39660.0}
    """

    #    All values in the returned dict will be rounded to 2 decimal places,
    #    With the use the round function in the corresponding numpy functions!
    #    The standard deviation and variance values will be unbiased,
    #    With the use the ddof parameter in the corresponding numpy functions!
    dict = {
            'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'var': round(np.var(items, ddof=1), 2),
            'std': round(np.std(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)
            }

    return dict



def five_num_summary(items):
    """
    This Function creates a Five Number Summary,
    which takes in a list of integers and returns a dictionary of the
    five number summary.

    Parameter:
    items - list as an input
    Returns:
    dict - A dict with keys 'max', 'median', 'min', 'q1', and 'q3'
    corresponding to the maximum, median, minimum, first quartile and
    third quartile, respectively.

    Example:
    >>>five_num_summary(gauteng)
    {'max': 39660.0,
     'median': 24403.5,
     'min': 8842.0,
     'q1': 18653.0,
     'q3': 36372.0}

    """

    for item in items:
        items = np.quantile(items, [1, .50, 0, .25, .75])
        # all numerical values should be rounded to two decimal places
        max = round(items[0], 2)
        median = round(items[1], 2)
        min = round(items[2], 2)
        q1 = round(items[3], 2)
        q3 = round(items[4], 2)

        dict = {'max': max, 'median': median, 'min': min, 'q1': q1, 'q3': q3}

    return dict


def date_parser(dates):
    """
    This function takes as input a list of these datetime strings,
    each string formatted as 'yyyy-mm-dd hh:mm:ss'
    and returns only the date in 'yyyy-mm-dd' format.

    Parameters:
    items -  list of datetime strings.
    Returns:
    list - A list of strings where each element in the returned list
    contains only the date in the 'yyyy-mm-dd' format.

    Example:

    >>>date_parser(dates[-3:])
    ['2019-11-20', '2019-11-20', '2019-11-20']

    """

    # An empty date list (to add sublists in it in the for loop)
    date_only = []

    # Setting up the condition
    for date in dates:
        my_list = date[: len(date) - 9]
        # Creating a sublist from my_list
        date_only.append(my_list)
        date_only[:]

    # Return the date only in 'yyyy-mm-dd' format
    return date_only


def extract_municipality_hashtags(df):
    """
    This function takes in a pandas dataframe
    and returns a modified dataframe
    that includes two new columns that contain information
    about the municipality and hashtag of the tweet.
    It will extract the municipality from a tweet using the given
    mun_dict dictonary, and insert the result into a new column named
    'municipality' in the same dataframe.
    It will extract a list of hashtags from a tweet into a new column named
    'hashtags' in the same dataframe.

    Parameter:
    df - A pandas dataframe.
    Returns:
    new_df - A modified daraframe that has two new columns
                'municipality' and 'hashtags'

    Example:
    >>>extract_municipality_hashtags(twitter_df.copy()).loc[4, 'hashtags']
    ['#eskomfreestate', '#mediastatement']

    """
    # Initialise new DataFrame
    new_df = pd.DataFrame([])
    # Create a list to hold all municipality strings
    mun_list = []
    # Create empty list to hold all the extracted hashtags.
    final_hash = []
    # create a flag variable to track every key in the row
    flag = 0

    for row in df['Tweets']:
        flag = 0
        # iterates through keys in mun_dict
        for key in mun_dict.keys():
            # if key is found in the row
            if key in row:
                # appends dictionary keys in mun_list
                mun_list.append(mun_dict[key])
                flag = 1
            break  # teminates loop
        if not flag:
            # adds nan to all hashtages that are not found into mun_list
            mun_list.append(np.nan)

    for row in df['Tweets']:
        a = [string for string in row.lower().split() if string[0][0] == '#']
        final_hash.append(a)
        # Extract a list of hashtags from a tweet
    final_hash = [np.nan if x == [] else x for x in final_hash]

    new_df['Tweets'] = df['Tweets']
    new_df['Date'] = df['Date']
    new_df['municipality'] = mun_list
    new_df['hashtags'] = final_hash

    # returns the modified dataframe.
    return new_df


def number_of_tweets_per_day(df):
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

    
def word_splitter(df):
    """
    This function splits the sentences in a dataframe's column
    into a list of the separate words.
    The created lists will be placed in a column named
    'Split Tweets' in the original dataframe.
    The resulting words will all be lowercase.

    Parameter:
    df - A pandas dataframe.
    Returns:
    df - A dataframe with a new column 'Split Tweets',
         that has a list of seperate words from sentences in
         'Tweets'.

    Exameple:
    >>>word_splitter(twitter_df.copy()).loc[0, 'Split Tweets']
    ['@bongadlulane',
     'please',
     'send',
     'an',
     'email',
     'to',
     'mediadesk@eskom.co.za']

    """

    df = pd.DataFrame(df, columns=['Tweets', 'Date', 'Split Tweets'])
    df['Date'] = dates
    df['Split Tweets'] = df['Tweets'].str.lower()
    df['Split Tweets'] = df['Split Tweets'].str.split()

    return df
 

    
def stop_words_remover(df):
    """
    This function removes english stop words from a tweet.
    It tokenises the sentences and
    removes all stop words in the tokenised list.
    The resulting tokenised list is placed
    in a column named "Without Stop Words".

    Parameter:
    df - A pandas dataframe
    Returns:
    new_df - A modified dataframe with a new column
             "Without Stop Words" that has all stop
             words removed.

    Example:
    >>>stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"]
    ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']

    """

    new_df = pd.DataFrame([])  # create new dataframe
    tokenised_list = []  # tokenised sentence

    for row in df['Tweets']:
        no_stops = [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
        # adds words that are not in stop word dictionary into tokenised_list
        tokenised_list.append(no_stops)

    # creates copy of tweets column
    new_df['Tweets'] = df['Tweets']
    # creates copy of column Date
    new_df['Date'] = df['Date']
    # creates column "Without stop words" containing tokenised list
    new_df['Without Stop Words'] = tokenised_list

    return new_df
