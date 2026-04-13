import matplotlib.pyplot as plt

# Sample Data (You can modify or take input)
apps = ["Instagram", "YouTube", "WhatsApp", "Chrome", "Spotify"]
usage_time = [3.5, 2.0, 1.5, 1.0, 2.0] # in hours
opens = [25, 15, 30, 10, 12]
categories = ["Social Media", "Entertainment", "Communication", "Productivity", "Entertainment"]

# Total Screen Time
total_screen_time = sum(usage_time)
avg_usage = total_screen_time / len(apps)

print("--- Smartphone Usage Analysis ---")
print(f"Total Screen Time: {total_screen_time} hrs")
print(f"Average App Usage: {avg_usage:.2f} hrs")

# Most Used App
max_usage = max(usage_time)
most_used_app = apps[usage_time.index(max_usage)]
print(f"Most Used App: {most_used_app}")

# Most Opened App
max_opens = max(opens)
most_opened_app = apps[opens.index(max_opens)]
print(f"Most Frequently Opened App: {most_opened_app}")

# Category Analysis
category_usage = {}
for i in range(len(apps)):
    if categories[i] in category_usage:
        category_usage[categories[i]] += usage_time[i]
    else:
        category_usage[categories[i]] = usage_time[i]

print("\nCategory-wise Usage:")
for cat, time in category_usage.items():
    print(f"{cat}: {time} hrs")

# Visualization

# Bar Chart (App Usage)
plt.figure()
plt.bar(apps, usage_time)
plt.title("App Usage Time (Hours)")
plt.xlabel("Apps")
plt.ylabel("Usage Time (hrs)")
plt.xticks(rotation=30)
plt.show()

# Pie Chart (Category Usage)
plt.figure()
plt.pie(category_usage.values(), labels=category_usage.keys(), autopct='%1.1f%%')
plt.title("Category-wise Usage Distribution")
plt.show()

# Line Graph (App Opens)
plt.figure()
plt.plot(apps, opens, marker='o')
plt.title("App Usage Frequency (Number of Opens)")
plt.xlabel("Apps")
plt.ylabel("Number of Opens")
plt.xticks(rotation=30)
plt.show()