# 4.测试人脸目录
import os, glob, numpy, json
from skimage import io
import dlib

     
def find_face(file):
    dlibdatdir= 'D:/360Downloads/ide/dlib-19.6'
    rootdir = r'E:\xsq\test\PycharmProjects\face-rec'
    rtdir = rootdir.replace('\\', '/')
    os.chdir(rtdir)
    with open("classier.json", "r", encoding='utf-8') as f:
        classier = json.load(f)
    f.close()
    os.chdir(dlibdatdir)
    # 1.人脸关键点检测器
    predictor_path = 'shape_predictor_68_face_landmarks.dat'
    # 2.人脸识别模型
    face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
    # 1.加载正脸检测器
    detector = dlib.get_frontal_face_detector()
    # 2.加载人脸关键点检测器
    sp = dlib.shape_predictor(predictor_path)
    # 3. 加载人脸识别模型
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)
    # 3. 加载人脸识别模型
    # 测试过程
    # print(glob.glob(os.path.join(img_path, "*.jpg")))
    img = io.imread(file)
    dets = detector(img, 1)
    dist = []
    for k, d in enumerate(dets):
       shape = sp(img, d)
       face_descriptor = facerec.compute_face_descriptor(img, shape)
       d_test = numpy.array(face_descriptor)
       # 计算欧式距离
       for i in [x[1] for x in classier]:
            dist_ = numpy.linalg.norm(i-d_test)
            dist.append(dist_)
    c_d = dict(zip([x[0] for x in classier], dist))
    cd_sorted = sorted(c_d.items(), key=lambda d:d[1])
    if len(cd_sorted)>0 and cd_sorted[0][1]<0.8:
        print("\t%s : 与标准样本的距离为%f\t%s"%(cd_sorted[0][0], cd_sorted[0][1], file))
        if cd_sorted[0][1]<0.4:
            dlib.hit_enter_to_continue()
        return cd_sorted[0][0]
    else:
        print("\t%s : %s"%('该图片无法完成人脸识别或人物颜值过低', file))
        return '无法识别'


def find_face_cap(img):
    dlibdatdir= 'D:/360Downloads/ide/dlib-19.6'
    rootdir = r'E:\xsq\test\PycharmProjects\face-rec'
    rtdir = rootdir.replace('\\', '/')
    os.chdir(rtdir)
    with open("classier.json", "r", encoding='utf-8') as f:
        classier = json.load(f)
    f.close()
    os.chdir(dlibdatdir)
    # 1.人脸关键点检测器
    predictor_path = 'shape_predictor_68_face_landmarks.dat'
    # 2.人脸识别模型
    face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
    # 1.加载正脸检测器
    detector = dlib.get_frontal_face_detector()
    # 2.加载人脸关键点检测器
    sp = dlib.shape_predictor(predictor_path)
    # 3. 加载人脸识别模型
    facerec = dlib.face_recognition_model_v1(face_rec_model_path)
    # 3. 加载人脸识别模型
    # 测试过程
    # print(glob.glob(os.path.join(img_path, "*.jpg")))
    # img = io.imread(file)
    dets = detector(img, 1)
    dist = []
    for k, d in enumerate(dets):
       shape = sp(img, d)
       face_descriptor = facerec.compute_face_descriptor(img, shape)
       d_test = numpy.array(face_descriptor)
       # 计算欧式距离
       for i in [x[1] for x in classier]:
            dist_ = numpy.linalg.norm(i-d_test)
            dist.append(dist_)
    c_d = dict(zip([x[0] for x in classier], dist))
    cd_sorted = sorted(c_d.items(), key=lambda d:d[1])
    if len(cd_sorted)>0 and cd_sorted[0][1]<0.8:
        print("\t%s : 与标准样本的距离为%f\t"%(cd_sorted[0][0], cd_sorted[0][1]))
        # if cd_sorted[0][1]<0.4:
        #     dlib.hit_enter_to_continue()
        return cd_sorted[0][0]
    else:
        print("\t%s "%('该图片无法完成人脸识别或人物颜值过低'))
        return '无法识别'
