import flet as ft

class Console(ft.Container):
    def build(self):
        self.output = ft.Column(height=100,scroll=ft.ScrollMode.ALWAYS,spacing=1)

        self.cmd_field = ft.TextField(
            hint_text="Enter Command",
            color=ft.colors.WHITE,
            bgcolor="#1f2833",
            on_submit=self.on_uplink
        )

        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=self.output,
                    expand=True,
                    border=ft.border.all(color=ft.colors.WHITE),
                    padding=5,
                ),
                self.cmd_field,
            ],
            spacing=25
        )

        self.expand = True
        self.border_radius = 2

    def on_uplink(self, e):
        self.output.controls.append(ft.Text(f">{self.cmd_field.value}"))
        self.cmd_field.value = ""
        self.output.update()
        self.update()
