
# Importing TensorFlow and printing the version
import tensorflow as tf
print(f"TensorFlow version: {tf.__version__}")

# Importing necessary libraries for GUI and image processing
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
from tensorflow import keras

import numpy as np
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model

# Dictionary mapping class indices to traffic sign descriptions
classes={
    0:'Speed limit (20km/h)',
    1:'Speed limit (30km/h)',
    2:'Speed limit (50km/h)',
    3:'Speed limit (60km/h)',
    4:'Speed limit (70km/h)',
    5:'Speed limit (80km/h)',
    6:'End of speed limit (80km/h)',
    7:'Speed limit (100km/h)',
    8:'Speed limit (120km/h)',
    9:'No passing',
    10:'No passing veh over 3.5 tons',
    11:'Right-of-way at intersection',
    12:'Priority road',
    13:'Yield',
    14:'Stop',
    15:'No vehicles',
    16:'Veh >3.5 tons prohibited',
    17:'No entry',
    18:'General caution',
    19:'Dangerous curve left',
    20:'Dangerous curve right',
    21:'Double curve',
    22:'Bumpy road',
    23:'Slippery road',
    24:'Road narrows on the right',
    25:'Road work',
    26:'Traffic signals',
    27:'Pedestrians',
    28:'Children crossing',
    29:'Bicycles crossing',
    30:'Beware of ice/snow',
    31:'Wild animals crossing',
    32:'End speed + passing limits',
    33:'Turn right ahead',
    34:'Turn left ahead',
    35:'Ahead only',
    36:'Go straight or right',
    37:'Go straight or left',
    38:'Keep right',
    39:'Keep left',
    40:'Roundabout mandatory',
    41:'End of no passing',
    42:'End no passing veh >3.5 tons'
}

# Loading the pre-trained model
model = load_model('model (2).h5')

# Setting up the main Tkinter window
top = tk.Tk()
top.geometry('800x600')
top.title('Traffic Sign Detection')
top.configure(background='magenta')

# Label for displaying the prediction result
label = Label(top, background='white', font=('arial', 15, 'bold'), foreground='black')

# Label for displaying the uploaded image
sign_image = Label(top)

# Function to classify the uploaded image
def classify(file_path):
    global label_packed
    # Opening and resizing the image
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = np.array(image)  # Converting image to numpy array
    image = np.expand_dims(image, axis=0)  # Adding batch dimension
    print(image.shape)  # Debugging: print the shape of the image
    predictions = model.predict(image)  # Making predictions using the model
    predicted_class = np.argmax(predictions, axis=1)[0]  # Getting the predicted class index
    sign = classes[predicted_class]  # Mapping index to class label
    print(sign)  # Debugging: print the predicted sign
    label.configure(foreground='#011638', text=sign)  # Updating the label with the prediction

# Function to show the classify button after image upload
def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)  # Positioning the button

# Function to handle image upload
def upload_image():
    try:
        file_path = filedialog.askopenfilename()  # Opening file dialog to select image
        uploaded = Image.open(file_path)  # Opening the uploaded image
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))  # Resizing image for display
        im = ImageTk.PhotoImage(uploaded)  # Converting image to PhotoImage for Tkinter
        sign_image.configure(image=im)  # Updating image label with the uploaded image
        sign_image.image = im  # Keeping a reference to the image
        label.configure(text='')  # Clearing the label text
        show_classify_button(file_path)  # Showing the classify button
    except:
        pass  # Handling exceptions silently (consider improving this)

# Button for uploading an image
upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='black', font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)  # Positioning the upload button

# Packing the image label and prediction label
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)

# Heading label for the application
heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='black')
heading.pack()

# Example image loading (for display purposes)
image_path = '22bf2613-d2a8-43d0-b342-e3d6d536926d.jpg'  
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)  # Creating a PhotoImage object
image_label = tk.Label(top, image=photo)  # Creating a label for the image
image_label.pack(pady=10)  # Adding the image label to the window

# Starting the Tkinter main loop
top.mainloop()
