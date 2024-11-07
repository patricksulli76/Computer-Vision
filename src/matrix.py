
import math
def rotateObject(matrix,angle):
    newObject = []
    for [x,y] in matrix:
        nx = math.cos(angle)*x + math.sin(angle)*y
        ny = -1*math.sin(angle)*x + math.cos(angle)*y
        newObject.append([nx,ny])
    return newObject