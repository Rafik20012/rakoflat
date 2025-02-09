import flet as ft  # Import the Flet module

def main(page: ft.Page):
    page.title = "Flet App Example"  # Set page title
    
    T = ft.Text("Hello, world!")  # Create a text widget
    page.add(T)  # Add text to the page

    page.update()  # Update the page to reflect changes

ft.app(target=main)  # Run the app
