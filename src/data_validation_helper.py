import pandas as pd
from pathlib import Path

def import_bball_refrence_player_year_csv(csv_file_name: Path, debug: bool = False) -> pd.DataFrame:
    #validate csv_file_name
    if (csv_file_name == None):
        raise TypeError(f"'csv_file_name' needs to be non empty (!= \"\").")
    if (not isinstance(csv_file_name, Path)):
        raise TypeError(f"type of 'csv_file_name' should be instance of 'pathlib.Path' - was {type(csv_file_name)} instead.")
    
    #read from file
    with open(csv_file_name, 'r') as read_file:
        csv_data = pd.read_csv(csv_file_name)
    
    csv_data.rename(columns={"Unnamed: 5": "Starting"})
    return csv_data

if (__name__ == '__main__'):
    print("This is a helper file")
    pass