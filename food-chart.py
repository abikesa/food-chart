import matplotlib.pyplot as plt

# Data for the pie chart
labels = [
    "Fruits", "Vegetables", "Nuts", "Cheese & Pâté",
    "Bread", "Salad", "Wine"
]
calories = [80, 35, 45, 110, 80, 120, 125]

# Create pie chart
fig, ax = plt.subplots()
ax.pie(calories, labels=labels, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.title("Estimated Calories per Person")

plt.show()
