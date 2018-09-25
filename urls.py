from App.apis.BannerApi import BannerResource
from App.apis.CinemasApi import CinemasResource
from App.apis.MoviesApi import MoviesResource
from App.apis.MyPermissionApi import MyPermissionResource
from App.apis.PermissionApi import PermissionResource
from App.exts import api
from App.apis.CityApi import CityResource
from App.apis.UserRegisterApi import UserRegisterResource
from App.apis.AccountActiveApi import AccountActivateResource
from App.apis.UserLoginApi import UserLoginResource


api.add_resource(CityResource,'/city/')
api.add_resource(UserRegisterResource,'/urr/')
api.add_resource(AccountActivateResource,'/aar/')
api.add_resource(UserLoginResource,'/ulr/')
api.add_resource(PermissionResource,'/pr/')
api.add_resource(MyPermissionResource,'/mpr/')
api.add_resource(BannerResource,'/br/')

api.add_resource(MoviesResource,'/mr/')
api.add_resource(CinemasResource,'/cr/')
