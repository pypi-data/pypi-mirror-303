import os
import logging
from copy import deepcopy
from typing import Optional, Dict

logger = logging.getLogger(__name__)


class PkgInfo:
    """Collection of information about a package"""

    def __init__(self, name: str, version: str, author: str, author_email: str,
                 lic: str, lic_url: str, path: Optional[str],
                 url: Optional[str], manual_url: Optional[str],
                 support_email: Optional[str], latest_url: Optional[str],
                 deps_dict: Optional[Dict[str, str]]):
        self._name = name
        if len(version.split('.')) < 2:
            raise RuntimeError("Invalid version: %s" % version)
        self._version = version
        self._author = author
        if '@' not in author_email:
            raise RuntimeError("Invalid author email: %s" % author_email)
        self._author_email = author_email
        self._lic = lic
        self._lic_url = lic_url
        if path is not None:
            self._path = path
        else:
            self._path = os.path.abspath(os.path.dirname(__file__))
        self._url = url
        self._manual_url = manual_url
        self._support_email = support_email
        self._latest_url = latest_url
        self._deps_dict = deps_dict

        # app info
        self._app_name = None  # type: Optional[str]
        self._app_version = None  # type: Optional[str]
        self._app_beta = False  # type: Optional[bool]
        self._app_author = None  # type: Optional[str]
        self._app_author_email = None  # type: Optional[str]
        self._app_lic = None  # type: Optional[str]
        self._app_lic_url = None  # type: Optional[str]
        self._app_path = None  # type: Optional[str]
        self._app_url = None  # type: Optional[str]
        self._app_manual_url = None  # type: Optional[str]
        self._app_support_email = None  # type: Optional[str]
        self._app_latest_url = None  # type: Optional[str]
        self._app_deps_dict = None  # type: Optional[Dict[str, str]]

        self._app_media_path = None  # type: Optional[str]
        self._app_main_window_object_name = None  # type: Optional[str]
        self._app_license_path = None  # type: Optional[str]
        self._app_icon_path = None  # type: Optional[str]
        self._app_tabs_icon_size = None  # type: Optional[int]
        self._app_toolbars_icon_size = None  # type: Optional[int]

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def author(self) -> str:
        return self._author

    @property
    def author_email(self) -> str:
        return self._author_email

    @property
    def lic(self) -> str:
        return self._lic

    @property
    def lic_url(self) -> str:
        return self._lic_url

    @property
    def path(self) -> str:
        return self._path

    @property
    def url(self) -> Optional[str]:
        return self._url

    @property
    def manual_url(self) -> Optional[str]:
        return self._manual_url

    @property
    def support_email(self) -> Optional[str]:
        return self._support_email

    @property
    def latest_url(self) -> Optional[str]:
        return self._latest_url

    @property
    def deps_dict(self) -> Optional[Dict[str, str]]:
        return self._deps_dict

    def app_info(self,
                 app_name: Optional[str] = None,
                 app_version: Optional[str] = None,
                 app_beta: Optional[bool] = False,
                 app_author: Optional[str] = None,
                 app_author_email: Optional[str] = None,
                 app_lic: Optional[str] = None,
                 app_lic_url: Optional[str] = None,
                 app_path: Optional[str] = None,
                 app_url: Optional[str] = None,
                 app_manual_url: Optional[str] = None,
                 app_support_email: Optional[str] = None,
                 app_latest_url: Optional[str] = None,
                 app_deps_dict: Optional[Dict[str, str]] = None,
                 app_media_path: Optional[str] = None,
                 app_main_window_object_name: str = "MainWindow",
                 app_license_path: Optional[str] = None,
                 app_icon_path: Optional[str] = None,
                 app_tabs_icon_size: int = 36,
                 app_toolbars_icon_size: int = 24
                 ) -> 'PkgInfo':
        app_info = deepcopy(self)
        if app_name is None:
            app_info.app_name = self._name
        else:
            app_info.app_name = app_name
        if app_version is None:
            app_info.app_version = self._version
        else:
            app_info.app_version = app_version
        app_info.app_beta = app_beta
        if app_author is None:
            app_info.app_author = self._author
        else:
            app_info.app_author = app_author
        if app_author_email is None:
            app_info.app_author_email = self._author_email
        else:
            app_info.app_author_email = app_author_email
        if app_lic is None:
            app_info.app_lic = self._lic
        else:
            app_info.app_lic = app_lic
        if app_lic_url is None:
            app_info.app_lic_url = self._lic_url
        else:
            app_info.app_lic_url = app_lic_url
        if app_path is None:
            app_info.app_path = self._path
        else:
            app_info.app_path = app_path
        if app_url is None:
            app_info.app_url = self._url
        else:
            app_info.app_url = app_url
        if app_manual_url is None:
            app_info.app_manual_url = self._manual_url
        else:
            app_info.app_manual_url = app_manual_url
        if app_support_email is None:
            app_info.app_support_email = self._support_email
        else:
            app_info.app_support_email = app_support_email
        if app_latest_url is None:
            app_info.app_latest_url = self._latest_url
        else:
            app_info.app_latest_url = app_latest_url
        if app_deps_dict is None:
            app_info.app_deps_dict = self._deps_dict
        else:
            app_info.app_deps_dict = app_deps_dict

        app_info.app_media_path = app_media_path
        app_info.app_main_window_object_name = app_main_window_object_name
        app_info.app_license_path = app_license_path
        app_info.app_icon_path = app_icon_path
        app_info.app_tabs_icon_size = app_tabs_icon_size
        app_info.app_toolbars_icon_size = app_toolbars_icon_size

        return app_info

    @property
    def app_name(self) -> str:
        return self._app_name

    @app_name.setter
    def app_name(self, value: str) -> None:
        self._app_name = value

    @property
    def app_version(self) -> str:
        return self._app_version

    @app_version.setter
    def app_version(self, value: str) -> None:
        self._app_version = value

    @property
    def app_beta(self) -> bool:
        return self._app_beta

    @app_beta.setter
    def app_beta(self, value: bool) -> None:
        self._app_beta = value

    @property
    def app_author(self) -> str:
        return self._app_author

    @app_author.setter
    def app_author(self, value: str) -> None:
        self._app_author = value

    @property
    def app_author_email(self) -> str:
        return self._app_author_email

    @app_author_email.setter
    def app_author_email(self, value: str) -> None:
        self._app_author_email = value

    @property
    def app_lic(self) -> str:
        return self._app_lic

    @app_lic.setter
    def app_lic(self, value: str) -> None:
        self._app_lic = value

    @property
    def app_lic_url(self) -> str:
        return self._app_lic_url

    @app_lic_url.setter
    def app_lic_url(self, value: str) -> None:
        self._app_lic_url = value

    @property
    def app_path(self) -> str:
        return self._app_path

    @app_path.setter
    def app_path(self, value: str) -> None:
        self._app_path = value

    @property
    def app_url(self) -> str:
        return self._app_url

    @app_url.setter
    def app_url(self, value: str) -> None:
        self._app_url = value

    @property
    def app_manual_url(self) -> str:
        return self._app_manual_url

    @app_manual_url.setter
    def app_manual_url(self, value: str) -> None:
        self._app_manual_url = value

    @property
    def app_support_email(self) -> str:
        return self._app_support_email

    @app_support_email.setter
    def app_support_email(self, value: str) -> None:
        self._app_support_email = value

    @property
    def app_latest_url(self) -> str:
        return self._app_latest_url

    @app_latest_url.setter
    def app_latest_url(self, value: str) -> None:
        self._app_latest_url = value

    @property
    def app_deps_dict(self) -> Dict[str, str]:
        return self._app_deps_dict

    @app_deps_dict.setter
    def app_deps_dict(self, value: Dict[str, str]) -> None:
        self._app_deps_dict = value

    @property
    def app_media_path(self) -> Optional[str]:
        return self._app_media_path

    @app_media_path.setter
    def app_media_path(self, value: str) -> None:
        self._app_media_path = value

    @property
    def app_main_window_object_name(self) -> Optional[str]:
        return self._app_main_window_object_name

    @app_main_window_object_name.setter
    def app_main_window_object_name(self, value: str) -> None:
        self._app_main_window_object_name = value

    @property
    def app_license_path(self) -> Optional[str]:
        return self._app_license_path

    @app_license_path.setter
    def app_license_path(self, value: str) -> None:
        self._app_license_path = value

    @property
    def app_icon_path(self) -> Optional[str]:
        return self._app_icon_path

    @app_icon_path.setter
    def app_icon_path(self, value: str) -> None:
        self._app_icon_path = value

    @property
    def app_tabs_icon_size(self) -> int:
        return self._app_tabs_icon_size

    @app_tabs_icon_size.setter
    def app_tabs_icon_size(self, value: int) -> None:
        self._app_tabs_icon_size = value

    @property
    def app_toolbars_icon_size(self) -> int:
        return self._app_toolbars_icon_size

    @app_toolbars_icon_size.setter
    def app_toolbars_icon_size(self, value: int) -> None:
        self._app_toolbars_icon_size = value

    def __str__(self) -> str:
        msg = "<%s>\n" % self.__class__.__name__
        for k, v in self.__dict__.items():
            msg += "  <%s: %s>\n" % (k, v)
        return msg
