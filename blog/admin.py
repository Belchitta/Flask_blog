from flask import url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect

from blog.models.tag import Tag
from blog.models.user import User
from blog.models.article import Article

from blog.extensions import db


class CustomView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_app.login'))


class TagAdminView(CustomView):
    column_searchable_list = ('name',)
    column_filters = ('name',)
    can_export = True
    export_types = ['csv, xlsx']
    create_modal = True
    edit_modal = True


class UserAdminView(CustomView):
    column_exclude_list = ('password',)
    column_details_exclude_list = ('password',)
    column_export_exclude_list = ('password',)
    column_searchable_list = ('first_name', 'last_name', 'username', 'is_staff', 'email')
    column_filters = ('first_name', 'last_name', 'username', 'is_staff', 'email')
    column_editable_list = ('first_name', 'last_name', 'is_staff')
    can_create = True
    can_edit = True
    can_delete = False


class ArticleAdminView(CustomView):
    can_export = True
    export_types = ('csv', 'xlsx')
    column_filters = ('author_id',)


class MyAdminIndexView(AdminIndexView):

    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth_app.login'))
        return super(MyAdminIndexView, self).index()


admin = Admin(
    name='Blog Admin',
    index_view=MyAdminIndexView(),
    template_mode='bootstrap4',
)

admin.add_view(TagAdminView(Tag, db.session, category='Models'))
admin.add_view(UserAdminView(User, db.session, category='Models'))
admin.add_view(ArticleAdminView(Article, db.session, category='Models'))
