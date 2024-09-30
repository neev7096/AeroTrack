import flet as ft

class Console(ft.Container):
    def build(self):
        self.output = ft.Column(controls=[ft.Text("Uplink Command Log: ",size=16,weight=ft.FontWeight.W_700)],height=100,scroll=ft.ScrollMode.ALWAYS,spacing=1)

        self.cmd_field = ft.TextField(
            hint_text="Enter Command",
            color=ft.colors.WHITE,
            bgcolor="#1f2833",
            on_submit=self.on_cmd
        )
        cmd_layout = ft.Column(
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
                            on_click=self.on_cmd_click,
                            height=44,
                            width=100
                        ),
                        ft.FilledTonalButton(
                            content=ft.Text("TEST"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=2),
                                bgcolor={ft.ControlState.HOVERED: "#45a29e", ft.ControlState.DEFAULT: "#1f2833"},
                                color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                            ),
                            on_click=self.on_cmd_click,
                            height=44,
                            width=100
                        ),
                        ft.FilledTonalButton(
                            content=ft.Text("ABORT"),
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=2),
                                bgcolor={ft.ControlState.HOVERED: ft.colors.RED, ft.ControlState.DEFAULT: "#1f2833"},
                                color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                            ),
                            on_click=self.on_cmd_click,
                            height=44,
                            width=100
                        )
                    ],
                    spacing=1
                ),
                self.cmd_field       
            ]
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=self.output,
                    expand=True,
                    border=ft.border.all(color=ft.colors.WHITE),
                    padding=5,
                ),
                cmd_layout,
            ],
            spacing=25
        )

        self.expand = True
        self.border_radius = 2

    def on_cmd(self, e):
        self.output.controls.append(ft.Text(f"> {self.cmd_field.value}"))
        self.cmd_field.value = ""
        self.output.update()
        self.update()

    def on_cmd_click(self, e):
        self.output.controls.append(ft.Text(f"> {e.control.content.value}"))
        self.output.update()
        self.update()