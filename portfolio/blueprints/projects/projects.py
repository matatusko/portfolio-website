from flask import Blueprint
from flask import render_template
from portfolio.utils import get_files_from_path, load_json 
from pathlib import Path
from flask import current_app

HERE = Path('blueprints/projects/static/content')

bp = Blueprint(
    name='projects', 
    import_name=__name__, 
    url_prefix='/projects',
    template_folder='templates',
    static_folder='static',
    static_url_path='/projects/'
)

@bp.route('/')
def projects():
    files = get_files_from_path(HERE, ext='.json')
    projects = [load_json(HERE/file) for file in files]
    return render_template('projects.html', projects=projects)

@bp.route('/<project_name>')
def project(project_name):
    file = project_name + '.json'
    project = load_json(HERE/file)
    return render_template('project.html', project=project)