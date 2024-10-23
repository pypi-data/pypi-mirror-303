# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:56:13 2023

@author: issaa
"""
import dyntrace.utility.csmip as Read_CSMIP_data
import pandas as pd
import pickle
import keras
import tensorflow as tf
import scipy.stats as stats

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
    
    #specify the train_folder_path and the test_folder_path
    #specify time step (each seismic event has different timesteps, so need to define manually)
    #specify output_response (e.g. Accel data in Channel 3, 5, 8 => then 3)
    #specify window size (stack size, please refer to Zhang2019 for details)
    train_folder_path = r'C:\Users\BRACE2\Desktop\CSMIP\data\training'
    test_folder_path = r'C:\Users\BRACE2\Desktop\CSMIP\data\testing'

    time_step = 7200
    output_response = 3
    window_size = 2
    
    #CSMIP data is read into "train_file" and "test_file".
    train_file = Read_CSMIP_data.Read_CSMIP_data(train_folder_path, time_step, output_response, window_size)
    test_file = Read_CSMIP_data.Read_CSMIP_data(test_folder_path, time_step, output_response, window_size)

    #The required 3d array will be generated for training/testing
    datax, datay = train_file.generate_3d_array()
    testx, testy = test_file.generate_3d_array()
    
    #load the trained model
    modelPath = r'C:\Users\BRACE2\Desktop\CSMIP\model\\'
    model_dict = load_model_dict("vanilla_30_addFC", modelPath)
    model = model_dict['model']
    
    #perform prediction and load the results in datapredict and testpredict
    datapredict = model.predict(datax)
    testpredict = model.predict(testx)
    print("train_loss:")
    print(model.evaluate(datax, datay, verbose=0))  
    print("test_loss:")
    print(model.evaluate(testx, testy, verbose=0))  
    
    #Sample Plot of training data
    plt.figure()
    plt.plot(model.predict(datax)[3,:,0], color='blue', lw=1.0)
    plt.plot(datay[3,:,0],':', color='red', alpha=0.8, lw=1.0)
    plt.title('Training Set: 3rd Floor Acceleration (x-direction)')
    plt.legend(["Predicted", "Real"])
    plt.xlabel("Time Step")
    plt.ylabel("Acceleration (cm/sec$^2$)")

    plt.figure()
    plt.plot(model.predict(datax)[3,:,1], color='blue',lw=1.0)
    plt.plot(datay[3,:,1],':', color='red', alpha=0.8, lw=1.0)
    plt.title('Training Set: Roof Acceleration (x-direction)')
    plt.legend(["Predicted", "Real"])
    plt.xlabel("Time Step")
    plt.ylabel("Acceleration (cm/sec$^2$)")
    
    #Sample Plot of testing data
    plt.figure()
    plt.plot(model.predict(testx)[3,:,0], color='blue', lw=1.0)
    plt.plot(testy[3,:,1],':', color='red', alpha=0.8, lw=1.0)
    plt.title('Testing Set: 3rd Floor Acceleration (x-direction)')
    plt.legend(["Predicted", "Real"])
    plt.xlabel("Time Step")
    plt.ylabel("Acceleration (cm/sec$^2$)")

    plt.figure()
    plt.plot(model.predict(testx)[3,:,1], color='blue',lw=1.0)
    plt.plot(testy[3,:,0],':', color='red', alpha=0.8, lw=1.0)
    plt.title('Testing Set: Roof Acceleration (x-direction)')
    plt.legend(["Predicted", "Real"])
    plt.xlabel("Time Step")
    plt.ylabel("Acceleration (cm/sec$^2$)")
    
    # Correlation Coefficient
    # Note: The resulting matrix from np.corrcoef shows this by having 1.0 
    # in both diagonal elements, indicating that each array is perfectly correlated
    # with itself, and < 1.0 in the off-diagonal elements, indicating that how the two arrays 
    # are correlated with each other.
    print("training corr")
    train_corr = np.corrcoef(datapredict.flatten(), datay.flatten())[0,1]
    print(train_corr)
    print("testing corr")
    test_corr = np.corrcoef(testpredict.flatten(), testy.flatten())[0,1]
    print(test_corr)
    
    
    # Error - evaluate the error between the predicted result and the real result
    errors = np.array([])

    x = (datapredict[:,:,0] - datay[:,:,0]) / np.max(np.abs(datay[:,:,0]), axis=1).reshape((-1,1))
    hist = np.histogram(x.flatten(), np.arange(-0.2, 0.201, 0.001))[0]
    errors = np.append(errors, hist)
    x = (datapredict[:,:,1] - datay[:,:,1]) / np.max(np.abs(datay[:,:,1]), axis=1).reshape((-1,1))
    hist = np.histogram(x.flatten(), np.arange(-0.2, 0.201, 0.001))[0]
    errors = np.append(errors, hist)
    x = (testpredict[:,:,0] - testy[:,:,0]) / np.max(np.abs(testy[:,:,0]), axis=1).reshape((-1,1))
    hist = np.histogram(x.flatten(), np.arange(-0.2, 0.201, 0.001))[0]
    errors = np.append(errors, hist)
    x = (testpredict[:,:,1] - testy[:,:,1]) / np.max(np.abs(testy[:,:,1]), axis=1).reshape((-1,1))
    hist = np.histogram(x.flatten(), np.arange(-0.2, 0.201, 0.001))[0]
    errors = np.append(errors, hist)
    
    errors = errors.reshape((-1, 4, 400))
    np.save("errors_new.npy", errors)   
    error = np.load("errors_new.npy")
    
    print(error.shape)
    
    # Print the error graph, a better result will lead to an error curve centralized to 0.
    plt.figure()
    plt.plot(np.arange(-20, 20, 0.1), error[0][0] / (np.sum(error[0][0]) * 0.001))
    plt.plot(np.arange(-20, 20, 0.1), error[0][1] / (np.sum(error[0][1]) * 0.001))
    plt.legend(["Third floor", "Roof"])
    plt.xlim(-20,20)
    plt.xlabel("Normalized Error (%)")
    plt.ylabel("PDF")
    plt.title('Training Set')

    plt.figure()
    plt.plot(np.arange(-20, 20, 0.1), error[0][2] / (np.sum(error[0][2]) * 0.001))
    plt.plot(np.arange(-20, 20, 0.1), error[0][3] / (np.sum(error[0][3]) * 0.001))
    plt.legend(["Third floor", "Roof"])
    plt.xlim(-20,20)
    plt.xlabel("Normalized Error (%)")
    plt.ylabel("PDF")
    plt.title('Testing Set')
    
    
    
    
    
    
    
    
    
