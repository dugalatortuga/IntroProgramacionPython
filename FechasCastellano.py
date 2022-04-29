from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

fechascastellano = datetime.now()

print(fechascastellano)
print("FECHA CASTELLANO:",fechascastellano.strftime("%A %d %b %Y"))

