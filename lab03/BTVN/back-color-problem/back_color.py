from random import *
from check import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes


def generate_quiz():
    text = ['blue','red','yellow','green']
    color = ['#3F51B5','#C62828','#FFD600','#4CAF50']

    return [
                choice(text),
                choice(color),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    click = [x,y]
    
    if quiz_type == 0:
        if text == 'blue':
            return is_inside(click,shapes[0]['rect'])
        if text == 'red':
            return is_inside(click,shapes[1]['rect'])
        if text == 'yellow':
            return is_inside(click,shapes[2]['rect'])
        if text == 'green':
            return is_inside(click,shapes[3]['rect'])
    else:
        if color == '#3F51B5':
            return is_inside(click,shapes[0]['rect'])
        if color == '#C62828':
            return is_inside(click,shapes[1]['rect'])
        if color == '#FFD600':
            return is_inside(click,shapes[2]['rect'])
        if color == '#4CAF50':
            return is_inside(click,shapes[3]['rect'])
            