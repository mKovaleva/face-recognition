#   You can get the trained model file from:
#   http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2.

import dlib

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()





