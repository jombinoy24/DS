import matplotlib.pyplot as plt
print("SJC22MCA-2027-Georgekutty Biju\nS3MCA")
transport_modes = ['Walking', 'cycling', 'car', 'Bus', 'train']
frequencies = [29, 15, 35, 18, 3]
plt.bar(transport_modes, frequencies, width=0.1, color='green')
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')
plt.show()