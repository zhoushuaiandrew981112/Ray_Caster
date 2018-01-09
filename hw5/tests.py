from data import *
from vector_math import *
from cast import *
from collisions import *
import unittest
from math import *

class TestData(unittest.TestCase):

    def test_Point_assignment(self):
        pt_a = Point(1, 2, 3)
        self.assertEqual(pt_a.x, 1)
        self.assertEqual(pt_a.y, 2)
        self.assertEqual(pt_a.z, 3)

    def test_Point_eq_function(self):
        pt_a = Point(1.1, 2.2, 3.3)
        self.assertEqual(pt_a, Point(1.1, 2.2, 3.3))

    def test_Vector_assignment(self):
        vec_a = Vector(4, 5, 6)
        self.assertEqual(vec_a.x, 4)
        self.assertEqual(vec_a.y, 5)
        self.assertEqual(vec_a.z, 6)

    def test_Vector_eq_function(self):
        vec_a = Vector(4.4, 5.5, 6.6)
        self.assertEqual(vec_a, Vector(4.4, 5.5, 6.6))

    def test_Ray_case_assignment(self):
        pt_a = Point(7, 8, 9)
        vec_a = Vector(10, 11, 12)
        ray_a = Ray(pt_a, vec_a)

        self.assertEqual(ray_a.pt, pt_a)
        self.assertEqual(ray_a.dir, vec_a)

    def test_Ray_eq_function(self):
        pt = Point(7.7, 8.8, 9.9)
        vec = Vector(10.10, 11.11, 12.12)
        ray = Ray(pt, vec)

        self.assertEqual(ray.pt, Point(7.7, 8.8, 9.9))
        self.assertEqual(ray.dir, Vector(10.10, 11.11, 12.12))

    def test_scale_vector(self):
        vec_a = Vector(1, 1, 1)
        self.assertTrue(scale_vector(vec_a, 3) == Vector(3, 3, 3))

    def test_dot_vector(self):
        vec_a = Vector(1, 1, 1)
        vec_b = Vector(2, 2, 2)
        self.assertTrue(dot_vector(vec_a, vec_b) == 6)

    def test_length_vector(self):
        vec_b = Vector(2, 2, 2)
        self.assertAlmostEqual(length_vector(vec_b), 3.4641016151377544)

    def test_normalize_vector(self):
        vec_c = Vector(5, 3, 4)
        self.assertTrue(normalize_vector(vec_c) == Vector(0.7071067811865475, 0.4242640687119285, 0.565685424949238))

    def test_difference_point(self):
        pt_a = Point(5, 4, 3)
        pt_b = Point(7, 8, 9)
        self.assertTrue(difference_point(pt_a, pt_b) == Vector(-2, -4, -6))

    def test_difference_vector(self):
        vec_b = Vector(2, 2, 2)
        vec_c = Vector(5, 3, 4)
        self.assertTrue(difference_vector(vec_b, vec_c) == Vector(-3, -1, -2))

    def test_translate_point(self):
        vec_c = Vector(5, 3, 4)
        pt_a = Point(5, 4, 3)
        self.assertTrue(translate_point(pt_a, vec_c) == Vector(10, 7, 7))

    def test_vector_from_to(self):
        pt_a = Point(5, 4, 3)
        pt_b = Point(7, 8, 9)
        self.assertTrue(vector_from_to(pt_a, pt_b) == Vector(2, 4, 6))

    def test_sphere_intersection_point(self):
        ray_pt_1 = Point(0, 0, 0)
        ray_dir_1 = Vector(1, 0, 0)
        sphere_center_1 = Point(0, 0, 0)
        sphere_radius_1 = 10
        self.assertTrue(sphere_intersection_point(Ray(ray_pt_1, ray_dir_1), Sphere(sphere_center_1, sphere_radius_1)) == Point(10, 0, 0))

        ray_pt_2 = Point(20,0,0)
        ray_dir_2 = Vector(0,1,0)
        sphere_center_2 = Point(0,0,0)
        sphere_radius_2 = 10
        self.assertTrue(sphere_intersection_point(Ray(ray_pt_2, ray_dir_2), Sphere(sphere_center_2, sphere_radius_2)) is None)

        ray_pt_3 = Point(0, 0, 0)
        ray_dir_3 = Vector(1, 2, 3)
        sphere_center_3 = Point(0, 0, 0)
        sphere_radius_3 = 10
        self.assertTrue(sphere_intersection_point(Ray(ray_pt_3, ray_dir_3), Sphere(sphere_center_3, sphere_radius_3)) == Point(2.672612419124244, 5.345224838248488, 8.017837257372733))

    def test_find_intersection_points(self):
        sphere_center_1 = Point(10, 0, 0)
        sphere_radius_1 = 50
        s_1 = Sphere(sphere_center_1, sphere_radius_1)

        sphere_center_2 = Point(0, 10, 0)
        sphere_radius_2 = 50
        s_2 = Sphere(sphere_center_2, sphere_radius_2)

        sphere_center_3 = Point(0, 0, 10)
        sphere_radius_3 = 50
        s_3 = Sphere(sphere_center_3, sphere_radius_3)

        ray_pt_a = Point(0, 0, 0)
        ray_dir_a = Vector(10, 10, 10)
        r_a = Ray(ray_pt_a, ray_dir_a)

        s_list = [s_1, s_2, s_3]
        n_s_list = find_intersection_points(s_list, r_a)
        self.assertTrue(n_s_list == [(s_1, Point(31.8133458177251, 31.8133458177251, 31.8133458177251)), (s_2, Point(31.8133458177251, 31.8133458177251, 31.8133458177251)), (s_3, Point(31.8133458177251, 31.8133458177251, 31.8133458177251))])

    def test_sphere_normal_at_point_1(self):
        point_sphere = Point(0.0, 0.0, 0.0)
        sphere = Sphere(point_sphere, 1.0)
        point = Point(-1.0, 0.0, 0.0)
        normal = sphere_normal_at_point(sphere, point)
        self.assertEqual(normal, Vector(-1.0, 0.0, 0.0))

    def test_sphere_normal_at_point_2(self):
        point_sphere = Point(0.0, 0.0, 0.0)
        sphere = Sphere(point_sphere, 1.0)
        point = Point(1.0, 0.0, 0.0)
        normal = sphere_normal_at_point(sphere, point)
        self.assertAlmostEqual(normal.x, 1.0)
        self.assertAlmostEqual(normal.y, 0.0)
        self.assertAlmostEqual(normal.z, 0.0)

    def test_finish(self):
        finish = Finish()
        self.assertAlmostEqual(finish.ambient, 1.0)
        self.assertAlmostEqual(finish.diffuse, 0.0)

    def test_light(self):
        light = Light(Point(-50.0, 50.0, -50.0), Color(3.0, 3.0, 3.0))
        self.assertAlmostEqual(light.pt.x, -50.0)
        self.assertAlmostEqual(light.pt.y, 50.0)
        self.assertAlmostEqual(light.pt.z, -50.0)
        self.assertAlmostEqual(light.color.r, 3.0)
        self.assertAlmostEqual(light.color.g, 3.0)
        self.assertAlmostEqual(light.color.b, 3.0)

if __name__ == '__main__':
    unittest.main()
