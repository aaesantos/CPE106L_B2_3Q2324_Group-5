import flet as ft
from flet import ElevatedButton, Text
import login
import billing
import sqlite3

class Controller:
    items = {}
    counter = len(items)

    @staticmethod
    def get_items():
        return Controller.items

    @staticmethod
    def add_item(data):
        Controller.items[Controller.counter] = data
        Controller.counter += 1




header_style = {
    "height": 60,
    "bgcolor": "#081d33",
    "border_radius": ft.border_radius.only(top_left=15, top_right=15),
    "padding": ft.padding.only(left=15, right=15),
}


def search_field(function: callable):
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=14,
        content_padding=0,
        cursor_color="white",
        cursor_width=1,
        color="white",
        hint_text="Search",
        on_change=function,
    )


def search_bar(control: ft.TextField):
    return ft.Container(
        width=350,
        bgcolor="white10",
        border_radius=6,
        opacity=0,
        animate_opacity=300,
        padding=8,
        content=ft.Row(
            spacing=10,
            vertical_alignment="center",
            controls=[
                ft.Icon(
                    name=ft.icons.SEARCH_ROUNDED,
                    size=17,
                    opacity=0.85,
                ),
                control,
            ],
        ),
    )


class Header(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**header_style, on_hover=self.toggle_search)
        self.dt = dt
        self.search_value = search_field(self.filter_dt_rows)
        self.search = search_bar(self.search_value)
        self.name = ft.Text("Bike Rental System", color="white")  # Changing text color to white
        self.content = ft.Row(
            alignment="spaceBetween",
            controls=[self.name, self.search]
        )

    def toggle_search(self, e: ft.HoverEvent):
        self.search.opacity = 1 if e.data == "true" else 0
        self.search.update()

    def filter_dt_rows(self, e):
        for data_rows in self.dt.rows:
            data_cell = data_rows.cells[0]
            data_rows.visible = (
                True
                if e.control.value.lower() in data_cell.content.value.lower()
                else False
            )
            data_rows.update()


form_style = {
    "border_radius": 8,
    "border": ft.border.all(1, "#ebebeb"),
    "bgcolor": "white10",
    "padding": 15,
}


def text_field():
    return ft.TextField(
        border_color="transparent",
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color="black",
        cursor_width=1,
        cursor_height=18,
        color="black",
    )


def text_field_container(expand: bool | int, name: str, control: ft.TextField):
    return ft.Container(
        expand=expand,
        height=45,
        bgcolor="#ebebeb",
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(
                    value=name,
                    size=9,
                    color="black",
                    weight="bold"
                ),
                control
            ]
        )
    )


class Form(ft.Container):
    def __init__(self, dt: ft.DataTable):
        super().__init__(**form_style)
        self.dt = dt
        self.row1_value = text_field()
        self.row2_value = text_field()
        self.row3_value = text_field()
        self.row4_value = text_field()
        self.row5_value = text_field()
        self.row1 = text_field_container(True, "Customer ID", self.row1_value)
        self.row2 = text_field_container(3, "Name", self.row2_value)
        self.row3 = text_field_container(1, "Age", self.row3_value)
        self.row4 = text_field_container(1, "ID Type", self.row4_value)
        self.row5 = text_field_container(1, "ID Number", self.row5_value)
        self.submit = ElevatedButton(text="Submit", on_click=self.submit_data)

        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.row1]),
                ft.Row(controls=[self.row2, self.row3, self.row4, self.row5]),
                self.submit,
            ]
        )

    def submit_data(self, e: ft.TapEvent):
        # Extracting values from input fields
        col1_value = self.row1_value.value
        col2_value = self.row2_value.value
        col3_value = self.row3_value.value
        col4_value = self.row4_value.value
        col5_value = self.row5_value.value

        # Inserting data into SQLite database
        conn = sqlite3.connect('C:\\AYEN\\SY 2023-2024\\TERM3\\CPE106L\\Database\\BRS.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Customer_info (Customer_ID, Name, age, ID_Type, ID_Number) VALUES (?, ?, ?, ?, ?)",
                       (col1_value, col2_value, col3_value, col4_value, col5_value))
        conn.commit()
        conn.close()

        # Clearing input fields
        self.clear_entries()

        # Refreshing the data table
        self.dt.fill_data_table()

    def clear_entries(self):
        self.row1_value.value = ""
        self.row2_value.value = ""
        self.row3_value.value = ""
        self.row4_value.value = ""
        self.content.update()


column_names1 = [
    "Customer ID", "Name", "Age", "ID Type", "ID number"
]

column_names2 = [
    "Bike ID", "Bike Type", "Bike Price", "Bike Stock"
]

data_table_style1 = {
    "expand": True,
    "border_radius": 8,
    "border": ft.border.all(2, "#ebebeb"),
    "horizontal_lines": ft.border.BorderSide(1, "#ebebeb"),
    "columns": [
        ft.DataColumn(ft.Text(index, size=12, color="black", weight="bold"))
        for index in column_names1
    ] + [ft.DataColumn(ft.Text(" ", size=12, color="black", weight="bold"))]  # Add delete button column
}

data_table_style2 = {
    "expand": True,
    "border_radius": 8,
    "border": ft.border.all(2, "#ebebeb"),
    "horizontal_lines": ft.border.BorderSide(1, "#ebebeb"),
    "columns": [
        ft.DataColumn(ft.Text(index, size=12, color="black", weight="bold"))
        for index in column_names2
    ]
}


class DataTable(ft.DataTable):
    def __init__(self, style):
        super().__init__(**style)
        self.rows = []

    def fill_data_table(self):
        self.rows = []  # Clear existing rows
        conn = sqlite3.connect('C:\\AYEN\\SY 2023-2024\\TERM3\\CPE106L\\Database\\BRS.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer_info")
        fetched_data = cursor.fetchall()
        conn.close()

        for values in fetched_data:
            data_row = ft.DataRow()
            data_row.cells = [
                ft.DataCell(ft.Text(str(value), color="black")) for value in values
            ]
            delete_button = ElevatedButton(
                text="Delete",
                bgcolor="red",
                color="white",
                on_click=lambda e, row=data_row: self.delete_data(row)
            )
            data_row.cells.append(ft.DataCell(delete_button))
            self.rows.append(data_row)
        self.update()

    def delete_data(self, row):
        id_to_delete = row.cells[0].content.value  # Assuming ID is in the first column
        conn = sqlite3.connect('C:\\AYEN\\SY 2023-2024\\TERM3\\CPE106L\\Database\\BRS.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Customer_info WHERE Customer_ID = ?", (id_to_delete,))
        conn.commit()
        conn.close()
        self.fill_data_table()  # Refresh the table after deletion

class DataTable2(ft.DataTable):
    def __init__(self, style):
        super().__init__(**style)
        # No need to fetch data here since it will be fetched in fill_data_table()
        self.rows = []

    def fill_data_table(self):
        self.rows = []  # Clear existing rows
        # Fetch data from the second table in the SQLite database
        # Modify the SQL query as needed
        conn = sqlite3.connect('C:\\AYEN\\SY 2023-2024\\TERM3\\CPE106L\\Database\\BRS.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bike_info")
        fetched_data = cursor.fetchall()
        conn.close()

        # Convert fetched data into rows for the DataTable
        for values in fetched_data:
            data_row = ft.DataRow()
            data_row.cells = [
                ft.DataCell(
                    ft.Text(str(value), color="black")  # Convert to string if necessary
                ) for value in values
            ]
            self.rows.append(data_row)
        self.update()


def logout(page):
    page.clean()
    login.main(page)

def go_to_billing(page):  # Pass page object as argument
    page.clean()
    billing.main(page)

def main(page: ft.Page):
    page.bgcolor = "#fdfdfd"
    table1 = DataTable(data_table_style1)
    header1 = Header(dt=table1)
    form1 = Form(dt=table1)

    table2 = DataTable2(data_table_style2)  # Creating the second table
    header2 = Header(dt=table2)  # Creating header for the second table

    logout_button = ElevatedButton(
        text="Log Out",
        style=ft.ButtonStyle(bgcolor="#ef5350", color="white"),
        on_click=lambda event: logout(page)
    )

    billing_button = ElevatedButton(
        text="Go to Billing",
        style=ft.ButtonStyle(bgcolor="#2196F3", color="white"),
        on_click=lambda event: go_to_billing(page)  # Pass page object to go_to_billing
    )

    page.add(
        ft.Column(
            expand=True,
            controls=[
                header1,  # Adding header for the first table
                form1,
                ft.Divider(height=2, color="transparent"),
                ft.Column(
                    scroll="hidden",
                    expand=True,
                    controls=[ft.Row(controls=[table1])]
                ),
                ft.Divider(height=2, color="transparent"),
                header2,
                ft.Column(
                    scroll="hidden",
                    expand=True,
                    controls=[ft.Row(controls=[table2])]  # Adding the second table
                ),
                ft.Row(controls=[billing_button, logout_button]),  # Adding buttons at the bottom left
            ],
        )
    )
    page.update()
    table1.fill_data_table()
    table2.fill_data_table()


if __name__ == '__main__':
    ft.app(target=main)
