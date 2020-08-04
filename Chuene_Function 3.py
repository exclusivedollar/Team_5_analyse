### START FUNCTION
def date_parser(dates):
    date_only =[]
    for date in dates:
        my_list = date[: len(date) - 9]
        date_only.append(my_list)
        date_only[:]
    return date_only
### END FUNCTION
  