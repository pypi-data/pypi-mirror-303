from PySide6 import QtWidgets

import logging

from hyo2.abc2.lib.package.pkg_info import PkgInfo

logger = logging.getLogger(__name__)


class LicenseTab(QtWidgets.QWidget):

    def __init__(self, app_info: PkgInfo, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self._ai = app_info

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.text = QtWidgets.QTextBrowser()
        self.text.setObjectName("LicenseTextBrowser")
        self.text.setReadOnly(True)
        self.text.setLineWrapMode(QtWidgets.QTextBrowser.NoWrap)
        self.text.setMinimumWidth(200)
        with open(self._ai.app_license_path, "r") as fid:
            self.text.setText(fid.read())
        self.layout.addWidget(self.text)
