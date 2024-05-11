import flet as ft
from flet import *
import homepage
import login
import datetime

now = datetime.datetime.now()
formatted_date = now.strftime("%d-%m-%Y")

def return_home(page):
    page.clean()
    homepage.main(page)

def main(page: ft.Page):
    page.scroll = "auto"
    page.theme_mode = "light"
    all_food = Column()

    def addtofood(e, con_input):
        item_name = con_input.content.controls[3].value
        quantity = con_input.content.controls[4].value

        new_item = Container(
            padding=10,
            bgcolor="yellow200",
            content=Column([
                Text(item_name, weight="bold", size=20),
                Text(f"Total Price: {quantity}", weight="bold", size=20),
                Row( alignment="spaceBetween")
            ])
        )
        all_food.controls.append(new_item)

        # Update the billing order dialog with the new item
        if page.dialog is not None:
            dialog_content = page.dialog.content
            dialog_content.controls.insert(-1, new_item)
            page.dialog.content = dialog_content
        else:
            mydialog = AlertDialog(
                title=Text("Billing Order: ", size=30, weight="bold"),
                content=Column([
                    Row([
                        Text(con_input.content.controls[0].value,
                             weight="bold", size=20
                             ),
                        Text(f"Order Date: {formatted_date}",
                             weight="bold"
                             ),
                    ]),
                    Row([
                        Text("Customer Name: ", weight="bold"),
                        Text(con_input.content.controls[1].value,
                             weight="bold"
                             ),
                    ], alignment="end"),
                    Text("You rented: ", weight="bold", size=25),
                    all_food
                ], scroll="auto")
            )
            page.dialog = mydialog
            mydialog.open = True

        # Clear text entries after adding to list
        for control in con_input.content.controls:
            if isinstance(control, TextField):
                control.value = ""

        page.update()

    page.update()
    con_input = Container(
        content=Column([
            TextField(label="Customer ID"),
            TextField(label="Customer Name"),
            Text("Input Bike Information", size=25, weight="bold"),
            TextField(label="Bike Type"),
            TextField(label="Bike Price"),
            ElevatedButton("Add to List", on_click=lambda e: addtofood(e, con_input))
        ])
    )

    def buildmyorder(e):
        mydialog = AlertDialog(
            title=Text("Billing Order: ", size=30, weight="bold"),
            content=Column([
                Row([
                    Text(con_input.content.controls[0].value,
                         weight="bold", size=20
                         ),
                    Text(f"Date: {formatted_date}",
                         weight="bold"
                         ),
                ]),
                Row([
                    Text("Customer Name", weight="bold"),
                    Text(con_input.content.controls[1].value,
                         weight="bold"
                         ),
                ], alignment="end"),
                Text("Bike Rented Billing", weight="bold", size=25),
                all_food
            ], scroll="auto")
        )
        page.dialog = mydialog
        mydialog.open = True
        page.update()

    button_container = Container(
        content=Row([
            FloatingActionButton(icon="arrow_back", bgcolor="blue", on_click=lambda event: return_home(page)),
            FloatingActionButton(icon="add", bgcolor="yellow", on_click=buildmyorder)
        ])
    )

    page.add(
        Column([
            con_input,
            Text("Bike Rental Billing", weight="bold", size=20),
            all_food,
            button_container  # Add the button container to the page
        ])
    )

if __name__ == '__main__':
    ft.app(target=main)
