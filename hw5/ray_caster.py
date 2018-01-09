from sys import *
from commandline import *
from cast import *
from data import *

# python3 ray_caster.py filename eye x y z view min_x max_x min_y max_y width height -light x y z r g b -ambient r g b

def final_casting_function():

    cmd_arg = argv

    config_data = get_config_data(cmd_arg[1:])
    #sphere_list = get_sphere_list(cmd_arg[1])

    if config_data is None:
        print("usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]")
        exit()

    try:
        fin = open(config_data.filename, "r")
    except:
        print("Can not open file " + config_data.filename)
        exit()

    sphere_list = get_sphere_list(fin)

    try:
        fin.close()
    except:
        print("Can not close file " + config_data.filename)
        exit()

    min_x = config_data.view_data.min_x
    max_x = config_data.view_data.max_x
    min_y = config_data.view_data.min_y
    max_y = config_data.view_data.max_y
    width = config_data.view_data.width
    height = config_data.view_data.height

    eye_point = config_data.eye_point
    ambient = config_data.ambient
    light = config_data.light

    file_name = "image.ppm"

    #print("before casting ray")
    cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light, file_name)
    #print("after casting ray")

final_casting_function()

