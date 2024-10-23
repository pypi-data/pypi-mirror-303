import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt

def parse_image_txt(filename):
    """Parses the gray-scale image saved in .txt format as saved from the "Video" tab in LabSpec6

    Params: 
    - filename: path to txt file containing gray-scale image data and X/Y positions of pixels

    Returns:
    - Numpy array (M) of x pixel positions
    - Numpy array (M) of y pixel positions
    - Numpy array (MxN) of gray-scale intensity values
    """

    with open(filename, encoding="latin-1") as f:
        x = None
        y = []
        vals = []
        for line in f:
            if line.startswith("#"):
                continue
            if line.startswith("\t"):
                x = [float(x) for x in line.split()]
            else:
                split = line.split()
                y.append(float(split[0]))
                vals.append([float(x) for x in split[1:]])
                


    return np.flip(np.array(x)), np.flip(np.array(y)), np.flip(np.array(vals))


def parse_image_comb(bmp_filename, txt_filename):
    """Returns PIL Image object with corresponding extends from .txt version of the image

    Params:
    - bmp_filename: Filename of the .bmp file taken from the LabSpec6 video feed
    - txt_filename: Filename of the .txt file taken from the LabSpec7 video feed

    Returns:
    - img: PIL Image object for use with matplotlib.pyplot.imshow
    - extent: Extents for use with matplotlib.pyplot.imshow"""

    x, y, gray = parse_image_txt(txt_filename)

    extent = (x[0], x[-1], y[-1], y[0])
    
    img = Image.open(bmp_filename)

    return img, extent


def parse_data_txt(filename):
    """Parses the .txt version of the l6m file when saving in the browser tab or map tab with the spectral window highlighted

    Params: 
    - filename: path to txt file version of l6m file

    Returns:
    - 1D array containing Raman shift (cm^-1) bins
    - 2D array containing (x, y) positions
    - 2D array with each row containing the counts for a given position
    """
    with open(filename, encoding="latin-1") as f:
        shift = None
        pos = []
        counts = []
        for line in f:
            if line.startswith("#"): continue
            if line.startswith("\t"):
                shift = [float(x) for x in line.split()]
            else:
                split = line.split()
                pos.append((float(split[1]), float(split[0])))
                counts.append([float(x) for x in split[2:]])


    return np.array(shift), np.array(pos), np.array(counts)

def extra_spectra_to_files(filename, dirname="extracted-spectra"):
    """Extracts all raman spectra to a subdirectory from the .txt version of the l6m map file. The spatial position of spectra is included in extracted filename.

    Params:
    - filename: path to txt file version of l6m file
    """
    os.makedirs(dirname, exist_ok=True)
    shift, pos, counts = parse_data_txt(filename)

    for i, p in enumerate(pos):
        stem = filename.replace(".txt", "")
        name = f"{stem}_{str(p[0]).replace(".", "p")}_{str(p[1]).replace(".", "p")}.dat"
        stack = np.vstack([shift, counts[i]]).T
        np.savetxt(f"{dirname}/{name}", stack)


def determine_rectangular_map_dim(pos):
    """Guesses the dimensions of a set of positions assuming the map is rectangular

    Params:
    - pos: 2d array with each row corresponding to an (X,Y) spectral position
    
    Returns:
    - tuple (M, N) containig the shape of the rectangular map
    """

    T = len(pos)
   
    v0 = pos[0][1]
    count = 0
    for i, p in enumerate(pos):
        if p[1] != v0:
            break

        count += 1

    return (T // count, count)

        

def extract_max_from_range(x, y, x_min, x_max, normalize=False):
    """Returns maximum y-value from a given x-range

    Useful for phase mapping where Raman intensity from a certain spectral
    region can be overlayed onto a microscope image

    Params:
    - x: x-values
    - y: y-values
    - x_min: lower x-bound for max search
    - x_max: upper x-bound for max search
    - normalize: Optional argument to normal the maximum value to the maximum of the spectra
    """
    start = np.argmax(x > x_min)
    end = np.argmax(x > x_max)

    if normalize:
        return np.max(y[start:end]) / np.max(y)

    return np.max(y[start:end])

def extract_maxes_from_range(shift, counts, shift_min, shift_max, normalize=False):
    """Returns all maxes for a given Raman shift range. Wrapper function for extract_max_from_range
    
    Params:
    - shift: Raman shift array
    - counts: 2D array of count data for map spectra
    - shift_min: lower bound for Raman shift
    - shift_max: upper bound for Raman shift
    - normalize: Optional argument to normalize extracted max value to the maximum of the spectrum

    Returns:
    - Array of extracted maximums"""

    maxes = []
    for c in counts:
        m = extract_max_from_range(shift, c, shift_min, shift_max)
        maxes.append(m)

    return np.array(maxes)


def extract_extent_from_pos_rect(pos, dim):
    """Extracts the extents from a given set of positions assuming rectangular grid

    Params:
    - pos: 2d array with each row correspodning to an (X,Y) spectral position
    - dim: Dimensions of the rectangular grid

    Returns:
    - tuple of (left, right, bottom, top)
    """

    x_min = pos[0][0]
    x_max = pos[-1][0]
    y_min = pos[-1][1]
    y_max = pos[0][1]
    dx = np.abs(pos[0][0] - pos[1][0])
    dy = np.abs(pos[0][1] - pos[dim[1]][1])

    return (x_min - dx / 2, x_max + dx/2, y_min + dy/2, y_max - dy/2)

def quickplot_rect_map(l6m_txt, img_bmp, img_txt, shift_min, shift_max, normalize=False):
    """Creates a quick matplotlib figure heatmap using provided shift_min and shift_max

    Params:
    - l6m_text: text version of the LabSpec6 map file
    - img_bmp: bitmap image of the camera view
    - img_txt: text version of the camera view
    - shift_min: minimum Raman shift (left bound) for finding maximum
    - shift_max: maximum Raman shift (right bound) for finding maximum
    - normalize: should max value extracted be normalized to maximum of spectrum?"""

    img, extent_camera = parse_image_comb(img_bmp, img_txt)
    shift, pos, counts = parse_data_txt(l6m_txt)
    dim = determine_rectangular_map_dim(pos)
    extent = extract_extent_from_pos_rect(pos, dim)

    maxes = np.reshape(extract_maxes_from_range(shift, counts, shift_min, shift_max),
                       dim)

    plt.figure()

    plt.imshow(img, extent=extent_camera)
    plt.imshow(maxes, extent=extent, alpha=0.5)
    plt.xlim(extent_camera[0], extent_camera[1])
    plt.ylim(extent_camera[2], extent_camera[3])
    plt.xlabel(r"X [$\mu$m]", fontsize=16)
    plt.ylabel(r"Y [$\mu$m]", fontsize=16)
    plt.show()

