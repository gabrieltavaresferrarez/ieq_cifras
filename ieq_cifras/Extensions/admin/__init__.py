from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from ieq_cifras.Extensions.database import database
from ieq_cifras.models import User, Band, RegAuditCifra, ComposicaoBand, Cifra

from sqlalchemy import inspect


admin = Admin(name='microblog', template_mode='bootstrap3')

class UserModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    column_searchable_list = ['username', 'email']
    column_editable_list = ['username']

    column_list = [c_attr.key for c_attr in inspect(User).mapper.column_attrs]
    column_exclude_list = ['password', ]


class BandModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    column_hide_backrefs = True
    column_searchable_list = ['name']
    column_editable_list = ['name']

class CifraModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    column_hide_backrefs = True

    column_searchable_list = ['name', 'author']
    column_editable_list = ['name', 'author', 'tom']

    column_list = [c_attr.key for c_attr in inspect(Cifra).mapper.column_attrs]

class ComposicaoBandModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    column_searchable_list = ['id_band', 'id_user']
    column_editable_list = ['id_band', 'id_user']

class RegAuditCifraModelView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

def init_app(app):
    admin.init_app(app)
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin.add_view(UserModelView(User, database.session, name='Users', endpoint='user_admin'))
    admin.add_view(CifraModelView(Cifra, database.session, name='Cifras', endpoint='cifra_admin'))
    admin.add_view(BandModelView(Band, database.session, name='Bands', endpoint='band_admin'))
    admin.add_view(ComposicaoBandModelView(ComposicaoBand, database.session, name='Composição Bands', endpoint='composicao_admin'))
    admin.add_view(RegAuditCifraModelView(RegAuditCifra, database.session, name='Registro Cifras', endpoint='regCifra_admin'))