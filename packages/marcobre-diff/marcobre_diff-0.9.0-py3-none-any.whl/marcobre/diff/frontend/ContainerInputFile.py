import os
import customtkinter as ctk
from tkinter import filedialog, Toplevel,Label,messagebox
import threading
import time
import configparser
from marcobre.diff.backend.algorithm.algorithm import algorithm_function
import csv

class ContainerInputFile(ctk.CTkFrame):
    def __init__(self, master, main_table, **kwargs):
        super().__init__(master, **kwargs)
        self.main_table = main_table

        self.config = configparser.ConfigParser()
        self.config_file = os.path.expanduser("~/.app_config.ini")

        self.file1_label = ctk.CTkLabel(self, text="Archivo 01: Modelo de bloques actual", anchor="w", text_color="#2D649B")
        self.file1_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 0), sticky="w")

        self.file2_label = ctk.CTkLabel(self, text="Archivo 02: Modelo de bloques de referencia", anchor="w", text_color="#2D649B")
        self.file2_label.grid(row=0, column=2, padx=(10, 5), pady=(10, 0), sticky="w")

        self.file1_entry = ctk.CTkEntry(self, width=370)
        self.file1_entry.grid(row=1, column=0, padx=(10, 5), pady=(0, 5), sticky="we")

        self.file1_button = ctk.CTkButton(
            self,
            text="Seleccionar",
            command=self.select_file1,
            width=120,
            fg_color="#E7EEF7",
            text_color="#2D649B",
        )
        self.file1_button.grid(row=1, column=1, padx=(5, 10), pady=(0, 5), sticky="w")


        self.file1_button.bind("<Enter>", lambda e: self.on_hover(self.file1_button, True))
        self.file1_button.bind("<Leave>", lambda e: self.on_hover(self.file1_button, False))

        self.file2_entry = ctk.CTkEntry(self, width=370)
        self.file2_entry.grid(row=1, column=2, padx=(10, 5), pady=(0, 5), sticky="we")

        self.file2_button = ctk.CTkButton(
            self,
            text="Seleccionar",
            command=self.select_file2,
            width=120,
            fg_color="#E7EEF7",
            text_color="#2D649B"
        )
        self.file2_button.grid(row=1, column=3, padx=(5, 10), pady=(0, 5), sticky="w")


        self.file2_button.bind("<Enter>", lambda e: self.on_hover(self.file2_button, True))
        self.file2_button.bind("<Leave>", lambda e: self.on_hover(self.file2_button, False))

        self.submit_btn = ctk.CTkButton(
            self,
            text="Procesar",
            width=180,
            command=self.on_submit,
            fg_color="#2D649B",
            text_color="#FFFFFF"
        )
        self.submit_btn.grid(row=1, column=4, padx=(10, 10), pady=(0, 10), sticky="e")
        self.submit_btn.bind("<Enter>", lambda e: self.on_hover_submit(self.submit_btn, True))
        self.submit_btn.bind("<Leave>", lambda e: self.on_hover_submit(self.submit_btn, False))

        self.timer_label = ctk.CTkLabel(self, text="")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(3, weight=0)
        self.grid_columnconfigure(4, weight=0)

        self.load_config()

        self.loader_frame = ctk.CTkFrame(self, fg_color="#FFFFFF")
        self.loader_frame.grid(row=2, column=0, columnspan=5, sticky="nsew")
        self.loader_frame.grid_remove()

        self.loader_label = ctk.CTkLabel(self.loader_frame, text="Procesando...", text_color="#2D649B")
        self.loader_label.pack(pady=2)

        self.loader_indicator = ctk.CTkProgressBar(self.loader_frame)
        self.loader_indicator.pack(pady=10)

    def on_hover_submit(self, button, hover):
        if hover:
            button.configure(fg_color="#2E6696", text_color="#FFFFFF")
            button.configure(cursor="hand2")
        else:
            button.configure(fg_color="#2D649B", text_color="#FFFFFF")
            button.configure(cursor="")

    def on_hover(self, button, hover):
        if hover:
            button.configure(fg_color="#E7EEF7", text_color="#2D649B")
            button.configure(cursor="hand2")
        else:
            button.configure(fg_color="#E7EEF7", text_color="#2D649B")
            button.configure(cursor="")

    def load_config(self):
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
            self.file1_path = self.config.get('Paths', 'file1', fallback='')
            self.file2_path = self.config.get('Paths', 'file2', fallback='')


            if not os.path.exists(self.file2_path):
                self.file2_path = ''

            # self.file1_entry.delete(0, ctk.END)
            # self.file1_entry.insert(0, self.file1_path)
            self.file2_entry.delete(0, ctk.END)
            self.file2_entry.insert(0, self.file2_path)
        else:
            self.file1_path = ''
            self.file2_path = ''
            self.config['Paths'] = {}

    def save_config(self):
        self.config['Paths']['file1'] = self.file1_entry.get()
        self.config['Paths']['file2'] = self.file2_entry.get()
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def select_file1(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file1_entry.delete(0, ctk.END)
            self.file1_entry.insert(0, file_path)
            self.save_config()

    def select_file2(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file2_entry.delete(0, ctk.END)
            self.file2_entry.insert(0, file_path)
            self.save_config()

    def on_submit(self):
        ref_file = self.file1_entry.get().strip()
        cmp_file = self.file2_entry.get().strip()

        if not ref_file or not cmp_file:
            messagebox.showwarning("Advertencia", "Por favor, seleccione ambos archivos antes de procesar.")
            return

        if not os.path.exists(ref_file):
            messagebox.showerror("Error", f"El archivo 1 no existe: {ref_file}")
            return

        if not os.path.exists(cmp_file):
            messagebox.showerror("Error", f"El archivo 2 no existe: {cmp_file}")
            return

        if not ref_file.lower().endswith('.csv'):
            messagebox.showerror("Error", f"El archivo 1 debe ser un CSV: {ref_file}")
            return

        if not cmp_file.lower().endswith('.csv'):
            messagebox.showerror("Error", f"El archivo 2 debe ser un CSV: {cmp_file}")
            return

        required_columns = ["X", "Y", "Z", "CUT", "CUAS", "CUCN", "CUR", "C", "FE", "AG", "S", "AU", "AS", "P", "LITH"]

        if not self.validate_csv_columns(ref_file, required_columns):
            return

        if not self.validate_csv_columns(cmp_file, required_columns):
            return

        self.submit_btn.configure(text="Procesando...", state="disabled")
        self.disable_inputs()
        self.timer_label.configure(text="Tiempo: 0 segundos")

        print(f"Archivo: {ref_file}, Archivo cmp: {cmp_file}")
        self.show_loader()
        threading.Thread(target=self.run_algorithm_with_timer, args=(ref_file, cmp_file)).start()

    def validate_csv_columns(self, file_path, required_columns):
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                header = next(reader)

                missing_columns = [col for col in required_columns if col not in header]

                if missing_columns:
                    messagebox.showerror("Error",
                                         f"El archivo {file_path} no contiene las columnas requeridas: {', '.join(missing_columns)}")
                    return False
                return True
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo {file_path}: {str(e)}")
            return False

    def run_algorithm_with_timer(self, ref_file, cmp_file):
        start_time = time.time()
        algorithm_function(ref_file, cmp_file)
        elapsed_time = time.time() - start_time

        self.timer_label.configure(text=f"Tiempo: {int(elapsed_time)} segundos")
        self.hide_loader()
        self.enable_inputs()
        self.master.main_table.refresh_table()

    def disable_inputs(self):
        self.file1_entry.configure(state="disabled")
        self.file2_entry.configure(state="disabled")
        self.file1_button.configure(state="disabled", fg_color="#E7EEF7")
        self.file2_button.configure(state="disabled", fg_color="#E7EEF7")
        self.loader_frame.grid()  # Mostrar loader
        self.loader_indicator.start()

    def enable_inputs(self):
        self.file1_entry.configure(state="normal")
        self.file2_entry.configure(state="normal")
        self.file1_button.configure(state="normal")
        self.file2_button.configure(state="normal")
        self.submit_btn.configure(text="Procesar", state="normal")
        self.loader_frame.grid_remove()
        self.loader_indicator.stop()

    def show_loader(self):
        self.loader_frame.grid()
        self.loader_indicator.start()

    def hide_loader(self):
        self.loader_frame.grid_remove()
        self.loader_indicator.stop()

# import os
# import customtkinter as ctk
# from tkinter import filedialog
# import threading
# import time
# import configparser
# from backend.algorithm.algorithm import algorithm_function
#
# class ContainerInputFile(ctk.CTkFrame):
#     def __init__(self, master, main_table, **kwargs):
#         super().__init__(master, **kwargs)
#         self.main_table = main_table
#
#         self.config = configparser.ConfigParser()
#         self.config_file = os.path.expanduser("~/.app_config.ini")
#
#
#
#         self.file1_label = ctk.CTkLabel(self, text="Archivo 01: Modelo de bloques actual", anchor="w",text_color="#2D649B")
#         self.file1_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 0), sticky="w")
#
#         self.file2_label = ctk.CTkLabel(self, text="Archivo 02: Modelo de bloques de referencia", anchor="w",text_color="#2D649B")
#         self.file2_label.grid(row=0, column=2, padx=(10, 5), pady=(10, 0), sticky="w")
#
#
#         self.file1_entry = ctk.CTkEntry(self, width=370)
#         self.file1_entry.grid(row=1, column=0, padx=(10, 5), pady=(0, 5), sticky="we")
#
#         self.file1_button = ctk.CTkButton(
#             self,
#             text="Seleccionar",
#             command=self.select_file1,
#             width=120,
#             fg_color="#E7EEF7",
#             text_color="#2D649B",
#         )
#         self.file1_button.grid(row=1, column=1, padx=(5, 10), pady=(0, 5), sticky="w")
#
#         # Bind hover events
#         self.file1_button.bind("<Enter>", lambda e: self.on_hover(self.file1_button, True))
#         self.file1_button.bind("<Leave>", lambda e: self.on_hover(self.file1_button, False))
#
#         self.file2_entry = ctk.CTkEntry(self, width=370)
#         self.file2_entry.grid(row=1, column=2, padx=(10, 5), pady=(0, 5), sticky="we")
#
#         self.file2_button = ctk.CTkButton(
#             self,
#             text="Seleccionar",
#             command=self.select_file2,
#             width=120,
#             fg_color = "#E7EEF7",
#             text_color = "#2D649B"
#         )
#         self.file2_button.grid(row=1, column=3, padx=(5, 10), pady=(0, 5), sticky="w")
#
#         # Bind hover events
#         self.file2_button.bind("<Enter>", lambda e: self.on_hover(self.file2_button, True))
#         self.file2_button.bind("<Leave>", lambda e: self.on_hover(self.file2_button, False))
#
#         self.submit_btn = ctk.CTkButton(
#             self,
#             text="Procesar",
#             width=180,
#
#             command=self.on_submit,
#             fg_color = "#2D649B",
#             text_color = "#FFFFFF"
#         )
#         self.submit_btn.grid(row=1, column=4, padx=(10, 10), pady=(0, 10), sticky="e")
#         self.submit_btn.bind("<Enter>", lambda e: self.on_hover_submit(self.submit_btn, True))
#         self.submit_btn.bind("<Leave>", lambda e: self.on_hover_submit(self.submit_btn, False))
#
#         self.timer_label = ctk.CTkLabel(self, text="")
#
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(2, weight=1)
#         self.grid_columnconfigure(1, weight=0)
#         self.grid_columnconfigure(3, weight=0)
#         self.grid_columnconfigure(4, weight=0)
#
#         self.load_config()
#     def on_hover_submit(self, button, hover):
#         if hover:
#             button.configure(fg_color="#2E6696", text_color="#FFFFFF")
#             button.configure(cursor="hand2")  # Cambia el cursor a pointer
#         else:
#             button.configure(fg_color="#2D649B", text_color="#FFFFFF")
#             button.configure(cursor="")  # Restablece el cursor al predeterminado
#
#
#     def on_hover(self, button, hover):
#         if hover:
#             button.configure(fg_color="#2E6696", text_color="#FFFFFF")
#             button.configure(cursor="hand2")  # Cambia el cursor a pointer
#         else:
#             button.configure(fg_color="#E7EEF7", text_color="#2D649B")
#             button.configure(cursor="")  # Restablece el cursor al predeterminado
#
#     def load_config(self):
#         if os.path.exists(self.config_file):
#             self.config.read(self.config_file)
#             self.file1_path = self.config.get('Paths', 'file1', fallback='')
#             self.file2_path = self.config.get('Paths', 'file2', fallback='')
#
#             # Verifica si solo el archivo 2 existe
#             if not os.path.exists(self.file2_path):
#                 self.file2_path = ''  # O asigna una referencia predeterminada si lo deseas
#
#             # self.file1_entry.delete(0, ctk.END)
#             # self.file1_entry.insert(0, self.file1_path)
#             self.file2_entry.delete(0, ctk.END)
#             self.file2_entry.insert(0, self.file2_path)
#         else:
#             self.file1_path = ''
#             self.file2_path = ''
#             self.config['Paths'] = {}
#
#     def save_config(self):
#         self.config['Paths']['file1'] = self.file1_entry.get()  # Save file1 path
#         self.config['Paths']['file2'] = self.file2_entry.get()  # Save file2 path
#         with open(self.config_file, 'w') as configfile:
#             self.config.write(configfile)
#
#     def select_file1(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             self.file1_entry.delete(0, ctk.END)
#             self.file1_entry.insert(0, file_path)
#             self.save_config()  # Save the path immediately after selection
#
#     def select_file2(self):
#         file_path = filedialog.askopenfilename()
#         if file_path:
#             self.file2_entry.delete(0, ctk.END)
#             self.file2_entry.insert(0, file_path)
#             self.save_config()  # Save the path immediately after selection
#
#     def on_submit(self):
#         self.submit_btn.configure(text="Cargando...", state="disabled")
#         self.disable_inputs()
#         self.timer_label.configure(text="Tiempo: 0 segundos")
#
#         ref_file = self.file1_entry.get()
#         cmp_file = self.file2_entry.get()
#         print(f"Archivo: {ref_file}, Archivo cmp: {cmp_file}")
#
#         threading.Thread(target=self.run_algorithm_with_timer, args=(ref_file, cmp_file)).start()
#
#     def run_algorithm_with_timer(self, ref_file, cmp_file):
#         start_time = time.time()
#         algorithm_function(ref_file, cmp_file)
#         elapsed_time = time.time() - start_time
#
#         self.timer_label.configure(text=f"Tiempo: {int(elapsed_time)} segundos")
#
#         self.enable_inputs()
#         self.master.main_table.refresh_table()
#
#     def disable_inputs(self):
#         self.file1_entry.configure(state="disabled")
#         self.file2_entry.configure(state="disabled")
#         self.file1_button.configure(state="disabled",fg_color="#E7EEF7")
#         self.file2_button.configure(state="disabled",fg_color="#E7EEF7")
#
#     def enable_inputs(self):
#         self.file1_entry.configure(state="normal")
#         self.file2_entry.configure(state="normal")
#         self.file1_button.configure(state="normal")
#         self.file2_button.configure(state="normal")
#         self.submit_btn.configure(text="Procesar", state="normal")
#
