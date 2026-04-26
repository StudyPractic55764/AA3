import ctypes
import sys


def relanzar_como_admin():

    #verificamos si el programa ya se está ejecutando con permisos de administrador
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True

    print("Solicitando permisos de administrador...")

    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        " ".join(sys.argv),
        None,
        1
    )

    return False

if not relanzar_como_admin():
    sys.exit()