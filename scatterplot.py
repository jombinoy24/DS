import matplotlib.pyplot as plt
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
product=['Jan','Feb','Mar','Apr','May','Jun','jul','Aug','Sep','Oct','Nov','Dec']
affordable_segment=[173,153,195,147,120,144,148,109,174,130,172,131]
luxuary_segment=[189,189,105,112,173,109,151,197,174,145,177,161]
super_luxuary=[185,185,126,134,196,153,112,133,200,145,167,110]
plt.scatter(product,affordable_segment,c='pink',s=100,label='Affordable Segment')
plt.scatter(product,luxuary_segment,c='yellow',s=100,label='Luxuary Segmnet')
plt.scatter(product,super_luxuary,c='blue',s=100,label='Super Luxuary Segment')
plt.xlabel('Days of week',fontsize=18)
plt.ylabel('Scale of segments',fontsize=18)
plt.title('Sales Data',fontsize=18)
plt.legend()
plt.show()