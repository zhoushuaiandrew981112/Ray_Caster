import data
import cast

min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 512
height = 384

eye_point = data.Point(0.0, 0.0, -14.0)
light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5))

sphere_1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0, 0.0, 1.0), data.Finish(0.2, 0.4, 0.5, 0.05))
sphere_2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0.0, 0.0), data.Finish(0.4, 0.4, 0.5, 0.05))

sphere_list = [sphere_1, sphere_2]

ambient = data.Color(1.0, 1.0, 1.0)

cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light)

"""
import data
import cast

min_x = -10
max_x = 10
min_y = -7.5
max_y = 7.5
width = 512
height = 384

eye_point = data.Point(0.0, 0.0, -14.0)
sphere_1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, data.Color(0.0, 0.0, 1.0))
sphere_2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, data.Color(1.0, 0.0, 0.0))

sphere_list = [sphere_1, sphere_2]

cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, data.Color(0.0, 0.0, 0.0))
"""