import sys,os,dlib,glob,numpy
from skimage import io
import json
# if len(sys.argv) != 5:
#     print "请检查参数是否正确"
#     exit()
rootdir = os.getcwd()
dlibdatdir= 'D:/360Downloads/ide/dlib-19.6'

os.chdir(dlibdatdir)
# 1.人脸关键点检测器
predictor_path = 'shape_predictor_68_face_landmarks.dat'
# 2.人脸识别模型
face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
# 3.样本人脸目录
faces_folder_path = 'd:/Pictures/beauty/face'
# 4.测试人脸目录
windowsimg_path = r'd:\Pictures\beauty'
img_path = windowsimg_path.replace('\\', '/')
# print(img_path)
# img_path = 'd:/Pictures/beauty/129724774_15086755267801n.jpg'
# img_path = 'd:/Pictures/beauty/耀天公主'
# img_path = 'd:/Pictures/beauty'
# 1.加载正脸检测器
detector = dlib.get_frontal_face_detector()
# 2.加载人脸关键点检测器
sp = dlib.shape_predictor(predictor_path)
# 3. 加载人脸识别模型
facerec = dlib.face_recognition_model_v1(face_rec_model_path)
# win = dlib.image_window()
# 候选人脸描述子list
classier = {}
descriptors = []
# candidate = ['chun','chun','ting','mm']
candidate = []
os.chdir(faces_folder_path)
for f in glob.glob("*.jpg"):
   # print("Processing file: {}".format(f))
   img = io.imread(f)
   #win.clear_overlay()
   #win.set_image(img)
   # 1.人脸检测
   dets = detector(img, 1)
   # print("Number of faces detected: {}".format(len(dets)))# 2.关键点检测
   for k, d in enumerate(dets):
       shape = sp(img, d)
       face_descriptor = facerec.compute_face_descriptor(img, shape)
       # 转换为numpy array
       v = numpy.array(face_descriptor).tolist()
       descriptors.append(v)
       name = "".join([a for a in f.split(".")[0] if a.isalpha()])
       candidate.append(name)
classier = dict(zip(candidate, descriptors))
os.chdir(rootdir)
with open("classier.json","w",encoding='utf-8') as f:
    json.dump(classier, f, ensure_ascii=False)
# 测试过程
# print(glob.glob(os.path.join(img_path, "*.jpg")))
os.chdir(img_path)
for f in glob.glob("*.jpg"):
    dlib.hit_enter_to_continue()
    img = io.imread(f)
    dets = detector(img, 1)
    dist = []
    for k, d in enumerate(dets):
       shape = sp(img, d)
       face_descriptor = facerec.compute_face_descriptor(img, shape)
       d_test = numpy.array(face_descriptor)
       # 计算欧式距离
       for i in descriptors:
            dist_ = numpy.linalg.norm(i-d_test)
            dist.append(dist_)
    c_d = dict(zip(candidate,dist))
    cd_sorted = sorted(c_d.items(), key=lambda d:d[1])
    if len(cd_sorted)>0 and cd_sorted[0][1]<0.8:
        print("\t%s : 与标准样本的距离为%f\t%s"%(cd_sorted[0][0], cd_sorted[0][1], '/'.join([img_path,f])))
    else:
        print("\t%s : %s"%('该图片无法完成人脸识别或人物颜值过低', '/'.join([img_path, f])))
