import flet as ft
from utils.Plotting2D import Plot2D
from utils.Plotting3D import Plot3D
from components.views.UplinkConsole import Console
import csv


class DefaultPageLayout(ft.Container):
    def build(self):
        self.graph_widget_1 = Plot2D("Altitude (m)", para_index=1)
        self.graph_widget_2 = Plot2D("Velocity (m/s)", para_index=2)
        self.graph_widget_3 = Plot2D("Acceleration (m/s^2)", para_index=3)
        self.graph_widget_4 = Plot2D("Thrust (N)", para_index=4)
        self.graph_widget_5 = Plot3D("Position")

        console = Console()
        root_column = ft.Column()
        row_1 = ft.Row(spacing=25)
        row_2 = ft.Row(spacing=25)

        #DataTable, Importing Parameters
        data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(value="PARAMETERS",weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text(value="DATA",weight=ft.FontWeight.BOLD),numeric=True)
            ],
            border=ft.border.all(1,ft.colors.WHITE),
            height=830,
            width=341
        )
        self.Parameters()
        self.fetch_data()
        for i in range(len(self.Plist)):
            data_table.rows.append(ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(value=self.Plist[i])),
                    ft.DataCell(ft.Text(value=self.data[i]))
                ]
            )
        )
        data_table.data_row_max_height = 40
        
        #Graph Section, Definition of Graph Layout
        graph_section = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(controls=[ft.Text(f"{self.graph_widget_1.header}"),self.graph_widget_1.get_chart()],
                            alignment=ft.alignment.center,spacing=0),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            border=ft.border.all(color=ft.colors.WHITE),
                            padding=10
                        ),
                        ft.Container(
                            content=ft.Column(controls=[ft.Text(f"{self.graph_widget_2.header}"),self.graph_widget_2.get_chart()],
                            alignment=ft.alignment.center,spacing=0),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            border=ft.border.all(color=ft.colors.WHITE),
                            padding=10
                        )
                    ],
                    spacing=0
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(controls=[ft.Text(f"{self.graph_widget_3.header}"),self.graph_widget_3.get_chart()],
                            alignment=ft.alignment.center,spacing=0),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            border=ft.border.all(color=ft.colors.WHITE),
                            padding=10
                        ),
                        ft.Container(
                            content=ft.Column(controls=[ft.Text(f"{self.graph_widget_4.header}"),self.graph_widget_4.get_chart()],
                            alignment=ft.alignment.center,spacing=0),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            border=ft.border.all(color=ft.colors.WHITE),
                            padding=10
                        )
                    ],
                    spacing=0
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Text("BOOT",size=10),
                                            ft.Text("IDLE",size=10),
                                            ft.Text("TEST",size=10),
                                            ft.Text("LAUNCH_PAD",size=10),
                                            ft.Text("ASCENT",size=10),
                                            ft.Text("DEPLOY",size=10),
                                            ft.Text("DESCENT",size=10),
                                            ft.Text("SDESCENT",size=10), 
                                            ft.Text("TOUCHDOWN",size=10)
                                        ],
                                        spacing=12
                                    ),
                                    ft.ProgressBar(
                                        value=0.25,
                                        bar_height=15,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text("Downlink Packet String:",weight=ft.FontWeight.W_700,size=16),
                                                ft.Text("> 2024ASI-CANSAT-001,BOOT,1.3,1,0,0.1,23.4,5,0,3.3,1.3,23.4532,72.6633,100,4,0.00,0.00,0.00"),
                                                ft.Text("> 2024ASI-CANSAT-001,BOOT,1.3,1,0,0.1,23.4,5,0,3.3,1.3,23.4532,72.6633,100,4,0.00,0.00,0.00"),
                                                ft.Text("> 2024ASI-CANSAT-001,BOOT,1.3,1,0,0.1,23.4,5,0,3.3,1.3,23.4532,72.6633,100,4,0.00,0.00,0.00"),
                                                ft.Text("> 2024ASI-CANSAT-001,BOOT,1.3,1,0,0.1,23.4,5,0,3.3,1.3,23.4532,72.6633,100,4,0.00,0.00,0.00"),
                                                ft.Text("> 2024ASI-CANSAT-001,BOOT,1.3,1,0,0.1,23.4,5,0,3.3,1.3,23.4532,72.6633,100,4,0.00,0.00,0.00"),
                                                ft.Text("> 2024ASI-CANSAT-001,BOOT,1.3,1,0,0.1,23.4,5,0,3.3,1.3,23.4532,72.6633,100,4,0.00,0.00,0.00")
                                            ],
                                            scroll=ft.ScrollMode.AUTO,
                                            height=200,
                                            spacing=0
                                        )
                                    )
                                ],
                            ),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            border=ft.border.all(color=ft.colors.WHITE),
                            alignment=ft.alignment.center,
                            padding=15
                        ),
                        ft.Container(
                            content=self.graph_widget_5.get_chart(),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            border=ft.border.all(color=ft.colors.WHITE),
                            padding=10
                        )
                    ],
                    spacing=0
                )
            ],
            spacing=0
        )

        #Rocket Model Visualization Area
        rendered_section=ft.Column(
            controls=[
                ft.Container(
                            content=ft.Text(""),
                            height=550,
                            width=300,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center, 
                            border=ft.border.all(color=ft.colors.WHITE)                          
                        ),
                ft.Container(
                            content=ft.Image(src="assets\\Screenshot 2024-09-28 202905.png"),
                            height=275,
                            width=300,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            padding=5,
                            border=ft.border.all(color=ft.colors.WHITE)
                        )
            ],
            spacing=0
        )

        #Command Panel Layout
        control_panel = ft.Container(
                        content=ft.Text(value="09 : 11 : 01",size=48,weight=ft.FontWeight.W_600,color=ft.colors.GREEN),
                        width=342,
                        height=113,
                        border=ft.border.all(color=ft.colors.WHITE),
                        alignment=ft.alignment.center
        )
        
        #Inserting controls into Root Widget
        row_1.controls.append(data_table) #Data Table into row_1
        row_1.controls.append(ft.Container(content=graph_section,
                                                  padding=0,expand=True,border=ft.border.all(color=ft.colors.WHITE))) #Graph Section into Container into row_1
        row_1.controls.append(ft.Container(content=rendered_section,
                                                  bgcolor=ft.colors.WHITE, padding=1,border=ft.border.all(color=ft.colors.WHITE))) #3D Vis Section into Container into row_1

        row_2.controls.append(control_panel)
        row_2.controls.append(console)
        root_column.controls=[row_1,row_2] #row_1 and row_2 into RootColumn

        self.content = root_column
    
    def Parameters(self):
        ParaFile = open('assets\\Parameters.txt', 'r')
        self.Plist = ParaFile.read()
        ParaFile.seek(0)                       #Import and split all required parameters (separated by space)
        self.Plist=self.Plist.split()

    def fetch_data(self):
        data_src = open("assets\\data\\Sample_Data.csv", 'r')
        reader = csv.reader(data_src)
        for row in reader:
            self.data=row

    
    def did_mount(self):
        self.page.run_thread(self.graph_widget_1.graphing())
        self.page.run_thread(self.graph_widget_2.graphing())
        self.page.run_thread(self.graph_widget_3.graphing())
        self.page.run_thread(self.graph_widget_4.graphing())
        self.page.run_thread(self.graph_widget_5.graphing(True))