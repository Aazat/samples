# Guides/notes and scripts for using tensorflow for Data Preprocessing, Model Training etc

# Data pipelines with tf.data api
1. Loading and preprocessing images in tf.data
  ## Using [`tf.keras.utils.image_dataset_from_directory(directory=,labels= 'inferred', batch_size= 32, image_size= (256,256),  `](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory)
  
  ## Iterating data in tf.dataset
   ``` 
   for batch in dataset :  
          process_batch 
   ```
   Which would be a tensor.
   Use tensor.numpy() to use numpy methods and processings.
            
## Standardizing images
  ### Using normalization layer
   ` normalization_layer = tf.keras.layers.Rescaling(1./255) `  
   
    Then      
    1. ` normalized_ds = ds.map(lambda x1,x2... : normalization_layer([x1,x2...]), remaining) `      
    2. Include normalization layer in model itself for better deployment
    
