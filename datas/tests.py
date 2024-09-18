# from datetime import datetime

# # Define the two dates
# start_date = datetime.strptime("9/17/2024 10:36 PM", "%m/%d/%Y %I:%M %p")
# end_date = datetime.strptime("10/20/2024 11:26 AM", "%m/%d/%Y %I:%M %p")

# # Calculate the difference between the two dates
# time_difference = end_date - start_date

# # Get the total seconds
# total_seconds = int(((time_difference.total_seconds() / 60) / 60) / 24)

# print(f"The total seconds between the two dates is: {total_seconds}")
# Define the end date as the current time (now)
from datetime import datetime

# Define the end date as the current time (now)
end_date = datetime.now()

# Define the start date
l="10:36 PM"
start_date = datetime.strptime(f"2024/9/12 {l}", "%Y/%m/%d %I:%M %p")

# # Calculate the difference between the two dates
# time_difference = end_date - start_date

# # Get the total seconds
# total_seconds = int(((time_difference.total_seconds() / 60) / 60) / 24)

# print(f"The total seconds between the two dates is: {total_seconds}")
# start_date = datetime.strptime(f"{user_last_date} {user_last_time}", "%Y-%m-%d %I:%M %p")
print(start_date)