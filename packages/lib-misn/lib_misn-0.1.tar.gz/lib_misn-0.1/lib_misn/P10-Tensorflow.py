import tensorflow as tf 
import numpy as np  
from tensorflow.keras.preprocessing.sequence import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences 

# Step 1: Prepare a dataset of labeled emails (spam and non-spam) 
emails = [ "Buy cheap watches! Free shipping!", "Meeting for lunch today?", "Claim your prize! You've won $1,000,000!", "Important meeting at 3 PM.", ] 
labels = [1, 0, 1, 0]

# Step 2: Tokenize and pad the email text data 
max_words = 1000 
max_len = 50

tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>") 
tokenizer.fit_on_texts(emails) 
sequences = tokenizer.texts_to_sequences(emails) 
X_padded = pad_sequences(sequences, maxlen=max_len, padding="post", truncating="post") 

# Step 3: Define the neural network model 
model = tf.keras.Sequential([ tf.keras.layers.Embedding(input_dim=max_words, output_dim=16, input_length=max_len), tf.keras.layers.Flatten(), tf.keras.layers.Dense(16, activation='relu'), tf.keras.layers.Dense(1, activation='sigmoid') ]) 

# Compile the model 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 4: Define training data and labels as NumPy arrays 
# # This is where you convert your training data and labels to NumPy arrays. # For this example, we will use the same data as 'emails' and 'labels'. 
training_data = np.array(X_padded) 
training_labels = np.array(labels) 

# Step 5: Train the model 
model.fit(training_data, training_labels, epochs=10) # You can adjust the number of epochs 

# Step 6: Test if 'Spam.txt' is spam or not 
file_path = "Spam.txt" 
# Read the content of the 'Spam.txt' file 
with open(file_path, "r", encoding="utf-8") as file: sample_email_text = file.read() 

# Tokenize and pad the sample email text 
sequences_sample = tokenizer.texts_to_sequences([sample_email_text]) 
sample_email_padded = pad_sequences(sequences_sample, maxlen=max_len, padding="post", truncating="post") 

# Use the trained model to make predictions 
prediction = model.predict(sample_email_padded) 

# Set a classification threshold (e.g., 0.5) 
threshold = 0.5 

# Classify the sample email based on the threshold 
if prediction > threshold: 
    print(f"Sample Email ('{file_path}'): SPAM")
else:
    print(f"Sample Email ('{file_path}'): NOT SPAM")