import matplotlib.pyplot as plt
import matplotlib as mpl
from pynput import keyboard
from plot import *
from matplotlib import cm

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
        print(aux)
        if(aux in keys):
            keys[aux] += 1
        else:
            keys[aux] = 1

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print(keys)
        
        return False

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

    for i in key_pos:
        if i in keys:
            x.append(key_pos[i][0])
            y.append(key_pos[i][1])
            v.append(keys.get(i))
            
    
    area = (50)**2  # 0 to 15 point radii

    img = plt.imread("la_keyboard.png")
    fig, ax = plt.subplots()
    ax.imshow(img)

    ##plt.scatter(x, y, s= area, c= cm.plasma(vf), alpha=0.6 )
    plt.scatter(x, y, s= area, c= v, cmap='plasma', vmax=sum(v) ,alpha=0.5)
    plt.colorbar()
    plt.show()
    #