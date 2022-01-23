from flask import Blueprint
from flask import render_template, request, redirect, url_for

bp = Blueprint(
    name='blog', 
    import_name=__name__, 
    url_prefix='/blog',
    template_folder='templates',
    static_folder='static',
)

@bp.route('/')
def blogs():
    return render_template('blogs.html')
    
@bp.route('/<blog>')
def blog(blog):
    data = {
        'title': 'First post!'
    }
    return render_template('blog.html', data=data)