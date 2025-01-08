import flet as ft

import flet_flashlight as ffl

def main(page: ft.Page):
    flashlight = ffl.Flashlight()
    page.overlay.append(flashlight)
    page.add(
        ft.TextButton("toggle", on_click=lambda _: flashlight.toggle())
    )

ft.app(main)
