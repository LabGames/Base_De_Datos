from .Interface_system import FormularioClientes
from .Interface_system_2 import FormularioTareas

class InterfaceSwitcher:
    def show_clientes(self):
        if self.current_interface:
            self.current_interface.destruir_interface()
        self.current_interface = FormularioClientes(self.db)
        self.current_interface.Formulario(self.root)

    def show_tareas(self):
        if self.current_interface:
            self.current_interface.destruir_interface()
        self.current_interface = FormularioTareas(self.db)
        self.current_interface.Formulario_2(self.root)
