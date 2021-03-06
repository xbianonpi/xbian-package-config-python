import resources.lib.translation
_ = resources.lib.translation.language.gettext

DATA = {
    "title": _("Update XBian"),
    "smalltitle": _("update"),
    "description": _("You can now choose how XBian will be updated and how "
                     "often to check for updates.[CR][CR]By default, XBian "
                     "will not be updated automatically, but you will be "
                     "advised when a new update is available.[CR][CR]"
                     "To update go to System -> XBian -> Update and select "
                     "the packages to upgrade.[CR][CR]If you wish XBian to "
                     "be updated automatically, you can set it now."),
    "action": [
        'categories.40_update.UpdateLabel',
        'categories.40_update.InventoryIntGui',
        'categories.40_update.updateAuto',
        'categories.40_update.snapAPT',
        'categories.40_update.updatePackageLabel',
        'categories.40_update.packageUpdate',
    ],
}
