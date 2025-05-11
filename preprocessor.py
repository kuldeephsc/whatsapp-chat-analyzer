import re
import pandas as pd
from datetime import datetime
def preprocess(data):
    #pattern to extract date and messages ? show optional \s =space \s? optional space

    pattern: str = r'\[?\d{1,2}\/\d{1,2}\/\d{2,4}\,\s\d{1,2}\:\d{1,2}\:?\d{1,2}?\s?[a|A|p|P]?[m|M]?\]?\s?\-?\s'

    #spliting the file based on pattern and put in to the massage [1:to remove starting null charecter ]
    messages = re.split(pattern, data)[1:]

    #processing to extract date and time of differnt format
    dates = [date.replace('[', '').replace(']', ' -') for date in re.findall(pattern, data)]#'[' convrted to null and ']' to '-'

    df = pd.DataFrame({'user-message': messages, 'message-date': dates})
    #error='coerce' if error  return NAT(not a time) combine_first() combined previous result with current result
    df['message-date'] = pd.to_datetime(df['message-date'], format='%d/%m/%Y, %H:%M - ', errors='coerce') \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%y, %H:%M - ', errors='coerce')) \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%Y, %H:%M:%S %p - ', errors='coerce')) \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%y, %H:%M:%S %p - ', errors='coerce')) \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%Y, %H:%M %p - ', errors='coerce')) \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%y, %H:%M %p - ', errors='coerce')) \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%Y, %H:%M:%S - ', errors='coerce')) \
        .combine_first(pd.to_datetime(df['message-date'], format='%d/%m/%y, %H:%M:%S - ', errors='coerce'))
    
    #change the column name
    df.rename(columns={'message-date': 'date'}, inplace=True)

    # seperate user and message
    users = []
    messages = []

    for message in df['user-message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:#appending user name and messages
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:#if not user name append as group notification
            users.append('group-notification')
            messages.append(entry[0])
    
    #creating new column in df
    df['user'] = users
    df['message'] = messages

    #deleting previous column
    df.drop(columns=['user-message'], inplace=True)

    #putting year month date in new column
    df['year']=df['date'].dt.year
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute

    return df
            


