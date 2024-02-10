# what_to_watch/opinions_app/api_views.py

# Импортируем метод jsonify
from flask import jsonify

from . import app
from .models import Opinion


# Явно разрешить метод GET
@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    # Получить объект по id или выбросить ошибку
    opinion = Opinion.query.get_or_404(id)
    # Конвертировать данные в JSON и вернуть объект и код ответа API
    return jsonify({'opinion': opinion.to_dict()}), 200
