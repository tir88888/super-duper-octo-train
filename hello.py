locations_data = {
    "start": {
        "description": "Вы стоите на перекрестке выбора... Куда вы хотите пойти?\n1) backend\n2) frontend\n3) Пойду гуглить, что такое IT",
        "options": {"1": "backend", "2": "frontend", "3": "google"},
        "picture": "pictures/1.jpg"
    },
    "backend": {
        "description": "Вы решили идти в backend\n1) Учиться дальше\n2) Вернуться на перекресток",
        "options": {"1": "deep_backend", "2": "start"},
        "picture": "pictures/2.jpg"
    },
    "deep_backend": {
        "description": "Кажется, вы столкнулись с струдностями в обучении...\n1) Продолжу учиться!\n2) Подумаю...",
        "options": {"1": "find_path", "2": "backend"},
        "picture": "pictures/3.jpg"
    },
    "find_path": {
        "description": "Поздравляю, вы смогли повысить свой ранг до backend Middle!",
        "options": {},
        "picture": "pictures/win.jpg"
    },
    "frontend": {
        "description": "Вы решили идти frontend\n1) Мне нравится:)\n2) Скучно, пойду изучать кибербезопасность:)\n3) Вернуться на перекресток",
        "options": {"1": "kaif", "2": "wasted", "3": "start"},
        "picture": "pictures/4.jpg"
    },
    "kaif": {
        "description": "Вы почти освоили навыки Junior! Ваши действия?\n1) Продолжу обучение:)\n2) Не мое:(",
        "options": {"1": "approach_kaif", "2": "frontend"},
        "picture": "pictures/5.jpg"
    },
    "approach_kaif": {
        "description": "УРА, вы смогли стать frontend Middle",
        "options": {},
        "picture": "pictures/win.jpg"
    },
    "wasted": {
        "description": "Вам надоело заниматься IT...\n1) Устал...\n2) Нет, не буду сидеть на двух стульях!",
        "options": {"1": "explore_wasted", "2": "frontend"},
        "picture": "pictures/6.jpg"
    },
    "explore_wasted": {
        "description": "УВЫ, вы забили на обучение и потеряли  свои навыки да и ещё заработали апатию и выгорание...",
        "options": {},
        "picture": "pictures/7.jpg"
    },
    "google": {
        "description": "Вы начали читать новости...\n1) Ну, давайте почитаем\n2) Я подумаю о своем выборе",
        "options": {"1": "talk_to_google", "2": "start"},
        "picture": "pictures/8.jpg"
    },
    "talk_to_google": {
        "description": "Аааа, ужас! IT-рынок рушится!, программистов на мясо!, теперь их заменит искусственный интеллект!\n :| Не спасибо, пойду скачивать взломанный Сбербанк и абузить темки...",
        "options": {},
        "picture": "pictures/9.jpg"
    }
}