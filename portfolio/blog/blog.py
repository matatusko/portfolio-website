from flask import Blueprint
from flask import render_template

bp = Blueprint(
    name='blog', 
    import_name=__name__, 
    url_prefix='/blog',
    template_folder='templates',
    static_folder='static',
    static_url_path='/blogs/'
)

@bp.route('/')
def blogs():
    return render_template('blogs.html')
    
@bp.route('/<blog>')
def blog(blog):
    data = {
        'title': blog
    }
    return render_template('blog.html', data=data)