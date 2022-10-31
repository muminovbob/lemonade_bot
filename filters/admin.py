import typing

from aiogram.dispatcher.filters import BoundFilter
from config import ADMINS


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return False
        return (str(obj.from_user.id) in ADMINS.split()) == self.is_admin
