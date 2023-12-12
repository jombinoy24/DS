import matplotlib.pyplot as plt
print("SJC22MCA2027- Georgekutty Biju\nS3MCA")
days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
drinks_sales = [300, 450, 150, 400, 650]
food_sales = [400, 500, 350, 300, 500]
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))
ax1.plot(days, drinks_sales, linestyle='dotted', color='cyan', marker='H', markersize=8, markerfacecolor='magenta', markeredgecolor='black')
ax1.set_xlabel('Days of week')
ax1.set_ylabel('Sale of Drinks')
ax1.set_title('Sales Data1', loc='right')
ax2.plot(days, food_sales, linestyle='dotted', color='cyan', marker='H', markersize=8, markerfacecolor='magenta', markeredgecolor='black')
ax2.set_xlabel('Days of week')
ax2.set_ylabel('Sale of Food')
ax2.set_title('Sales Data2', loc='right')
ax1.grid(color='blue')
ax2.grid(color='blue')
plt.tight_layout()
plt.show()