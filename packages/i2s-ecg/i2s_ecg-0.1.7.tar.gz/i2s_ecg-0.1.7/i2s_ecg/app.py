# app.py
# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image
from streamlit_cropper import st_cropper
from ecg import ECG
import numpy as np
from ecg import figures_dir
import os
import shutil

ecg = ECG()#create ecg
st.title("Heartbeat cycles Extracting and Numerical signal transformation of ECG Image")
st.markdown("help to make heartbeat cycles extracting and numerical signal transformation of ECG Image:sunglasses:")
# upload ECG image
uploaded_file = st.file_uploader("please choose the ECG image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # If a new image is uploaded, reset session state variables
    if 'uploaded_file' not in st.session_state or st.session_state['uploaded_file'] != uploaded_file:
        if os.path.exists(figures_dir):
            shutil.rmtree(figures_dir)  # Delete the folder and its contents.
        os.makedirs(figures_dir)  #recreate figures_dir
        st.session_state['rotation_angle'] = 0
        st.session_state['crop_done'] = False
        st.session_state['edited_image'] = None
        st.session_state['uploaded_file'] = uploaded_file
    
    image = Image.open(uploaded_file)

    # Rotate and crop image
    if not st.session_state['crop_done']:
        st.write("Rotate the image")
        rotate_angle = st.selectbox("Rotate Angle", [-180, -90, 0, 90, 180], index=2)
        st.session_state['rotation_angle'] = rotate_angle
        rotated_img = image.rotate(st.session_state['rotation_angle'], expand=True)
        st.image(rotated_img, caption='Rotated Image', use_column_width=True)

        with st.expander("Edit Image", expanded=True):
            st.write("Crop and Rotate Image")
            aspect_ratio = (16, 9)
            box_color = st.color_picker("Box Color", "#0000FF")

            # Cropping
            cropped_img = st_cropper(rotated_img, realtime_update=True, box_color=box_color, aspect_ratio=aspect_ratio)
            st.write("Cropped Image")
            st.image(cropped_img, use_column_width=True)
            # Save cropped image to disk
            if st.button("Save and Close"):
                # Adjust image size
                cropped_img.thumbnail((1024, 1024), Image.LANCZOS)
                # Save cropped image to disk
                
                st.session_state['edited_image'] = cropped_img
                st.session_state['crop_done'] = True
                #st.experimental_rerun()
                st.rerun()
                cropped_img.save(os.path.join(figures_dir, "cropped_image.jpg"))
    else:
        st.write("Edited Image (Resized to 1024x1024)")
        st.image(st.session_state['edited_image'], use_column_width=True)
        # Save cropped image to disk
        cropped_img = st.session_state['edited_image']
        cropped_img.save(os.path.join(figures_dir, "cropped_image.jpg"))

    if cropped_img is not None:
        """Download ECG image"""
        ecg_user_image = ecg.getImage(os.path.join(figures_dir, "cropped_image.jpg"))
        # display ECG image
        st.image(ecg_user_image)

        """Divide Leads"""
        # Call the Divide leads method
        dividing_leads = ecg.DividingLeads()
        my_expander1 = st.expander(label='DIVIDING LEAD')
        with my_expander1:
            st.image(os.path.join(figures_dir, 'Leads_1-12_figure.jpg'))
            st.image(os.path.join(figures_dir, 'Long_Lead_13_figure.jpg'))

        """Lead Pre-processing"""
        ecg_preprocessed_leads = ecg.PreprocessingLeads()

        my_expander2 = st.expander(label='PREPROCESSED LEAD')
        with my_expander2:
            st.image(os.path.join(figures_dir, 'Preprossed_Leads_1-12_figure.png'))
            st.image(os.path.join(figures_dir, 'Preprossed_Leads_13_figure.png'))
        
        """Numerical Conversion (1-12)"""
        # Call the signal extraction method
        ec_signal_extraction = ecg.SignalExtraction_Scaling()
        my_expander3 = st.expander(label='CONTOUR LEADS')
        with my_expander3:
            st.image(os.path.join(figures_dir, 'Contour_Leads_1-12_figure.png'))
        
        """Extract Heartbeat Cycle"""
        # Call the heart beat detection method
        ecg_heart_beat = ecg.Extractheart_period()
        my_expander4 = st.expander(label='HEARTBEAT CYCLES EXTRACTING')
        with my_expander4:
            st.image(os.path.join(figures_dir, 'final_Normalized_Scaled_X_2.png'))
            st.image(os.path.join(figures_dir, 'Normalized_Scaled_X_2_segment.png'))
        

        """Convert to 1D Signal"""
        # Call the combine and convert to 1D signal method
        ecg_1dsignal = ecg.CombineConvert1Dsignal()
        my_expander5 = st.expander(label='1D Signals')
        with my_expander5:
            st.write(ecg_1dsignal)
        
        """Data Downgrading"""
        # Call the dimensionality reduction function
        ecg_final = ecg.DimensionalReduciton(ecg_1dsignal)
        my_expander6 = st.expander(label='Dimensional Reduction')
        with my_expander6:
            st.write(ecg_final)
        
        """Prediction"""
        # Call the pretrained ML model for prediction
        ecg_model ,ecg_probability = ecg.ModelLoad_predict(ecg_final)
        my_expander7 = st.expander(label='PREDICTION')
        with my_expander7:
            if ecg_model == 0:
                st.write("Your ECG corresponds to Abnormal Heartbeat\n")
            elif ecg_model == 1:
                st.write("Your ECG corresponds to Myocardial Infarction\n")
            elif ecg_model == 2:
                st.write("Your ECG is Normal\n")
            else:
                st.write("Your ECG corresponds to History of Myocardial Infarction\n") 
            st.write(f"Prediction Probability: {ecg_probability:.2%}")