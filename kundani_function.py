def dictionary_of_metrics(items):

    dict ={'mean':round(np.mean(items),2),
         'median':round(np.median(items),2),
         'var':round(np.var(items,ddof=1),2),
         'std':round(np.mean(items,ddof=1),2),
         'max':round(np.max(items),2)}



     return dict
gauteng = ebp_df['Gauteng']
