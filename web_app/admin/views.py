from flask import Blueprint,render_template
from web_app.user.decorators import admin_required
blueprint = Blueprint('admin',__name__,url_prefix="/admin")


@blueprint.route('/')
@admin_required
def admin_index():
    title = 'панель управления'
    return render_template('admin/index.html', page_text=title)