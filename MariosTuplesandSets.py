#6
#Define a tulpe
coordinates=(123,55)

#Print the values
print("The x-coordinate is ",coordinates[0])
print("The y-coordinate is ",coordinates[1])

---
#7
#Create a set
colors=set(["red","green","blue"])

#Add a color
colors.add("yellow")
colors.add("yellow") #Only adds it once, duplicates are ignored
print(colors)

#Remove a color
colors.discard("green")
light_colors=set(["lightyellow","lightgreen"])

#Combine the sets
colors.union(light_colors)
