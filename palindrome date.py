#Gabriela Fuller
#“I have not given or received any unauthorized assistance on this assignment.”
#https://youtu.be/s7xXF_Zfixc

def is_palindrome(date_str):
  # Checks if a given date string is a palindrome
  day, month, year = map(int, date_str.split("/"))
  return str(year) == str(year)[::-1] and str(month) == str(month)[::-1] and str(day) == str(day)[::-1]

def generate_dates(start_year, end_year):
  # Generates all valid dates in the specified year range in DD/MM/YYYY format
  for year in range(start_year, end_year + 1):
    for month in range(1, 13):
      if month in (4, 6, 9, 11) or year % 4 == 0 and month == 2:
        days_in_month = 31
      elif month == 2:
        days_in_month = 28
      else:
        days_in_month = 30
      for day in range(1, days_in_month + 1):
        date_str = f"{day:02d}/{month:02d}/{year:04d}"
        yield date_str

def save_palindromes(filename, start_year, end_year):
  # Saves palindrome dates to a file
  with open(filename, "w") as file:
    for date_str in generate_dates(start_year, end_year):
      if is_palindrome(date_str):
        file.write(f"{date_str}\n")

# Set the filename and year range
filename = "palindrome_dates.txt"
start_year = 2001
end_year = 2100

# Save the palindrome dates to the file
save_palindromes(filename, start_year, end_year)

print(f"Palindrome dates saved to '{filename}'.")