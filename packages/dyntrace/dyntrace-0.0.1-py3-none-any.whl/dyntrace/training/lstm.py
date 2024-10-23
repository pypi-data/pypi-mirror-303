# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:42:44 2023

@author: Issac
"""
import dyntrace.utility.csmip as Read_CSMIP_data
import pandas as pd
import numpy as np
import os
import random
import pickle
import time

from numpy.random import randn
from scipy.interpolate import interp1d
import scipy.stats as stats

import keras
import tensorflow as tf

# lstm autoencoder recreate sequence
from numpy import array
from keras import optimizers
from keras.models import *
from keras.layers import *
from keras.callbacks import *
from keras.utils.vis_utils import plot_model
from keras.activations import sigmoid
from keras.activations import relu
from keras import backend as K

import matplotlib.pyplot as plt
import pydot
import keras.utils.vis_utils as vis_utils
vis_utils.pydot = pydot

import seaborn as sn
from sklearn import svm
from sklearn.linear_model import *
from sklearn.neural_network import *
from sklearn.metrics import *
from sklearn.model_selection import *
from sklearn.utils import *
from sklearn.manifold import *
from scipy import io  

from scipy.io import loadmat

import warnings
warnings.filterwarnings("ignore")

def save_model_dict(dictionary, name, modelPath):   
    dictionary['model'].save(modelPath+r"model_response\\"+name+"_model.h5")
    f = open(modelPath+r"model_response\\"+name+"_history.pkl","wb")
    pickle.dump(dictionary['history'].history, f)
    f.close()
    f = open("runtime.txt", "a")
    f.write(name+" runtime: ")
    f.write(str(dictionary['runtime']/60))
    f.write("\n")
    f.close()
    
def load_model_dict(name, modelPath):
    dictionary = {}
    try:
        model = load_model(modelPath+r"model_response\\"+name+".hdf5")
    except:
        model = load_model(modelPath+r"model_response\\"+name+"_model.h5")
    dictionary['model'] = model
    f = open(modelPath+r"model_response\\"+name+"_history.pkl", 'rb')
    history = pickle.load(f)
    f.close()
    dictionary['history'] = history
    return dictionary

if __name__ == "__main__":
    
    #specify the train_folder_path
    #specify time step (each seismic event has different timesteps, so need to define manually)
    #specify output_response (e.g. Accel data in Channel 3, 5, 8 => then 3)
    #specify window size (stack size, please refer to Zhang2019 for details)
    train_folder_path = r'C:\Users\BRACE2\Desktop\CSMIP\data\training'
    time_step = 13000
    output_response = 3
    window_size = 1
    
    #CSMIP data is read into "train_file".
    train_file = Read_CSMIP_data.Read_CSMIP_data(train_folder_path, time_step, output_response, window_size)
    
    #The required 3d array will be generated for training
    datax, datay = train_file.generate_3d_array()
    
    _, n_step, featurex = datax.shape
    _, n_step, featurey = datay.shape
    
    print(featurex)
    print(featurey)
    
    print(n_step)
    
    n_unit = 30
    n_epoch = 10000
    min_lr = 1e-5 #1e-5
                
    inputs = Input(shape=(n_step, featurex))
    #print (inputs)
    outputs = TimeDistributed(Dense(featurey))(LSTM(n_unit, return_sequences=True)(inputs))
    print (outputs)
    
    model1 = Model(inputs=inputs, outputs=outputs)
    
    modelPath = r'C:\Users\BRACE2\Desktop\CSMIP\model\\'
    mcp_save = ModelCheckpoint(modelPath+ "vanilla_" +str(n_unit)+".hdf5", save_best_only=True, monitor='loss', mode='min')
    reduce_lr_loss = ReduceLROnPlateau(monitor='loss', factor=0.9, patience=500, verbose=1, mode='min', min_lr=min_lr) #1e-5 50
    early_stopping = EarlyStopping(monitor='loss', patience=5000, verbose=False, restore_best_weights=True) #2000
    
    #adam = optimizers.Adam(lr=1e-5)
    model1.compile(optimizer='adam', loss='mean_squared_error')
    starttime = time.time()
    # history = model1.fit(datax, datay, shuffle=True, epochs=n_epoch, verbose=1, callbacks=[mcp_save, reduce_lr_loss, early_stopping])
    
    history = model1.fit(datax, datay, shuffle=True, validation_split=0.2, epochs=n_epoch, verbose=1)
    
    runtime = time.time()-starttime
    
    dictionary = {}
    dictionary['model'] = model1
    dictionary['history'] = history
    dictionary['runtime'] = runtime
    save_model_dict(dictionary, "vanilla_"+str(n_unit)+"_addFC", modelPath)
