from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np

class FreshRotton():

    def detect(self,path):

        tf.config.threading.set_intra_op_parallelism_threads(8)
        tf.config.threading.set_inter_op_parallelism_threads(8)
        model = load_model('frcd.h5')

        img_path = path
        img = image.load_img(img_path, target_size=(240, 240))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # Make predictions
        predictions = model.predict(img_array)
        pind = np.argmax(predictions, axis=1)[0]  

        # Map the predicted index to the class name
        list=['freshapples', 'freshbanana', 'freshcucumber', 'freshokra', 'freshoranges', 'freshpotato', 'freshtomato', 'rottenapples', 'rottenbanana', 'rottencucumber', 'rottenokra', 'rottenoranges', 'rottenpotato', 'rottentomato']
        return list[pind]
