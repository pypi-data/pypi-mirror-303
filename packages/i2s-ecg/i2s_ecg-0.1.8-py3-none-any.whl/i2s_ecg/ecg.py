#ecg.py
# -*- coding:utf-8 -*-
from skimage.io import imread
from skimage import color
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu,gaussian
from skimage.transform import resize
from numpy import asarray
from skimage.metrics import structural_similarity
from skimage import measure
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import joblib
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import os
from natsort import natsorted
from sklearn import linear_model, tree, ensemble
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import re

# Define the project root directory
project_root = os.path.dirname(os.path.abspath(__file__))

# Define data, model, and output directories

data_dir = os.path.join(project_root, 'data')
models_dir = os.path.join(project_root, 'models')
outputs_dir = os.path.join(project_root, 'outputs')


# Ensure the output directory exists
# Ensure these directories exist, and create them if they do not
os.makedirs(data_dir, exist_ok=True)
os.makedirs(models_dir, exist_ok=True)
os.makedirs(outputs_dir, exist_ok=True)
os.makedirs(os.path.join(outputs_dir, 'figures'), exist_ok=True)
os.makedirs(os.path.join(outputs_dir, 'results'), exist_ok=True)

figures_dir=os.path.join(outputs_dir, 'figures')
#results_dir=os.path.join(outputs_dir,'results')

def crop_top_four_leads(image):
    """ Extract 2/3 of the image""" 
    height, width = image.shape[:2]
    crop_region = (0, 0, width, int(height * 2 / 3))
    cropped_image = image[crop_region[1]:crop_region[3], crop_region[0]:crop_region[2]]

    return cropped_image    

def divide_into_leads(image):
    """Split the picture into 12 short leads and 1 long lead"""
    leads = []#Creating a collection of leads
    lead_width = image.shape[1] // 4#Get the width of the image/4
    lead_height = image.shape[0] // 4#Get the height of the image/4
    #Divide out four rows, dividing each of the first three rows into four leads
    for i in range(3):
        for j in range(4):
            leads.append(image[i * lead_height:(i + 1) * lead_height, j * lead_width:(j + 1) * lead_width])
    #Divide out the last row and divide each column of the last row into 1 long lead
    leads.append(image[3 * lead_height:image.shape[0], :])

    return leads

# Graphing segmented data
def plot_segment(segment_df, filename):
    # Reading segmented data
    segment_data = pd.read_csv(filename)
    
    # Draw plots
    plt.figure()
    plt.plot(segment_data['X'], label='Segment Data')
    plt.gca().invert_yaxis()
    plt.title(f'Plot for {filename}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    
    # Save the plot
    save_filename = filename.replace('.csv', '.png')
    plt.savefig(save_filename)
    plt.show()
    print(f"Segment plot saved as {save_filename}")

def segment_data(filename):
    df = pd.read_csv(filename)
    match = re.search(r'Normalized_Scaled_X_\d+\.csv', filename)
    match=match.group()
    print(match)
    match=match.replace('.csv','')
    print(match)

    fig6, ax6 = plt.subplots()
    plt.gca().invert_yaxis()
    ax6.plot(df, linewidth=1, color='black', linestyle='solid')

    peaks, _ = find_peaks(-df['X'])
    local_minima = df.iloc[peaks]
    local_minima_sorted = local_minima.sort_values(by='X')
    top_four_indexes = local_minima_sorted.head(6).index.tolist()
    min_value = df['X'].min()
    local_minima_filtered = [index for index in top_four_indexes if df.at[index, 'X'] < (min_value +0.1)]
    sorted_indexes = sorted(local_minima_filtered)
    print("Top  local minima indexes (sorted and filtered):", sorted_indexes)
    if len(sorted_indexes)<=1:
        return
    for index in sorted_indexes:
        ax6.axvline(x=index, color='red', linestyle=':')

    l1 = sorted_indexes[0] if sorted_indexes else None
    l2 = sorted_indexes[1] if len(sorted_indexes) > 1 else None
    l3 = sorted_indexes[2] if len(sorted_indexes) > 2 else None
    r1 = sorted_indexes[3] if len(sorted_indexes)>3 else None
    r2 = sorted_indexes[4] if len(sorted_indexes)>4 else None
    r3 =sorted_indexes[5] if len(sorted_indexes)>5 else None


    dis=sorted_indexes[1]-sorted_indexes[0] if len(sorted_indexes)>1 else 0
    for index in sorted_indexes:
        ax6.axvline(x=index, color='red', linestyle='--')
        if index-dis//3+1>0:
            ax6.axvline(x=index-dis//3, color='blue', linestyle='--')

    save_filename = f'{figures_dir}/final_{match}.png'
    plt.savefig(save_filename)
    plt.show()
    print(f"Segment plot saved as {save_filename}")

    # **New Logic for Selecting the Segment**
    distances = []
    for i in range(len(sorted_indexes) - 1):
        distances.append(sorted_indexes[i+1] - (sorted_indexes[i] - dis / 3))

    # **Find the index of a pair with a moderately suitable distance**
    median_distance = pd.Series(distances).median()  # Calculate the median distance
    deviation = pd.Series(distances).std()  # Calculate the standard deviation
    
    # Find the index of a distance close to the median
    best_index = -1
    min_diff = float('inf')
    for i, d in enumerate(distances):
        diff = abs(d - median_distance)
        if diff < min_diff and diff < deviation * 1.5:  # Adjust the multiplier as needed
            min_diff = diff
            best_index = i
    
    if best_index == -1:
        print("No suitable distance found.")
        return

    # Define the segment based on the selected blue lines
    start_index = sorted_indexes[best_index] - dis / 3 + 1
    end_index = sorted_indexes[best_index + 1] - dis / 3
    
    segment_case = df.loc[start_index:end_index]
    segment_case_path = f'{figures_dir}/Normalized_Scaled_X_{i}_segment.csv'
    segment_case.to_csv(segment_case_path, index=False)

# Plot and save segment image
    plot_segment(segment_case, segment_case_path)


class ECG:
    def  getImage(self,image):
        """
        Function: Read picture
        Return: array of pictures
        """
        self.image = imread(image)
        return self.image
    
    def GrayImage(self):
        """
        Function: grayscale the picture
        Return : array of grayscaled images
        """
        self.gray_image = color.rgb2gray(self.image)
        return self.gray_image
    
    def DividingLeads(self):
        """
		Function: call the functions crop_top_four_leads() and divide_into_leads() to split the image into 12 short leads and 1 long lead
		Return : array of leads after dividing
		"""
        #Get leads
        self.image_resize=crop_top_four_leads(self.image)
        self.leads = divide_into_leads(self.image_resize)

        #Create an image window of the entire 12 short leads
        fig , ax = plt.subplots(4,3)
        fig.set_size_inches(10, 10)#Setting the whole window size
        x_counter=0
        y_counter=0
        #Create a subgraph of 12 leads and save the final image
        for x,y in enumerate(self.leads[:len(self.leads)-1]):
            if (x+1)%3==0:#Change line when every 3 leads
                ax[x_counter][y_counter].imshow(y)
                ax[x_counter][y_counter].axis('off')#Close Axis
                ax[x_counter][y_counter].set_title("leads {}".format(x+1))#Name the lead
                x_counter+=1
                y_counter=0
            else:
                ax[x_counter][y_counter].imshow(y)
                ax[x_counter][y_counter].axis('off')
                ax[x_counter][y_counter].set_title("leads {}".format(x+1))
                y_counter+=1
        fig.savefig(os.path.join(figures_dir, 'Leads_1-12_figure.jpg'))

        #Create a window with long leads and save the final image
        fig1 , ax1 = plt.subplots()
        fig1.set_size_inches(10, 10)
        ax1.imshow(self.leads[12])
        ax1.set_title("Leads 13")
        ax1.axis('off')
        fig1.savefig(os.path.join(figures_dir, 'Long_Lead_13_figure.jpg'))

        return self.leads
    
    def PreprocessingLeads(self):
        """
        Function: Preprocess the leads by converting to grayscale, applying Gaussian blur, and global thresholding for binarization.
        Return: array of preprocessed leads
        """
        # Create an image window for the entire 12 short leads
        fig2 , ax2 = plt.subplots(4,3)
        fig2.set_size_inches(10, 10)
        x_counter=0
        y_counter=0

        for x,y in enumerate(self.leads[:len(self.leads)-1]):
            grayscale = color.rgb2gray(y)# Grayscale conversion
            blurred_image = gaussian(grayscale, sigma=1)# Gaussian blur to smooth the image and reduce noise
            global_thresh = threshold_otsu(blurred_image)# Calculate global thresholding using Otsu's method
            binary_global = blurred_image < global_thresh# Binarize the image
			#resize image
            # binary_global = resize(binary_global, (300, 450))
            if (x+1)%3==0:
                ax2[x_counter][y_counter].imshow(binary_global,cmap="gray")
                ax2[x_counter][y_counter].axis('off')
                ax2[x_counter][y_counter].set_title("pre-processed Leads {} image".format(x+1))
                x_counter+=1
                y_counter=0
            else:
                ax2[x_counter][y_counter].imshow(binary_global,cmap="gray")
                ax2[x_counter][y_counter].axis('off')
                ax2[x_counter][y_counter].set_title("pre-processed Leads {} image".format(x+1))
                y_counter+=1
        fig2.savefig(os.path.join(figures_dir, 'Preprossed_Leads_1-12_figure.png'))

        # Create a window for the long lead and save the final image
        fig3 , ax3 = plt.subplots()
        fig3.set_size_inches(10, 10)
        grayscale = color.rgb2gray(self.leads[-1])
        blurred_image = gaussian(grayscale, sigma=1)
        global_thresh = threshold_otsu(blurred_image)
        print(global_thresh)
        binary_global = blurred_image < global_thresh
        ax3.imshow(binary_global,cmap='gray')
        ax3.set_title("Leads 13")
        ax3.axis('off')
        fig3.savefig(os.path.join(figures_dir, 'Preprossed_Leads_13_figure.png'))

    def SignalExtraction_Scaling(self):
        """
        Function: Detect contours, extract signals, and scale the signals.
        Return: array of 1D signals
        """
        fig4 , ax4 = plt.subplots(4,3)
		#fig4.set_size_inches(10, 10)
        x_counter=0
        y_counter=0
        for x,y in enumerate(self.leads[:len(self.leads)-1]):
            # Preprocessing
            grayscale = color.rgb2gray(y)
            blurred_image = gaussian(grayscale, sigma=0.7)
            global_thresh = threshold_otsu(blurred_image)
            binary_global = blurred_image < global_thresh
			# #resize image
            # binary_global = resize(binary_global, (300, 450))

			# Detect contours
            contours = measure.find_contours(binary_global,0.8)
            contours_shape = sorted([x.shape for x in contours])[::-1][0:1]# Sort by shape, select the largest contour
            for contour in contours:# Iterate through all contours and resize to (255, 2)
                if contour.shape in contours_shape:
                    test = resize(contour, (255, 2))
            if (x+1)%3==0:
                ax4[x_counter][y_counter].invert_yaxis()
                ax4[x_counter][y_counter].plot(test[:, 1], test[:, 0],linewidth=1,color='black')
                ax4[x_counter][y_counter].axis('image')
                ax4[x_counter][y_counter].set_title("Contour {} image".format(x+1))
                x_counter+=1
                y_counter=0
            else:
                ax4[x_counter][y_counter].invert_yaxis()
                ax4[x_counter][y_counter].plot(test[:, 1], test[:, 0],linewidth=1,color='black')
                ax4[x_counter][y_counter].axis('image')
                ax4[x_counter][y_counter].set_title("Contour {} image".format(x+1))
                y_counter+=1
        
        #Signal Extraction and Signal Scaling
            lead_no=x
            scaler = MinMaxScaler()# Normalization tool
            fit_transform_data = scaler.fit_transform(test)# Normalize the test data
            Normalized_Scaled=pd.DataFrame(fit_transform_data[:,0], columns = ['X'])# Convert the normalized data to a DataFrame
            Normalized_Scaled=Normalized_Scaled.T# Transpose
			#Save normalized data to CSV file
            csv_file_path = os.path.join(figures_dir, f'Scaled_1DLead_{lead_no+1}.csv')
            if os.path.isfile(csv_file_path):
                Normalized_Scaled.to_csv(csv_file_path, mode='a', index=False)
            else:
                Normalized_Scaled.to_csv(csv_file_path, index=False)
	      	# Save original data to CSV in a separate folder
		
        fig4.savefig(os.path.join(figures_dir, 'Contour_Leads_1-12_figure.png'))

    def Extractheart_period(self):
        """
        Function: Extraction of heartbeat cycles
        """
        for i in range(1, 13):
            print(i)
            filename = f'{figures_dir}/Scaled_1DLead_{i}.csv'
            print(filename)
            df1 = pd.read_csv(filename)
            df1_t = df1.T
            df1_t.columns = ['X']
            output_path = f'{figures_dir}/Normalized_Scaled_X_{i}.csv'
            df1_t.to_csv(output_path, index=False)
            segment_data(output_path)


    def CombineConvert1Dsignal(self):
        """
        Function: Combine 1D signals into one DataFrame
		"""
        test_final=pd.DataFrame()
        for i in range(1, 13):
            filename = f'{figures_dir}/Scaled_1DLead_{i}.csv'
            df1 = pd.read_csv(filename)
            test_final=pd.concat([test_final,df1],axis=1,ignore_index=True)
        if test_final.shape[0] > 1:
            test_final = test_final.iloc[[0]]

        return test_final    
    

    def DimensionalReduciton(self, test_final):
        """
        Function: Dimensional Reduction using PCA
        Return: array of 2D data after PCA
        """
        # Load the trained PCA model
        pca_loaded_model = joblib.load(os.path.join(data_dir, 'PCA_ECG.pkl'))
        result = pca_loaded_model.transform(test_final)
        final_df = pd.DataFrame(result)
        return final_df

    def ModelLoad_predict(self, final_df):
        # Load the prediction model
        current_dir = os.path.dirname(os.path.abspath(__file__))
        loaded_model = joblib.load(os.path.join(data_dir, 'Heart_Disease_Prediction_using_ECG.pkl'))
        # Use the model to make predictions and obtain probabilities
        probabilities = loaded_model.predict_proba(final_df)
        result = np.argmax(probabilities, axis=1)  # Obtain forecast categories
        # prediction categories and corresponding probabilities
        prediction = result[0]
        probability = probabilities[0][prediction]
        
        return prediction, probability