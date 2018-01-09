from vector_math import *
from data import *
from math import *


# helper functions
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def quad_solve_1(a, b, c):
    return (-b + sqrt(discriminant(a, b, c))) / (2 * a)


def quad_solve_2(a, b, c):
    d = discriminant(a, b, c)
    if d >= 0:
        return (-b - sqrt(d)) / (2 * a)

def point_intersect(ray, t):
    point_intersect = translate_point(ray.pt, scale_vector(ray.dir, t))
    return point_intersect

def sphere_intersection_point(ray, sphere):
    a = length_vector(ray.dir) ** 2
    b = 2 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir)
    c = length_vector(difference_vector(ray.pt, sphere.center))**2 - sphere.radius ** 2
    d = discriminant(a, b, c)

    if d < 0:
        return None
    elif d == 0:
        t = quad_solve_1(a, b, c)
        if t > 0:
            return point_intersect(ray, t)
        else:
            return None
    elif d > 0:
        t_1 = quad_solve_1(a, b, c)
        t_2 = quad_solve_2(a, b, c)

        if t_1 > 0 and t_2 > 0:
            return point_intersect(ray, min(t_1, t_2))
        elif (t_1 < 0 and t_2 > 0) or (t_1 > 0 and t_2 < 0):
            return point_intersect(ray, max(t_1, t_2))
        elif t_1 == 0 and t_2 == 0:
            return ray.pt
        else:
            return None
    else:
        return None


"""
def sphere_intersection_point(ray, sphere):
    A = dot_vector(ray.dir, ray.dir)
    B = dot_vector(scale_vector(difference_point(ray.pt, sphere.center), 2), ray.dir)
    C = dot_vector(difference_point(ray.pt, sphere.center), difference_point(ray.pt, sphere.center)) - sphere.radius ** 2

    delta = (B ** 2 - 4 * A * C)

    if delta < 0:
        return None
    else:
        t1 = (-B + sqrt(delta)) / (2 * A)
        t2 = (-B - sqrt(delta)) / (2 * A)
        if t1 > t2:
            tmin = t2
            tmax = t1
        else:
            tmin = t1
            tmax = t2

    if tmin >= 0:
        p1 = translate_point(ray.pt, scale_vector(ray.dir, tmin))
        return p1

    elif tmax >= 0:
        p2 = translate_point(ray.pt, scale_vector(ray.dir, tmax))
        return p2

    else:
        return None
"""

def find_intersection_points(sphere_list, ray):
    new_list = []
    for sphere in sphere_list:
        p = sphere_intersection_point(ray, sphere)
        if p is not None:
            new_list.append((sphere, p))
    return new_list

def sphere_normal_at_point(sphere, point):
    return normalize_vector(vector_from_to(sphere.center, point))
