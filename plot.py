import matplotlib.pyplot as plt
import matplotlib as mpl
from pynput import keyboard
from matplotlib import cm


def heatmap_plot(heat):
    extent = 0, 1000, 0, 400
    img = plt.imread("la_keyboard_grid.png")
    fig, ax = plt.subplots()
    im1 = plt.imshow(img, extent=extent)
    im2 = plt.imshow(heat, cmap='plasma', alpha = 0.8, interpolation='nearest',extent=extent)
    plt.colorbar(shrink=0.7)
    plt.show()

def opacity_plot(x,y,opacity):
    img = plt.imread("la_keyboard.png")
    fig, ax = plt.subplots()
    ax.imshow(img)

    sc = plt.scatter(x, y, c=opacity, s=3600)
    plt.show()

def bar_plot(pressed,values):
    plt.bar(pressed, height=values)
    plt.show()

key_pos = {
    # key : [ position(x,y) , value,  ]
    #first row
    'esc':      [ (40 ,40), 0 ],
    'f1':       [ (100,40), 0 ],
    'f2':       [ (160,40), 0 ],
    'f3':       [ (220,40), 0 ],
    'f4':       [ (280,40), 0 ],
    'f5':       [ (340,40), 0 ],
    'f6':       [ (400,40), 0 ],
    'f7':       [ (460,40), 0 ],
    'f8':       [ (520,40), 0 ],
    'f9':       [ (580,40), 0 ],
    'f10':      [ (640,40), 0 ],
    'f11':      [ (700,40), 0 ],
    'f12':      [ (760,40), 0 ],
    'print_screen': [ (820,40), 0], 
    'insert':   [ (880,40), 0],
    'delete':   [ (940,40), 0],

    #second row
    '|':        [ (40,100)  , 0 ],
    '1':        [ (100,100) , 0 ],
    '2':        [ (160,100) , 0 ],
    '3':        [ (220,100) , 0 ],
    '4':        [ (280,100) , 0 ],
    '5':        [ (340,100) , 0 ],
    '6':        [ (400,100) , 0 ],
    '7':        [ (460,100) , 0 ],
    '8':        [ (520,100) , 0 ],
    '9':        [ (580,100) , 0 ],
    '0':        [ (640,100) , 0 ],
    "'":        [ (700,100) , 0 ],
    '¿':        [ (760,100) , 0 ],
    'backspace':[ (855,100) , 0 ],
    'backspace2': [] ,
    'home':     [ (945,100) , 0 ],

    #third row
    'tab':      [ (55,160)  , 0 ],
    'q':        [ (135,160) , 0 ],
    'w':        [ (195,160) , 0 ],
    'e':        [ (255,160) , 0 ],
    'r':        [ (315,160) , 0 ],
    't':        [ (375,160) , 0 ],
    'y':        [ (435,160) , 0 ],
    'u':        [ (495,160) , 0 ],
    'i':        [ (555,160) , 0 ],
    'o':        [ (615,160) , 0 ],
    'p':        [ (675,160) , 0 ],
    '´':        [ (735,160) , 0 ],
    '+':        [ (795,160) , 0 ],
    'enter':    [ (875,190) , 0 ],
    'enter2':   [],
    'page_up':  [ (945,160) , 0 ],

    #forth row
    'caps_lock':[ (55,220)  , 0 ],
    'a':        [ (150,220) , 0 ],
    's':        [ (210,220) , 0 ],
    'd':        [ (270,220) , 0 ],
    'f':        [ (330,220) , 0 ],
    'g':        [ (390,220) , 0 ],
    'h':        [ (450,220) , 0 ],
    'j':        [ (510,220) , 0 ],
    'k':        [ (570,220) , 0 ],
    'l':        [ (630,220) , 0 ],
    'ñ':        [ (690,220) , 0 ],
    '{':        [ (750,220) , 0 ],
    '}':        [ (810,220) , 0 ],
    'enter3':   [],
    'enter4':   [],
    'page_down':[ (945,220) , 0 ], 

    #fivth row
    'shift':    [ (55,280)  , 0 ],
    '<':        [ (120,280) , 0 ],
    'z':        [ (180,280) , 0 ],
    'x':        [ (240,280) , 0 ],
    'c':        [ (300,280) , 0 ],
    'v':        [ (360,280) , 0 ],
    'b':        [ (420,280) , 0 ],
    'n':        [ (480,280) , 0 ],
    'm':        [ (540,280) , 0 ],
    ',':        [ (600,280) , 0 ],
    '.':        [ (660,280) , 0 ],
    '-':        [ (720,280) , 0 ],
    'shift_r':  [ (800,280) , 0 ],
    'shift_r2': [],
    'up':       [ (885,280) , 0 ],
    'end':      [ (945,280) , 0 ],

    #sixth row
    'ctrl_l':   [ (55,340)  , 0 ],
    'cmd':      [ (135,340) , 0 ],
    'alt_l':    [ (210,340) , 0 ],
    'space':    [ (450,340) , 0 ],
    'space2':   [],
    'space3':   [],
    'space4':   [],
    'space5':   [],
    'space6':   [],
    'space7':   [],
    'alt_r':    [ (640,340) , 0 ],
    'menu':     [ (700,340) , 0 ],
    'ctrl_r':   [ (760,340) , 0 ],
    'left':     [ (825,340) , 0 ],
    'down':     [ (885,340) , 0 ],
    'right':    [ (945,340) , 0 ]
}


#
key_pos['backspace2'] = key_pos['backspace']

key_pos['enter2'] = key_pos['enter']
key_pos['enter3'] = key_pos['enter']
key_pos['enter4'] = key_pos['enter']

key_pos['shift_r2'] = key_pos['shift_r']

key_pos['space2'] = key_pos['space']
key_pos['space3'] = key_pos['space']
key_pos['space4'] = key_pos['space']
key_pos['space5'] = key_pos['space']
key_pos['space6'] = key_pos['space']
key_pos['space7'] = key_pos['space']