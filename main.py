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

def to_opacityscale(array):
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
    a = []

    for i in key_pos:
        if i in keys:
            x.append(key_pos[i][0][0])
            y.append(key_pos[i][0][1])

            v.append(keys.get(i))
            pressed.append(i)
            key_pos[i][1] = keys.get(i)
    
        a.append(key_pos.get(i)[1])
    
    heat = np.zeros((6,16))
    start = 0
    row = 0
    for i in range(len(a)):
        print(i)
        print(start)
        if (  (i+1) % 16 ) == 0:
            print('entro')
            heat[row] = a[start:i+1]
            row += 1
            start = i+1


    bwv = to_opacityscale(v)
    area = (50)**2  # 0 to 15 point radii


    #heatmap
    print(heat)

    
    extent = 0, 1000, 0, 400
    img = plt.imread("la_keyboard_grid.png")
    fig, ax = plt.subplots()
    im1 = plt.imshow(img, extent=extent)
    im2 = plt.imshow(heat, cmap='plasma', alpha = 0.8, interpolation='bilinear',extent=extent)
    plt.colorbar(shrink=0.7)
    plt.show()


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
    
    