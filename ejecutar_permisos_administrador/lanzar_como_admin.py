import ctypes
import sys


def relanzar_como_admin():
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