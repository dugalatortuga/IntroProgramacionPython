#ZONAS HORARIAS
from datetime import datetime
import pytz
from pytz import timezone
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))
