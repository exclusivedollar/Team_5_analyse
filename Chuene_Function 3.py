### START FUNCTION
""" This function takes as input a list of these datetime strings, each string formatted as 'yyyy-mm-dd hh:mm:ss' 
and returns only the date in 'yyyy-mm-dd' format.

    Parameters:
   >
    items: (list), list of datetime strings.

    Returns:
  >
returns a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format."""

def date_parser(dates):                       # The function date_parser takes in a datetime string input formatted as 'yyyy-mm-dd hh:mm:ss'
    date_only =[]                             # An empty date list (to add sublists in it in the for loop)
    for date in dates:                        # Setting up the condition
        my_list = date[: len(date) - 9]       
        date_only.append(my_list)             # Creating a sublist from my_list
        date_only[:]                          
    return date_only                          # Return the date only in 'yyyy-mm-dd' format
### END FUNCTION
  
