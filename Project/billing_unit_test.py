import unittest
from unittest.mock import patch
import datetime

import flet
from flet import *

import homepage
import login
import billing # Replace with your actual script name

class TestMainFunction(unittest.TestCase):
    def setUp(self):
        self.page = flet.Page()
        self.all_food = flet.Column()
        self.formatted_date = datetime.datetime.now().strftime("%d-%m-%Y")

    def test_addtofood(self):
        # Test adding an item to the billing order
        con_input = flet.Container(
            content=flet.Column([
                flet.TextField(label="Customer ID"),
                flet.TextField(label="Customer Name"),
                flet.Text("Input Bike Information", size=25, weight="bold"),
                flet.TextField(label="Bike Type", value="Mountain Bike"),
                flet.TextField(label="Bike Price", value="50"),
                flet.ElevatedButton("Add to List", on_click=lambda e: billing.addtofood(e, con_input))
            ])
        )

        # Mock dialog to prevent errors
        with patch.object(flet, 'AlertDialog') as mock_dialog:
            billing.addtofood(None, con_input)

            # Check if the new item is added to all_food
            self.assertEqual(len(self.all_food.controls), 1)
            self.assertIsInstance(self.all_food.controls[0], flet.Container)
            self.assertEqual(len(self.all_food.controls[0].content.controls), 3)  # Assuming 3 controls are added per item

    def test_buildmyorder(self):
        # Test building the billing order
        con_input = flet.Container(
            content=flet.Column([
                flet.TextField(label="Customer ID", value="12345"),
                flet.TextField(label="Customer Name", value="John Doe"),
                flet.Text("Input Bike Information", size=25, weight="bold"),
                flet.TextField(label="Bike Type", value="Mountain Bike"),
                flet.TextField(label="Bike Price", value="50"),
                flet.ElevatedButton("Add to List", on_click=lambda e: billing.addtofood(e, con_input))
            ])
        )

        # Mock dialog to prevent errors
        with patch.object(flet, 'AlertDialog') as mock_dialog:
            billing.addtofood(None, con_input)

            billing.buildmyorder(None)

            # Check if the dialog is created with correct content
            mock_dialog.assert_called_once_with(
                title=flet.Text("Billing Order: ", size=30, weight="bold"),
                content=flet.Column([
                    flet.Row([
                        flet.Text("12345", weight="bold", size=20),
                        flet.Text(f"Date: {self.formatted_date}", weight="bold"),
                    ]),
                    flet.Row([
                        flet.Text("Customer Name", weight="bold"),
                        flet.Text("John Doe", weight="bold"),
                    ], alignment="end"),
                    flet.Text("Bike Rented Billing", weight="bold", size=25),
                    self.all_food
                ], scroll="auto")
            )

if __name__ == '__main__':
    unittest.main()
