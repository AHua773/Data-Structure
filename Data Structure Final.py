
from typing import List
from collections import namedtuple
import time
import numpy as np
from operator import itemgetter


# Create a 2D point at x, y,Return a string representation of this Point,to get the properties of the point.
class Point(namedtuple("Point", "x y")):
#Return a string representation of this Point
    def __repr__(self) -> str:
        return f'Point{tuple(self)!r}'

#Create a rectangle with the lowest(Bottom left) and highest(Top right) points of a given rectangle,return a string representation of this rectangle and determined if the points within the rectangular area.
class Rectangle(namedtuple("Rectangle", "lower upper")):
#Return a string representation of this rectangle
    def __repr__(self) -> str:
        return f'Rectangle{tuple(self)!r}'
#Returns the points within the rectangular area
    def is_contains(self, p: Point) -> bool:
        return self.lower.x <= p.x <= self.upper.x and self.lower.y <= p.y <= self.upper.y

#Create a Node class and get the various properties of Node
class Node(namedtuple("Node", "location left right")):
    """
    location: Point
    left: Node
    right: Node
    """

    def __repr__(self):
        return f'{tuple(self)!r}'

#Create the KDTree class.
class KDTree:
    """k-d tree"""
#Initialization, storage root node
    def __init__(self):
        self._root = None
        self._n = 0

class KDTree:
    """k-d tree"""

    def __init__(self):
        self._root = None
        self._lengh = 0
    
    def insert(self, p: List[Point]):
        node= Node(location=None, left=None, right=None,)#Build the node
        if not List[Point]:#Checks if the given list is empty
            return None
        else:
            if self.root==None:#If there is no root node, follow the steps to create a new KD tree
                axis = self._lengh % 2    #k=2,The axis of the sort is the remainder of Lengh divided by K
                p.sort(key=itemgetter(axis))   # Sort point list by axis and choose median as pivot element
                median = len(p) // 2  #Calculate the median and generate the root
                self.root==p[median]
                
                node.location=p[median],   #Using the median as the boundary, divide the left and right trees, and generate subtrees by analogy with this method
               
                node.left=KDTree(p[:median], self._lengh + 1),
                node.right=KDTree(p[median + 1 :],self._lengh + 1)
                return  node
            else:
                for point in p:
                    axis = self._lengh % 2
                    def isLeftTreeNode(self, point): #First, define the functions for the left and right subtrees
                        return point.aixs < self.point.aixs #By selected axis, the row is smaller than on the left and greater than on the right
    
                    def isRightTreeNode(self, point):
                        return point.aixs > self.point.aixs
                    
                    if point==self.root: #Skip if the inserted value already exists
                        pass

                    if not self.leftTree and self.rightTree:  #If only the right subtree exists
                        if self.isLeftTreeNode(point):   #If the insertion point is smaller than the root node, it is replaced with the root node, and the original root node becomes the right subtree
                            node.right=self.root,
                            node.location=point,
                            self.root=point
                        else:
                            node.left=point
                        return

                    if not self.rightTree and self.leftTree:   #Only the left subtree is the same as above
                        if self.isRightTreeNode(point):
                            node.left=self.root,
                            node.location=point,
                            self.root=point
                        else:
                            node.right=point
                        return
                    
                    else:   #If there are trees on both sides of the corresponding root node, the size is proportional by axis to root node
                        if self.isRightTreeNode(point):
                            node.right=point
                        else:
                            node.left=point
                        return
                    
            self_lengh+=1  #The left and right subtrees call themselves recursively
            node.left=left
            node.right=right


    def range(self, rectangle: Rectangle) -> List[Point]:
        result=[]
        for x in List[Point]:   #Take the point loop sequentially from the given set, and if it meets the is_contains, it means that it is within the rectangular extent, and added to the result list
        for x in List[Point]:   
	        if rectangle.is_contains(self,x) is True:
		        result.append(x)		    
		   
			   
        return result	
   












                 


            
     

          
        
