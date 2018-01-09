import data
import vector_math
import collisions


light_obj = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(0, 0, 0))


def compute_ambient_color(sphere, ambient):
    ambient_r = sphere.color.r * sphere.finish.ambient * ambient.r
    ambient_b = sphere.color.g * sphere.finish.ambient * ambient.g
    ambient_g = sphere.color.b * sphere.finish.ambient * ambient.b
    return data.Color(ambient_r, ambient_b, ambient_g)

def compute_diffuse_color(n_dot_l_dir, light, sphere):
    diffuse_r = sphere.color.r * n_dot_l_dir * light.color.r * sphere.finish.diffuse
    diffuse_g = sphere.color.g * n_dot_l_dir * light.color.g * sphere.finish.diffuse
    diffuse_b = sphere.color.b * n_dot_l_dir * light.color.b * sphere.finish.diffuse
    return data.Color(diffuse_r, diffuse_g, diffuse_b)

def compute_specular_color(light, sphere, specular_intensity):
    if sphere.finish.roughness == 0:
        return data.Color(0.0, 0.0, 0.0)
    else:
        specular_r = light.color.r * sphere.finish.specular * (specular_intensity ** (1 / sphere.finish.roughness))
        specular_g = light.color.g * sphere.finish.specular * (specular_intensity ** (1 / sphere.finish.roughness))
        specular_b = light.color.b * sphere.finish.specular * (specular_intensity ** (1 / sphere.finish.roughness))
        return data.Color(specular_r, specular_g, specular_b)

def add_color(color1,color2):
    r = color1.r + color2.r
    g = color1.g + color2.g
    b = color1.b + color2.b
    return data.Color(r, g, b)


def cast_ray(ray, sphere_list, light = light_obj, ambient = data.Color(), eye_point = data.Point(0, 0, -14)):

    # intersections contains a list of tuples of spheres and points, ex: [(Sphere_1, Point_1), (Sphere_2, Point_2), ...]
    intersections = collisions.find_intersection_points(sphere_list, ray)

    if len(intersections) == 0:
        return data.Color(1.0, 1.0, 1.0)
    else:

        # initializing variable that stores the index and the distance of the tuple with the smallest distance
        index_of_nearest_sphere = 0
        distance_of_nearest_sphere = vector_math.distance_between(intersections[0][1], ray.pt)

        # loop through all_intersection_point and find the index of the tuple that contains the sphere & intersection with the smallest distance from ray's point
        for index in range(0, len(intersections)):
            distance_between_points = vector_math.distance_between(intersections[index][1], ray.pt)
            if distance_between_points < distance_of_nearest_sphere:
                index_of_nearest_sphere = index
                distance_of_nearest_sphere = distance_between_points

        # storing the sphere and intersection point in to variables for later usage
        nearest_sphere = intersections[index_of_nearest_sphere][0]
        nearest_intersection = intersections[index_of_nearest_sphere][1]


        # ==== color calculation based on ambient light, diffusion, light color and location ====
        # Impricision of floats can create collision issues with the sphere where the point lies when using the computed intersection
        # A point "pe" that is 0.01 above te intersection point will be used instead
        sphere_normal_vector = collisions.sphere_normal_at_point(nearest_sphere, nearest_intersection)
        pe_translate_direction_vector = vector_math.scale_vector(sphere_normal_vector, 0.01)
        # new point PE is now found
        pe = vector_math.translate_point(nearest_intersection, pe_translate_direction_vector)

        # === determine whether diffusivity is applicable -- determine if there are any obstruction of light vectors ===
        # comput vector from pe to light point then compute normalized vector from pe to to light point
        l_dir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.pt))
        n_dot_l_dir = vector_math.dot_vector(sphere_normal_vector, l_dir)

        #              === computing the specular_intensity ===
        reflection_vector = vector_math.difference_vector(l_dir ,vector_math.scale_vector(sphere_normal_vector, 2 * n_dot_l_dir))
        #creating the direction vector that points from eye_point to pe
        v_dir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, pe)) #Vdir
        # specular_intensity is defined to be the dot product of reflection_vector and the direction vector from eye_point to pe
        specular_intensity = vector_math.dot_vector(v_dir, reflection_vector)

        ambient_color = compute_ambient_color(nearest_sphere, ambient)

        if n_dot_l_dir > 0:
            ray_to_point = data.Ray(pe,l_dir)
            inter = collisions.find_intersection_points(sphere_list, ray_to_point)
            if len(inter) == 0:
                diffuse_color = compute_diffuse_color(n_dot_l_dir, light, intersections[index_of_nearest_sphere][0])
                if specular_intensity > 0:
                    specular_color = compute_specular_color(light, nearest_sphere, specular_intensity)
                    return add_color(add_color(specular_color, diffuse_color), ambient_color)
                else:
                    return add_color(diffuse_color, ambient_color)
            else:
                return ambient_color
        elif specular_intensity > 0:
            specular_color = compute_specular_color(light, nearest_sphere, specular_intensity)
            return add_color(specular_color, ambient_color)
        else:
            return ambient_color


# cast_all_ray function writes a ppm file in the in the specified file
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light, file_name):

    # not certain about the file type of the image file here, I put .txt for now
    image_file = open(file_name, "w")

    num_of_pixel_x = (max_x - min_x) / float(width)
    num_of_pixel_y = (max_y - min_y) / float(height)

    #print("P3")
    #print(str(width), str(height))
    #print("255")
    image_file.write("P3\n")
    image_file.write(str(width) + " " + str(height) + "\n")
    image_file.write("255\n")

    #print("before going in double for loop in cast_all_rays")
    count = 0

    for row in range(height):
        #print("in row loop")
        y = max_y - row * num_of_pixel_y
        for col in range(width):
            x = min_x + col * num_of_pixel_x
            # z-coordinate is constant there for z = 0.0 for all point on image plane
            point_on_image_plane = data.Point(x, y, 0.0)
            ray_direction_vector = vector_math.difference_point(point_on_image_plane, eye_point)
            constructed_ray = data.Ray(eye_point, ray_direction_vector)
            pixel_color = cast_ray(constructed_ray, sphere_list, light, ambient, eye_point)
            #print('{:4d}{:4d}{:4d}'.format(min(int(pixel_color.r * 255), 255), min(int(pixel_color.g * 255), 255), min(int(pixel_color.b * 255), 255)), end='   ')
            image_file.write('{0:4d}{1:4d}{2:4d}'.format(min(int(pixel_color.r * 255), 255), min(int(pixel_color.g * 255), 255), min(int(pixel_color.b * 255), 255)))
            count += 1
            print("loop time " + str(count))
        image_file.write("\n")
        #print("loop time " + str(count))
    image_file.close()

"""
# image is generated by generating a ppm P3 image file with cast_all_rays function
# cast_all_rays function prints a ppm P3 format file
def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient, light = light_obj):

    num_of_pixel_x = (max_x - min_x) / float(width)
    num_of_pixel_y = (max_y - min_y) / float(height)

    print("P3")
    print(str(width), str(height))
    print("255")

    for row in range(height):
        y = max_y - row * num_of_pixel_y
        for col in range(width):
            x = min_x + col * num_of_pixel_x
            # z-coordinate is constant there for z = 0.0 for all point on image plane
            point_on_image_plane = data.Point(x, y, 0.0)
            ray_direction_vector = vector_math.difference_point(point_on_image_plane, eye_point)
            constructed_ray = data.Ray(eye_point, ray_direction_vector)
            pixel_color = cast_ray(constructed_ray, sphere_list, light, ambient, eye_point)
            print('{:4d}{:4d}{:4d}'.format(min(int(pixel_color.r * 255), 255), min(int(pixel_color.g * 255), 255), min(int(pixel_color.b * 255), 255)), end='   ')
        print()
"""