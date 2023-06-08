import dlib,numpy
import cv2
# 人脸关键点检测器
predictor_path = "shape_predictor_68_face_landmarks.dat"
# 人脸识别模型、提取特征值
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
# 加载模型
detector = dlib.get_frontal_face_detector() #人脸检测
sp = dlib.shape_predictor(predictor_path) #关键点检测
facerec = dlib.face_recognition_model_v1(face_rec_model_path)# 编码
image_path='train_images/11.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 人脸检测
dets = detector(image, 1)
if len(dets)==1:
    print('检测到人脸')
shape = sp(image, dets[0])# 关键点
# 提取特征
face_descriptor = facerec.compute_face_descriptor(image, shape)#获取到128位的编码
v = numpy.array(face_descriptor)
print(v)
