import logging

from PySide6 import QtWidgets

from hyo2.abc2.app.app_style.app_style import AppStyle
from hyo2.abc2.lib.package.pkg_helper import PkgHelper
from hyo2.abc2.lib.package.pkg_info import PkgInfo

logger = logging.getLogger(__name__)


class GeneralInfoTab(QtWidgets.QWidget):

    def __init__(self, app_info: PkgInfo, parent: QtWidgets.QWidget = None, with_ocs_email: bool = False):
        super().__init__(parent)
        self._ai = app_info

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.text = QtWidgets.QTextBrowser()
        self.text.setReadOnly(True)
        self.text.setMinimumWidth(200)
        self.text.setOpenLinks(True)
        self.text.setOpenExternalLinks(True)
        self.text.document().setDefaultStyleSheet(AppStyle.html_css())
        self.text.setHtml(PkgHelper(pkg_info=app_info).pkg_info(qt_html=True, with_ocs_email=with_ocs_email))
        self.layout.addWidget(self.text)
