from flask import Blueprint
from flask import render_template

bp = Blueprint(
    name='projects', 
    import_name=__name__, 
    url_prefix='/projects',
    template_folder='templates',
    static_folder='static',    
)

@bp.route('/')
def projects():
    return render_template('projects.html')

@bp.route('/<project_name>')
def project(project_name):
    data = {
        'title': project_name
    }
    return render_template('project.html', data=data)