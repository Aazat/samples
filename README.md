# Guides/notes and scripts for using tensorflow for Data Preprocessing, Model Training etc

# [Data pipelines with tf.data](https://cs230.stanford.edu/blog/datapipeline/#best-practices) api
  ##  1. Loading and preprocessing images in tf.data
  ## Using [`tf.keras.utils.image_dataset_from_directory(directory=,labels= 'inferred', batch_size= 32, image_size= (256,256))  `](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory)
  
  ## Iterating data in tf.dataset
   ``` 
   for batch in dataset :  
          process_batch 
   ```
   or  
   ```
    for batch in dataset.take(1):
        process(batch)
   ```
   
   Which would be a tensor.
   Use tensor.numpy() to use numpy methods and processings.
            
## Standardizing images
  ### Using normalization layer
   ` normalization_layer = tf.keras.layers.Rescaling(1./255) `  
    Then      
    1. ` normalized_ds = ds.map(lambda x1,x2... : normalization_layer([x1,x2...]), remaining) `      
    2. Include normalization layer in model itself for better deployment.  

# [tf.data.Dataset.from_tensor_slices](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices)  
` from_tensor_slices(tensors, name=None) `  

## Usage Example  

  **# Slicing a 1-D tensor produces scalar tensor elements**
```
        dataset = tf.data.Dataset.from_tensor_slices([1,2,3])
        list(dataset.as_numpy_iterator()) 
```  
 **# Slicing a tuple of 1D tensors produce tuple elements containing scaler tensors**  
 ```
        dataset = tf.data.Dataset.from_tensor_slices(([1,2],[3,4],[5,6]))
 ```
   would produce `[(1,3,5), (2,4,6)]` instead of `[1,2], [3,4], [5,6]`  
