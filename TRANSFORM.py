from EXTRACT import *
import pandas as pd
from openpyxl import load_workbook

class Transform():
    def __init__(self,starter,finisher):
        self.starter=starter
        self.finisher=finisher


    def determine(self,filename):
  
        # Define the columns in the order you want
        Columns_s = ['Trendshift_id', 'Rep Name', 'GitHub Website', 'Website', 'Description', 'Language Name', 'Star', 'Fork','Createdate']

        # Initialize a list to hold DataFrames
        dataframes = []

        # List of method names and corresponding column names
        methods_and_columns = [
            ('gettrendshiftid', 'Trendshift_id'),
            ('getrepname', 'Rep Name'),
            ('getgiturl', 'GitHub Website'),
            ('getweburl', 'Website'),
            ('getdescription', 'Description'),
            ('getlangname', 'Language Name'),
            ('getstars', 'Star'),
            ('getforks', 'Fork'),
            ('getcreatdate','Createdate')
        ]

        # Create DataFrames using a for loop
        for method, column_name in methods_and_columns:
            # Call the method and create a DataFrame
            data = getattr(TrendShift(self.starter, self.finisher), method)()  # Call the method dynamically
            df = pd.DataFrame(data, columns=[column_name])
            dataframes.append(df)  # Add the DataFrame to the list

        # Concatenate all DataFrames along the columns axis
        df_combined = pd.concat(dataframes, axis=1,ignore_index=True)

        # Reorder columns
        df_combined.columns=Columns_s

        # Display the combined DataFrame
        df_combined.to_excel(f'{filename}.xlsx',index=0)



            




