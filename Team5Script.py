def dictionary_of_metrics(items):
    """returns a dictionary of the metrics from a list of items """
    dict = {'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'var': round(np.var(items, ddof=1), 2),
            'std': round(np.std(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)}
    return dict


def five_num_summary(items):
    """" returns a five number summary from a list of items"""
    for item in items:
        items = np.quantile(items, [1, .50, 0, .25, .75])
    max = round(items[0], 2)
    median = round(items[1], 2)
    min = round(items[2], 2)
    q1 = round(items[3], 2)
    q3 = round(items[4], 2)
    dictionary = {'max': max, 'median': median, 'min': min, 'q1': q1, 'q3': q3}
    return dictionary


def date_parser(dates):  
    """ This function takes as input a list of these datetime strings,
    each string formatted as 'yyyy-mm-dd hh:mm:ss' 
    and returns only the date in 'yyyy-mm-dd' format.
    Parameters:
    >
    items: (list), list of datetime strings.
    Returns:
    >
    returns a list of strings where each element in the
    returned list contains only the date in the 'yyyy-mm-dd' format.""" 
    date_only =[]  '# An empty date list (to add sublists in it in the for loop)'
    for date in dates:  '# Setting up the condition'
        my_list = date[: len(date) - 9]    
        date_only.append(my_list)  '# Creating a sublist from my_list'
        date_only[:]                     
    '# Return the date only in 'yyyy-mm-dd' format'
    return date_only


def extract_municipality_hashtags(df):
    """returns modified dataframe with a municipality and hashtag column"""
    new_df = pd.DataFrame([])  '#Initialise new DataFrame'
    mun_list = []    '#Create a list to hold all municipality strings'
    final_hash = []    '#Create empty list to hold all the extracted hashtags.'
    flag = 0   '#create a flag variable to track every key in the row'
    for row in df['Tweets']:
        flag = 0
        for key in mun_dict.keys():  '# iterates through keys in mun_dict'
        if key in row:  '# if key is found in the row'
            mun_list.append(mun_dict[key])  '#appends dictionary keys in mun_list'
                flag = 1
            break   '# teminates loop'
        if not flag:
            mun_list.append(np.nan)  '# adds nan to all hashtages that are not found into mun_list'  
    for row in df['Tweets']:
        final_hash.append([string for string in row.lower().split() if string[0][0] == '#'])
    final_hash = [np.nan if x == [] else x for x in final_hash]  '#Extract a list of hashtags from a tweet'

    new_df['Tweets'] = df['Tweets']
    new_df['Date'] = df['Date']
    new_df['municipality'] = mun_list
    new_df['hashtags'] = final_hash

    '#returns the modified dataframe.'
    return new_df

def number_of_tweets_per_day(df):
    """ The Function takes in a pandas dataframe as input.
    It then returns a new dataframe, grouped by day, with the
    number of tweets for that day. """
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df1 = df.groupby('Date').count()
    return df1

    
def word_splitter(df):
    """Splits and lowercases sentences in a dataframe's column
    into a list of seperate words.
    Created lists will be placed in a column named 'Split Tweets' in the
    original dataframe.Also known as tokenization.
    Arguments : Takes in a pandas dataframe as an input
    Returns: returns a modified dataframe"""

    dframe = pd.DataFrame(df, columns=['Tweets', 'Date', 'Split Tweets'])  '#Creates a new Dataframe using the given one'
    dframe['Date'] = dates   '#Creates a column called 'Date' and assign given dates to it'
    dframe['Split Tweets']= dframe['Tweets'].str.lower()   '#Lowercase all strings under 'Split Tweets''
    dframe['Split Tweets']= dframe['Split Tweets'].str.split()  '#Splits every character in strings under 'Split Tweet''
    return dframe 

    
def stop_words_remover(df):
    """function to remove english stop words"""
    new_df = pd.DataFrame([])  '#creates a new dataframe'
    tokenised_list = []  '#tokenised sentence'
    for row in df['Tweets']:
        no_stops = [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
        tokenised_list.append(no_stops)  '#adds words that are not in stop word dictionary into tokenised_list'
    new_df['Tweets'] = df['Tweets']  '#creates copy of tweets column'
    new_df['Date'] = df['Date']  '#creates copy of column Date'
    new_df['Without Stop Words'] = tokenised_list  '# creates column "Without stop words" containing tokenised list'
    return new_df
