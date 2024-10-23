from argparse import ArgumentParser
from subprocess import run


def update_dependencies(verbose=False):
    result = run("pip list", shell=True, capture_output=True, text=True)

    output = result.stdout

    lines = output.splitlines()[2:]

    column = [line.split()[0] for line in lines]

    command = "pip install --upgrade "

    for package in column:
        command += f"{package} "

    print("Actualizando paquetes.")

    result = run(command, shell=True, capture_output=verbose, text=True)

    print("Paquetes actualizados con éxito.")


def main():
    parser = ArgumentParser(description='Actualice todas las dependencias instaladas con pip.')

    parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0.0', help='Mostrar el número de versión del programa y salir.')
    parser.add_argument('-V', '--verbose', action='store_true', default=False, help='Mostrar más información al ejecutar el programa.')
    
    args = parser.parse_args()
    
    update_dependencies(not args.verbose)