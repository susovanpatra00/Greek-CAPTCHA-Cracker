import cv2
import numpy as np
import pickle

classes = {0:'ALPHA', 1:'BETA', 2:'CHI', 3:'DELTA',4:'EPSILON', 5:'ETA', 6:'GAMMA', 7:'IOTA',8:'KAPPA', 9:'LAMDA', 10:'MU',11:'NU',12:'OMEGA', 13:'OMICRON', 14:'PHI',15:'PI',16:'PSI',17:'RHO',18:'SIGMA',19:'TAU',20:'THETA',21:'UPSILON',22:'XI',23:'ZETA'}

def bgremove3(myimage):
    # BG Remover 3
    myimage_hsv = cv2.cvtColor(myimage, cv2.COLOR_BGR2HSV)
     
    #Take S and remove any value that is less than half
    s = myimage_hsv[:,:,1]
    s = np.where(s < 127, 0, 1) # Any value below 127 will be excluded
 
 
    # Combine our two masks based on S and V into a single "Foreground"
    foreground = np.where(s > 0, 1, 0).astype(np.uint8)  #Casting back into 8bit integer
 
    background = np.where(foreground==0,255,0).astype(np.uint8) # Invert foreground to get background in uint8
    background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)  # Convert background back into BGR space
    foreground=cv2.bitwise_and(myimage,myimage,mask=foreground) # Apply our foreground map to original image
    finalimage = background+foreground # Combine foreground and background
 
    return finalimage
def bgremove4(myimage):
    # BG Remover 3
    myimage_hsv = cv2.cvtColor(myimage, cv2.COLOR_BGR2HSV)
    # We increase the brightness of the image and then mod by 255
    v = myimage_hsv[:,:,2] 
    v = np.where(v > 170, 0, 1)  # Any value above 127 will be part of our mask
 
    # Combine our two masks based on S and V into a single "Foreground"
    foreground = np.where(v > 0, 1, 0).astype(np.uint8)  #Casting back into 8bit integer
 
    background = np.where(foreground==0,255,0).astype(np.uint8) # Invert foreground to get background in uint8
    background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)  # Convert background back into BGR space
    foreground=cv2.bitwise_and(myimage,myimage,mask=foreground) # Apply our foreground map to original image
    finalimage = background+foreground # Combine foreground and background
 
    return finalimage




# DO NOT CHANGE THE NAME OF THIS METHOD OR ITS INPUT OUTPUT BEHAVIOR

# INPUT CONVENTION
# filenames: a list of strings containing filenames of images

# OUTPUT CONVENTION
# The method must return a list of strings. Make sure that the length of the list is the same as
# the number of filenames that were given. The evaluation code may give unexpected results if
# this convention is not followed.
final = []
def decaptcha( filenames ):

	labels = []
	# The use of a model file is just for sake of illustration
	image = [ cv2.imread(filenames[i]) for i in range( len(filenames) ) ]	
	hsvImage =[ cv2.cvtColor(image[i], cv2.COLOR_BGR2HSV) for i in range(len(filenames))]
	np.array(final)
	# print(type(final))
	final1 = []
	c = 0
	# bgremove3(image)
	npzModel = pickle.load(open("model.npz", 'rb'))
	for i in range(len(filenames)):
			a = bgremove3(image[i])
			y = bgremove4(a)
			grayImage = cv2.cvtColor(y, cv2.COLOR_BGR2GRAY)
			thresh = 128
			img_binary = cv2.threshold(grayImage, thresh, 255, cv2.THRESH_BINARY)[1]
			final1.append(img_binary)
			z = np.average(img_binary,axis=0)
			markup_pt = []
			for p in range(500):
				if(z[p] < 255 and z[p-1] == 255 and p!= 0):
					markup_pt.append(p)
				if(p!= 0 and z[p-1] < 255 and z[p] == 255):
					markup_pt.append(p)
			# print(">>>>>>>>>>.",markup_pt,i)
			char1 = np.array(img_binary[0:150,markup_pt[0]:markup_pt[1]])
			char2 = np.array(img_binary[0:150,markup_pt[2]:markup_pt[3]])
			char3 = np.array(img_binary[0:150,markup_pt[4]:markup_pt[5]])
			res1 = cv2.resize(char1, dsize=(25, 25), interpolation=cv2.INTER_CUBIC).flatten()
			res2 = cv2.resize(char2, dsize=(25, 25), interpolation=cv2.INTER_CUBIC).flatten()
			res3 = cv2.resize(char3, dsize=(25, 25), interpolation=cv2.INTER_CUBIC).flatten()
			final.append(res1)
			final.append(res2)
			final.append(res3)
	
	prediction = []
	temp = []
	counter  = 0
	yPred = npzModel.predict(final)
	for i in yPred:
		prediction.append(classes[i])
		counter +=1
		if(counter ==3):
			counter =0
			my_string = ','.join(prediction)
			labels.append(my_string)
			prediction = []
	# print(labels)

	return labels