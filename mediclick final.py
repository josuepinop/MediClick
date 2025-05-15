import tkinter as tk
from tkinter import messagebox
import webbrowser
import random
import os

# —— Colores y estilos ——
BG_COLOR = "#f7f9fc"
FG_COLOR = "#003366"
BTN_BG = "#005eb8"
BTN_FG = "white"
BTN_ACTIVE = "#004a99"
CARD_COLOR = "white"
AVISO_COLOR = "#e6f2ff"
OK_COLOR = "#2e8b57"
ERROR_COLOR = "#cc0000"

FONT_TITLE = ("Arial", 18, "bold")
FONT_LABEL = ("Arial", 12)
FONT_SMALL = ("Arial", 10)

USER_FILE = "usuarios.txt"

# —— Funciones de usuario ——
def guardar_usuario(usuario, contrasena):
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            f.write("")
    with open(USER_FILE, "a") as f:
        f.write(f"{usuario},{contrasena}\n")

def verificar_credenciales(usuario, contrasena):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 2 and datos[0] == usuario and datos[1] == contrasena:
                return True
    return False

def usuario_existente(usuario):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 2 and datos[0] == usuario:
                return True
    return False

# —— Datos de ejemplo ——
MEDICINES = {
    "Aspirina": ["Cruz Verde", "Farmatodo"],
    "Paracetamol": ["La Rebaja", "Cruz Verde"],
    "Ibuprofeno": ["Farmatodo", "La Rebaja"],
    "Amoxicilina": ["Cruz Verde", "La Rebaja"],
    "Loratadina": ["Farmatodo"],
    "Omeprazol": ["La Rebaja"],
    "Metformina": ["Cruz Verde"],
    "Salbutamol": ["Farmatodo", "Cruz Verde"]
}

PHARMACIES = {
"Cruz Verde": {
        "hours": "8:00 – 20:00",
        "address": "Carrera 45 # 23-12, Medellín",
        "map_url": "https://www.google.com/maps/place/Cruz+verde+Molinos/@6.2390272,-75.6088832,15z/data=!4m6!3m5!1s0x8e4429c860bd5f57:0x7dde41914638a42a!8m2!3d6.2327785!4d-75.604201!16s%2Fg%2F11fmrfhbcd?entry=ttu&g_ep=EgoyMDI1MDUwNS4wIKXMDSoASAFQAw%3D%3D"
    },
    "Farmatodo": {
        "hours": "7:00 – 22:00",
        "address": "Calle 10 # 50-60, Medellín",
        "map_url": "https://www.google.com/maps/place/Cruz+verde+Molinos/@6.2390272,-75.6088832,15z/data=!4m6!3m5!1s0x8e4429c860bd5f57:0x7dde41914638a42a!8m2!3d6.2327785!4d-75.604201!16s%2Fg%2F11fmrfhbcd?entry=ttu&g_ep=EgoyMDI1MDUwNS4wIKXMDSoASAFQAw%3D%3D"
    },
    "La Rebaja": {
        "hours": "9:00 – 19:00",
        "address": "Transversal 39 # 24-45, Medellín",
        "map_url": "https://www.google.com/maps/place/la+rebaja+No.+40+DROGUERIA+Santa+Gema+Medellin/@6.2457,-75.6208997,15z/data=!4m6!3m5!1s0x8e4429975a9e998d:0xa8aa9515f4f170f3!8m2!3d6.2457!4d-75.6018453!16s%2Fg%2F1ptw9v8xz?entry=ttu&g_ep=EgoyMDI1MDUwNS4wIKXMDSoASAFQAw%3D%3D"
    }
}

FAQ = [
    ("¿Cómo registro una cuenta?", "Haz clic en Registrarse y completa los campos solicitados."),
    ("¿Olvidé mi contraseña?", "Este prototipo no incluye recuperación de contraseña."),
    ("¿Cómo buscar un medicamento?", "En el menú principal usa la opción Buscar Medicamentos."),
    ("¿Cómo ver horarios de farmacias?", "En Ver Farmacias selecciona la farmacia deseada."),
    ("¿Cómo contactar soporte?", "En la sección Ayuda/Soporte encuentras las FAQs."),
    ("¿Soporte en línea?", "Puedes chatear con nosotros en WhatsApp: https://wa.me/573001112233")
]

ventana = tk.Tk()
ventana.title("Mediclick - Prototipo")
ventana.geometry("500x600")
ventana.configure(bg=BG_COLOR)

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def abrir_maps(nombre):
    webbrowser.open(PHARMACIES[nombre]["map_url"])

def crear_boton(texto, comando, ancho=30, color=None):
    return tk.Button(
        ventana, text=texto, width=ancho,
        bg=BTN_BG if not color else color,
        fg=BTN_FG, activebackground=BTN_ACTIVE,
        relief="flat", font=FONT_LABEL, command=comando
    )

def pantalla_inicio():
    limpiar_ventana()
    frame = tk.Frame(ventana, bg=CARD_COLOR, bd=1, relief="solid")
    frame.place(relx=0.5, rely=0.35, anchor="center", width=400, height=180)

    tk.Label(frame, text="Presentamos", font=FONT_LABEL, bg=CARD_COLOR, fg=FG_COLOR).pack(pady=(15, 0))
    tk.Label(frame, text="MediClick", font=("Arial", 20, "bold"), bg=CARD_COLOR, fg=FG_COLOR).pack()
    tk.Label(frame, text="Tu tiempo es valioso", font=FONT_SMALL, bg=CARD_COLOR, fg=FG_COLOR).pack(pady=2)
    tk.Label(frame, text="Tus medicamentos a un click", font=FONT_SMALL, bg=CARD_COLOR, fg=FG_COLOR).pack(pady=2)

    aviso = tk.Label(ventana, text="Consulta en tiempo real la disponibilidad de tus medicamentos",
        font=FONT_SMALL, bg=AVISO_COLOR, fg=FG_COLOR, relief="flat")
    aviso.pack(pady=(20, 10), padx=15, fill="x")

    crear_boton("DESCARGA AHORA", pantalla_login).pack(pady=15)

def pantalla_login():
    limpiar_ventana()
    tk.Label(ventana, text="Iniciar Sesión", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)
    tk.Label(ventana, text="Usuario", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).pack()
    usuario_entry = tk.Entry(ventana); usuario_entry.pack()
    tk.Label(ventana, text="Contraseña", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).pack()
    contra_entry = tk.Entry(ventana, show="*"); contra_entry.pack()

    def intentar_login():
        usuario = usuario_entry.get().strip()
        contra = contra_entry.get().strip()
        if not usuario or not contra:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return
        if verificar_credenciales(usuario, contra):
            pantalla_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    crear_boton("Ingresar", intentar_login).pack(pady=15)
    crear_boton("Registrarse", pantalla_registro).pack(pady=5)
    crear_boton("Volver", pantalla_inicio).pack()

def pantalla_registro():
    limpiar_ventana()
    tk.Label(ventana, text="Registro de Usuario", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)
    tk.Label(ventana, text="Usuario", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).pack()
    usuario_entry = tk.Entry(ventana); usuario_entry.pack()
    tk.Label(ventana, text="Contraseña", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).pack()
    contra_entry = tk.Entry(ventana, show="*"); contra_entry.pack()

    def registrar():
        usuario = usuario_entry.get().strip()
        contra = contra_entry.get().strip()
        if not usuario or not contra:
            messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
            return
        if usuario_existente(usuario):
            messagebox.showerror("Error", "Ese usuario ya está registrado.")
            return
        guardar_usuario(usuario, contra)
        messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
        pantalla_login()

    crear_boton("Registrarme", registrar).pack(pady=15)
    crear_boton("Volver", pantalla_login).pack()

def pantalla_menu():
    limpiar_ventana()
    tk.Label(ventana, text="Menú Principal", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)
    crear_boton("Buscar Medicamentos", pantalla_buscar).pack(pady=5)
    crear_boton("Ver Farmacias", pantalla_ver_farmacias).pack(pady=5)
    crear_boton("Ayuda / Soporte", pantalla_ayuda).pack(pady=5)
    crear_boton("Cerrar Sesión", pantalla_inicio).pack(pady=20)

def pantalla_buscar():
    limpiar_ventana()
    tk.Label(ventana, text="Buscar Medicamento", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)
    med_var = tk.StringVar(value=list(MEDICINES.keys())[0])
    tk.OptionMenu(ventana, med_var, *MEDICINES.keys()).pack(pady=10)
    def do_search():
        sel = med_var.get()
        lista = MEDICINES.get(sel, [])
        pantalla_lista_farmacias(lista, sel)
    crear_boton("Buscar", do_search).pack(pady=10)
    crear_boton("Volver", pantalla_menu).pack(pady=5)

def pantalla_lista_farmacias(lista, medicamento):
    limpiar_ventana()
    disponibilidad = [(farm, random.choice([True, False])) for farm in lista]
    disponibles = [d for d in disponibilidad if d[1]]
    titulo = (f"{medicamento} disponible en:" if disponibles 
              else f"{medicamento} no disponible actualmente en ninguna farmacia")
    tk.Label(ventana, text=titulo, font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)

    for farm, disponible in disponibilidad:
        color = OK_COLOR if disponible else ERROR_COLOR
        estado = "✅ Disponible" if disponible else "❌ Agotado"
        texto = f"{farm} - {estado}"
        btn = tk.Button(
            ventana, text=texto, width=35, font=FONT_LABEL,
            fg=color, bg="white", relief="solid",
            command=lambda f=farm: pantalla_detalle_farmacia(f)
        )
        btn.pack(pady=4)

    crear_boton("Volver", pantalla_menu).pack(pady=20)

def pantalla_ver_farmacias():
    limpiar_ventana()
    tk.Label(ventana, text="Todas las Farmacias", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)
    for farm in PHARMACIES:
        crear_boton(farm, lambda f=farm: pantalla_detalle_farmacia(f)).pack(pady=3)
    crear_boton("Volver", pantalla_menu).pack(pady=20)

def pantalla_detalle_farmacia(nombre):
    datos = PHARMACIES.get(nombre, {})
    limpiar_ventana()
    tk.Label(ventana, text=nombre, font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)
    tk.Label(ventana, text=f"Horario: {datos.get('hours')}", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
    tk.Label(ventana, text=f"Dirección: {datos.get('address')}", font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)
    crear_boton("Ver en Google Maps", lambda: abrir_maps(nombre)).pack(pady=10)
    crear_boton("Volver", pantalla_menu).pack(pady=20)

def pantalla_ayuda():
    limpiar_ventana()
    tk.Label(ventana, text="Preguntas Frecuentes", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=15)
    canvas = tk.Canvas(ventana, bg=BG_COLOR, highlightthickness=0)
    frame = tk.Frame(canvas, bg=BG_COLOR)
    scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    for q, a in FAQ:
        tk.Label(frame, text="❓ " + q, font=("Arial", 12, "bold"), bg=BG_COLOR, fg=FG_COLOR, wraplength=400, justify="left").pack(anchor="w", pady=(10, 0))
        tk.Label(frame, text="→ " + a, font=FONT_LABEL, bg=BG_COLOR, fg=FG_COLOR, wraplength=400, justify="left").pack(anchor="w")
    crear_boton("Volver", pantalla_menu).pack(pady=10)

pantalla_inicio()
ventana.mainloop()
