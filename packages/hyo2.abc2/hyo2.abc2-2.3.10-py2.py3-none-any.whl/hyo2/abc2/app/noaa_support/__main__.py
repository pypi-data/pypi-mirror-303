import logging
import os
import sys
from PySide6 import QtWidgets, QtGui

from hyo2.abc2.app.noaa_support.noaa_s57_dialog import NOAAS57Dialog
from hyo2.abc2.app.noaa_support import app_info
from hyo2.abc2.app.app_style.app_style import AppStyle

logger = logging.getLogger()


def set_logging(default_logging=logging.WARNING, hyo2_logging=logging.INFO, abc_logging=logging.DEBUG):
    logging.basicConfig(
        level=default_logging,
        format="%(levelname)-9s %(name)s.%(funcName)s:%(lineno)d > %(message)s"
    )
    logging.getLogger("hyo2").setLevel(hyo2_logging)
    logging.getLogger("hyo2.abc2").setLevel(abc_logging)


set_logging()

app = QtWidgets.QApplication([])
app.setApplicationName('NOAA S57')
app.setOrganizationName("HydrOffice")
app.setOrganizationDomain("hydroffice.org")
AppStyle.apply(app=app)

d = NOAAS57Dialog(app_info=app_info)
d.setWindowIcon(QtGui.QIcon(app_info.app_icon_path))
d.show()

sys.exit(app.exec())
