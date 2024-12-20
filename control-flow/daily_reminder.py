Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes/no):  ")
Priority = input("Priority (high/medium/low): ")



match Priority:
    case "high":
      reminder = f"**Urgent!** {Task}"
      if Time_Bound == "yes":
        reminder += " that requires immediate attention today!"
    case "medium":
      reminder = f"**Important:** {Task}"
      if Time_Bound == "yes":
        reminder += " - Please address soon."
    case "low":
      reminder = f"{Task}"
      if Time_Bound == "yes":
        reminder += " - Keep in mind."
    case _:
      reminder = f"**Unknown Priority:** {Task}"

print(f"reminder: {reminder}")