# sanitization of csv/txt files

# goals of sanitization
# 1) identify primary key and flag duplicates
# 2) flag nulls
# 3) data type consistency ????
# 4) sanitize special characters such as commas, quotes, etc.
# 5) validate header names against meta data from db ????

# can use either pandas or csv library, pandas gives control over larger
# data sets while csv library gives more precise control and is used for
# smaller data sets


##########################################################################


# Importing Pandas library for large-scale data manipulation
import pandas as pd 

# Setting variable for file path
file = "./monsh2.csv"

# Setting data frame for file to break the CSV down into parsable data
d_frame = pd.read_csv(file)

def primary_key_sanitization(d_frame):
    try:
        col_num = int(input("Enter the column number corresponding to the primary key of your data: "))
        if col_num < 0 or col_num >= len(d_frame.columns):
            raise IndexError('Invalid column number.')
    except IndexError as err:
        print(err)
        return
    
    p_key = d_frame.columns[col_num]
    
    dupli_check = d_frame[d_frame.duplicated(subset=[p_key], keep=False)]
    
    if not dupli_check.empty:
        print(f"\nDuplicates found in the specified column '{p_key}':")
        print(dupli_check)
    else:
        print(f"\nNo duplicates found in specified column.")
    
    return d_frame

def identify_nulls(d_frame):
    null_sum = d_frame.isnull().sum()
    
    print("Null values within each column:")
    print(null_sum)
    
    tuple_nulls = d_frame[d_frame.isnull().any(axis=1)]
    
    if not tuple_nulls.empty:
        print("\nRows containing null values:")
        print(tuple_nulls)
    else: 
        print("\nNo rows containing null values.")
    
    return d_frame

# def special_character_cleanse(d_frame):
    
    
d_frame = primary_key_sanitization(d_frame)
d_frame = identify_nulls(d_frame)  

# print(d_frame.head(10))