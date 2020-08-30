import matplotlib.pyplot as plt
import matplotlib as mpl
from pynput import keyboard
from plot import *
from matplotlib import cm
import numpy as np

keys = {}

def on_press(key):
    try:
        aux = key.char.lower()
        if(aux in keys):
            keys[aux] += 1
        else:
            keys[aux] = 1
    except AttributeError:
        aux = str(key).replace('Key.','')
        if(aux in keys):
            keys[aux] += 1
        else:
            keys[aux] = 1

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print(keys)
        
        return False

def to_grayscale(array):
    local = max(array)
    aux = []
    for i in array:
        aux.append( (0,0,0,i/local) )
    return aux

if __name__ == "__main__":

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()
            
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    x = []
    y = []
    v = []
    pressed = []

    for i in key_pos:
        if i in keys:
            x.append(key_pos[i][0])
            y.append(key_pos[i][1])
            v.append(keys.get(i))
            pressed.append(i)

    bwv = to_grayscale(v)
    area = (50)**2  # 0 to 15 point radii

    #heatmap?? kind of
    '''
    img = plt.imread("la_keyboard.png")
    fig, ax = plt.subplots()
    ax.imshow(img)

    plt.scatter(x, y, s= area, c= v, cmap='plasma',vmax=sum(v) ,alpha=0.5)
    plt.colorbar(shrink=0.7)
    plt.show()
    '''

    #grayscale
    
    img = plt.imread("la_keyboard.png")
    fig, ax = plt.subplots()
    ax.imshow(img)

    sc = plt.scatter(x, y, c=bwv, s=area)
    plt.show()

    #bars
    plt.bar(pressed, height=v)
    plt.show()
    #

    '''
    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)
    
    cmap = mpl.cm.Greys
    norm = mpl.colors.Normalize(vmin=5, vmax=10)
    
    cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                    norm=norm,
                                    orientation='horizontal')
    cb1.set_label('Some Units')
    fig.show()
    '''

    heat = np.array([[2.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 4.2],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                    [2.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                    [2.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                    [2.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
                    [2.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 4.2]])

    extent = 0, 1000, 0, 400
    img = plt.imread("la_keyboard_grid.png")
    fig, ax = plt.subplots()
    im1 = plt.imshow(img, extent=extent)
    im2 = plt.imshow(heat, cmap='plasma', alpha = 0.8, interpolation='bilinear',extent=extent)
    plt.colorbar(shrink=0.7)
    plt.show()
    