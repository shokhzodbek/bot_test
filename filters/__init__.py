
from loader import dp
from .admin import AdminFilter
from .group import IsGroup
from .shaxsiy import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
