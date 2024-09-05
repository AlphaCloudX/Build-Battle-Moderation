from nbt import nbt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 30 files and load them all, then isolate each plot, then store them all in a giant array

nbtfile = nbt.NBTFile("worlds/20.schematic", 'rb')

# X, Y, Z dimensions
width = nbtfile['Width'].value
height = nbtfile['Height'].value
length = nbtfile['Length'].value

# Create the world array with the shape (width, length, height)
worldArray = np.array(nbtfile['Blocks']).reshape(height, length, width).transpose(2, 1, 0)

# Mask the zeros
masked_data = np.ma.masked_where(worldArray == 0, worldArray)

print(masked_data.shape)

# Find where the floor begins
layerStart = 0
for i in range(masked_data.shape[-1]):
    if np.unique(masked_data[:, :, i]).tolist()[0] == 159:
        layerStart = i + 1
        break

# For Solo
# 0-4     5-31   32-36
# Border  plot   Border
# Note The Border Between Plots Is 9 Not 10

# For Teams
# 0-5     6-46   47-52
# Border  plot   Border
# Note The Border Between Plots For Teams Is 11 Not 12

if masked_data.shape[0] == 313:
    plotSize = 41
    border = 6
    print("Detected Teams Mode")
else:
    plotSize = 27
    border = 5
    print("Detected Solo Mode")

trimmedWorld = masked_data[border:-border, border:-border, layerStart:]

# Account for the strange border between plots
offset = ((border * 2) - 1)

# Number of blocks (as border) to remove between plots
borderToRemove = (offset * 5)  # Assuming each block has 5 units of border
# 5 Is how many lines between plots there are

# Calculate the number of plots to count after removing borders
plotsToCount = trimmedWorld.shape[0] - borderToRemove

# Calculate the total number of plots assuming a 27x27 grid
totalPlots = plotsToCount // plotSize

# Get the dimensions of the trimmed world
trimmedLength = trimmedWorld.shape[0]
trimmedWidth = trimmedWorld.shape[1]

# Initialize an empty list to store plots
plots = []

# Loop to extract plots from the trimmed world
for i in range(0, totalPlots):  # step by 27 to extract each plot
    for j in range(0, totalPlots):
        # Extracting a 27x27 plot but preventing hitting the 9/11 long borders
        left = (i * plotSize) + (i * offset)
        right = ((i + 1) * plotSize) + (i * offset)

        top = (j * plotSize) + (j * offset)
        bottom = ((j + 1) * plotSize) + (j * offset)

        plot = trimmedWorld[left:right, top:bottom]
        plots.append(plot)

# Print total plots to verify
print(len(plots))

index = 0

# for index in range(36):
print(index)
for index in range(len(plots)):
    # Create a figure and 3D axis
    ax = plt.figure().add_subplot(projection='3d')

    # Create a voxel grid where blocks are present
    ax.voxels(plots[index], facecolors='blue', edgecolor='none')  # Remove edgecolor for faster rendering

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('Y')

    # Set aspect ratio to be equal (optional, depending on your use case)
    ax.set_box_aspect([plots[index].shape[0], plots[index].shape[1], plots[index].shape[2]])

    ax.view_init(elev=30, azim=-65)

    # Show the plot
    plt.show()

# print(masked_data.shape)
# print(masked_data)
#
# fig, ax = plt.subplots()
# im = ax.imshow(masked_data)
# plt.show()


# # Create a figure and 3D axis
# ax = plt.figure().add_subplot(projection='3d')
#
# # Create a voxel grid where blocks are present
# ax.voxels(masked_data, facecolors='blue', edgecolor='none')  # Remove edgecolor for faster rendering
#
# # Set labels
# ax.set_xlabel('X')
# ax.set_ylabel('Z')
# ax.set_zlabel('Y')
#
# # Set aspect ratio to be equal (optional, depending on your use case)
# ax.set_box_aspect([masked_data.shape[0], masked_data.shape[1], masked_data.shape[2]])
#
# # Show the plot
# plt.show()


# # Downsample the array (Optional: Use only if the array is too large)
# downsample_factor = 6
# masked_data = masked_data[::downsample_factor, ::downsample_factor, ::downsample_factor]
#
# # Create a figure and 3D axis
# ax = plt.figure().add_subplot(projection='3d')
#
# # Create a voxel grid where blocks are present
# ax.voxels(masked_data, facecolors='blue', edgecolor='none')  # Remove edgecolor for faster rendering
#
# # Set labels
# ax.set_xlabel('X')
# ax.set_ylabel('Z')
# ax.set_zlabel('Y')
#
# # Set aspect ratio to be equal (optional, depending on your use case)
# ax.set_box_aspect([masked_data.shape[0], masked_data.shape[1], masked_data.shape[2]])
#
# # Show the plot
# plt.show()
