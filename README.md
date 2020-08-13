# **CREATING METRICS FROM COMPANY DATA**

## **TABLE OF CONTENTS**

- [General Information](#General-information)
- [Problem Statement](#problem-statement)
- [Technologies, Platforms and Knowledge Areas](#Technologies-Platforms-and-Knowledge-areas)
- [Setup](#setup)
- [Detailed Metric Functions](#detailed-metric-functions)
- [Features](#features)
- [Project Status](#project-status)
- [Contribution](#contribution)
- [Questions](#questions)
- [License](#license)


## **General Information**

A python function is a set of statements that take specified inputs and produce an output after performing computational requirements. The function is a convenient way to avoid repeatedly performing the same task all over again for different inputs. Apart from functions that comes along with the python package, there are python built-in function such as return, print(), list() ,etc, and other function that can be created as users which are called user-defined function. These functions are really not different from the built in functions for the reason that they make our work in terms of coding easier, readable and of course save time. Functions could be used in combination with each other on projects of different requiorements from a computational and approach point of view.

The goal for this [project](https://github.com/exclusivedollar/Team_5_analyse) was to create a set of functions that describe useful metrics in Eskom 
data. The project is scenario based, we placed the project on the context that we are Data Scietist working for Eskom and that the company requires certain metrics to be calculated for their analytics team. Our main project focus was to create 7 functions, that will be able to to process both numerical and text data using python to output metrics for the analytical team to use. The 7 functions were as follows:

- Function 1 : Metric Dictionary
- Function 2 : 5 Number Summary
- Function 3 : Date Parser
- Function 4 : Hashtags & Municipality Extractor
- Function 5 : Number of Tweets per day 
- Function 6 : Word Splitter
- Function 7 : Stop Word Remover
---

 ## **Problem Statement**

 Company data can be used to derive insight from defined metrics to better understand customer behaviour trends.

--- 

## **Technologies, Platforms and Knowledge Areas**

The project is created and executed using;

_Knowledge:_

- List manipulation
- Dictionaries
- Basic Statistics and Aggregations
- Function definitions
- PEP8 coding style
- Numpy
- Pandas

_Technolgies & Platforms_

- Anaconda
- Jupyter
- Visual Studio Code
- Github and Github Desktop

---


## **Setup**

- Installing package

You can install the package onto any computer (with internet access).

Issue the command below to install your package from GitHub.
(make sure to replace your-name and your-repo with the appropriate text)

https://github.com/exclusivedollar/Team_5_analyse.git

If you need to install a later version of your package, then use:

pip install --upgrade https://github.com/exclusivedollar/Team_5_analyse.git


- Running the package

---

## **Detailed Metric Functions**

  This section highlights the important elements necessary to understand each function from utilization perspective. It will touch on what each function does, the input, the parameters involved and the output of each.

### **Function 1 :  Metric Dictionary**

 This function creates a Metric Dictionary,
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
    

### **Function 2 : 5 Number Summary**

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



### **Function 3 : Date Parser**



This function takes as input a list of these datetime strings,
    each string formatted as 'yyyy-mm-dd hh:mm:ss'
    and returns only the date in 'yyyy-mm-dd' format.

    Parameters:
    items -  list of datetime strings.
    Returns:
    list - A list of strings where each element in the returned list
    contains only the date in the 'yyyy-mm-dd' format.

    Example:

    >>>date_parser(dates[-3:]) = 
    ['2019-11-20', '2019-11-20', '2019-11-20']




### **Function 4 : Hashtags & Municipality Extractor**


 This function takes in a pandas dataframe
    and returns a modified dataframe
    that includes two new columns that contain information
    about the municipality and hashtag of the tweet.
    It will extract the municipality from a tweet using the given
    mun_dict dictonary, and insert the result into a new column named
    'municipality' in the same dataframe.
    It will extract a list of hashtags from a tweet into a new column named
    'hashtags' in the same dataframe


    Parameter:
    df - A pandas dataframe.
    Returns:
    new_df - A modified daraframe that has two new columns
                'municipality' and 'hashtags'

    Example:
    >>>extract_municipality_hashtags(twitter_df.copy()).loc[4, 'hashtags']
    ['#eskomfreestate', '#mediastatement']

### **Function 5 : Number of Tweets per day**

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


### **Function 6 : Word Splitter**

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




### **Function 7 : Stop Word Remover**


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
---





## **Project Status**

There are no further developments and plans for this [project](https://github.com/exclusivedollar/Team_5_analyse) at this point.

---

## **Contribution**

The following contributors were equally involved in creating and executing this project:

- Sammy Maakwana https://github.com/exclusivedollar
- Kundani Netshiongolwe https://github.com/K-Netshiongolwe
- Palesa Hlungwani https://github.com/PTStace
- Lesedi Madumo https://github.com/Lesedi-Coder
- Chuene Mokgokong https://github.com/Grewies

---

## **Questions**

If you have any question, you can contact us individually:

Github profile : [Palesa Hlungwani](https://github.com/PTStace) ; [Lesedi Madumo](https://github.com/Lesedi-Coder) ; [Chuene Mokgokong](https://github.com/Grewies) ; [Kundani Netshiongolwe](https://github.com/K-Netshiongolwe) ; [Sammy Maakwana](https://github.com/exclusivedollar)


email: [Palesa Hlungwani](ptshlungwani@gmail.com) ; [Lesedi Madumo](lesedi10madumo@gmail.com) ; [Chuene Mokgokong](mokgokonggrewies01@gmail.com) ; [Kundani Netshiongolwe](netshiongolwekundani@gmail.com) ; [Sammy Maakwana](maakwana@gmail.com) .


## **License**

The package is Open Source, it's open to all for usage.

## **Acknowledgement**

We would like to express our deepest gratitute to the Explore Data Science Academy (EDSA) for this lifetime opportunity and the knowledge they have shared with us.

Thank you!
