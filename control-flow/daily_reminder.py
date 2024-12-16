task = input(" enter your task: ")
priority = input("the task’s priority (high, medium, low): ")
time_bound = input(" time-bound (yes or no): ")


match priority:
    case "high":
      reminder = f"**Urgent!** {task}"
      if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    case "medium":
      reminder = f"**Important:** {task}"
      if time_bound == "yes":
        reminder += " - Please address soon."
    case "low":
      reminder = f"{task}"
      if time_bound == "yes":
        reminder += " - Keep in mind."
    case _:
      reminder = f"**Unknown Priority:** {task}"

print(reminder)