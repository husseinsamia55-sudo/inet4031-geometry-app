import math
import sphere

def test_sphere_volume_1():
    assert round(sphere.volume(1), 3) == round((4/3) * math.pi * 1**3, 3)

def test_sphere_volume_2():
    assert round(sphere.volume(2), 3) == round((4/3) * math.pi * 8, 3)

def test_sphere_volume_3():
    assert round(sphere.volume(3), 3) == round((4/3) * math.pi * 27, 3)
