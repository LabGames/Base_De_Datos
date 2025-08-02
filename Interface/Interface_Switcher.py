from .Interface_system import FormularioClientes
from .Interface_system_2 import FormularioTareas

class InterfaceSwitcher:
    def __init__(self, root):
        self.root = root
        self.db = None
        self.current_interface = None

    def set_db(self, db):
        self.db = db

    def show_clientes(self):
        if self.current_interface:
            self.current_interface.destruir_interface()
        self.current_interface = FormularioClientes(self.db, self)
        self.current_interface.Formulario(self.root)

    def show_tareas(self):
        if self.current_interface:
            self.current_interface.destruir_interface()
        self.current_interface = FormularioTareas(self.db, self)
        self.current_interface.Formulario_2(self.root)

    def set_size(x, y):
        if 'FormularioClientes' in globals() and hasattr(FormularioClientes, 'set_screen_size'):
            FormularioClientes.set_screen_size(x, y)
            
        if 'FormularioTareas' in globals() and hasattr(FormularioTareas, 'set_screen_size'):
            FormularioTareas.set_screen_size(x, y)