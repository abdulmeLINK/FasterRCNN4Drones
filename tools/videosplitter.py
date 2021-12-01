import cv2
input_path = "E:\\tknfst\\ulasimdayapayzeka\\ornek.mp4"
cam = cv2.VideoCapture(input_path)
ret_val, img = cam.read()
c=0;
while ret_val:
    cv2.imwrite("images/frame%d.jpg" % c, img)     # save frame as JPEG file      
    ret_val,img = cam.read()
    c+=1