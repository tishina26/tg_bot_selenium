# tg_bot_selenium
это реализация телеграм бота, который ухаживает  за лошадьми в интерет игре Lowadi. Бот нужен для дистанционного запуска автоматического ухода, причем есть возможность запустить для разных аккаунтов (если разные люди используют бота, вводя свои логины и пароли)
файл test_bot.py отвечает за сам телеграм бот - задает вопросы, принимает ответы, потом импортирует функцию main из второго файла new_functions.py, которая отвечает за свзять с интернет игрой, используя библиотеку Selenium.