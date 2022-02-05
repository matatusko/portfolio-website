from flask import Blueprint
from flask import render_template
from portfolio.utils import load_json

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
    return render_template('home.html')
