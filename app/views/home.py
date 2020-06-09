from flask import Blueprint, render_template

bp = Blueprint('', __name__, url_prefix='', static_folder='../static')

# Load the index page
@bp.route('/')
def index():
    return render_template('home.html')