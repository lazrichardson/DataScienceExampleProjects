from matplotlib import pyplot as plt
import algos as al
import stumpy
from PIL import Image
import pandas as pd
from scipy import stats
import numpy as np


def split_img(img, crop_factor):
    """ Split the image into squares, crop factor determines num of squares e.g. 4 -> 4 squares """
    # assign the width and height based on input image
    width, height = img.size
    # vertical iterations
    cropped_images = []
    cropped_image_coordinates = []
    for j in range(crop_factor):
        # horizontal iterations
        for i in range(crop_factor):
            # assign values for the crop box
            left = (width / crop_factor * i)  # scan rightward
            upper = (height / crop_factor * j)  # scan down
            right = (width / crop_factor) + (width / crop_factor * i)  # scan rightward
            lower = (height / crop_factor) + (height / crop_factor * j)  # scan down
            box = (left, upper, right, lower)
            # crop + add to series
            region = img.crop(box)
            cropped_images.append(region)
            # save file
            # filename = "crop_{}_{}.png".format(j, i)
            # region.save(filename)
            cropped_image_coordinates.append(box)
    return cropped_images, cropped_image_coordinates


def make_image_array(img, avg_window):
    # convert PIL images to array
    img_array = np.asarray(img)
    # print(img_array.shape)
    # convert array to 1-D;
    parsed_image = img_array.flatten()
    parsed_image = al.rolling_avg(parsed_image, avg_window)
    return np.array(parsed_image)  # average based on avg_window number


def print_plot(image, file_cycle):
    plt.plot(image)
    # filename = "plot{}.pdf".format(file_cycle)
    # plt.savefig(filename)
    plt.show()


def plot_comparison(query, target, idx):
    # Adapted from source: https://stumpy.readthedocs.io/en/latest/Tutorial_Pattern_Searching.html
    # Since MASS computes z-normalized Euclidean distances, we should z-normalize our subsequences before plotting
    q_z_norm = stumpy.core.z_norm(query.values)
    t_z_norm = stumpy.core.z_norm(target.values[idx:idx + len(query)])

    plt.suptitle('Comparing The Query To Its Nearest Neighbor', fontsize='30')
    plt.xlabel('N', fontsize='20')
    plt.ylabel('Value', fontsize='20')
    plt.plot(q_z_norm, lw=2, color="C1", label="Query Subsequence, Q_df")
    plt.plot(t_z_norm, lw=2, label="Nearest Neighbor Subsequence From T_df")
    plt.legend()
    plt.show()


def cut_from_main_image(image, start, end):
    # convert PIL images to array
    img_array = np.asarray(image)
    # print(img_array.shape)
    # convert array to 1-D;
    a, b, c = np.unravel_index(start, img_array.shape)
    d, e, f = np.unravel_index(end, img_array.shape)
    print(img_array[a][b][c])
    print(img_array[d][e][f])
    data = img_array[a:d][b:e][c:f]
    Image.getpixel(a)
    img = Image.fromarray(data)
    img.show()


def find_image(query_path, target_path, num_segments, query_avg_window, target_avg_window):
    # Load the query_array
    query_img = Image.open(query_path)
    query_array = make_image_array(query_img, query_avg_window)
    # print_plot(query_array, 1)
    print(f"Imported Query Image: {len(query_array)}")
    # Load the comparison image
    target_img = Image.open(target_path)
    split_target_images, split_target_coordinates = split_img(target_img, num_segments)
    print("Imported Target Image")
    # split into sections
    split_target_image_data = []
    for image in split_target_images:
        array = make_image_array(image, target_avg_window)
        split_target_image_data.append(array)
        print(f"Split import:{len(array)}")
    # run motif on each section
    query_array = pd.DataFrame(query_array, columns=['values'])
    # cycle through split images and add the results to list
    p_value_results = []
    index_of_pattern = []

    for image in split_target_image_data:
        chicken = pd.DataFrame(image, columns=['values'])
        # find nearest neighbors
        distance_profile = stumpy.core.mass(query_array, chicken)
        idx = np.argmin(distance_profile)
        x = query_array
        y = chicken[idx:(idx + len(query_array))]
        # run kruskal wallis to find similarity
        statistic, p_value = stats.kruskal(x, y)
        p_value_results.append(p_value)
        index_of_pattern.append(idx)

    # best scoring has highest p value
    best_scoring = max(p_value_results)

    # take the best scoring image and do the report
    best_image_index = p_value_results.index(best_scoring)
    best_chicken_image = split_target_images[best_image_index]
    idx = index_of_pattern[best_image_index]
    target_image_array = pd.DataFrame(split_target_image_data[best_image_index], columns=['values'])

    # report
    best_chicken_image.show()
    print(f'The best scoring match is located at:{split_target_coordinates[best_image_index]} (left,upper,right,lower)')
    plot_comparison(query_array, target_image_array, idx)
    print(best_scoring)
