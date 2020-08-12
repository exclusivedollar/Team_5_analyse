def extract_municipality_hashtags(df):#takes pandas dataframe as input
    # your code here
    
    """returns modified dataframe with a municipality and hashtag column"""
    
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
