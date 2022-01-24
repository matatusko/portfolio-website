from flask import Blueprint
from flask import render_template

bp = Blueprint(
    name='home', 
    import_name=__name__, 
    url_prefix='/',
    template_folder='templates',
    static_folder='static',    
)

@bp.route('/')
def home():
    return render_template('home.html')