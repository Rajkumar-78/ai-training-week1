import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 135, 180, 210]
expenses = [80, 95, 90, 110, 125]
students = ["A", "B", "C", "D", "E"]
scores = [75, 88, 82, 95, 79]
categories = ["Python", "Git", "SQL", "ML"]
hours = [10, 6, 8, 12]
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(months, sales, marker="o")
axes[0, 0].set_title("Monthly Sales")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")
axes[0, 1].bar(months, expenses)
axes[0, 1].set_title("Monthly Expenses")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Expenses")
axes[1, 0].bar(students, scores)
axes[1, 0].set_title("Student Scores")
axes[1, 0].set_xlabel("Student")
axes[1, 0].set_ylabel("Score")
axes[1, 1].pie(hours, labels=categories, autopct="%1.1f%%")
axes[1, 1].set_title("Study Hours by Topic")
fig.suptitle("AI Training Week 1 - Data Visualization")
plt.tight_layout()
plt.savefig("charts.png", dpi=150, bbox_inches="tight")
plt.show()
