
import pkg_resources
from PIL import Image
from marcobre.diff.backend.backend import create_historical_table
import customtkinter as ctk

import marcobre.diff
from marcobre.diff.frontend.ContainerInputFile import ContainerInputFile
from marcobre.diff.frontend.MainTable import MainTable

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        create_historical_table()

        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')
        self.title('Marcobre - Reducción del tiempo de procesamiento de modelo de bloques')
        self.geometry('1280x720')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)


        #logo_path = 'frontend/images/logo.png'
        logo_path = pkg_resources.resource_filename(marcobre.diff.PKG_NAME, 'static/frontend/images/logo.png')
        self.logo_image = ctk.CTkImage(light_image=Image.open(logo_path),
                                        dark_image=Image.open(logo_path),
                                        size=(130, 27))


        self.logo_label = ctk.CTkLabel(self, image=self.logo_image,text="")
        self.logo_label.grid(
            column=0,
            row=0,
            padx=(10, 5),
            pady=(10, 0),
            sticky="nw"
        )


        self.title_label = ctk.CTkLabel(self, text='REDUCCIÓN DEL TIEMPO DE PROCESAMIENTO DE MODELO DE BLOQUES',
                                         font=("Arial", 16, "bold"),
                                         text_color="#2E6696")
        self.title_label.grid(
            column=0,
            row=1,
            padx=(10, 10),
            pady=(5, 10),
            sticky="nsew"
        )


        self.main_table = MainTable(self)
        self.main_table.grid(
            column=0,
            row=3,
            padx=(20, 20),
            pady=(10,20),
            sticky="nsew"
        )


        self.container_input_file = ContainerInputFile(self, main_table=self.main_table,fg_color="#FFFFFF")
        self.container_input_file.grid(
            column=0,
            row=2,
            padx=(20, 20),
            pady=10,
            sticky="nsew",

        )





