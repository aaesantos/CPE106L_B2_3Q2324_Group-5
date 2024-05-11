import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
import homepage

def main(page: ft.Page):
    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False

    text_adminId: TextField = TextField(label='Administrator ID', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='Log in', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Login', width=200, disabled=True)

    def validate(_: ft.ControlEvent):
        if checkbox_signup.value and text_adminId.value == 'admin' and text_password.value == 'password':
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def submit(_: ft.ControlEvent):
        if not button_submit.disabled:
            page.clean()
            homepage.main(page)

    checkbox_signup.on_change = validate
    text_adminId.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    page.add(
        Row(
            controls=[
                Column(
                    [text_adminId, text_password, checkbox_signup, button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    ft.app(target=main)
