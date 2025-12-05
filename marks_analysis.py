import pandas as pd

# Load CSV data
data = pd.read_csv('students.csv')

# Calculate average marks
data['Average'] = data.mean(axis=1)

# Find top performer
top_student = data.loc[data['Average'].idxmax(), 'Name']

print("Average marks of each student:")
print(data[['Name', 'Average']])
print("\nTop performer:", top_student)
