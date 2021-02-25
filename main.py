from command import Command

bot = Command()
bot.execute('Encender') # Soportado
bot.execute('Comer') # No soportado

bot.register('Comer') # Agregamos
bot.execute('Comer')