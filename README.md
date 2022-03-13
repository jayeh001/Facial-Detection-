# Facial Detection Machine Learning App #
## This is a project created by Team Constellation for SF Hacks 2021 ##

### Technologies Used: ###
- Python
- DeepFace
- OpenCV
- Jupyter Notebook and Google Colab
- FER2013 Dataset from Kaggle
- Flask

---

### Inspiration ###
Emotions are a difficult thing to pin down for most people. There is a reason why a big thing in therapy and mental health is guiding you through understanding your emotions because sometimes it can get so complex. 

---

### What this does ###
A user with a webcam can enter our app to provide us with a clear view of their face and providing live video footage of their reactions. Our app can instantly detect any facial changes in real time and provides feedback based on the current facial expression. Although this is in its rudimentary stage and only provides written feedback, we hope to be able to expand upon this in the future to provide possible guided meditations depending on mood or even suggest specific activities. 

---

### How it works ###
Our Python Flask back end ultilizes the Haar Cascades machine learning detection algorithm from OpenCV along with DeepFace to analyze facial expressions in real time. The user's webcam sends constant data to feed the algorithm and our web app can in turn return feedback confirmation that it has detected the user's current emotion. We used a react front end to provide a very simplistic user interface. 

---

### Challenges we had ###
Setting up the ML algorithm and the different dependencies was a struggle! We had one teammate who had constant crashes while trying to run the algorithm on his computer. Setting up the flask environment was also difficult because it was all of our first times ever using this framework and the documentation did not make it any easier. 

---

### What's next ###
This is in its rudimentary stage and only provides written feedback, we hope to be able to expand upon this in the future to provide possible guided meditations depending on mood or even suggest specific activities to help boost the user's mood. 
