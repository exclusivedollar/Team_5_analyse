### START FUNCTION
"""This function takes as input a list of these datetime strings,
each string formatted as 'yyyy-mm-dd hh:mm:ss'
and returns only the date in 'yyyy-mm-dd' format.
    input:
    list of datetime strings as 'yyyy-mm-dd hh:mm:ss'
    Returns:
returns a list of strings where each element in
the returned list contains only the date in the 'yyyy-mm-dd' format."""

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
### END FUNCTION
