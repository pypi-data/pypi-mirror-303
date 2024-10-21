import numpy as np
import matplotlib.pyplot as plt

def plot_image(image, show=True):
    if image is None:
        raise ValueError("Image cannot be None")
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array.")
    
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    
    if show:
        plt.show()

def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    names_lst = ['Image {}'.format(i + 1) for i in range(number_images)]
    
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')
        
    fig.tight_layout()
    plt.show()

def plot_histogram(image, normalized=False):
    if image is None:
        raise ValueError("Image cannot be None")
    if not isinstance(image, np.ndarray):
        raise TypeError("Input must be a numpy array.")
    
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_lst = ['red', 'green', 'blue']
    
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title(f'{color.title()} Histogram')
        hist, bins = np.histogram(image[:, :, index].ravel(), bins=256)
        if normalized:
            hist = hist / hist.sum()  
        ax.plot(bins[:-1], hist, color=color, alpha=0.8)
    
    fig.tight_layout()
    plt.show()
