from utility import *


class Point:
    """class defines a point"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

    """returns a string value of the representation of point in the form of "(x, y, z)"   """
    def print_pt(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


class Vector:
    """class defines a vector"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y) and epsilon_equal(self.z, other.z)

    """returns a string value of the representation of the vector in the form of "<x, y, z>"  """
    def print_vec(self):
        return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"


class Color:
    def __init__(self, r = 0.0, g = 0.0, b = 0.0):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        cond1 = epsilon_equal(self.r, other.r)
        cond2 = epsilon_equal(self.g, other.g)
        cond3 = epsilon_equal(self.b, other.b)
        return cond1 and cond2 and cond3


class Ray:
    """class defines a ray"""
    # pt = Point object
    # vec = Vector object

    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return (self.pt == other.pt) and (self.dir == other.dir)


class Light:
    def __init__(self, pt, color):
        self.pt = pt
        self.color = color

    def __eq__(self, other):
        return self.pt == other.pt and self.color == other.color


class Finish:
    def __init__(self, ambient = 1.0, diffuse = 0.0, specular = 0.0, roughness = 0.0):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return (epsilon_eq(self.ambient, other.ambient) and
                epsilon_eq(self.diffuse, other.diffuse) and
                epsilon_eq(self.specular, other.specular) and
                epsilon_eq(self.roughness, other.roughness))


class Sphere:

    def __init__(self, center, radius, color = Color(), finish = Finish()):
        self.center = center  # point
        self.radius = float(radius)  # number
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return (self.center == other.center
                and epsilon_eq(self.radius, other.radius)
                and self.color == other.color
                and self.finish == other.finish)


class View:

    def __init__(self, min_x, max_x, min_y, max_y, width, height):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.width = width
        self.height = height

    def __eq__(self, other):
        if not self.min_x == other.min_x:
            return False
        if not self.max_x == other.max_x:
            return False
        if not self.min_y == other.min_y:
            return False
        if not self.max_y == other.max_y:
            return False
        if not self.width == other.width:
            return False
        if not self.height == other.height:
            return False
        else:
            return True

class ConfigData:

    def __init__(self, filename, eye_point, view_data, light, ambient):
        self.filename = filename
        self.eye_point = eye_point
        self.view_data = view_data
        self.light = light
        self.ambient = ambient

    def __eq__(self, other):
        if not isinstance(other, config_data):
            return False
        if self.filename != other.filename:
            return False
        if not self.eye_point == other.eye_point:
            return False
        if not self.view_data == other.view_data:
            return False
        if not self.light == other.light:
            return False
        if not self.ambient == other.ambient:
            return False
        else:
            return True

