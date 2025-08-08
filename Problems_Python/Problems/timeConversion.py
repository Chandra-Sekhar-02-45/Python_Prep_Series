# Program to convert given time in seconds or minutes to hours

time = input("Enter the time with unit (e.g., 3600S or 120M): ")  # Read input string
seconds = ( time[-1] == "S" )  # Check if the last character is 'S' meaning seconds

time = int(time[:-1])  # Remove the last character (S or M) to get the numeric part

if seconds:
    # Convert seconds to hours
    s_hrs = time / 3600               # 3600 seconds = 1 hour
    s_hrs = round(s_hrs, 2)           # Round to 2 decimal places
    hrs = str(s_hrs) + "H"            # Add 'H' to indicate hours
else:
    # Convert minutes to hours
    min_hrs = time / 60               # 60 minutes = 1 hour
    min_hrs = round(min_hrs, 2)
    hrs = str(min_hrs) + "H"

print("Time in hours:", hrs)          # Print the converted value