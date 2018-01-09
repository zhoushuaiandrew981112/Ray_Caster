from data import *
from math import *


# scale_vector returns a new vector after multiplying the input vector with a scalar
def scale_vector(vector, scalar):
    result_vector = Vector(vector.x * scalar, vector.y * scalar, vector.z * scalar)
    return result_vector


# dot_vector returns a int or float that is the dot product of the 2 in put vectors
def dot_vector(vector_1, vector_2):
    x_product = vector_1.x * vector_2.x
    y_product = vector_1.y * vector_2.y
    z_product = vector_1.z * vector_2.z
    return x_product + y_product + z_product


# length_vector returns int or float that is the length of the input vector
def length_vector(vector):
    return sqrt(vector.x ** 2 + vector.y ** 2 + vector.z ** 2)


# normalize_vector returns a new vector that is the unit vector of the input vector
def normalize_vector(vector):
    vector_mag = length_vector(vector)
    vec_x = vector.x / vector_mag
    vec_y = vector.y / vector_mag
    vec_z = vector.z / vector_mag
    unit_vector = Vector(vec_x, vec_y, vec_z)
    return unit_vector

# difference_point returns a new vector constructed by subtracting point2 from point1
def difference_point(point1, point2):
    d_x = point1.x - point2.x
    d_y = point1.y - point2.y
    d_z = point1.z - point2.z
    result_vector = Vector(d_x, d_y, d_z)
    return result_vector


# difference_vector returns a new vector constructed by subtracting vector 1 from vector2
def difference_vector(vector1, vector2):
    d_x = vector1.x - vector2.x
    d_y = vector1.y - vector2.y
    d_z = vector1.z - vector2.z
    result_vector = Vector(d_x, d_y, d_z)
    return result_vector

def distance_between(point1, point2):
    return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2 + (point1.z - point2.z)**2)


# translate_point returns a new point that is constructed
# by moving input point through the direction and magnitude of the input vector
def translate_point(point, vector):
    new_x = point.x + vector.x
    new_y = point.y + vector.y
    new_z = point.z + vector.z
    new_point = Point(new_x, new_y, new_z)
    return new_point


# vector_from_to returns a new vector that is constructed by originating at from_point and points at to_point
def vector_from_to(from_point, to_point):
    d_x = to_point.x - from_point.x
    d_y = to_point.y - from_point.y
    d_z = to_point.z - from_point.z
    result_vector = Vector(d_x, d_y, d_z)
    return result_vector