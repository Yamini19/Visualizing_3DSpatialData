import numpy as np
import matplotlib.pyplot as plt
import math

data = np.fromfile("volume.raw", dtype='int16')
data3D = np.reshape(data, (421,512, 512))



P = np.reshape([255,0,210],3)
M = np.reshape([255,255,210],3)

P1 = np.zeros(3)

P1= P
P1[2] = P[2]

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
for l in range(421):
    Rl[0] = [P1[0], P1[1], l]
    Rr[0] = [P1[0], P1[1], l]
    # Rl[0] = [255, 511, l]
    # Rr[0] = [255, 511, l]
    print(l)
    for m in range(256):
        n = 0
        while(n <=511):
            x = int(Rr[n ][2])
            y = int(Rr[n ][1])
            z = int(Rr[n ][0])
            if(0<=x<=420 and 0<=y<=511 and 0<=z<=511):
                Image[l][255+m+1] = Image[l][255+m+1]+ data3D[x][y][z]
            x = int(Rl[n ][2])
            y = int(Rl[n ][1])
            z = int(Rl[n ][0])
            if (0 <= x <= 420 and 0 <= y <= 511 and 0 <= z <= 511):
                Image[l][255 - m] = Image[l][255 - m] + data3D[x][y][z]
            Rr[n + 1] = Rr[n ] + C0
            Rl[n + 1] = Rl[n ] + C0
            n +=1
        Rl[0] = Rl[0] +Sl
        Rr[0] = Rr[0] +Sr

ax1, fig1 = plt.subplots()
fig1.imshow(Image, cmap='gray')
plt.show()