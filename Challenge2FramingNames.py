def createFrame(names):
  max_length = max(len(item) for item in names)

  names_table = "*" * (max_length + 4) + "\n"
  
  for item in names:
    names_table += f"* {item:<{max_length}} *"

  names_table += "*" * (max_length + 4)
  return names_table