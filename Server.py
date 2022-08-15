import flask
from flask import render_template
import werkzeug
import time
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import itertools
from rules import *
import numba as nb
from flask import send_file
import sys
nam1="abc"
#global nam2
nam2="nj"

def mainfunc(img,rul):
    h,w,c=img.shape
    iar=np.asarray(img)
    li5=[]
    for i in range(h):
        li4=[]
        for j in range(w):
            li3=[]
            for k in range(c):

                b=list(format(iar[i][j][k],'b').zfill(8))
                li3.append([int(q) for q in b] )
            li4.append(li3)
        li5.append(li4)
   # import itertools
    def XOR(x,y,z):
        if x!=z:
            return 1
        else:
            return 0

    def NOT(x):
        if x == 1:
            return 0
        else:
            return 1

    def R90(p,q,r): #Working
        return XOR(p,q,r)

    def R102(p,q,r): #Working
        return XOR(p,q,r)

    def R153(p,q,r):
        return NOT(q)*NOT(r) + q*r

    def R254(p,q,r):
        return 1 - (1 - p)*(1 - q)*(1 - r)

    def R250(p,q,r):
        return p + r - p * r


    def R30(p,q,r): #Working
        return (p + q + r + q * r)% 2

    def R110(p,q,r):
        return ((1 + p) * q * r + q + r)

    def R130(p,q,r):
        return NOT(p)*NOT(q)*r + p*q*r

    def R156(p,q,r):
        return NOT(p)*q + p*q*r + p*NOT(q)*NOT(r)

    def R51(p,q,r):
        a = NOT(q)
        return a

   # from rules import *
   # import numba as nb

    def HashFunC(L,time,RV):
        j = 0
        IV1 = L[:]
        IV2 = []
        x = 0
        RV = False
        Rec = False
        IV = L[:]
        for j in range(1,time):
            if Rec == True:
                return j-1,IV
                break
            x = 0
            IV2.clear()
            for i in IV:
                if x == 0:
                    a = 0
                    b = i
                    c = IV[x+1]
                    IV2.append(R90(a,b,c))
                    x = x+1
                else:
                    if x == 7:
                        a = IV[x-1]
                        b = i
                        c = 0
                   
                        if RV == False:
                        
                            IV2.append(R90(a,b,c))
                        else:
                       
                            IV2.append(R30(a,b,c))
                  
                        if IV2 == IV1:
                        
                        
                            Rec = True
                            IV = IV2[:]
                            break
                        IV = IV2[:]
                        break
                    else:
                        a = IV[x-1]
                        b = i
                        c = IV[x+1]
                    
                        if RV == False:
                       
                            IV2.append(R90(a,b,c))
                        else:

                            if x == 1:
                            
                                IV2.append(R30(a,b,c))
                            elif x == 2:
                            
                                IV2.append(R90(a,b,c))
                            elif x == 3:
                            
                                IV2.append(R30(a,b,c))
                            elif x == 4:
                            
                                IV2.append(R90(a,b,c))
                            elif x == 5:
                            
                                IV2.append(R30(a,b,c))
                            elif x == 6:
                            
                                IV2.append(R90(a,b,c))

                        x = x+1
        return j,IV
    list1=[]
    for i in range(h):
        list2=[]
        for j in range(w):
            list3=[]
            for k in range(c):
         
                list3.append(int("".join(str(x) for x in (HashFunC(li5[i][j][k],rul,False))[1]), 2))
            list2.append(list3)
        list1.append(list2)



    return np.asarray(list1)
    #nam2=nam1+"Encrypt.jpeg"

    #cv2.imwrite(nam2, abc)
    
app = flask.Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        nam1="lastuploaded.jpeg"
        imagefile.save(nam1)
        img=cv2.imread(nam1)
        abc=mainfunc(img,10)
        #nam2=nam1+"Encrypt.jpeg"
        cv2.imwrite("lastEncrypted.jpeg",abc)
        image_num = image_num + 1
    print("\n")
    return "Image(s) Uploaded Successfully. Come Back Soon."


@app.route("/showencrypted")
def showencrypted():
    #print(os.getcwd())
    message = "lastEncrypted.jpeg"
    return send_file(message, mimetype='image/jpeg')

@app.route("/showdecrypted")
def showdecrypted():
    #print(os.getcwd())
    message = "lastuploaded.jpeg"
    return send_file(message, mimetype='image/jpeg')

@app.route("/decrypt")
def decrypt():
    print("\nNumber of Received Images : 1", file=sys.stdout)
    im=cv2.imread("lastEncrypted.jpeg")
    pqr=mainfunc(im,5)
    cv2.imwrite("lastDecrypted.jpeg",pqr)
    return "Image(s) Uploaded Successfully. Come Back Soon."
app.run(host="0.0.0.0", port=5000, debug=True)
