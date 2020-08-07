def five_num_summary (items):
    for item in items:
        items = np.quantile(items,[1, .50, 0, .25, .75])
        
"""" returns a five number summary from a list of items"""
        max = round(items[0],2) # all numerical values should be rounded to two decimal places
        median = round(items[1],2)
        min = round(items[2],2)
        q1 = round(items[3],2)
        q3 = round(items[4],2)
        
        dictionary = {'max':max, 'median':median, 'min':min, 'q1':q1, 'q3':q3}

    return dictionary
