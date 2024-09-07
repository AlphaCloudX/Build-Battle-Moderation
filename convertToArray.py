import csv
import h5py
from nbt import nbt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 30 files and load them all, then isolate each plot, then store them all in a giant array
totalFiles = 30

"""need to create buttons to annotate builds
good, bad, unfinished
theme
appropriate or inappropriate



create a slider to rotate the plot around


store in an array, then find adjust all plots so they're the same size


save into h5 file

array, classification, theme, extra comments"""


def readFile(number):
    out = []

    with open(str(number), 'r', encoding="utf8") as f:
        file = csv.reader(f, delimiter=',')

        for row in file:
            out.append(row)

    return out


csvFiles = readFile(f"worlds/replays.csv")

# Initialize an empty list to store plots
plots = []
themes = []

for k in range(1, totalFiles + 1):
    print(f"Reading {k}")
    nbtfile = nbt.NBTFile(f"worlds/{k}.schematic", 'rb')

    theme = csvFiles[k - 1][1]

    # X, Y, Z dimensions
    width = nbtfile['Width'].value
    height = nbtfile['Height'].value
    length = nbtfile['Length'].value

    # Create the world array with the shape (width, length, height)
    worldArray = np.array(nbtfile['Blocks']).reshape(height, length, width).transpose(2, 1, 0)

    # Mask the zeros
    masked_data = np.ma.masked_where(worldArray == 0, worldArray)

    print(masked_data.shape)
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

    trimmedWorld = masked_data[border:-border, border:-border, :]

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

    # Loop to extract plots from the trimmed world
    for i in range(0, totalPlots):  # step by 27 to extract each plot
        for j in range(0, totalPlots):
            # Extracting a plot but preventing hitting the odd sized borders
            left = (i * plotSize) + (i * offset)
            right = ((i + 1) * plotSize) + (i * offset)

            top = (j * plotSize) + (j * offset)
            bottom = ((j + 1) * plotSize) + (j * offset)

            plot = trimmedWorld[left:right, top:bottom]

            # Find where the floor begins
            floorStart = 0
            for l in range(masked_data.shape[-1]):
                if np.unique(plot[:, :, l]).tolist()[0] == 159:
                    floorStart = l + 1
                    break

            # Check to see if the plot is empty
            if np.unique(plot[:, :, floorStart + 1:])[0].data != 0:

                # Remove Extra Height now that the plot is valid
                heightStart = 0
                for l in range(masked_data.shape[-1] - 1, floorStart, -1):
                    if np.unique(plot[:, :, l]).tolist()[0] is not None:
                        heightStart = l + 1
                        break

                print(f"{floorStart} -> {heightStart}")

                # Save the theme and plot
                plots.append(plot[:, :, floorStart + 1:heightStart])
                themes.append(theme)

# Step 1: Find the maximum dimensions
maxL = 0
maxW = 0
maxH = 0

for i in plots:
    if i.shape[0] > maxL:
        maxL = i.shape[0]
    if i.shape[1] > maxW:
        maxW = i.shape[1]
    if i.shape[2] > maxH:
        maxH = i.shape[2]

print("Max dims:")
print(maxL, maxW, maxH)

# Pad The Np Array with 0's so they're all the same size
finalPlots = []

# Pad with 0's
for i in range(len(plots)):
    padL = (0, maxL - plots[i].shape[0])
    padW = (0, maxW - plots[i].shape[1])
    padH = (0, maxH - plots[i].shape[2])

    padShape = [padL, padW, padH]

    paddedPlot = np.pad(plots[i], padShape, mode='constant', constant_values=0)
    finalPlots.append(paddedPlot)

# Path to save the HDF5 file
path = 'Build_Battle_Data.h5'

# Save the data
with h5py.File(path, 'w') as f:
    f.create_dataset('image', data=finalPlots)
    f.create_dataset('label', data=themes)

f.close()

#
# index = 0
#
# # for index in range(36):
# print(index)
# for index in range(len(finalPlots)):
#     print(np.unique(finalPlots[index]))
#
#     # Create a figure and 3D axis
#     ax = plt.figure().add_subplot(projection='3d')
#
#     # Create a voxel grid where blocks are present
#     ax.voxels(finalPlots[index], facecolors='blue', edgecolor='none')  # Remove edgecolor for faster rendering
#
#     # Set labels
#     ax.set_xlabel('X')
#     ax.set_ylabel('Z')
#     ax.set_zlabel('Y')
#
#     # Set aspect ratio to be equal (optional, depending on your use case)
#     ax.set_box_aspect([finalPlots[index].shape[0], finalPlots[index].shape[1], finalPlots[index].shape[2]])
#
#     ax.view_init(elev=30, azim=-65)
#
#     # Show the plot
#     plt.show()
