Task = input(" Enter your task: ")
Priority = input(" Priority (high/medium/low): ")
Time_Bound = input(" Is it time-bound? (yes/no):  ")


match Priority:
    case "high":
      reminder = f"**Urgent!** {task}"
      if Time_Bound == "yes":
        reminder += " that requires immediate attention today!"
    case "medium":
      reminder = f"**Important:** {task}"
      if Time_Bound == "yes":
        reminder += " - Please address soon."
    case "low":
      reminder = f"{task}"
      if Time_Bound == "yes":
        reminder += " - Keep in mind."
    case _:
      reminder = f"**Unknown Priority:** {task}"

print(reminder)