import pandas as pd
user_input = input("Enter string values separated by commas (e.g., Aaba,Baca,CABA,bird): ")

data = [item if item.lower() != 'none' else None for item in user_input.split(',')]

s = pd.Series(data)

s_upper = s.str.upper()

s_lower = s.str.lower()

s_length = s.str.len()

print("\nOriginal Series:\n", s)
print("\nUppercase:\n", s_upper)
print("\nLowercase:\n", s_lower)
print("\nLength of strings:\n", s_length)
