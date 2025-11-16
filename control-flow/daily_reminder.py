# Prompt for a single task
task = input("Enter the task: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Process the task based on priority
match priority:
    case "high":
        reminder = f"The task '{task}' is high priority."
    case "medium":
        reminder = f"The task '{task}' is medium priority."
    case "low":
        reminder = f"The task '{task}' is low priority."
    case _:
        reminder = f"The task '{task}' has an unknown priority."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This is a time-bound task that requires immediate attention today!"

# Print the customized reminder
print(reminder)