import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button, Slider
from matplotlib import cm
from matplotlib.colors import Normalize

#Load the data from the HDF5 file
# Existing file path
path = 'Build_Battle_Data.h5'

# Data to append
ratings = [(0, 'good'), (1, 'bad'), (2, 'good'), (3, 'good'), (4, 'good'), (5, 'bad'), (6, 'good'), (7, 'good'), (8, 'bad'), (9, 'good'), (10, 'good'), (11, 'good'), (12, 'good'), (13, 'good'), (14, 'bad'), (15, 'good'), (16, 'good'), (17, 'good'), (18, 'good'), (19, 'good'), (20, 'good'), (21, 'bad'), (22, 'good'), (23, 'bad'), (24, 'good'), (25, 'good'), (26, 'good'), (27, 'good'), (28, 'good'), (29, 'good'), (30, 'good'), (31, 'good'), (32, 'good'), (33, 'good'), (34, 'good'), (35, 'good'), (36, 'good'), (37, 'good'), (37, 'bad'), (38, 'good'), (39, 'good'), (40, 'good'), (41, 'good'), (42, 'good'), (43, 'bad'), (44, 'good'), (45, 'bad'), (46, 'good'), (47, 'bad'), (48, 'good'), (49, 'good'), (50, 'good'), (51, 'bad'), (52, 'good'), (53, 'bad'), (54, 'good'), (55, 'good'), (56, 'good'), (57, 'good'), (58, 'good'), (59, 'good'), (60, 'good'), (61, 'good'), (62, 'good'), (63, 'good'), (64, 'good'), (65, 'good'), (66, 'good'), (67, 'good'), (68, 'good'), (69, 'good'), (70, 'good'), (71, 'good'), (72, 'good'), (73, 'good'), (74, 'bad'), (75, 'bad'), (76, 'good'), (77, 'good'), (78, 'good'), (79, 'good'), (80, 'good'), (81, 'good'), (82, 'bad'), (83, 'bad'), (84, 'good'), (85, 'good'), (86, 'good'), (87, 'good'), (88, 'bad'), (89, 'good'), (90, 'good'), (91, 'good'), (92, 'good'), (93, 'good'), (94, 'good'), (95, 'good'), (96, 'good'), (97, 'good'), (98, 'good'), (99, 'good'), (100, 'bad'), (101, 'good'), (102, 'good'), (103, 'bad'), (104, 'bad'), (105, 'bad'), (106, 'bad'), (107, 'good'), (108, 'bad'), (109, 'good'), (110, 'good'), (111, 'good'), (112, 'bad'), (113, 'good'), (114, 'good'), (115, 'good'), (116, 'good'), (117, 'bad'), (118, 'good'), (119, 'good'), (120, 'bad'), (121, 'good'), (122, 'good'), (123, 'bad'), (124, 'good'), (125, 'good'), (126, 'good'), (127, 'good'), (128, 'good'), (129, 'good'), (130, 'good'), (131, 'good'), (132, 'good'), (133, 'good'), (134, 'good'), (135, 'bad'), (136, 'good'), (137, 'bad'), (138, 'good'), (139, 'good'), (140, 'good'), (141, 'good'), (142, 'good'), (143, 'good'), (144, 'good'), (145, 'good'), (146, 'good'), (147, 'good'), (148, 'good'), (149, 'good'), (150, 'good'), (151, 'good'), (152, 'good'), (153, 'good'), (154, 'good'), (155, 'good'), (156, 'good'), (157, 'bad'), (158, 'good'), (159, 'good'), (160, 'good'), (161, 'bad'), (162, 'good'), (163, 'bad'), (164, 'good'), (165, 'good'), (166, 'good'), (167, 'good'), (168, 'bad'), (169, 'good'), (170, 'good'), (171, 'good'), (172, 'good'), (173, 'good'), (174, 'good'), (175, 'bad'), (176, 'good'), (177, 'good'), (178, 'good'), (179, 'good'), (180, 'good'), (181, 'good'), (182, 'good'), (183, 'good'), (184, 'bad'), (185, 'good'), (186, 'good'), (187, 'good'), (188, 'good'), (189, 'bad'), (190, 'good'), (191, 'bad'), (192, 'good'), (193, 'bad'), (194, 'good'), (195, 'bad'), (196, 'good'), (197, 'good'), (198, 'bad'), (199, 'good'), (200, 'good'), (201, 'good'), (202, 'good'), (203, 'good'), (204, 'good'), (205, 'good'), (206, 'good'), (207, 'good'), (208, 'good'), (209, 'good'), (210, 'good'), (211, 'good'), (212, 'good'), (213, 'bad'), (214, 'good'), (215, 'good'), (216, 'good'), (217, 'good'), (218, 'good'), (219, 'good'), (220, 'good'), (221, 'good'), (222, 'good'), (223, 'good'), (224, 'bad'), (225, 'good'), (226, 'good'), (227, 'good'), (228, 'bad'), (229, 'good'), (230, 'good'), (231, 'good'), (232, 'good'), (233, 'bad'), (234, 'good'), (235, 'good'), (236, 'good'), (237, 'bad'), (238, 'bad'), (239, 'bad'), (240, 'bad'), (241, 'good'), (242, 'good'), (243, 'bad'), (244, 'good'), (245, 'bad'), (246, 'good'), (247, 'good'), (248, 'good'), (249, 'good'), (250, 'good'), (251, 'bad'), (252, 'good'), (253, 'good'), (254, 'good'), (255, 'good'), (256, 'good'), (257, 'good'), (258, 'bad'), (259, 'good'), (260, 'good'), (261, 'good'), (262, 'good'), (263, 'good'), (264, 'bad'), (265, 'good'), (266, 'bad'), (267, 'good'), (268, 'good'), (269, 'good'), (270, 'bad'), (271, 'bad'), (272, 'bad'), (273, 'bad'), (274, 'bad'), (275, 'bad'), (276, 'good'), (277, 'good'), (278, 'good'), (279, 'good'), (280, 'good'), (281, 'good'), (282, 'good'), (283, 'good'), (284, 'bad'), (285, 'good'), (286, 'good'), (287, 'good'), (288, 'good'), (289, 'good'), (290, 'bad'), (291, 'good'), (292, 'good'), (293, 'good'), (294, 'good'), (295, 'good'), (296, 'good'), (297, 'good'), (298, 'good'), (299, 'good'), (300, 'good'), (301, 'good'), (302, 'good'), (303, 'good'), (304, 'bad'), (305, 'good'), (306, 'good'), (307, 'good'), (308, 'good'), (309, 'good'), (310, 'good'), (311, 'bad'), (312, 'good'), (313, 'good'), (314, 'good'), (315, 'good'), (316, 'good'), (317, 'good'), (318, 'good'), (319, 'good'), (320, 'good'), (321, 'good'), (322, 'bad'), (323, 'good'), (324, 'good'), (325, 'good'), (326, 'good'), (327, 'good'), (328, 'good'), (329, 'good'), (330, 'good'), (331, 'good'), (332, 'good'), (333, 'good'), (334, 'good'), (335, 'good'), (336, 'bad'), (337, 'good'), (338, 'good'), (339, 'bad'), (340, 'good'), (341, 'good'), (342, 'good'), (343, 'bad'), (344, 'good'), (345, 'good'), (346, 'good'), (347, 'good'), (348, 'good'), (349, 'bad'), (350, 'good'), (351, 'good'), (352, 'bad'), (353, 'good'), (354, 'good'), (355, 'good'), (356, 'good'), (357, 'bad'), (358, 'good'), (359, 'good'), (360, 'good'), (361, 'good'), (362, 'good'), (363, 'bad'), (364, 'good'), (365, 'good'), (366, 'good'), (367, 'good'), (368, 'good'), (369, 'good'), (370, 'good'), (371, 'good'), (372, 'bad'), (373, 'good'), (374, 'bad'), (375, 'good'), (376, 'good'), (377, 'good'), (378, 'good'), (379, 'good'), (380, 'good')]
ratingWords = [word for _, word in ratings]

classification = [(0, 'appropriate'), (1, 'appropriate'), (2, 'appropriate'), (3, 'appropriate'), (4, 'appropriate'), (5, 'appropriate'), (6, 'appropriate'), (7, 'appropriate'), (8, 'appropriate'), (9, 'appropriate'), (10, 'appropriate'), (11, 'appropriate'), (12, 'appropriate'), (13, 'appropriate'), (14, 'appropriate'), (15, 'appropriate'), (16, 'appropriate'), (17, 'appropriate'), (18, 'appropriate'), (19, 'appropriate'), (20, 'appropriate'), (21, 'appropriate'), (22, 'appropriate'), (23, 'appropriate'), (24, 'appropriate'), (25, 'appropriate'), (26, 'appropriate'), (27, 'appropriate'), (28, 'appropriate'), (29, 'appropriate'), (30, 'appropriate'), (31, 'appropriate'), (32, 'appropriate'), (33, 'appropriate'), (34, 'appropriate'), (35, 'appropriate'), (36, 'appropriate'), (37, 'appropriate'), (37, 'appropriate'), (38, 'appropriate'), (39, 'appropriate'), (40, 'appropriate'), (41, 'appropriate'), (42, 'appropriate'), (43, 'inappropriate'), (44, 'appropriate'), (45, 'appropriate'), (46, 'appropriate'), (47, 'inappropriate'), (48, 'appropriate'), (49, 'appropriate'), (50, 'appropriate'), (51, 'appropriate'), (52, 'appropriate'), (53, 'appropriate'), (54, 'appropriate'), (55, 'appropriate'), (56, 'appropriate'), (57, 'appropriate'), (58, 'appropriate'), (59, 'appropriate'), (60, 'appropriate'), (61, 'appropriate'), (62, 'appropriate'), (63, 'appropriate'), (64, 'appropriate'), (65, 'appropriate'), (66, 'appropriate'), (67, 'appropriate'), (68, 'appropriate'), (69, 'appropriate'), (70, 'appropriate'), (71, 'appropriate'), (72, 'appropriate'), (73, 'appropriate'), (74, 'appropriate'), (75, 'appropriate'), (76, 'appropriate'), (77, 'appropriate'), (78, 'appropriate'), (79, 'appropriate'), (80, 'appropriate'), (81, 'appropriate'), (82, 'inappropriate'), (83, 'appropriate'), (84, 'appropriate'), (85, 'appropriate'), (86, 'appropriate'), (87, 'appropriate'), (88, 'appropriate'), (89, 'appropriate'), (90, 'appropriate'), (91, 'appropriate'), (92, 'appropriate'), (93, 'appropriate'), (94, 'appropriate'), (95, 'appropriate'), (96, 'appropriate'), (97, 'appropriate'), (98, 'appropriate'), (99, 'appropriate'), (100, 'inappropriate'), (101, 'appropriate'), (102, 'appropriate'), (103, 'inappropriate'), (104, 'appropriate'), (105, 'appropriate'), (106, 'appropriate'), (107, 'appropriate'), (108, 'appropriate'), (109, 'appropriate'), (110, 'appropriate'), (111, 'appropriate'), (112, 'appropriate'), (113, 'appropriate'), (114, 'appropriate'), (115, 'appropriate'), (116, 'appropriate'), (117, 'appropriate'), (118, 'appropriate'), (119, 'appropriate'), (120, 'appropriate'), (121, 'appropriate'), (122, 'appropriate'), (123, 'appropriate'), (124, 'appropriate'), (125, 'appropriate'), (126, 'appropriate'), (127, 'appropriate'), (128, 'appropriate'), (129, 'appropriate'), (130, 'appropriate'), (131, 'appropriate'), (132, 'appropriate'), (133, 'appropriate'), (134, 'appropriate'), (135, 'appropriate'), (136, 'appropriate'), (137, 'appropriate'), (138, 'appropriate'), (139, 'appropriate'), (140, 'appropriate'), (141, 'appropriate'), (142, 'appropriate'), (143, 'appropriate'), (144, 'appropriate'), (145, 'appropriate'), (146, 'appropriate'), (147, 'appropriate'), (148, 'appropriate'), (149, 'appropriate'), (150, 'appropriate'), (151, 'appropriate'), (152, 'appropriate'), (153, 'appropriate'), (154, 'appropriate'), (155, 'appropriate'), (156, 'appropriate'), (157, 'appropriate'), (158, 'appropriate'), (159, 'appropriate'), (160, 'appropriate'), (161, 'appropriate'), (162, 'appropriate'), (163, 'appropriate'), (164, 'appropriate'), (165, 'appropriate'), (166, 'appropriate'), (167, 'appropriate'), (168, 'appropriate'), (169, 'appropriate'), (170, 'appropriate'), (171, 'appropriate'), (172, 'appropriate'), (173, 'appropriate'), (174, 'appropriate'), (175, 'appropriate'), (176, 'appropriate'), (177, 'appropriate'), (178, 'appropriate'), (179, 'appropriate'), (180, 'appropriate'), (181, 'appropriate'), (182, 'appropriate'), (183, 'appropriate'), (184, 'inappropriate'), (185, 'appropriate'), (186, 'appropriate'), (187, 'appropriate'), (188, 'appropriate'), (189, 'inappropriate'), (190, 'appropriate'), (191, 'inappropriate'), (192, 'appropriate'), (193, 'inappropriate'), (194, 'appropriate'), (195, 'inappropriate'), (195, 'appropriate'), (196, 'appropriate'), (197, 'appropriate'), (198, 'appropriate'), (199, 'appropriate'), (200, 'appropriate'), (201, 'appropriate'), (202, 'appropriate'), (203, 'appropriate'), (204, 'appropriate'), (205, 'appropriate'), (206, 'appropriate'), (207, 'appropriate'), (208, 'appropriate'), (209, 'appropriate'), (210, 'appropriate'), (211, 'appropriate'), (212, 'appropriate'), (213, 'appropriate'), (214, 'appropriate'), (215, 'appropriate'), (216, 'appropriate'), (217, 'appropriate'), (218, 'appropriate'), (219, 'appropriate'), (220, 'appropriate'), (221, 'appropriate'), (222, 'appropriate'), (223, 'appropriate'), (224, 'appropriate'), (225, 'appropriate'), (226, 'appropriate'), (227, 'appropriate'), (228, 'appropriate'), (229, 'appropriate'), (230, 'appropriate'), (231, 'appropriate'), (232, 'appropriate'), (233, 'inappropriate'), (234, 'appropriate'), (235, 'appropriate'), (236, 'appropriate'), (237, 'inappropriate'), (238, 'inappropriate'), (239, 'appropriate'), (240, 'appropriate'), (241, 'appropriate'), (242, 'appropriate'), (243, 'appropriate'), (244, 'appropriate'), (245, 'inappropriate'), (246, 'appropriate'), (247, 'appropriate'), (248, 'appropriate'), (249, 'appropriate'), (250, 'appropriate'), (251, 'appropriate'), (252, 'appropriate'), (253, 'appropriate'), (254, 'appropriate'), (255, 'appropriate'), (256, 'appropriate'), (257, 'appropriate'), (258, 'appropriate'), (259, 'appropriate'), (260, 'appropriate'), (261, 'appropriate'), (262, 'appropriate'), (263, 'appropriate'), (264, 'appropriate'), (265, 'appropriate'), (266, 'appropriate'), (267, 'appropriate'), (268, 'appropriate'), (269, 'appropriate'), (270, 'appropriate'), (271, 'appropriate'), (272, 'appropriate'), (273, 'appropriate'), (274, 'inappropriate'), (275, 'appropriate'), (276, 'appropriate'), (277, 'appropriate'), (278, 'appropriate'), (279, 'appropriate'), (280, 'appropriate'), (281, 'appropriate'), (282, 'appropriate'), (283, 'appropriate'), (284, 'appropriate'), (285, 'appropriate'), (286, 'appropriate'), (287, 'appropriate'), (288, 'appropriate'), (289, 'appropriate'), (290, 'inappropriate'), (291, 'appropriate'), (292, 'appropriate'), (293, 'appropriate'), (294, 'appropriate'), (295, 'appropriate'), (296, 'appropriate'), (297, 'appropriate'), (298, 'appropriate'), (299, 'appropriate'), (300, 'appropriate'), (301, 'appropriate'), (302, 'appropriate'), (303, 'appropriate'), (304, 'appropriate'), (305, 'appropriate'), (306, 'appropriate'), (307, 'appropriate'), (308, 'appropriate'), (309, 'appropriate'), (310, 'appropriate'), (311, 'appropriate'), (312, 'appropriate'), (313, 'appropriate'), (314, 'appropriate'), (315, 'appropriate'), (316, 'appropriate'), (317, 'appropriate'), (318, 'appropriate'), (319, 'appropriate'), (320, 'appropriate'), (321, 'appropriate'), (322, 'appropriate'), (323, 'appropriate'), (324, 'appropriate'), (325, 'appropriate'), (326, 'appropriate'), (327, 'appropriate'), (328, 'appropriate'), (329, 'appropriate'), (330, 'appropriate'), (331, 'appropriate'), (332, 'appropriate'), (333, 'appropriate'), (334, 'appropriate'), (335, 'appropriate'), (336, 'appropriate'), (337, 'appropriate'), (338, 'appropriate'), (339, 'inappropriate'), (340, 'appropriate'), (341, 'appropriate'), (342, 'appropriate'), (343, 'appropriate'), (344, 'appropriate'), (345, 'appropriate'), (346, 'appropriate'), (347, 'appropriate'), (348, 'appropriate'), (349, 'appropriate'), (350, 'appropriate'), (351, 'appropriate'), (352, 'appropriate'), (353, 'appropriate'), (354, 'appropriate'), (355, 'appropriate'), (356, 'appropriate'), (357, 'inappropriate'), (358, 'appropriate'), (359, 'appropriate'), (360, 'appropriate'), (361, 'appropriate'), (362, 'appropriate'), (363, 'inappropriate'), (364, 'appropriate'), (365, 'appropriate'), (366, 'appropriate'), (367, 'appropriate'), (368, 'appropriate'), (369, 'appropriate'), (370, 'appropriate'), (371, 'appropriate'), (372, 'appropriate'), (373, 'appropriate'), (374, 'appropriate'), (375, 'appropriate'), (376, 'appropriate'), (377, 'appropriate'), (378, 'appropriate'), (379, 'appropriate'), (380, 'appropriate')]
classWords = [word for _, word in classification]

with h5py.File(path, 'a') as f:
    f.create_dataset('rating', data=ratingWords)
    f.create_dataset('classification', data=classWords)

f.close()

# Something is broken where it may not properly save, need to fix this later or just create a proper ui
# Hopefully this isnt needed as future data may contain labels
# # Store classifications here (theme, rating, classification)
# ratings = []
# classifications = []
#
# # Initialize index for images
# index = 0
# total_images = len(finalPlots)
#
# # Function to plot 3D build with custom colors
# def plot_voxel(index, azim_angle):
#     ax.cla()
#
#     # Get the voxel data for the current index
#     voxels = finalPlots[index]
#
#     # Create a colormap and normalize the voxel values
#     norm = Normalize(vmin=np.min(voxels), vmax=np.max(voxels))
#     cmap = cm.get_cmap('rainbow')  # You can use any colormap you like
#
#     # Map the voxel values to colors using the colormap, set alpha to 0 for zeros
#     colors = cmap(norm(voxels))
#     colors[voxels == 0] = [0, 0, 0, 0]  # Set color to transparent for 0 values
#
#     # Plot the voxels
#     ax.voxels(voxels, facecolors=colors, edgecolor='none')
#     ax.set_xlabel('X')
#     ax.set_ylabel('Z')
#     ax.set_zlabel('Y')
#     ax.set_box_aspect([voxels.shape[0], voxels.shape[1], voxels.shape[2]])
#     ax.view_init(elev=30, azim=azim_angle)
#
#     # Update the title to display the image number
#     plt.title(f"Image {index + 1}/{total_images}")
#     plt.draw()
#
# # Function to display current ratings and classifications
# def display_selections():
#     print(f"Ratings so far: {ratings}")
#     print(f"Classifications so far: {classifications}")
#
# # Function to save the rating
# def save_rating(rating_value, index):
#     ratings.append((index, rating_value))
#     display_selections()
#
# # Function to save the classification
# def save_classification(classification_value, index):
#     classifications.append((index, classification_value))
#     display_selections()
#
# # Button callback functions
# def good_callback(event):
#     save_rating('good', index)
#
# def bad_callback(event):
#     save_rating('bad', index)
#
# def appropriate_callback(event):
#     save_classification('appropriate', index)
#
# def inappropriate_callback(event):
#     save_classification('inappropriate', index)
#
# # Slider update function
# def update_slider(val):
#     azim_angle = slider.val
#     plot_voxel(index, azim_angle)
#
# # Function to go to the next image
# def next_image(event):
#     global index
#     index += 1
#     if index >= total_images:
#         index = 0  # Wrap around to the first image
#     plot_voxel(index, slider.val)
#
# # Function to save ratings and classifications to HDF5 file
# def save_to_hdf5():
#     with h5py.File(path, 'a') as f:  # Open the file in append mode
#         # Check if 'ratings' and 'classifications' datasets exist, create if not
#         if 'ratings' not in f:
#             f.create_dataset('ratings', data=np.array(ratings, dtype='S'))
#         else:
#             # Append new data to 'ratings'
#             f['ratings'].resize((f['ratings'].shape[0] + len(ratings)), axis=0)
#             f['ratings'][-len(ratings):] = np.array(ratings, dtype='S')
#
#         if 'classifications' not in f:
#             f.create_dataset('classifications', data=np.array(classifications, dtype='S'))
#         else:
#             # Append new data to 'classifications'
#             f['classifications'].resize((f['classifications'].shape[0] + len(classifications)), axis=0)
#             f['classifications'][-len(classifications):] = np.array(classifications, dtype='S')
#
#     print("Ratings and classifications saved to HDF5 file.")
#
# # Set up the figure and axis
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot initial voxel (index 0)
# plot_voxel(index, azim_angle=30)
#
# # Create sliders and buttons
# ax_slider = plt.axes([0.25, 0.02, 0.65, 0.03])
# slider = Slider(ax_slider, 'Rotation', -180, 180, valinit=30)
# slider.on_changed(update_slider)
#
# # Create button positions
# ax_good = plt.axes([0.1, 0.85, 0.1, 0.075])
# ax_bad = plt.axes([0.2, 0.85, 0.1, 0.075])
# ax_appropriate = plt.axes([0.4, 0.85, 0.1, 0.075])
# ax_inappropriate = plt.axes([0.5, 0.85, 0.1, 0.075])
# ax_next = plt.axes([0.7, 0.85, 0.1, 0.075])  # Button for next image
# ax_save = plt.axes([0.85, 0.85, 0.1, 0.075])  # Button for saving to HDF5
#
# # Create buttons
# button_good = Button(ax_good, 'Good')
# button_good.on_clicked(good_callback)
#
# button_bad = Button(ax_bad, 'Bad')
# button_bad.on_clicked(bad_callback)
#
# button_appropriate = Button(ax_appropriate, 'Appropriate')
# button_appropriate.on_clicked(appropriate_callback)
#
# button_inappropriate = Button(ax_inappropriate, 'Inappropriate')
# button_inappropriate.on_clicked(inappropriate_callback)
#
# button_next = Button(ax_next, 'Next')
# button_next.on_clicked(next_image)
#
# button_save = Button(ax_save, 'Save')
# button_save.on_clicked(lambda event: save_to_hdf5())
#
# plt.show()
