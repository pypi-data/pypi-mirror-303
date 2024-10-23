
import tensorflow as tf
import keras

# ---> Define custom layer to transform probabilities (logits) into respective labels
@keras.saving.register_keras_serializable()
class ProbToLabel(tf.keras.layers.Layer):
    def __init__(self, i_cl_map=None, **kwargs):
        super().__init__(**kwargs)
        # Class index map (dictionary mapping index to respective class)
        self.i_cl_map = i_cl_map if i_cl_map is not None else {}

    # Method for returning a function that returns the class name associated with the
    # respective class index
    def i_cl_map_func(self, i_cl):
        return lambda: tf.constant(self.i_cl_map[i_cl], dtype=tf.string)

    def call(self, inputs):
        # Tensor of indices of the classes with the highest probabilities
        i_cl = tf.argmax(inputs, axis=-1)
        # Tensow with the respective labels
        # [NOTE: a SymbolicTensor cannot be used a dictionary key, hence the method used
        # below for the mapping from index to label.]
        y = tf.map_fn(
            # Element-wise function to apply
            fn=lambda i_cl_i: 
                tf.case(
                    # List of tuple pairs (case's condition and respective function to
                    # return when condition holds true)
                    pred_fn_pairs=[
                        (tf.equal(i_cl_i, tf.constant(i_cl_j, dtype=tf.int64)),
                         self.i_cl_map_func(i_cl_j))
                        for i_cl_j in self.i_cl_map.keys()
                    ],
                ),
            # Elements (the tensor of indices)
            elems=i_cl,
            # Element output type
            fn_output_signature=tf.string
        )
        return y

    # Method for getting configuration dictionary of the model
    def get_config(self):
        # Get configuration from parent class
        config = super().get_config()
        # Convert i_cl_map attribute's keys to strings for JSON compatibility
        config.update({"i_cl_map": 
            {str(key):value for (key, value) in self.i_cl_map.items()}
        })
        return config
    
    # Class method for using a configuration that ensures the keys of the i_cl_map
    # attribute to be integers when loading from file  
    @classmethod
    def from_config(cls, config):
        # Get i_cl_map attribute from configuration dictionary
        i_cl_map = config.pop("i_cl_map", {})
        # Convert i_cl_map keys to integers
        i_cl_map = {int(key): value for (key, value) in i_cl_map.items()}
        # Return layer object with the updated i_cl_map attribute
        return cls(i_cl_map=i_cl_map, **config)
