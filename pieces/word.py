import numpy as np
import cv2
from sentence import Sentence

class Word(object): 
       
    # Constructor 
    def __init__(self, parent, characters): 
        if not isinstance(parent, Sentence):
            print('Parent of a word should be a sentence!!')
            raise TypeError
        self.parent = parent            # The sentence that this word is within
        self.chars = characters         # Gets filled with Character objects

    def draw(self):
        pass
   
