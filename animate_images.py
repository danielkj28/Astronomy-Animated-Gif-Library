# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:24:00 2024

@author: Daniel
"""
import imageio
from os import listdir
from os.path import isfile, join

def main(name,chapter):
    images = []
    
    imagePath = 'D:/Graduate_Research/Animated_gif_library/gifs_chapter/chapter_' + str(chapter) + '/' + name + '/' + name + '_images/'
    fileNames = [f for f in listdir(imagePath) if isfile(join(imagePath, f))]
    
    gifPath = 'D:/Graduate_Research/Animated_gif_library/gifs_chapter/chapter_' + str(chapter) + '/' + name + '/' + name + '.gif'
    
    for fileName in fileNames:
        print(fileName)
        fileName = imagePath + fileName
        images.append(imageio.imread(fileName))
        imageio.mimsave(gifPath, images)