The app developed by the user leverages a Flask API and integrates a ResNet CNN model, alongside EasyOCR powered by an LLM. It processes package items and fresh produce, focusing on identifying the freshness of fruits and vegetables. The model has been trained on 3,000 images, with ten specific categories: fresh (apples, cucumber, oranges, potato, tomato) and rotten (apples, cucumber, oranges, potato, tomato).

By analyzing the input data through image classification and optical character recognition, the app generates an executive summary of the detected freshness status of the produce. This solution is highly relevant for quality control in grocery and packaging industries, where detecting fresh and rotten items efficiently can streamline operations and reduce waste.

dataset link-https://www.kaggle.com/datasets/muhriddinmuxiddinov/fruits-and-vegetables-dataset
ml model-https://drive.google.com/drive/folders/1lTeg3DNfFV_YdI5nGxLITDLXeGt8zDiH?usp=sharing

how to use
1 - install requriments
2 - get model weights from drive and save in dir
3 - get gemini api and update it 
