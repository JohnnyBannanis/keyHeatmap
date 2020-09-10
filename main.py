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
    values = []
    pressed = []
    v_heat = []

    for i in key_pos:
        if i in keys:
            x.append(key_pos[i][0][0])
            y.append(key_pos[i][0][1])

            values.append(keys.get(i))
            pressed.append(i)
            key_pos[i][1] = keys.get(i)
    
        v_heat.append(key_pos.get(i)[1])
    
    heat = np.zeros((6,16))
    start = 0
    row = 0
    for i in range(len(v_heat)):
        if (i+1) % 16 == 0:
            heat[row] = v_heat[start:i+1]
            row += 1
            start = i+1

    opacity = to_opacityscale(values)

    generate_figure(x,y,heat,values,pressed,opacity)

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
    
    