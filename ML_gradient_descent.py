import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

#a = [int(x) for x in input("Enter number").split()]
#print(a)
def gradient_descent(x,y):
    m_curr = b_curr = 0
    learning_rate = 0.001
    iterations = 1000
    cost_lst  = []
    i_lst = []
    n=len(x)
    fig=plt.figure()
    camera=Camera(fig)
    plt.scatter(x,y,c='green',marker='+')
    for i in range(iterations):
        y_pred = m_curr*x+b_curr
        #plt.plot(x,y_pred,color='red')
        #camera.snap()
        cost  = sum([value **2 for value in (y-y_pred)])

        cost_lst.append(cost)
        i_lst.append(i)
        plt.plot(i_lst, cost_lst, color='green')
        camera.snap()
        md = -(2/n)*sum(x*(y-y_pred))
        bd = -(2 / n) * sum((y - y_pred))
        m_curr = m_curr- learning_rate*md
        b_curr = b_curr - learning_rate * bd

        print("m {} b {} cost {} i {}".format(m_curr,b_curr,cost,i))
    animate=camera.animate()
    plt.show()
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)
