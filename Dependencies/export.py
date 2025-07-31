import os
import subprocess
from tkinter import filedialog, messagebox

def export_project_to_exe():
    """
    Usa PyInstaller para crear un ejecutable de la aplicación principal (main.py),
    incluyendo todos los archivos y carpetas del proyecto (como scripts, bases de datos, etc).
    Permite al usuario elegir la carpeta de destino para el .exe generado.
    """
    output_dir = filedialog.askdirectory(title="Selecciona la carpeta de destino del ejecutable")
    if not output_dir:
        return

    project_dir = os.path.dirname(os.path.abspath(__file__))
    main_script = os.path.join(project_dir, "main.py")

    add_data_args = []
    image_exts = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico')
    resource_exts = ('.py', '.sqlite', '.db', '.txt', '.xml', '.json', '.csv') + image_exts
    for root, dirs, files in os.walk(project_dir):
        for name in files:
            if name.endswith('.py') and os.path.abspath(os.path.join(root, name)) == os.path.abspath(main_script):
                continue
            if name.lower().endswith(resource_exts):
                file_path = os.path.join(root, name)
                rel_path = os.path.relpath(file_path, project_dir)
                add_data_args.append(f"{rel_path};{rel_path}")
        for name in dirs:
            dir_path = os.path.join(root, name)
            rel_path = os.path.relpath(dir_path, project_dir)
            if not rel_path.startswith('.'):
                add_data_args.append(f"{rel_path};{rel_path}")

    add_data_args = list(set(add_data_args))

    cmd = [
        "pyinstaller",
        "--onefile",
        f"--distpath={output_dir}",
    ]
    for data in add_data_args:
        cmd.extend(["--add-data", data.replace("/", os.sep).replace("\\", os.sep)])
    cmd.append(main_script)

    try:
        subprocess.run(cmd, check=True)
        messagebox.showinfo("Exportación exitosa", f"El ejecutable ha sido creado en: {output_dir}\n\nRecuerda que los archivos de datos estarán junto al .exe en la carpeta generada.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo crear el ejecutable.\n{e}")
