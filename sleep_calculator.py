from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def calculate_wakeup_time(bedtime):
    # Obtener la hora actual
    now = datetime.now()

    # Convertir la hora de dormir a un objeto de tipo datetime
    bedtime = datetime.strptime(bedtime, '%H:%M')

    # Calcular la duración del sueño mínimo (6 horas) y máximo (8 horas)
    min_sleep_duration = timedelta(hours=6)
    max_sleep_duration = timedelta(hours=8)

    # Calcular la hora de despertar mínima y máxima sumando la duración del sueño al tiempo de dormir
    wakeup_time_min = (bedtime + min_sleep_duration).strftime('%H:%M')
    wakeup_time_max = (bedtime + max_sleep_duration).strftime('%H:%M')

    return wakeup_time_min, wakeup_time_max

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        bedtime_input = request.form['bedtime']
        wakeup_time_min, wakeup_time_max = calculate_wakeup_time(bedtime_input)
        return render_template('index.html', wakeup_time_min=wakeup_time_min, wakeup_time_max=wakeup_time_max)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
