import matplotlib.pyplot as plt
import numpy as np
n=6 #number of array items
x=[24, 32, 40, 48, 64, 80] #example data with distance and speed of an objec
y=[4, 6, 10, 12, 18, 27]
def least_square_fitting():
    
    xi=[]# create an empty array
    
    sx, sy, sxx, sxy, s, st=0, 0, 0, 0, 0, 0
    for i in range(n):
        sx +=x[i]
        sxx += x[i]*x[i]
        sy += y[i]
        sxy += x[i]*y[i]
        
    a = (n*sxy - sx*sy)/(n*sxx - sx*sx)# comes from y=a*x + b fit line 
    b = (sxx*sy - sx*sxy)/(n*sxx - sx*sx)
    for i in range(0, n):
        s += pow((y[i] - a*x[i])-b, 2)#square sum
        st += pow(y[i] - (sx/n), 2)
    for i in range(n):
        xii=b + a*x[i]
        xi.append(xii)
    r2=(st-s)/st#r square
    
    print("coeff1:", a,"coeff2:", b, "square sum:",  s, "r square:", r2 )
    plt.plot(x, y, '.')
    plt.plot(x, xi, '-')
    plt.show()
    
