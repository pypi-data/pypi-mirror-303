# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:42:44 2023

@author: Issac
"""
import Read_CSMIP_data 
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
from sklearn.preprocessing import MinMaxScaler

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
    time_step = 30000
    output_response = 5
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
    
    s_kernel = 10
    n_filter = 20
    n_epoch = 10000
    min_lr = 1e-5
    max_dilation = 512
    
    inputs = Input(shape=(n_step, featurex), name='inputs')
    dilation = 1
    outputs = Reshape((1, n_step, featurex))(inputs) #1*n_step*n_unit
    
    while (dilation <= max_dilation):
        outputs = Conv2D(filters=n_filter, kernel_size=(s_kernel, featurex), dilation_rate=(dilation, 1), padding='same', data_format="channels_first")(outputs)  
        dilation *= 2
        #print(K.int_shape(outputs))
    outputs = Permute((2,1,3))(outputs) #(n_step-s_kernel+1)*n_filter*featurex
    #print(K.int_shape(outputs))
    outputs = Reshape((n_step, n_filter*featurex))(outputs) #(n_step-s_kernel+1)*n_filter
    print(K.int_shape(outputs))
    outputs = TimeDistributed(Dense(featurey))(outputs)
    
    model7 = Model(inputs=inputs, outputs=outputs)
    
    modelPath = r'C:\Users\BRACE2\Desktop\CSMIP\model\\'
    mcp_save = ModelCheckpoint(modelPath + "tcn" + str(s_kernel)+"_"+str(n_filter)+"_"+str(max_dilation)+".hdf5", save_best_only=True, monitor='loss', mode='min')
    reduce_lr_loss = ReduceLROnPlateau(monitor='loss', factor=0.9, patience=500, verbose=1, mode='min', min_lr=min_lr) #1e-5 50
    early_stopping = EarlyStopping(monitor='loss', patience=20000, verbose=False, restore_best_weights=True)

    #adam = optimizers.Adam(lr=1e-5)
    model7.compile(optimizer='adam', loss='mean_squared_error')
    starttime = time.time()
    history = model7.fit(datax, datay, shuffle=True, epochs=n_epoch, verbose=1, callbacks=[mcp_save, reduce_lr_loss, early_stopping]) # validation_split=0.2
    runtime = time.time()-starttime

    
    dictionary = {}
    dictionary['model'] = model7
    dictionary['history'] = history
    dictionary['runtime'] = runtime
    save_model_dict(dictionary, "tcn"+str(s_kernel)+"_"+str(n_filter)+"_"+str(max_dilation), modelPath)
    
    