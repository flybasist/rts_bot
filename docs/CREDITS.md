# Сторонние компоненты

rts_bot не содержит чужого кода: репозиторий состоит из исходников автора под лицензией GPLv3. Всё перечисленное ниже
устанавливается отдельно (`pip install`) и в репозиторий не входит. Список версий не зафиксирован.

## Python и библиотеки

| Компонент | Зачем | Условия |
|---|---|---|
| Python 3 | Среда выполнения | Python Software Foundation License |
| [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (`telebot`) | Работа с Telegram Bot API | GPLv2 |
| [PyYAML](https://pyyaml.org/) | Чтение `settings.yaml` | MIT |
| [schedule](https://github.com/dbader/schedule) | Расписание стикеров по будням | MIT |
| SQLite (`sqlite3` из стандартной библиотеки Python) | Хранение данных | Общественное достояние |

Условия проверяйте у авторов библиотек: они определяются ими.

## Telegram

Бот работает через Telegram Bot API. rts_bot не связан с Telegram и не одобрен им.
