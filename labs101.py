import matplotlib.pyplot as plt
#x-coordinate of left sides of bar
left = [1,2,3,4,5]
#height of the bars
height = [10,24,36,40,5]
#label for bars
tick_label = ['one','two','three','four','five']
#plotting a bar chart
plt.bar(left,height,tick_label = tick_label,width = 0.5,color = ['red','green'])
#naming the x-axis
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')
#plot title
plt.title("My bar chart!")
#function to show the plot
plt.show()
