from pynput import keyboard

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm

import numpy as np

key_pos = {
    'a': (150,220),
    'b': (420,280),
    'c': (300,50),
}

keys = {}

def on_press(key):
    try:
        if(key.char in keys):
            keys[key.char] += 1
        else:
            keys[key.char] = 1
    except AttributeError:
        if(key in keys):
            keys[key] += 1
        else:
            keys[key] = 1

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


    # Fixing random state for reproducibility
    np.random.seed(19680801)
    
    
    #N = 1
    #x = np.random.rand(N)
    #y = np.random.rand(N)
    x = []
    y = []

    for i in key_pos:
        x.append(key_pos[i][0])
        y.append(key_pos[i][1])
        
    colors = np.random.rand(3)
    area = (30 * np.random.rand(1))**2  # 0 to 15 point radii
    
    img = plt.imread("la_keyboard.png")
    fig, ax = plt.subplots()
    ax.imshow(img)

    plt.scatter(x, y, s=area, c=cm.inferno(np.abs(y)), alpha=1)
    plt.show()