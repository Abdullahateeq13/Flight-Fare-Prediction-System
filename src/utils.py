import os 
import sys
import pandas as pd



def remove_null_values(df):
    """
    Remove null values from a DataFrame if any are found, otherwise return the original DataFrame.
    
    Args:
    df (pandas.DataFrame): The DataFrame to check for null values.
    
    Returns:
    pandas.DataFrame: The DataFrame with null values removed if any were found, otherwise the original DataFrame.
    """
    if df.isnull().sum().sum() > 0:
        df.dropna(inplace=True)
        print("Null values removed from DataFrame.")
    else:
        print("No null values found in DataFrame.")
    
    return df


def extract_date_time_info(df, date_col, dep_time_col, arrival_time_col, duration_col):
    """
    Extracts date and time information from the specified columns of the given DataFrame.
    
    Args:
    - df (pandas.DataFrame): The DataFrame containing the columns to extract information from.
    - date_col (str): The name of the column containing the date information in "DD/MM/YYYY" format.
    - dep_time_col (str): The name of the column containing the departure time information in "HH:MM" format.
    - arrival_time_col (str): The name of the column containing the arrival time information in "HH:MM" format.
    - duration_col (str): The name of the column containing the duration information in "Xh Ym" or "Xh" or "Ym" format.
    
    Returns:
    - pandas.DataFrame: The DataFrame with extracted date and time information, and dropped columns.
    """
    # Extract journey day and month from date column
    df["Journey_day"] = pd.to_datetime(df[date_col], format="%d/%m/%Y").dt.day
    df["Journey_month"] = pd.to_datetime(df[date_col], format="%d/%m/%Y").dt.month
    df.drop([date_col], axis=1, inplace=True)

    # Extract departure hour and minute from departure time column
    df["Dep_hour"] = pd.to_datetime(df[dep_time_col]).dt.hour
    df["Dep_min"] = pd.to_datetime(df[dep_time_col]).dt.minute
    df.drop([dep_time_col], axis=1, inplace=True)

    # Extract arrival hour and minute from arrival time column
    df["Arr_hour"] = pd.to_datetime(df[arrival_time_col]).dt.hour
    df["Arr_min"] = pd.to_datetime(df[arrival_time_col]).dt.minute
    df.drop([arrival_time_col], axis=1, inplace=True)

    # Extract duration hours and minutes from duration column
    duration_hours = []
    duration_mins = []
    for duration in df[duration_col]:
        hours = 0
        mins = 0
        duration_parts = duration.split()
        if len(duration_parts) == 2:
            hours = int(duration_parts[0][:-1])
            mins = int(duration_parts[1][:-1])
        elif "h" in duration_parts[0]:
            hours = int(duration_parts[0][:-1])
        else:
            mins = int(duration_parts[0][:-1])
        duration_hours.append(hours)
        duration_mins.append(mins)
    df["Duration_hours"] = duration_hours
    df["Duration_mins"] = duration_mins
    df.drop([duration_col], axis=1, inplace=True)

    return df


def one_hot_encoding_data(train_data):
    """
    One-hot encode categorical columns in train_data and replace stop information with integer values.

    Args:
    train_data (pd.DataFrame): input dataframe with categorical columns to be one-hot encoded and stop information to be replaced with integer values.

    Returns:
    pd.DataFrame: one-hot encoded dataframe with replaced stop information and original categorical columns dropped.
    """

    # One-hot encode Airline
    Airline = pd.get_dummies(train_data[["Airline"]], drop_first=True)
    
    # One-hot encode Source
    Source = pd.get_dummies(train_data[["Source"]], drop_first=True)
    
    # One-hot encode Destination
    Destination = pd.get_dummies(train_data[["Destination"]], drop_first=True)
    
    # Replace "non-stop", "1 stop", etc. with 0, 1, etc.
    train_data.replace({"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}, inplace=True)
    
    # Drop original categorical columns
    train_data.drop(["Airline", "Source", "Destination", "Additional_Info","Route"], axis=1, inplace=True)
    
    # Concatenate one-hot encoded columns and drop original categorical columns
    data_train = pd.concat([train_data, Airline, Source, Destination], axis=1)
    
    # Return the one-hot encoded dataframe with replaced stop information and original categorical columns dropped
    return data_train