import logging
import os
import sys
from PySide6 import QtCore, QtGui, QtWidgets, QtWebEngineCore

logger = logging.getLogger(__name__)


class DownloadWidget(QtWidgets.QProgressBar):
    finished = QtCore.Signal()
    remove_requested = QtCore.Signal()

    def __init__(self, download_request: QtWebEngineCore.QWebEngineDownloadRequest) -> None:
        super(DownloadWidget, self).__init__()
        self.download_request = download_request
        self._path = os.path.normpath(os.path.join(self.download_request.downloadDirectory(),
                                                   self.download_request.downloadFileName()))
        # logger.debug("Download path: %s" % self._path)
        self.download_request.receivedBytesChanged.connect(self._download_progress)
        self.download_request.stateChanged.connect(self._update_tool_tip())
        self.download_request.isFinishedChanged.connect(self._finished)

        self.setMaximumWidth(300)
        # Shorten the file name
        description = QtCore.QFileInfo(self._path).fileName()
        description_length = len(description)
        if description_length > 30:
            description = '{}...{}'.format(description[0:10], description[description_length - 10:])

        self.setFormat('{} %p%'.format(description))
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setMinimum(0)
        self.setValue(0)
        self.setMaximum(100)
        self._update_tool_tip()

        # Force progress bar text to be shown on macoS by using 'fusion' style
        if sys.platform == 'darwin':
            # noinspection PyCallByClass,PyTypeChecker
            self.setStyle(QtWidgets.QStyleFactory.create('fusion'))

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # noinspection PyUnresolvedReferences
        self.customContextMenuRequested.connect(self.context_menu_event)

    @classmethod
    def open_file(cls, file: str) -> None:
        # noinspection PyTypeChecker,PyCallByClass
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(file))

    @classmethod
    def open_download_directory(cls) -> None:
        path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DownloadLocation)
        cls.open_file(path)

    def _download_progress(self) -> None:
        received = self.download_request.receivedBytes()
        total = self.download_request.totalBytes()
        if total == -1:
            self.setValue(50)
        else:
            # logger.debug("Download %s/%s" % (received, total))
            self.setValue(int(100.0 * received / total))

    def _update_tool_tip(self) -> None:
        state = self.download_request.state()
        # logger.debug("Update %s" % state)

        tool_tip = "{}\n{}".format(self.download_request.url().toString(),
                                   QtCore.QDir.toNativeSeparators(self._path))
        total_bytes = self.download_request.totalBytes()
        if total_bytes > 0:
            tool_tip += "\n{}K".format(total_bytes / 1024)

        if state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadRequested:
            tool_tip += "\n(requested)"
        elif state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadInProgress:
            tool_tip += "\n(downloading)"
        elif state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadCompleted:
            tool_tip += "\n(completed)"
        elif state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadCancelled:
            tool_tip += "\n(cancelled)"
        else:
            tool_tip += "\n(interrupted)"

        self.setToolTip(tool_tip)

    def _finished(self) -> None:
        # logger.debug("Download finished")
        self._update_tool_tip()
        self.setValue(100)
        self.finished.emit()

    def _launch(self) -> None:
        self.open_file(self._path)

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:

        if self.download_request.state() == QtWebEngineCore.QWebEngineDownloadRequest.DownloadCompleted:
            self._launch()

        event.ignore()

    def context_menu_event(self, event: QtGui.QMouseEvent) -> None:
        state = self.download_request.state()
        context_menu = QtWidgets.QMenu()
        launch_action = context_menu.addAction("Launch")
        launch_action.setEnabled(state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadCompleted)
        show_in_folder_action = context_menu.addAction("Show in Folder")
        show_in_folder_action.setEnabled(state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadCompleted)
        cancel_action = context_menu.addAction("Cancel")
        cancel_action.setEnabled(state == QtWebEngineCore.QWebEngineDownloadRequest.DownloadInProgress)
        remove_action = context_menu.addAction("Remove")
        remove_action.setEnabled(state != QtWebEngineCore.QWebEngineDownloadRequest.DownloadInProgress)

        # noinspection PyTypeChecker
        chosen_action = context_menu.exec_(self.mapToGlobal(event))
        if chosen_action == launch_action:
            self._launch()
        elif chosen_action == show_in_folder_action:
            self.open_file(self._path)
        elif chosen_action == cancel_action:
            self.download_request.cancel()
        elif chosen_action == remove_action:
            # noinspection PyUnresolvedReferences
            self.remove_requested.emit()
