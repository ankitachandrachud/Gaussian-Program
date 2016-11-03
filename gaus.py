#import Tkinter as tk
from Tkinter import *
import matplotlib.pyplot as plt              #All required libraries imported
import numpy as np
import matplotlib.mlab as mlab
import math
root =Tk()
class App():                                #A Class defined to manage the displays on screen
    def __init__(self):
        # type: () -> object

        #top = tk()
        L1 = Label(root,text="Mu")
        L1.grid( row = 0, column = 0)
        self.stringmu = IntVar()
        E1 = Entry(root,textvariable  = self.stringmu, bd =5)
        E1.grid( row = 0, column = 1)

        L2 = Label(text="Sigma")
        L2.grid( row = 1, column = 0)
        self.stringsigma= IntVar()

        E2 = Entry(root,textvariable = self.stringsigma, bd =5)

        E2.grid( row = 1, column = 1)



        but = Button(root, text = "Gaussian Graph", command= lambda: self.showplots())
        but.grid( row = 2, column = 1)
        #but1 = Button(top, text="Poisson Graph", command=lambda:main())
        #but1.grid(row=3, column=1)


        root.mainloop()



    def showplots(self):
        mu = self.stringmu.get()                        #Value of mu transfered to variable mu
        variance = self.stringsigma.get()               #Value of Variance taken

        sigma = float(math.sqrt(variance))              #Formula

        x = np.linspace(-3, 3, 100)                     #Used to get the values on x axis of graph
                                                        # Sequence is usually ( start,stop, samples)

        plt.plot(x,mlab.normpdf(x, mu, sigma),linewidth=5.5)         # Command to plot the graph

        plt.xlabel('some numbers')                     # "some number is the label for X axis

        plt.ylabel('some numbers')                     # "some number is the label for Y axis

        plt.title('Gaussian Values')                   #Title of the graph


        #plt.text(1,1, r'$\mu=mu,\ \sigma=variance')

        #plt.annotate('mu'= mu,'sigma'= variance, xy=(1.3, 0.37), xytext=(2.4, 0.34))

        #arrowprops=dict(facecolor='black', shrink=0.05),


        plt.show()


App()
