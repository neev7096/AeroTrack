import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import csv
from flet.matplotlib_chart import MatplotlibChart
import time
import random

class Plot3D():
    def __init__(self,plot_id: int):
        self.x_data = []
        self.y_data = []
        self.z_data = []

        self.fig = plt.figure(figsize=(15,15))
        self.ax = plt.axes(projection='3d')
        self.line, = self.ax.plot([],[],[])

        self.chart = MatplotlibChart(self.fig,original_size=True)

    def graphing(self,running: bool):
        i=0
        while running:
            self.x_data.append(len(self.y_data))
            self.y_data.append(random.randint(1,2))
            self.z_data.append(random.randint(1,10))

            self.ax.clear()
            self.ax.plot(self.x_data,self.y_data,self.z_data,linewidth=5,color='r')
            
            self.chart.update()

            if i>15:
                break
            i+=1

    def get_chart(self):
        return self.chart