from django.utils.translation import gettext_lazy as _

from netbox.registry import registry
from netbox.navigation import *
from netbox.navigation.menu import MENUS


PHONE = Menu(
    label=_('Phone'),
    icon_class="mdi mdi-phone",
    groups=(
        MenuGroup(
            label=_('Phone'),
            items=(
                MenuItem(
                    link=f'plugins:sop_phone:phoneinfo_list',
                    link_text=_('Informations'),
                    permissions=[f'sop_phone.view_phoneinfo'],
                    buttons=(
                        MenuItemButton(
                            link=f'plugins:sop_phone:phoneinfo_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phoneinfo'],
                        ),
                    ),
                ),
                MenuItem(
                    link=f'plugins:sop_phone:phonedelivery_list',
                    link_text=_('Deliveries'),
                    permissions=[f'sop_phone.view_phonedelivery'],
                    buttons=(
                        MenuItemButton(
                            link=f'plugins:sop_phone:phonedelivery_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phonedelivery'],
                        ),
                    ),
                ),
                MenuItem(
                    link=f'plugins:sop_phone:phonedid_list',
                    link_text=_('DIDs'),
                    permissions=[f'sop_phone.view_phonedid'],
                    buttons=(
                        MenuItemButton(
                            link=f'plugins:sop_phone:phonedid_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phonedid'],
                        ),
                        MenuItemButton(
                            link=f'plugins:sop_phone:phonedid_import',
                            title='Import',
                            icon_class='mdi mdi-upload',
                            permissions=[f'sop_phone.add_phonedid'],
                        ),
                    ),
                ),
                MenuItem(
                    link=f'plugins:sop_phone:phonemaintainer_list',
                    link_text=_('Maintainers'),
                    permissions=[f'sop_phone.view_phonemaintainer'],
                    buttons=(
                        MenuItemButton(
                            link=f'plugins:sop_phone:phonemaintainer_add',
                            title='Add',
                            icon_class='mdi mdi-plus-thick',
                            permissions=[f'sop_phone.add_phonemaintainer'],
                        ),
                        MenuItemButton(
                            link=f'plugins:sop_phone:phonemaintainer_import',
                            title='Import',
                            icon_class='mdi mdi-upload',
                            permissions=[f'sop_phone.add_phonemaintainer'],
                        ),
                    ),
                ),
            ),
        ),
    ),
)

MENUS.append(PHONE)
