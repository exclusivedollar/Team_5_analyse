def dictionary_of_metrics(items):
    # your code here
    """returns a dictionary of the metrics from a list of items """
    dict = {'mean': round(np.mean(items), 2),
            'median': round(np.median(items), 2),
            'var': round(np.var(items, ddof=1), 2),
            'std': round(np.std(items, ddof=1), 2),
            'min': round(np.min(items), 2),
            'max': round(np.max(items), 2)}
    return dict


def five_num_summary(items):
    for item in items:
        items = np.quantile(items, [1, .50, 0, .25, .75])
    """" returns a five number summary from a list of items"""
    max = round(items[0], 2)
    median = round(items[1], 2)
    min = round(items[2], 2)
    q1 = round(items[3], 2)
    q3 = round(items[4], 2)
    dictionary = {'max': max, 'median': median, 'min': min, 'q1': q1, 'q3': q3}
    return dictionary


def date_parser(dates):
    # Creating a new date list.
    date_only = []
    for date in dates:
        my_list = date[:len(date)-9]
# Append values from my list to date_only list.
        date_only.append(my_list)
        date_only[:]
# returned list contains only the date in the 'yyyy-mm-dd' format.
    return date_only


def extract_municipality_hashtags(df):
        """returns modified dataframe with a municipality and hashtag column"""
    # dictionary mapping official municipality twitter handles
    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'}
    
    new_df = pd.DataFrame([])  #Initialise new DataFrame
    mun_list = []    #Create a list to hold all municipality strings
    final_hash = []    #Create empty list to hold all the extracted hashtags.
    flag = 0   #create a flag variable to track every key in the row
    
    for row in df['Tweets']:
        flag = 0
        for key in mun_dict.keys(): # iterates through keys in mun_dict
            if key in row: # if key is found in the row 
                mun_list.append(mun_dict[key]) #appends dictionary keys in mun_list 
                flag = 1
            break # teminates loop
        if not flag:
            mun_list.append(np.nan) # adds nan to all hashtages that are not found into mun_list
            
            
    for row in df['Tweets']:
        final_hash.append([string for string in row.lower().split() if string[0][0] =='#'])
    final_hash = [np.nan if x ==[] else x for x in final_hash] #Extract a list of hashtags from a tweet 
    
    
    new_df['Tweets'] = df['Tweets'] 
    new_df['Date'] = df['Date']
    new_df['municipality'] = mun_list
    new_df['hashtags'] = final_hash
    
    #returns the modified dataframe.
    return new_df 
    
def word_splitter(df):    
    dframe = pd.DataFrame(df,columns =['Tweets','Date','Split Tweets'])
    dframe['Date'] = dates
    dframe['Split Tweets']= dframe['Tweets'].str.lower()
    dframe['Split Tweets']= dframe['Split Tweets'].str.split()  
    return dframe
    
def stop_words_remover(df): #takes in a pandas dataframe as input
    # your code here
    """function to remove english stop words"""

    new_df = pd.DataFrame([]) #creat new dataframe
    tokenised_list = [] # tokenised sentence
    stop_words_dict = {'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]}
    
    for row in df['Tweets']:
        no_stops = [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
        tokenised_list.append(no_stops) # adds words that are not in stop word dictionary into tokenised_list
    
    new_df['Tweets'] = df['Tweets'] #creats copy of tweets column
    new_df['Date'] = df['Date']# creates copy of column Date
    
    new_df['without stop words'] = tokenised_list # creates column "Without stop words" containing tokenised list
    
    return new_df
### END FUNCTION
    