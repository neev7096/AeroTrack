import matplotlib.pyplot as plt
import csv
from flet.matplotlib_chart import MatplotlibChart
import time
import random


class Plot2D():
    def __init__(self,plot_id: int):
        plt.style.use('dark_background')
        self.x_data = []
        self.y_data = []

        self.fig, self.ax = plt.subplots(figsize=(11,6))
        self.line, = self.ax.plot([],[])

        self.ax.grid(visible=True,linewidth=0.4)
        self.ax.tick_params(axis=('both'),labelsize='18')

        self.chart = MatplotlibChart(self.fig)

    def graphing(self,running: bool):
        i=0
        while running:
            self.x_data.append(len(self.y_data))
            self.y_data.append(random.randint(10,1000))

            self.line.set_xdata(self.x_data)
            self.line.set_ydata(self.y_data)

            self.ax.set_xlim(min(self.x_data), max(self.x_data))
            self.ax.set_ylim(min(self.y_data)-1, max(self.y_data)+1)
            self.chart.update()

            if i>50:
                break
            i+=1

    def get_chart(self):
        return self.chart