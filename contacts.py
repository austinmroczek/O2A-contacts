import argparse
import pandas as pd

# columns to automatically delete from the Outlook export
# 'Notes' column seems to contain errors
DROP_COLUMNS = ["Notes"]

# Outlook -> Apple
MAP_COLUMNS = {
    "Title": "Prefix",
    "E-mail Address": "Email (work)", 
    "E-mail 2 Address": "Email (home)",
    "E-mail 3 Address": "Email (other)",
    "Business Phone": "Phone (work)",
    "Business Phone 2":"Phone (work)",
    "Business Fax": "Phone (work fax)",
    "Mobile Phone": "Phone (mobile)",
    "Primary Phone": "Phone (main)",
    "Other Fax":"Phone (home fax)",
    "IMAddress":"AIM",
    "Web Page":"Home Page",
    "Personal Web Page":"Personal Home Page",
    "Home Postal Code":"Home ZIP",
    "Business Postal Code":"Business ZIP",
    "Assistant's Name":"Related Name (assistant)",
    "Manager's Name":"Related Name (manager)",
    }

parser = argparse.ArgumentParser()
parser.add_argument("contacts_file", help="the path of the CSV file containing contacts")
args = parser.parse_args()

df = pd.read_csv(args.contacts_file, on_bad_lines="error", encoding_errors="strict")

df.rename(columns=MAP_COLUMNS, inplace=True)

# drop columns we don't want
df = df.drop(DROP_COLUMNS, axis=1)

# drop empty rows
df.dropna(axis=0, how="all", inplace=True)

# drop empty columns
df.dropna(axis=1, how="all", inplace=True)

# display column names and number of records in each
df.info()

# save to file
df.to_csv("contacts_new.csv")
