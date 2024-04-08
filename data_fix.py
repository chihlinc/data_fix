import pandas as pd


def get_out_of_date_entries(df_full: pd.DataFrame, df_latest: pd.DataFrame) -> pd.DataFrame:
    # Identify the entries in df_latest that aren't the latest in df_full
    # Return a dataframe of the links that are out of date
    
    latest_issue_per_group = df_full.groupby(['signal_key_id', 'geo_key_id', 'time_type', 'time_value'])['issue'].max().reset_index()
    latest_issue_per_group.rename(columns={'issue': 'latest_issue'}, inplace=True)

    # Left join df_latest with the aggregated DataFrame
    merged_df = df_latest.merge(latest_issue_per_group, on=['signal_key_id', 'geo_key_id', 'time_type', 'time_value'], how='left')

    # Filter the rows based on the conditions
    df_ood = merged_df[(merged_df['latest_issue'].isnull()) | (merged_df['issue'] != merged_df['latest_issue'])]


    # drop the issue(from datafull)
    df_ood = df_ood.drop(columns=['issue'])
 
    # keep the latest_issue and rename it
    df_ood = df_ood.rename(columns={"latest_issue": "issue"})
    
    return df_ood
    
    # ps. might want to think about how you could use this at the end of the program for testing

def get_latest_entries(df_full: pd.DataFrame, df_ood: pd.DataFrame) -> pd.DataFrame:
    # Identify the latest entries in df_full for the entries that are in df_ood (df out of date)
    # Return a dataframe of the updates entries for df_ood
    
    df_full_latest = df_full[df_full['issue'] == df_full.groupby(['signal_key_id', 'geo_key_id', 'time_type', 'time_value'])['issue'].transform('max')]
    # Merge df_ood with df_full_latest based on the match columns
    df_updates = df_ood.merge(df_full_latest, on=['signal_key_id', 'geo_key_id', 'time_type', 'time_value'], suffixes=('_ood', '_full_latest'), how='inner')

    df_updates = df_updates.drop(columns=['value_ood', 
                                      'lag_ood', 
                                      'stderr_ood', 
                                      'sample_size_ood', 
                                      'value_updated_timestamp_ood',
                                      'missing_value_ood',
                                      'missing_stderr_ood',
                                      'missing_sample_size_ood',
                                     'computation_as_of_dt_ood', 
                                     'issue_ood'])

    df_updates = df_updates.rename(columns={"issue_full_latest": "issue",
                                       "value_full_latest":"value",
                                       "stderr_full_latest":"stderr",
                                       "sample_size_full_latest":"sample_size",
                                       "lag_full_latest":"lag",
                                       "value_updated_timestamp_full_latest":"value_updated_timestamp",
                                       "computation_as_of_dt_full_latest":"computation_as_of_dt",
                                       "missing_value_full_latest":"missing_value",
                                       "missing_stderr_full_latest":"missing_stderr",
                                       "missing_sample_size_full_latest":"missing_sample_size"})




    return df_updates


    

def update_epimetric_latest(df_latest: pd.DataFrame, df_updates: pd.DataFrame) -> pd.DataFrame:
    # Update the entries in df_latest with the values in df_updates where the keys match
    # Return a dataframe of all entries of df_latest including the updates
    df_latest_updates = df_updates.merge(df_latest, on=['signal_key_id', 'geo_key_id', 'time_type', 'time_value'], suffixes=('_updates', '_latest'), how='right')

    # Use issue_updates' value to replace issue_latest's value where issue_updates is not NaN
    df_latest_updates['issue_latest'] = df_latest_updates['issue_updates'].fillna(df_latest_updates['issue_latest'])
    df_latest_updates['value_latest'] = df_latest_updates['value_updates'].fillna(df_latest_updates['value_latest'])
    df_latest_updates['stderr_latest'] = df_latest_updates['stderr_updates'].fillna(df_latest_updates['stderr_latest'])
    df_latest_updates['sample_size_latest'] = df_latest_updates['sample_size_updates'].fillna(df_latest_updates['sample_size_latest'])
    df_latest_updates['lag_latest'] = df_latest_updates['lag_updates'].fillna(df_latest_updates['lag_latest'])
    df_latest_updates['value_updated_timestamp_latest'] = df_latest_updates['value_updated_timestamp_updates'].fillna(df_latest_updates['value_updated_timestamp_latest'])
    df_latest_updates['computation_as_of_dt_latest'] = df_latest_updates['computation_as_of_dt_updates'].fillna(df_latest_updates['computation_as_of_dt_latest'])
    df_latest_updates['missing_value_latest'] = df_latest_updates['missing_value_updates'].fillna(df_latest_updates['missing_value_latest'])
    df_latest_updates['missing_stderr_latest'] = df_latest_updates['missing_stderr_updates'].fillna(df_latest_updates['missing_stderr_latest'])
    df_latest_updates['missing_sample_size_latest'] = df_latest_updates['missing_sample_size_updates'].fillna(df_latest_updates['missing_sample_size_latest'])

    # Drop the redundant columns
    df_latest_updates.drop(columns=['issue_updates', 'value_updates', 'stderr_updates', 'sample_size_updates', 'lag_updates', 'value_updated_timestamp_updates', 'computation_as_of_dt_updates', 'missing_value_updates', 'missing_stderr_updates', 'missing_sample_size_updates'], inplace=True)

    # Rename issue_latest column to issue and other updated columns
    df_latest_updates.rename(columns={'issue_latest': 'issue',
                                  'value_latest': 'value',
                                  'stderr_latest':'stderr',
                                  'sample_size_latest':'sample_size',
                                  'lag_latest':'lag',
                                  'value_updated_timestamp_latest':'value_updated_timestamp',
                                  'computation_as_of_dt_latest':'computation_as_of_dt',
                                  'missing_value_latest':'missing_value',
                                  'missing_stderr_latest':'missing_stderr',
                                  'missing_sample_size_latest':'missing_sample_size'
                                 }, inplace=True)

    # Show the updated DataFrame
    return df_latest_updates
   
    # ps. Assure that the size of the dataframe did not change

if __name__ == '__main__':
    df_latest = pd.read_csv('data/epimetric_latest.csv')
    df_full = pd.read_csv('data/epimetric_full.csv')
    
    
    #get_out_of_date_entries(df_full, df_latest)
    #print(get_out_of_date_entries(df_full, df_latest))
    epimetric_latest_fixed = update_epimetric_latest(df_latest, update_epimetric_latest(df_latest, get_out_of_date_entries(df_full, df_latest)))
    

    ##output your resulting dataframe to a CSV
    epimetric_latest_fixed.to_csv('./data/epimetric_latest_fixed.csv', index=False)