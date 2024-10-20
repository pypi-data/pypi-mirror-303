import logging
import os
from typing import Optional

from PySide6 import QtCore, QtGui, QtWidgets, QtWebEngineCore, QtWebEngineWidgets

from hyo2.abc2.app.browser.download_widget import DownloadWidget
from hyo2.abc2.app.pkg_info import app_info
from hyo2.abc2.lib.package.pkg_helper import PkgHelper

logger = logging.getLogger(__name__)


class WebEnginePage(QtWebEngineCore.QWebEnginePage):

    def javaScriptConsoleMessage(self, level, message, line_number, source_id):
        if ("slideshare" in source_id) or ("hydroffice.org" in source_id):
            return
        if "ch-ua-" in message:
            return

        logger.debug("QWebEngine: %s[#%d] -> %s" % (source_id, line_number, message))


class Browser(QtWidgets.QMainWindow):

    def __init__(self, parent: Optional[QtWidgets.QWidget] = None, url: str = "https://www.hydroffice.org") -> None:
        super().__init__(parent)

        self.setWindowTitle('Browser')

        self._actions = {}
        self._create_menu()

        self._tool_bar = QtWidgets.QToolBar()
        self._tool_bar.setIconSize(QtCore.QSize(16, 16))
        self.addToolBar(self._tool_bar)
        for action in self._actions.values():
            if not action.icon().isNull():
                self._tool_bar.addAction(action)

        self.address_line_edit = QtWidgets.QLineEdit()
        self.address_line_edit.setClearButtonEnabled(True)
        # noinspection PyUnresolvedReferences
        self.address_line_edit.returnPressed.connect(self._load)
        self._tool_bar.addWidget(self.address_line_edit)

        self.view = QtWebEngineWidgets.QWebEngineView()
        # self.view.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.PluginsEnabled, True)
        # self.view.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.FullScreenSupportEnabled, True)
        # self.view.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.AllowRunningInsecureContent, True)
        # self.view.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.SpatialNavigationEnabled, True)
        self.view.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.JavascriptEnabled, True)
        self.view.settings().setAttribute(QtWebEngineCore.QWebEngineSettings.JavascriptCanOpenWindows, True)
        self.view.settings().setAttribute(
            QtWebEngineCore.QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.view.settings().setAttribute(
            QtWebEngineCore.QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        # self.interceptor = RequestInterceptor()
        self.profile = QtWebEngineCore.QWebEngineProfile()
        # self.profile.setRequestInterceptor(self.interceptor)
        # noinspection PyUnresolvedReferences
        self.profile.downloadRequested.connect(self._download_requested)
        self.profile.setPersistentCookiesPolicy(QtWebEngineCore.QWebEngineProfile.NoPersistentCookies)
        self.profile.setHttpCacheType(QtWebEngineCore.QWebEngineProfile.NoCache)
        self.profile.setPersistentStoragePath(self._web_engine_folder())
        self.page = WebEnginePage(self.profile, self.view)
        self.view.setPage(self.page)

        # noinspection PyUnresolvedReferences
        self.view.page().titleChanged.connect(self.setWindowTitle)
        # noinspection PyUnresolvedReferences
        self.view.page().urlChanged.connect(self._url_changed)
        self.setCentralWidget(self.view)

        self.change_url(url=url)

    @classmethod
    def _web_engine_folder(cls) -> str:
        dir_path = os.path.abspath(os.path.join(PkgHelper(pkg_info=app_info).hydroffice_folder(), "WebEngine"))
        if not os.path.exists(dir_path):  # create it if it does not exist
            os.makedirs(dir_path)
        return dir_path

    def _create_menu(self) -> None:
        style_icons = ':/qt-project.org/styles/commonstyle/images/'

        # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
        back_action = QtGui.QAction(QtGui.QIcon.fromTheme("go-previous", QtGui.QIcon(style_icons + 'left-32.png')),
                                    "Back", self, shortcut=QtGui.QKeySequence(QtGui.QKeySequence.Back),
                                    triggered=self.back)

        self._actions[QtWebEngineCore.QWebEnginePage.Back] = back_action

        # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
        forward_action = QtGui.QAction(QtGui.QIcon.fromTheme("go-next", QtGui.QIcon(style_icons + 'right-32.png')),
                                       "Forward", self, shortcut=QtGui.QKeySequence(QtGui.QKeySequence.Forward),
                                       triggered=self.forward)
        self._actions[QtWebEngineCore.QWebEnginePage.Forward] = forward_action

        # noinspection PyArgumentList
        reload_action = QtGui.QAction(QtGui.QIcon(style_icons + 'refresh-32.png'), "Reload", self,
                                      shortcut=QtGui.QKeySequence(QtGui.QKeySequence.Refresh),
                                      triggered=self.reload)
        self._actions[QtWebEngineCore.QWebEnginePage.Reload] = reload_action

    def change_url(self, url: str) -> None:
        self.address_line_edit.setText(url)
        self._load()

    def url(self) -> str:
        return self.address_line_edit.text()

    def _load(self) -> None:
        url = QtCore.QUrl.fromUserInput(self.address_line_edit.text().strip())
        if url.isValid():
            self.view.load(url)

    def back(self) -> None:
        self.view.page().triggerAction(QtWebEngineCore.QWebEnginePage.Back)

    def forward(self) -> None:
        self.view.page().triggerAction(QtWebEngineCore.QWebEnginePage.Forward)

    def reload(self) -> None:
        self.view.page().triggerAction(QtWebEngineCore.QWebEnginePage.Reload)

    def _url_changed(self, url: QtCore.QUrl) -> None:
        self.address_line_edit.setText(url.toString())

    def _download_requested(self, item: QtWebEngineCore.QWebEngineDownloadRequest) -> None:

        # Remove old downloads before opening a new one
        for old_download in self.statusBar().children():
            if type(old_download).__name__ != 'DownloadWidget':
                continue
            if old_download.download_request.state() != QtWebEngineCore.QWebEngineDownloadRequest.DownloadInProgress:
                self.statusBar().removeWidget(old_download)
                del old_download

        item.accept()
        download_widget = DownloadWidget(item)
        download_widget.remove_requested.connect(self._remove_download_requested, QtCore.Qt.QueuedConnection)

        self.statusBar().addWidget(download_widget)

    def _remove_download_requested(self):
        download_widget = self.sender()
        self.statusBar().removeWidget(download_widget)
        del download_widget
