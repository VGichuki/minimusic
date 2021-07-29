from django import template as tt
import math
import pytz
import datetime

tt.Template('{{ x|time:"H:i:s" }}').render(tt.Context({'x': datetime.datetime.fromtimestamp(12345, pytz.utc)}))
u'03:25:45'

def time_formatter(time):
    time = int(time)
    minutes = math.floor((time%3600)/60)
    seconds = math.floor(time%60)

    if seconds<10:
        seconds = f'0{seconds}'
    return f'{minutes}:{seconds}'
    