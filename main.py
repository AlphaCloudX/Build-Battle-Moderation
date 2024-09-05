from nbt import nbt
from nbt.chunk import BlockArray
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

nbtfile = nbt.NBTFile("worlds/1.schematic", 'rb')

# X
width = nbtfile['Width'].value

# Y
height = nbtfile['Height'].value

# Z
length = nbtfile['Length'].value

blockData = nbtfile['Blocks']

# Create the world array with the shape (width, length, height)
worldArray = np.zeros((width, length, height), dtype=np.uint8)

# Fill the world array with block data
for x in range(width):
    for y in range(height):
        for z in range(length):
            elementPosition = (y * length + z) * width + x
            worldArray[x, z, y] = blockData[elementPosition]

# Mask the zeros
masked_data = np.ma.masked_where(worldArray == 0, worldArray)

# Create a bigger figure and 3D axis
fig = plt.figure(figsize=(10, 10))  # Adjust the size as needed
ax = fig.add_subplot(111, projection='3d')

# Get the coordinates for the non-zero values
x, y, z = np.nonzero(masked_data)

# Plot the non-zero values
ax.scatter(x, y, z, c=masked_data[x, y, z], cmap='viridis', marker='.', alpha=1)

# Set the viewing angle for a more top-down view
ax.view_init(elev=50, azim=225)  # Adjust elev and azim for your preferred view

ax.set_xlabel('Z', fontsize=20)
ax.set_ylabel('X')
ax.set_zlabel('Y', fontsize=30)

plt.title("Build Battle Map Viewer Side View")

# Show the plot
plt.show()



# Create a bigger figure and 3D axis
fig = plt.figure(figsize=(10, 10))  # Adjust the size as needed
ax = fig.add_subplot(111, projection='3d')

# Get the coordinates for the non-zero values
x, y, z = np.nonzero(masked_data)

# Plot the non-zero values
ax.scatter(x, y, z, c=masked_data[x, y, z], cmap='viridis', marker='.', alpha=1)

# Set the viewing angle for a more top-down view
ax.view_init(elev=90, azim=-90)  # Adjust elev and azim for your preferred view

ax.set_xlabel('Z', fontsize=20)
ax.set_ylabel('X')
ax.set_zlabel('Y', fontsize=30)

plt.title("Build Battle Map Viewer Top Down")

# Show the plot
plt.show()






