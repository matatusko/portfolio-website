from flask import Blueprint
from flask import render_template
from portfolio.utils import load_json
from pathlib import Path

HERE = Path('blueprints/home/static/content')

bp = Blueprint(
    name='home', 
    import_name=__name__, 
    url_prefix='/',
    template_folder='templates',
    static_folder='static',
    static_url_path='/home/'
)

@bp.route('/')
def home():
    data = {
        'skills': load_json(HERE/'skills.json', key='skills'),
        'experience': load_json(HERE/'experience.json', key='experience')
    }

    return render_template('home.html', data=data)
