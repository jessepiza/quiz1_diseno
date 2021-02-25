class Command:
    def __init__(self):
        self.list_commands = ['Encender', 'Apagar', 'Hablar', 'Dormir']

    def execute(self, command):
        if command in self.list_commands:
            print(f"El comando recibido es {command} y es soportado. Se ejecutará.")
        else:
            print(f"El comando recibido no está soportado.")

    def register(self, command):
        self.list_commands.append(command)