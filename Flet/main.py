import flet as ft


class TimeMineApp:
    def __init__(self, page:ft.Page):
        self.page = page
        self.active_session_start_time = None
        self.create_ui()

    def create_ui(self):

        pass

def main(page: ft.Page):
    app = TimeMineApp(page)

    app.title = "My first Flet App"
    app.page.add(ft.Text("Hello World, This is TimeMine"))
    app.page.add(ft.Card())


ft.app(target=main)