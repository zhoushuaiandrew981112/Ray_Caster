from data import *


def process_line(line):
    string_list = line.strip().split()
    float_list = []
    if len(string_list) != 11:
        raise RuntimeError("The input file is not properly formatted")
    for i in range(len(string_list)):
        float_list.append(float(string_list[i]))

    point = Point(float_list[0], float_list[1], float_list[2])
    radius = float_list[3]
    color = Color(float_list[4], float_list[5], float_list[6])
    finish = Finish(float_list[7], float_list[8], float_list[9], float_list[10])

    return Sphere(point, radius, color, finish)

"""
# f_name is the filename inputted from the command line argument, should be argv[1]
def get_sphere_list(f_name):
    sphere_list = []
    counter = 0
    print("before try and except")
    try:
        file = open(f_name, "r")
        for line in file:
            #print(line)
            sphere_list.append(process_line(line))
            counter += 1
    except:
        print("malformed sphere on line " + str(counter) + " ... skipping")
        counter += 1
        exit(1)

    file.close()

    return sphere_list
"""

def get_sphere_list(f_obj):
    sphere_list = []
    counter = 0

    for line in f_obj:
        #print(line)
        sphere_list.append(process_line(line))
        counter += 1

    return sphere_list


def get_arguments(parameter, flag, count):
    try:
        index = parameter.index(flag)
    except:
        return None
    if index + 1 + count < len(parameter):
        return None
    args = []
    for c in range(count):
        try:
            args.append(float(parameter[index + 1 + c]))
        except:
            return None
    return args


def get_eye_point(parameter):
    args = get_arguments(parameter, "-eye", 3)
    if args is None:
        return Point(0.0, 0.0, -14.0)
    else:
        return Point(args[0], args[1], args[2])


def get_view_data(parameter):
    args = get_arguments(parameter, "-view", 6)
    if args is None:
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 512
        height = 384
        return View(min_x, max_x, min_y, max_y, width, height)
    else:
        return View(args[0], args[1], args[2], args[3], args[4], args[5])


def get_light(parameter):
    args = get_arguments(parameter, "-light", 6)
    if args is None:
        return Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
    else:
        return Light(Point(args[0], args[1], args[2]), Color(args[3], args[4], args[5]))


def get_ambient(parameter):
    args = get_arguments(parameter, "-ambient", 3)
    if args is None:
        return Color(1.0, 1.0, 1.0)
    else:
        return Color(args[0], args[1], args[2])


def get_config_data(parameter):
    if len(parameter) == 0:
        return None
    filename = parameter[0]
    eye_pt = get_eye_point(parameter[1:])
    view_data = get_view_data(parameter[1:])
    light = get_light(parameter[1:])
    ambient = get_ambient(parameter[1:])

    return ConfigData(filename, eye_pt, view_data, light, ambient)