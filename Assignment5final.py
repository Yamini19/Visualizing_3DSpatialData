import numpy as np
import matplotlib.pyplot as plt
import math
# ********************Read the raw file to numpy Array*************************************************************
def VolumeTransformation(A, angle):
    Array2D = np.reshape(A, (421,512, 512))

    P = np.reshape([255,511,210],3) #center of Image plain -- parallel to x axis
    M = np.reshape([255,255,210],3)

    P1 = np.zeros(3)

    P1[0] = int(((P[0]-M[0])*np.cos(np.deg2rad(angle)))- ((P[1]-M[1])*np.sin(np.deg2rad(angle))) + M[0])
    P1[1] = int(((P[0]-M[0])*np.sin(np.deg2rad(angle)))+ ((P[1]-M[1])*np.cos(np.deg2rad(angle))) + M[1])
    P1[2] = P[2]
    print(M)
    print(P1)
    C= M-P1
    print(C)
    #print(P1)
    C0 = np.zeros(3)
    C0 = np.round((C * 1/(np.sqrt((M[0]-P1[0])**2 + (M[1]-P1[1])**2 + (M[2]-P1[2])**2))))

    print(C0)

    Sl = np.reshape((-1*C0[1],C0[0],C[2]),3)
    Sr = np.reshape((C0[1],-1 * C0[0],C[2]),3)

    print(Sl)
    print(Sr)
    Rl = np.zeros((513, 3))
    Rr = np.zeros((513, 3))

    Image = np.zeros((421, 512))
    for k in range(421):
        Rl[0] = [P1[0], P1[1], k]
        Rr[0] = [P1[0], P1[1], k]
        print(k)
        for j in range(256):
            i = 0
            while(i<=511):
                x = int(Rr[i][2])
                y = int(Rr[i][1])
                z = int(Rr[i][0])
                if(0<=x<=420 and 0<=y<=511 and 0<=z<=511):
                    Image[k][255+j+1] = Image[k][255+j+1]+ Array2D[x][y][z]
                x = int(Rl[i][2])
                y = int(Rl[i][1])
                z = int(Rl[i][0])
                if (0 <= x <= 420 and 0 <= y <= 511 and 0 <= z <= 511):
                    Image[k][255 - j] = Image[k][255 - j] + Array2D[x][y][z]
                Rr[i + 1] = Rr[i] + C0
                Rl[i + 1] = Rl[i] + C0
                i +=1
            Rl[0] = Rl[0] +Sl
            Rr[0] = Rr[0] +Sr

    return Image



## a. Image plane along x axis

A = np.fromfile("volume.raw", dtype='int16')
Image = VolumeTransformation(A, 0)

ax, fig = plt.subplots()
fig.imshow(Image, cmap='gray')
ax.savefig("a.Visualization(yaxis).png")

## b. Image plane turned at 45 degree
angle = 45
Image2 =VolumeTransformation(A, angle)

ax1, fig1 = plt.subplots()
fig1.imshow(Image2, cmap='gray')
ax1.savefig("b.Visualization(@45).png")
plt.show()