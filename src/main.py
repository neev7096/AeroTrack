import flet as ft
from components.views.DefaultView import DefaultPageLayout

def main(page: ft.Page):
    page.title = "Apogee3 Telemetry"
    page.theme_mode = "dark"
    page.window.full_screen = True
    
    default_page = DefaultPageLayout()

    def menu_button_click(e):
        pass

    app_bar=ft.AppBar(
        bgcolor="#45a29e",
        toolbar_height=35,
        title=ft.MenuBar(
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("File"),
                    height=23,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Export (.csv)"),
                            height=23,
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: "#c5c6c7"},
                                color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE},
                                shape=ft.ContinuousRectangleBorder(radius=1)
                            ),
                            on_click=menu_button_click
                        )
                    ],
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.HOVERED: "#c5c6c7", ft.ControlState.DEFAULT: "1f2833"},
                        color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                    )
                ),
                ft.SubmenuButton(
                    content=ft.Text("Port"),
                    height=23,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Browse File"),
                            height=23,
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.HOVERED: "#c5c6c7"},
                                color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE},
                                shape=ft.ContinuousRectangleBorder(radius=1)
                            ),
                            on_click=menu_button_click
                        )
                    ],
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.HOVERED: "#c5c6c7", ft.ControlState.DEFAULT: "1f2833"},
                        color={ft.ControlState.HOVERED: ft.colors.BLACK, ft.ControlState.DEFAULT: ft.colors.WHITE}
                    )
                )
            ]
        )
    )

    root_layout = ft.Tabs(
        selected_index=0,
        animation_duration=25,
        tabs=[
            ft.Tab(
                text="Home",
                content=ft.Container(
                    default_page
                ),
            ),
            ft.Tab(
                text="Launch Pad",
                content=ft.Container(
                    ft.Text("Launch Pad")
                ),
            ),
            ft.Tab(
                text="Rocket Flight Computer",
                content=ft.Container(
                    ft.Text("Rocket Flight Computer")
                ),
            ),
            ft.Tab(
                text="CAN-SAT",
                content=ft.Container(
                    ft.Text("CAN-SAT")
                )
            ),
        ],
        expand=1
    )

    page.add(app_bar,root_layout)

ft.app(target=main)