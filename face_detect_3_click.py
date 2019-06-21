
# coding: utf-8

# In[1]:



import cv2
# loading  face trained  data
facehaar=cv2.CascadeClassifier('face.xml')
#eyeshaar=cv2.CascadeClassifier('haarcascade_eye.xml')
#-*smilehaar=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
cap=cv2.VideoCapture(0)


# image read  #  plz operate all operation in  gray scale
#virat_img=cv2.imread('virat.jpg')
#print(virat_img.shape)
while(cap.isOpened()):
    status,frame=cap.read()
#  face detector  apply in  virat_img--scalling  range 
    face_only=facehaar.detectMultiScale(frame,1.15,5)
   # eyes_only=eyeshaar.detectMultiScale(frame,1.15,5)
    
    # print(eyes_only)
    for  x,y,w,h in  face_only:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
   # for ex,ey,ew,eh in eyes_only:
    #    cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('face_detect',frame)
    if len(face_only) > 3:
        cv2.imwrite("pic.jpg",frame)
        print("photo clicked")
    if cv2.waitKey(10) & 0xff==ord('q'):
        break


#  its normal display 
#cv2.imshow('all',virat_img)
#cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()


# In[ ]:




