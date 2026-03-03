# Dataset from Activity 1
steps = {
    "Jili": [2200, 5900, 5800],
    "Krissy": [3500, 6740, 4000],
    "Lien": [4000, 6000, 5700]
}

# Print each row and calculate total and average
for person, daily_steps in steps.items():
    print(person, "steps:", daily_steps)
    
    total_steps = sum(daily_steps)
    avg_steps = total_steps / len(daily_steps)
    
    print("Total steps:", total_steps)
    print("Average steps:", avg_steps)
    print()

# Optional: Find the maximum and minimum step count in the entire dataset
all_steps = []
for daily_steps in steps.values():
    all_steps.extend(daily_steps)

print("Maximum steps in the dataset:", max(all_steps))
print("Minimum steps in the dataset:", min(all_steps))
