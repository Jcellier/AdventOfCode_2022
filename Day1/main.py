# Open the file for reading
with open("input.txt", "r") as file:
  # Read lines of input and calculate the total Calories carried by the top three Elves
  elf_calories = []  # list to store total Calories for each Elf
  current_elf = 0  # index of the current Elf in the list
  for line in file:
    if line.strip() == "":  # check for blank line
      current_elf += 1  # move to the next Elf
    else:
      calories = int(line)  # convert the line to an integer
      if current_elf == len(elf_calories):
        elf_calories.append(calories)
      else:
        elf_calories[current_elf] = elf_calories[current_elf] + calories  # add the Calories to the current Elf's total

  # sort the elf_calories list in descending order
  elf_calories = sorted(elf_calories, reverse=True)

  # take the top three values from the sorted list
  top_three_calories = elf_calories[:3]

  # calculate the total Calories carried by the top three Elves
  total_calories = sum(top_three_calories)

  print(f"The top three Elves are carrying a total of {total_calories} Calories.")