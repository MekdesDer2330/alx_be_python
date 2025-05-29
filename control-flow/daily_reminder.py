
# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = ""

# Process the task based on priority using if-elif-else statements
if priority == "high":
    reminder_message = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder_message = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder_message = f"'{task}' is a low priority task"
else:
    print("Invalid priority level. Please enter high, medium, or low.")
    exit()

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += ". Consider completing it when you have free time."
else:
    print("Invalid response for time-bound question. Please enter yes or no.")
    exit()

# Provide the customized reminder
print(reminder_message)
