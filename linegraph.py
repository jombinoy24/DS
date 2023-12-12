import matplotlib.pyplot as plt
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]
plt.figure(figsize=(10, 6))
plt.plot(years, car_values, linestyle='-.', color='red', label='Car Value', marker='*', markersize=20, markerfacecolor='green', markeredgecolor='green')
plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title('Value Depreciation', loc='left')
plt.legend()
plt.grid(True)
plt.show()