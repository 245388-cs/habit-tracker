habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True)
]

for habit, completed in habits:
    if completed:
        print(habit + ": Done")
    else:
        print(habit + ": Not done")


def habit_report(habits):
    completed = sum(1 for habit, status in habits if status)
    total = len(habits)

    return {
        "completed": completed,
        "total": total
    }


print(habit_report(habits))