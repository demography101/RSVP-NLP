import pandas as pd
import numpy as np
import random

rand_num = 100

RSVP_status = ['Attending', 'Not Going', 'Maybe', 'N/A']
RSVP = random.choices(RSVP_status, k=rand_num) # random generation, with replacement
RSVP_df = pd.DataFrame(RSVP) # Convert into dataframe
RSVP_df.columns = ['RSVP'] # Rename column


# Manual word Search
# Copy + paste each word
# ['Attending', 'Not Going', 'Available', 'N/A']
word = 'Attending'
all_text = ' '.join(RSVP_df.astype(str).values.flatten())
count = RSVP_df.apply(lambda row: row.astype(str).str.contains(word, case=False).sum(), axis=1).sum()
print(f"{count} guests RVSP'd '{word}'.")



# Automate
# Count occurrences for each phrase
for phrase in RSVP_status:
    RSVP_df[phrase] =  RSVP_df['RSVP'].str.count(phrase)

# save last few columns
RSVP_total = RSVP_df.iloc[:, -4:]
RSVP_total =  RSVP_df.sum()


# Convert Series to DataFrame with index as a column
df = RSVP_total.reset_index()
df.columns = ['rsvp', 'total'] # Rename columns 
df = df[df['rsvp'] != 'RSVP'] # Remove extra column
df['total'] = df['total'].astype(int) # convert column into interger value
df['perct'] = round(df['total']/sum(df['total'])*100,0)


print(f"I had" , rand_num, "people RSVP.")
for index, row in df.iterrows():
    print(f"I had {row['total']} ({row['perct']}%) people RSVP as '{row['rsvp']}'.")


    
    
    
    
