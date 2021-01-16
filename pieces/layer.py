import numpy as np
import cv2

class Layer(object): 
       
    # Constructor 
    def __init__(self, parent, sentences): 
        self.parent = parent           # Another layer that this layer is within, or None for outermost ring.
        self.sentences = sentences     # Gets filled with Sentence objects

    def draw(self):
        pass
   
