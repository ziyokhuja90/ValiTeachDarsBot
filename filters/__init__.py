from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . import Admin

if __name__ == "filters":
    dp.filters_factory.bind(Admin.AdminFilter)
    pass
