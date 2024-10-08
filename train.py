import h5py
import numpy as np

path = 'Build_Battle_Data.h5'
with h5py.File(path, 'r') as f:
    finalPlots = f['image'][:]
    themes = f['theme'][:]
    rating = f['rating'][:]
    classification = f['classification'][:]

appropriateDataPlot = []
appropriateDataTheme = []

inappropriateDataPlot = []
inappropriateDataTheme = []

# filter to only use good appropriate or bad inappropriate
for i in range(len(finalPlots)):

    if rating[i] == b"good" and classification[i] == b"appropriate":
        appropriateDataPlot.append(finalPlots[i])
        appropriateDataTheme.append(themes[i])

    elif rating[i] == b"bad" and classification[i] == b"inappropriate":
        inappropriateDataPlot.append(finalPlots[i])
        inappropriateDataTheme.append(themes[i])

appropriateDataLabels = np.ones(len(appropriateDataPlot))
inappropriateDataLabels = np.zeros(len(inappropriateDataPlot))

print(appropriateDataPlot)
print(appropriateDataLabels)
#
# print(inappropriateDataPlot)
# print(inappropriateDataLabels)