# Imports
from tkinter import Canvas
from .file_selector import FileSelector
from .is_inside import is_inside
from os import getcwd, listdir
from math import ceil  # To get max page conversion

# File Selector List class
class FileSelectorList():
    def __init__(
            self,
            master: Canvas,
            x,
            y,
            offset_x,
            offset_y,
            overlooked_directory,
            conf,
            theme,
            extension="toml",
            additional_callback=lambda: None,
            callback_upon_selected_click=lambda: None # the function that runs when you click an already selected file
    ):
        # Initialization
        self.master = master
        self.init_coordinates = (x-(offset_x//2), y-(offset_y//2), x+(offset_x//2), y+(offset_y//2))
        self.directory_path = overlooked_directory
        self.extension = extension
        self.theme = theme
        self.conf = conf
        self.directory_elements = [x for x in listdir(self.directory_path) if x.split(".")[1] == self.extension]

        # Functionality variables
        self.callback = additional_callback
        self.selected_callback = callback_upon_selected_click
        self.current_page = 1
        self.max_page_amount = ceil(len(self.directory_path)/4)
        self.selected_selector = None

        # Drawing out main rectangle and page
        self.rect = self.master.create_rectangle(*self.init_coordinates, width=2, fill=self.theme["selector_list_fill"])
        self.draw_page(self.current_page)

        # Bindings
        self.master.bind("<Button-1>", self.handle_lclick, add="+")

    def draw_page(self, page_number):
        pass

    def select(self, selector: FileSelector):
        if self.selected_selector is not None:
            self.selected_selector.deselect()
        self.selected_selector = selector
        selector.select()

    def nullify_selection(self):
        if self.selected_selector is not None:
            self.selected_selector.deselect()
            self.selected_selector = None

    def handle_lclick(self, event):
        pass

