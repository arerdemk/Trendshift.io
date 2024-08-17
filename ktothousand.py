import pandas as pd

# Load the data
df = pd.read_excel('Excels\\1-3900.xlsx')

# Define the conversion function
def convert_k_to_thousands(value):
    if isinstance(value, str):
        # Replace 'k' with '*1000' and evaluate
        try:
            return eval(value.replace('k', '*1000'))
        except:
            return value  # Return as-is if there's an issue with eval
    else:
        return value  # If not a string, return the value as-is

# Apply the function to the 'Star' column
df['Star'] = df['Star'].apply(convert_k_to_thousands)
df['Fork']=df['Fork'].apply(convert_k_to_thousands)

# Print the updated column
df.to_excel("Merged3900.xlsx",index=0)
