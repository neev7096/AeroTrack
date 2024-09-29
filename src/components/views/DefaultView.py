import flet as ft
import csv

class DefaultPageLayout(ft.Container):
    def build(self):
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
                            content=ft.Text(".."),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(".."),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                        )
                    ],
                    spacing=1
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(".."),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(".."),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                        )
                    ],
                    spacing=1
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text("TIMELINE", color=ft.colors.WHITE),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            content=ft.Text(".."),
                            height=275,
                            width=495,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                        )
                    ],
                    spacing=1
                )
            ],
            spacing=1
        )

        #Rocket Model Visualization Area
        rendered_section=ft.Column(
            controls=[
                ft.Container(
                            content=ft.Text(".."),
                            height=550,
                            width=300,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center                            
                        ),
                ft.Container(
                            content=ft.Text(".."),
                            height=275,
                            width=300,
                            bgcolor=ft.colors.BLACK,
                            alignment=ft.alignment.center,
                            padding=5
                        )
            ],
            spacing=1
        )

        #Command Panel Layout
        control_panel = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.FilledTonalButton(
                                content=ft.Text("IDLE"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2),
                                    bgcolor={ft.ControlState.HOVERED: "#45a29e", ft.ControlState.DEFAULT: "#1f2833"},
                                    color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                                ),
                                height=44,
                                width=113
                            ),
                            ft.FilledTonalButton(
                                content=ft.Text("TEST"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2),
                                    bgcolor={ft.ControlState.HOVERED: "#45a29e", ft.ControlState.DEFAULT: "#1f2833"},
                                    color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                                ),
                                height=44,
                                width=113
                            ),
                            ft.FilledTonalButton(
                                content=ft.Text("ABORT"),
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=2),
                                    bgcolor={ft.ControlState.HOVERED: ft.colors.RED, ft.ControlState.DEFAULT: "#1f2833"},
                                    color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                                ),
                                height=44,
                                width=113
                            )
                        ],
                        spacing=1,
                        expand=True
                    ),
                    ft.Container(
                        content=ft.Text(value="11 : 11 : 11",size=48,weight=ft.FontWeight.W_600,color=ft.colors.GREEN),
                        width=342,
                        height=67,
                        alignment=ft.alignment.center
                    )
                ],
                spacing=10
            ),
            height=112,   
        )
        
        #Inserting controls into Root Widget
        row_1.controls.append(data_table) #Data Table into row_1
        row_1.controls.append(ft.Container(content=graph_section,
                                                  bgcolor=ft.colors.WHITE, padding=1,expand=True)) #Graph Section into Container into row_1
        row_1.controls.append(ft.Container(content=rendered_section,
                                                  bgcolor=ft.colors.WHITE, padding=1)) #3D Vis Section into Container into row_1

        row_2.controls.append(control_panel)
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