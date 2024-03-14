import os
from pathlib import Path #for Unix / Windows compatibility

import pandas as pd
from data_validation_helper import *

def main() -> None:
    #change working directory to project root to make it easier to work with sibling folders

    DATAPATH = Path(r"data")
    read_file = DATAPATH / "csv" / "Luka_Doncic" / "2022-2023.csv"
    
    data = import_bball_refrence_player_year_csv(read_file)

    print(data.head())

if __name__ == '__main__':
    main()