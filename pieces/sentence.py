import numpy as np
import cv2
from layer import Layer

class Sentence(object): 
       
    # Constructor 
    def __init__(self, parent, words): 
        if not isinstance(parent, Layer):
            print('Parent of a sentence should be a layer!!')
            raise TypeError
        self.parent = parent           # The layer that this sentence is within
        self.words = words             # Gets filled with Word objects

    def draw(self):
        pass
   
