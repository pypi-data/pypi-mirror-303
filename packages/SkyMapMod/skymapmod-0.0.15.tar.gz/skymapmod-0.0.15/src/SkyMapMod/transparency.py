#для работы с прозрачностями атмосферы -- пересчет и тд
import numpy as np
from .zodiac import cos

#на вход подаем спектр и два угла, на выходе получаем другой спектр
def other_angle_transparency(initial_tr, initial_angle, angle):
    return initial_tr ** (cos(initial_angle) / cos(angle))