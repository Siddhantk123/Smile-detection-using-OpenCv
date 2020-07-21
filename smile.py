import cv2, time
#time is added to add some time sleep
#cv2 is the open cv image and video processing python library


#to load our haarcascade for face detection and smile, we use
#cascade classifier
#load...
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")

#till here we have imported our packages and loaded our haarcascade.

#Now, lets call our video capture function to record the frame from WEBCAM
video=cv2.VideoCapture(0)
#we are writing here 0 to capture photos from our web cam
#if we have a wifi cam ten we can write doen the ip address of WIFI CAM.
'''
a video is a slide show of picture.
so lets run a loop through all the captured image and 
fullfill our need. or that we are running infinite loop
in while loop what we will be doing
1.in each slide show we will be checking that the picture o face is present 
in the slide show or not

'''
while True:
    check,frame= video.read()
    #Converting coloured image into black and white image(gray)
    #featured image in black and white is more accurate than the coloured images
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    '''
    now we will do the comparision of gray image wite the
    face_cascade image.face cascade already contains different kind
    of human face hence the comarison will give out accurate result

    first we will do face recognition and inside face recognition 
    we will do smile recognition.
    '''
    #comparision
    face= face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
         #scale factor will act as a zoom inorder to do the clear
         #comparision
    #Now, the output of face will be four values-X axix,Y axis, width and
    # height(x,y,w,h)
    #face is gray image here
    #rectangle face
    for x,y,w,h in face:
        #we will create rectangle on the original frame
        #frame variable which is coloured
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        #0,225,0 is a BGR color
        #3 is width od rectangele
        #Now lets do the same things for smile so copy and paste the
        #code inside this face
        #comparision for smile
        smile= smile_cascade.detectMultiScale(gray,scaleFactor=1.9,minNeighbors=20)
        #drawing rectangle for smile
        for x,y,w,h in smile:
            img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    #let dispaly. we will use cv2.imshow() method GUI
    cv2.imshow('Smile detection',frame) #create GUI SECOND parametr is the image that has to be desplayed
    key=cv2.waitKey(1) #key variable used to exit the GUI
    #defining the condition in which the GUI will be exited
    if key==ord('q'):
        break
#At the end we would want to stop our video or release it
    

video.release()
cv2.destroyAllwindows
            





          






