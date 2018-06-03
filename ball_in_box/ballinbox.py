import math
import random
import numpy
import validate as val

__all__ = ['ball_in_box']

def divideArea(L):
   #将正方形区域分成很多个点，放入点列表中
   #divide the area
    points=numpy.linspace(-1,1,150)
    for x in points:
        for y in points:
            L.append((x,y))
    return L
  

def calDistance(center,blockOrCircle):
    return math.sqrt((center[0]-blockOrCircle[0])**2+(center[1]-blockOrCircle[1])**2)


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """
    allPointsList=divideArea(L=[])
    circlesList=[]

    #依次找符合条件的最大圆.
    
    for i in range(0,m):
        maxCircle=[0,0,0]
        for point in allPointsList:
            unsureRadium=min(map(abs,[point[0]-1,point[0]+1,point[1]-1,point[1]+1]))
            for block in blockers:
                unsureRadium=min(unsureRadium,calDistance(point,block))
            for circle in circlesList:
                unsureRadium=min(unsureRadium,calDistance(point,circle)-circle[2])
            if  unsureRadium > maxCircle[2]:
                maxCircle[0]=point[0]
                maxCircle[1]=point[1]
                maxCircle[2]=unsureRadium

        circlesList.append(maxCircle)   
        allPointsList = list(filter(lambda p: calDistance(p,maxCircle) > maxCircle[2] , allPointsList))       

    return circlesList