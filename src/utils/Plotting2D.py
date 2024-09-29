import matplotlib.pyplot as plt
import csv
from flet.matplotlib_chart import MatplotlibChart
import time
import random


class Plot2D():
    def __init__(self,plot_name: str,**kwargs):
        self.header = plot_name
        self.para_index = kwargs.get('para_index')
        self.running = False

        plt.style.use('dark_background')
        self.x_data = []
        self.y_data = []

        self.fig, self.ax = plt.subplots(figsize=(15,7))
        self.line, = self.ax.plot([],[],linewidth=3)
        self.ax.set_xlabel("Mission Time (s)",fontsize=26)
        self.ax.set_ylabel(self.header,fontsize=26)

        self.ax.grid(visible=True,linewidth=0.4)
        self.ax.tick_params(axis=('both'),labelsize='24')

        self.chart = MatplotlibChart(self.fig)

    def graphing(self):
        self.running = True
        while self.running:
            data_gen = self.fetch_data()
            for x,y in data_gen:    
                self.x_data.append(x)
                self.y_data.append(y)

                self.line.set_xdata(self.x_data)
                self.line.set_ydata(self.y_data)

                self.ax.set_xlim(min(self.x_data), max(self.x_data))
                self.ax.set_ylim(min(self.y_data)-1, max(self.y_data)+1)
                self.chart.update()

    def fetch_data(self):
        with open("assets\\data\\neev_data.csv", 'r') as data_src:
            reader = csv.reader(data_src)
            last_row = None
            for row in reader:
                yield float(row[0]), float(row[self.para_index])
            self.running = False

    def get_chart(self):
        return self.chart