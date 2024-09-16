task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case 'high':
        ans = f"\'{task}\' is a {priority} priority task that requires immediate attention today!"
    case 'medium':
        ans = f"\'{task}\' is a {priority} priority task. Finish it ASAP!"
    case 'low':
        ans= f"\'{task}\' is a {priority} priority task. Consider completing it when you have free time."
if time_bound=='yes':
    print(f"Reminder: {ans}")
else:
    print(f"Note: {ans}")

