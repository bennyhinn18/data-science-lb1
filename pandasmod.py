import pandas as pd

def create_sample_dataframe():
    data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
            'Age': [25, 30, 35, 40],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

    df = pd.DataFrame(data)
    return df

def print_dataframe_info(df):
    print(df.info())

def filter_dataframe_by_age(df, age):
    filtered_df = df[df['Age'] > age]
    return filtered_df
