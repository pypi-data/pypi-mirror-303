import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import numpy as np


def red():
    reds = ['#8C2F1B', '#A0543F', '#B57863', '#C99D86', '#DEC1AA']
    return reds


def blue():
    blues = ['#367FBF', '#5C94C2', '#81A8C5', '#A7BDC8', '#CCD1CB']
    return blues


def green():
    greens = ['#007161','#308877','#61A08D','#91B7A2','#C2CFB8']
    return greens


def yellow():
    yellows = ['#F2B544','#F2BF60','#F2C97B','#F2D297','#F2DCB2']
    return yellows


def purple():
    purples = ['#BC488B','#C76898','#D287A6','#DCA7B3','#E7C6C1']
    return purples


def greyscale():
    greyscales = ['#fcfaf4', '#c0beb9', '#84827e', '#494642', '#0d0a07']
    return greyscales


def colors():
    color = ['#8C2F1B', '#367FBF','#007161', '#F2B544','#BC488B']
    return color


def gradient(color1, color2, n):
    # Convert hex colors to RGB
    rgb1 = np.array(mcolors.hex2color(color1))
    rgb2 = np.array(mcolors.hex2color(color2))

    # Generate linearly spaced numbers between the two colors
    gradients = np.linspace(rgb1, rgb2, n)

    # Convert RGB values back to hex
    gradients = [mcolors.rgb2hex(rgb) for rgb in gradients]

    return gradients


def divergent(color1, color2, n):
    # Split n into two parts (half for each gradient)
    n_half = n // 2

    # Generate gradient from color1 to white
    gradient1 = gradient(color1, "#ffffff", n_half + 1)[:-1]  # Remove duplicate white

    # Generate gradient from white to color2
    gradient2 = gradient("#ffffff", color2, n_half + 1)

    # Combine both gradients to form a divergent palette
    divergents = gradient1 + gradient2

    return divergents