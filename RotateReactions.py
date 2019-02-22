# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:15:24 2019

@author: Till
"""

import numpy as np

def local2global(theta, Fx, Fy, Fz):
    
    theta_rad = theta * 180/np.pi
    
    FX = Fx
    FY = np.cos(theta_rad) * Fy - np.sin(theta_rad) * Fz
    FZ = np.cos(theta_rad) * Fz + np.sin(theta_rad) * Fy
    
    return FX, FY, FZ


def global2local(theta, FX, FY, FZ):
    
    theta_rad = theta * 180/np.pi
    
    Fx = FX
    Fy = np.cos(theta_rad) * FY + np.sin(theta) * FZ
    Fz = np.cos(theta_rad) * FZ + np.sin(theta) * FY
    
    return Fx, Fy, Fz
    
    