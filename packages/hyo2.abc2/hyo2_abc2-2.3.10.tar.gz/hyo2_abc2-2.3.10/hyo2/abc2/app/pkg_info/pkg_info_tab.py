import logging
import os
from typing import Optional

from PySide6 import QtCore, QtGui, QtWidgets

from hyo2.abc2.app.browser.browser import Browser
from hyo2.abc2.app.noaa_support.noaa_s57_dialog import NOAAS57Dialog
from hyo2.abc2.app.pkg_info.pkg_about.pkg_about_dialog import PkgAboutDialog
from hyo2.abc2.lib.package.pkg_helper import PkgHelper
from hyo2.abc2.lib.package.pkg_info import PkgInfo

logger = logging.getLogger(__name__)


class PkgInfoTab(QtWidgets.QMainWindow):
    media = os.path.join(os.path.dirname(__file__), "media")

    def __init__(self, main_win: QtWidgets.QMainWindow,
                 app_info: PkgInfo,
                 tab_name: str = "App Info Tab", start_url: Optional[str] = None,
                 default_url: str = "https://www.hydroffice.org",
                 with_online_manual: bool = False,
                 with_offline_manual: bool = False,
                 with_bug_report: bool = False,
                 with_hydroffice_link: bool = False,
                 with_ccom_link: bool = False,
                 with_noaa_link: bool = False,
                 with_unh_link: bool = False,
                 with_license: bool = False,
                 with_noaa_57: bool = False,
                 with_ocs_email: bool = False
                 ):
        super().__init__(main_win)
        self.main_win = main_win
        self._with_ocs_email = with_ocs_email
        self._ai = app_info
        self.defaul_url = default_url
        self.settings = QtCore.QSettings()

        self.setWindowTitle(tab_name)
        self.setContentsMargins(0, 0, 0, 0)

        # add main frame and layout
        self.frame = QtWidgets.QFrame(parent=self)
        self.setCentralWidget(self.frame)
        self.frame_layout = QtWidgets.QVBoxLayout()
        self.frame.setLayout(self.frame_layout)

        if start_url is None:
            start_url = PkgHelper(pkg_info=self._ai).web_url()
        self.start_url = start_url

        # add browser
        if self._has_qt_web_engine_process():
            self.browser = Browser(url=self.start_url)
            self.frame_layout.addWidget(self.browser)
        else:
            self.browser = None

        # add about dialog
        self.about_dlg = PkgAboutDialog(app_info=self._ai, parent=self,
                                        with_locale_tab=True, with_gdal_tab=True, with_ocs_email=self._with_ocs_email)
        self.about_dlg.hide()

        icon_size = QtCore.QSize(self._ai.app_toolbars_icon_size, self._ai.app_toolbars_icon_size)

        # noinspection PyArgumentList
        self.toolbar = self.addToolBar('Shortcuts')
        self.toolbar.setIconSize(icon_size)

        # home
        self.home_action = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'home.png')), 'Home page', self)
        # noinspection PyUnresolvedReferences
        self.home_action.triggered.connect(self.load_default)
        self.toolbar.addAction(self.home_action)

        # online manual
        self.open_online_manual_action = None
        if with_online_manual:
            self.open_online_manual_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'online_manual.png')), 'Online Manual', self)
            self.open_online_manual_action.setStatusTip('Open the online manual')
            # noinspection PyUnresolvedReferences
            self.open_online_manual_action.triggered.connect(self.open_online_manual)
            self.toolbar.addAction(self.open_online_manual_action)

        # offline manual
        self.open_offline_manual_action = None
        if with_offline_manual:
            self.open_offline_manual_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'offline_manual.png')), 'Offline Manual', self)
            self.open_offline_manual_action.setStatusTip('Open the offline manual')
            # noinspection PyUnresolvedReferences
            self.open_offline_manual_action.triggered.connect(self.open_offline_manual)
            self.toolbar.addAction(self.open_offline_manual_action)

        # bug report
        self.fill_bug_report_action = None
        if with_bug_report:
            self.fill_bug_report_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'bug.png')), 'Bug Report', self)
            self.fill_bug_report_action.setStatusTip('Fill a bug report')
            # noinspection PyUnresolvedReferences
            self.fill_bug_report_action.triggered.connect(self.fill_bug_report)
            self.toolbar.addAction(self.fill_bug_report_action)

        self.toolbar.addSeparator()

        # HydrOffice.org
        self.hyo_action = None
        if with_hydroffice_link:
            self.hyo_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'hyo.png')), 'HydrOffice.org', self)
            # noinspection PyUnresolvedReferences
            self.hyo_action.triggered.connect(self.load_hydroffice_org)
            self.toolbar.addAction(self.hyo_action)

        # noaa
        self.noaa_action = None
        if with_noaa_link:
            self.noaa_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'noaa.png')), 'nauticalcharts.noaa.gov', self)
            # noinspection PyUnresolvedReferences
            self.noaa_action.triggered.connect(self.load_noaa_ocs_gov)
            self.toolbar.addAction(self.noaa_action)

        # ccom.unh.edu
        self.ccom_action = None
        if with_ccom_link:
            self.ccom_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'ccom.png')), 'ccom.unh.edu', self)
            # noinspection PyUnresolvedReferences
            self.ccom_action.triggered.connect(self.load_ccom_unh_edu)
            self.toolbar.addAction(self.ccom_action)

        # unh.edu
        self.unh_action = None
        if with_unh_link:
            self.unh_action = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'unh.png')), 'unh.edu', self)
            # noinspection PyUnresolvedReferences
            self.unh_action.triggered.connect(self.load_unh_edu)
            self.toolbar.addAction(self.unh_action)

        self.toolbar.addSeparator()

        self.noaa_support_action = None
        if with_noaa_57:
            # noaa support
            self.toolbar.addSeparator()
            self.noaa_support_action = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'noaa_support.png')),
                                                     'NOAA S57 Support Files', self)
            # noinspection PyUnresolvedReferences
            self.noaa_support_action.triggered.connect(self.show_noaa_support)
            self.toolbar.addAction(self.noaa_support_action)

        self.toolbar.addSeparator()

        # license
        self.license_action = None
        if with_license:
            self.license_action = QtGui.QAction(
                QtGui.QIcon(os.path.join(self.media, 'license.png')), 'License', self)
            self.license_action.setStatusTip('License info')
            # noinspection PyUnresolvedReferences
            self.license_action.triggered.connect(self.load_license)
            self.toolbar.addAction(self.license_action)

        # authors
        self.authors_dialog = None
        self.authors_action = QtGui.QAction(QtGui.QIcon(os.path.join(self.media, 'authors.png')), 'Contacts', self)
        self.authors_action.setStatusTip('Contact Authors')
        # noinspection PyUnresolvedReferences
        self.authors_action.triggered.connect(self.show_authors)
        self.toolbar.addAction(self.authors_action)

        # about
        self.show_about_action = QtGui.QAction(QtGui.QIcon(self._ai.app_icon_path), 'About', self)
        self.show_about_action.setStatusTip('Info about %s' % app_info.app_name)
        # noinspection PyUnresolvedReferences
        self.show_about_action.triggered.connect(self.about_dlg.switch_visible)
        self.toolbar.addAction(self.show_about_action)

    @classmethod
    def _has_qt_web_engine_process(cls) -> bool:
        # noinspection PyArgumentList
        exe_path = os.path.abspath(QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.LibraryExecutablesPath))
        # FIXME: workaround for Pydro22's qt.conf
        if "Library" in exe_path:
            return False
        if not os.path.exists(exe_path):
            logger.error("Unable to locate the path to Qt executables: %s" % exe_path)
            return False

        wep_exe = os.path.join(exe_path, "QtWebEngineProcess.exe")
        if not os.path.exists(wep_exe):
            logger.error("Unable to locate QtWebEngineProcess.exe: %s" % wep_exe)
            return False

        logger.info("Running %s" % wep_exe)
        return True

    # ### ICON RESIZE ###

    def set_toolbars_icon_size(self, icon_size: int) -> None:
        self.toolbar.setIconSize(QtCore.QSize(icon_size, icon_size))

    # ### ACTIONS ###

    def load_default(self) -> None:
        if self.browser:
            self.browser.change_url(self.defaul_url)

    def open_online_manual(self) -> None:
        logger.debug("open online manual")
        PkgHelper.explore_folder(self._ai.app_manual_url)

    def open_offline_manual(self) -> None:
        logger.debug("open offline manual")
        pdf_path = os.path.join(self._ai.app_media_path, "manual.pdf")
        if not os.path.exists(pdf_path):
            logger.warning("unable to find offline manual at %s" % pdf_path)
            return

        PkgHelper.explore_folder(pdf_path)

    @classmethod
    def fill_bug_report(cls) -> None:
        logger.debug("fill bug report")
        raise RuntimeError("USER")

    def load_hydroffice_org(self):
        if self.browser:
            self.browser.change_url('https://www.hydroffice.org')

    @classmethod
    def load_noaa_ocs_gov(cls):
        url = 'https://www.nauticalcharts.noaa.gov/'
        PkgHelper.explore_folder(url)

    @classmethod
    def load_ccom_unh_edu(cls):
        url = 'https://ccom.unh.edu'
        PkgHelper.explore_folder(url)

    @classmethod
    def load_unh_edu(cls):
        url = 'https://www.unh.edu'
        PkgHelper.explore_folder(url)

    @classmethod
    def load_ausseabed_gov_au(cls):
        url = 'https://www.ausseabed.gov.au/'
        PkgHelper.explore_folder(url)

    def show_noaa_support(self):
        self.change_url(PkgHelper(pkg_info=self._ai).web_url("noaa_support"))
        noaa_s57 = NOAAS57Dialog(parent=self, app_info=self._ai)
        noaa_s57.exec_()

    def load_license(self):
        if self.browser:
            self.browser.change_url('https://www.hydroffice.org/license/')

    def show_authors(self):

        if self.authors_dialog is None:
            # create an author dialog
            self.authors_dialog = QtWidgets.QDialog(self)
            self.authors_dialog.setWindowTitle("Write us")
            self.authors_dialog.setMaximumSize(QtCore.QSize(150, 120))
            self.authors_dialog.setMaximumSize(QtCore.QSize(300, 240))
            vbox = QtWidgets.QVBoxLayout()
            self.authors_dialog.setLayout(vbox)

            hbox = QtWidgets.QHBoxLayout()
            vbox.addLayout(hbox)
            hbox.addStretch()
            logo = QtWidgets.QLabel()
            logo.setPixmap(QtGui.QPixmap(self._ai.app_icon_path))
            hbox.addWidget(logo)
            hbox.addStretch()

            vbox.addSpacing(10)

            text0 = QtWidgets.QLabel(self.authors_dialog)
            text0.setOpenExternalLinks(True)
            vbox.addWidget(text0)
            txt = """
            <b>For bugs and troubleshooting:</b><br>
            <a href=\"mailto:%s?Subject=%s\">%s</a>
            <br><br>""" % (self._ai.app_support_email, self._ai.app_name,
                           self._ai.app_support_email)

            if self._with_ocs_email:
                txt += """
                <b>NOAA bugs and feature requests:</b><br>
                <a href=\"mailto:ocs.qctools@noaa.gov?Subject=%s\">ocs.qctools@noaa.gov</a>
                <br><br>""" % self._ai.app_name

            txt += "<b>For comments and ideas for new features:</b><br>\n"
            author_names = self._ai.app_author.split(";")
            author_emails = self._ai.app_author_email.split(";")
            for idx, _ in enumerate(author_names):
                txt += "%s  <a href=\"mailto:%s?Subject=%s\">%s</a><br>\n" \
                       % (author_names[idx], author_emails[idx], self._ai.app_name,
                          author_emails[idx])
            text0.setText(txt)

        self.authors_dialog.show()

    def change_url(self, url: str) -> None:
        if self.browser:
            self.browser.change_url(url)
