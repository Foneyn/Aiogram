import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Ваш API ключ для сервиса погоды (например, OpenWeatherMap)
WEATHER_API_KEY = 'ваш_ключ_погоды'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Функция для получения прогноза погоды
def get_weather(city):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"Температура в {city}: {temperature}°C\nУсловия: {description}"
    else:
        return "Не удалось получить прогноз погоды. Проверьте имя города."

    # Обработчик команды /start
    def start(update: Update, context: CallbackContext):
        update.message.reply_text('Привет! Я бот прогноза погоды. Используйте команду /weather, чтобы узнать погоду.')

    # Обработчик команды /help
    def help_command(update: Update, context: CallbackContext):
        update.message.reply_text('Используйте /weather <город>, чтобы узнать погоду.')

    # Обработчик команды /weather
    def weather(update: Update, context: CallbackContext):
        city = ' '.join(context.args)
        if not city:
            update.message.reply_text('Пожалуйста, укажите город после команды /weather.')
        else:
            weather_report = get_weather(city)
            update.message.reply_text(weather_report)

    def main():
        # Создайте экземпляр Updater и передайте токен вашего бота
        updater = Updater("ваш_токен_бота")

        # Получите диспетчер для регистрации обработчиков
        dispatcher = updater.dispatcher

        # Зарегистрируйте обработчики команд
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(CommandHandler("weather", weather))

        # Начните поллинг
        updater.start_polling()

        # Работайте, пока не будет получен сигнал для остановки
        updater.idle()

    if __name__ == '__main__':
        main()
