# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:57:23 2023

@author: Issac
"""
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from scipy.signal import resample
from scipy.signal import butter, filtfilt, sosfilt
import matplotlib.pyplot as plt

class Read_CSMIP_data():
    def __init__(self, filePath, time_step, output_response, window_size):

        self.CSMIP_folder_path = filePath
        self.time_step = time_step
        self.output_response = output_response
        self.window_size = window_size

    def split_by_n(self, seq, n):
        while seq:
            yield seq[:n]
            seq = seq[n:]

    def read_response(self, fileName):
        with open(fileName, 'r') as file:
            Lines = file.readlines()
            for index, item in enumerate(Lines):
                if ("Accelerogram points" in item):
                    accel_index = index
                elif ("End of Data" in item):
                    end_index = index

            accel_lines = Lines[accel_index + 1: end_index]


            num_char = 9

            accel_data = []
            for item in accel_lines:
                data =  list(self.split_by_n(item, num_char))
                for datum in data:
                    if len(datum) == num_char:
                        accel_data.append(datum)


            return accel_data

    def Generate_data(self, X_data0, y_data0, window_size=50):
        X_new_temp = []
        y_new_temp = []
        for ii in range(len(X_data0)):
            X_temp = X_data0[ii]
            y_temp = y_data0[ii]
            X_new = []
            y_new = []
            for jj in range(int(np.floor(len(X_temp) / window_size))):
                X_new.append(X_temp[jj * window_size:(jj + 1) * window_size])
                y_new.append(y_temp[(jj + 1) * window_size - 1, :])
                # y_new.append(y_temp[(jj + 1) * window_size - 1])

            X_new_temp.append(np.array(X_new))
            y_new_temp.append(np.array(y_new))

        X_data_new0 = np.array(X_new_temp)
        y_data_new0 = np.array(y_new_temp)

        return X_data_new0, y_data_new0

    def butter_highpass_filter_1D(self, time_series_array, cutoff_freq, sampling_freq):

        nyquist_freq = 0.5 * sampling_freq
        normalized_cutoff = cutoff_freq / nyquist_freq

        # Set up Butterworth filter
        b, a = butter(2, normalized_cutoff, btype='highpass')
        # sos = butter(2, cutoff_freq, btype='highpass',  fs=sampling_freq, output='sos')

        # Apply filter to time series array
        filtered_array = filtfilt(b, a, time_series_array)


        return filtered_array
    def butter_lowpass_filter_1D(self, time_series_array, cutoff_freq, sampling_freq):

        nyquist_freq = 0.5 * sampling_freq
        normalized_cutoff = cutoff_freq / nyquist_freq

        # Set up Butterworth filter
        b, a = butter(2, normalized_cutoff, btype='lowpass')
        # sos = butter(2, cutoff_freq, btype='highpass',  fs=sampling_freq, output='sos')

        # Apply filter to time series array
        filtered_array = filtfilt(b, a, time_series_array)
        return filtered_array

    def resample_1d_array(self, array, original_freq, target_freq):
        """
        Resample a 1D numpy array from a given frequency to a target frequency using linear interpolation.

        Parameters:
        array (numpy.ndarray): The 1D numpy array to resample.
        original_freq (float): The original frequency of the array.
        target_freq (float): The target frequency to resample the array to.

        Returns:
        numpy.ndarray: The resampled array.
        """
        time_stamps = np.arange(len(array)) / original_freq
        target_time_stamps = np.arange(0, time_stamps[-1], 1/target_freq)
        return np.interp(target_time_stamps, time_stamps, array)

    def generate_3d_array(self):

        accel_channel_comb = np.zeros((1, self.time_step, 1))
        accel_GM_comb = np.zeros((1, self.time_step, self.output_response))

        files = os.listdir(self.CSMIP_folder_path )

        for index, file_name in enumerate(files):
            channels_path = self.CSMIP_folder_path + r'\\'+ file_name
            channels_files = os.listdir(channels_path )

            for item in channels_files:
                channel_fileName = channels_path + r'\\' + item
                accel_output = np.array(self.read_response(channel_fileName),dtype=float) 
                # accel_output = self.butter_highpass_filter_1D(accel_output, 0.1, 200)
                # accel_output = self.butter_lowpass_filter_1D(accel_output, 20, 200)

                # Resample the data if the time step is much less than the specified time step
                #Plot the graph for comparison (original Vs Resampled Data)
                #Focus on the few training/testing sets first, so 9000
                # time_step = len(accel_output)
                new_time_step = int(accel_output.shape[0] * (100/200))
                accel_output = resample(accel_output, new_time_step)
                # accel_output = self.resample_1d_array(accel_output, 200, 100)
                    # old_x = np.arange(len(accel_output))
                    # new_x = np.linspace(0, len(accel_output)-1, self.time_step)
                    # accel_output = np.interp(new_x, old_x, accel_output)
                    # displ_output = np.interp(new_x, old_x, displ_output)
                    # Plot the original and resampled lists
                    # plt.plot(old_x, accel_output, 'b-', label='Original List')
                    # plt.plot(new_x, accel_output_resample, 'r--', label='Resampled List')
                    # plt.legend()
                    # plt.show()
                    # accel_output = accel_output_resample


                # Pad zero terms at the end of the array if the time step is less than self.timestep
                time_step = len(accel_output)
                accel_output = np.pad(accel_output, (0, self.time_step - time_step),mode='constant')
                # time_step = len(displ_output)
                # displ_output = np.pad(displ_output, (0, self.time_step - time_step),mode='constant')

                accel_output = np.reshape(accel_output, [1 , self.time_step, 1]) 
                # accel_output = self.butter_highpass_filter(accel_output, 0.1, 100)
                accel_channel_comb = np.append(accel_channel_comb,accel_output,axis=2)

            accel_channel_comb = accel_channel_comb[:,:,1:]  
            accel_GM_comb = np.append(accel_GM_comb,accel_channel_comb,axis=0)
            accel_channel_comb = np.zeros((1, self.time_step, 1))

        accel_GM_comb = accel_GM_comb[1:,:,:]  

        X_data = accel_GM_comb[:,:,0]
        y_data = accel_GM_comb[:,:,1:]

        X_data = np.reshape(X_data, [X_data.shape[0], X_data.shape[1], 1])

        # Scale data
        # X_data_flatten = np.reshape(X_data, [X_data.shape[0]*X_data.shape[1], 1])
        # scaler_X = MinMaxScaler(feature_range=(-1, 1))
        # scaler_X.fit(X_data_flatten)
        # X_data_flatten_map = scaler_X.transform(X_data_flatten)
        # X_data_map = np.reshape(X_data_flatten_map, [X_data.shape[0], X_data.shape[1], 1])

        # y_data_flatten = np.reshape(y_data, [y_data.shape[0]*y_data.shape[1], y_data.shape[2]])
        # scaler_y = MinMaxScaler(feature_range=(-1, 1))
        # scaler_y.fit(y_data_flatten)
        # y_data_flatten_map = scaler_y.transform(y_data_flatten)
        # y_data_map = np.reshape(y_data_flatten_map, [y_data.shape[0], y_data.shape[1], y_data.shape[2]])

        # Normalize data
        # X_data_normalized = tf.keras.utils.normalize(X_data, axis=1)
        # y_data_normalized = tf.keras.utils.normalize(y_data, axis=1)
        X_data_new, y_data_new = self.Generate_data(X_data, y_data, self.window_size)

        X_data_new = np.reshape(X_data_new, [X_data_new.shape[0], X_data_new.shape[1], X_data_new.shape[2]])

        return X_data_new , y_data_new
#if __name__ == "__main__":


