import re
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td

def to_date(date_str: str):
    """A function to convert date description to a datetime object.

    Args:
        date_str (str): date description 

    Raises:
        NotImplementedError: Only date description with a mention of `jour`are supported

    Returns:
        datetime: datetime corresponding to the description
    """     
    digits_str = re.search( r'(\d+)\W(\w*)', date_str)# digits_str.group(0) should return smth like 10 jours
    if digits_str:
        ref = digits_str.group(2)
        if re.match('jour', ref):
            days = int(digits_str.group(1))
            return (dt.today() - td(days = days)).date()
        else :#TODO
            raise NotImplementedError
    elif re.search( r'(?!\d+\W)(\w*)', date_str).group(0):
        return dt.today().date()

def process_offers(df,pattern):
    """A function to process a dataframe of job offers.

    Args:
        df (Dataframe): job offers dataframe
        pattern (rString): a pattern to be matched by the job description. Could be a key word. 

    Returns:
        DataFrame: A dataframe of job offers sorted by date with an additionnal column to show the offers that match the pattern.
    """    

    df['datetime'] = df['date'].apply(to_date)
    df = df.sort_values('datetime',ascending=False )
    df['filter'] = df['description'].apply(lambda x : len(re.findall(pattern, x, re.IGNORECASE))>0)
    return df