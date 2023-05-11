'''
userrole - specific user/role management for this application

This is needed to update local database tables when using common users database
'''

# homegrown
from webmodules import user_datastore
from ...model import update_local_tables
from ...version import __docversion__
from loutilities.user.views.userrole import UserView, InterestView, RoleView

superadminguide = f'https://webmodules.readthedocs.io/en/{__docversion__}/super-admin-guide.html'

class LocalUserView(UserView):
    def editor_method_postcommit(self, form):
        update_local_tables()
user_view = LocalUserView(
    pagename='users',
    user_datastore=user_datastore,
    roles_accepted=['super-admin'],
    endpoint='userrole.users',
    rule='/users',
    templateargs={'adminguide': superadminguide},
)
user_view.register()

class LocalInterestView(InterestView):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        args = dict(
            templateargs={'adminguide': superadminguide},
        )
        args.update(kwargs)

        # initialize inherited class, and a couple of attributes
        super().__init__(**args)

    def editor_method_postcommit(self, form):
        update_local_tables()
interest_view = LocalInterestView()
interest_view.register()

class LocalRoleView(RoleView):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        args = dict(
            templateargs={'adminguide': superadminguide},
        )
        args.update(kwargs)

        # initialize inherited class, and a couple of attributes
        super().__init__(**args)

    def editor_method_postcommit(self, form):
        update_local_tables()
role_view = LocalRoleView()
role_view.register()
