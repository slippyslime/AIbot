# Чат с ИИ на Django

Веб-приложение-чат: пользователь задаёт вопрос, приложение отправляет его в языковую модель через [OpenRouter](https://openrouter.ai) (бесплатные модели с суффиксом `:free`) и показывает ответ. Все вопросы и ответы сохраняются в базе, на странице видны последние 10.

## Запуск

Нужен Python 3.12+.

```bash
git clone github.com/slippyslime/AIbot
cd AIbot

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env             # и впишите свой OPENROUTER_API_KEY
python manage.py migrate
python manage.py runserver
```

Откройте http://127.0.0.1:8000/.
