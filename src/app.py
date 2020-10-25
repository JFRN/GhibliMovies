from flask import Flask, render_template_string
from ghibli import GhibliConsumer
import time
app = Flask(__name__)

Ghibli = GhibliConsumer()


@app.route('/')
def index() -> str:
    return 'Nothing to see here'


@app.route('/movies')
def movies() -> str:
    """
    TODO: Use templates instead of this
    """
    films = get_films_fixed()
    page = ''
    for film_id, film in films.items():
        page += f"{film['title']}</br>"
        for people_id, person in film['people'].items():
            page += f"&ensp;&ensp;{person['name']}</br>"
    return page


_last_time_fetched = 0
_last_films_fetched = None


def get_films_fixed():
    global _last_time_fetched
    global _last_films_fetched
    if time.time() - _last_time_fetched >= 60:
        _last_time_fetched = time.time()
        _last_films_fetched = Ghibli.get_films_fixed()
    return _last_films_fetched


if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)
