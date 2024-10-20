import os
from PySide6 import QtWidgets
from qt_material import apply_stylesheet


class AppStyle:

    here = os.path.abspath(os.path.dirname(__file__))
    media = os.path.abspath(os.path.join(here, "media"))

    @classmethod
    def apply(cls, app: QtWidgets.QApplication) -> None:
        xml_path = os.path.abspath(os.path.join(cls.media, "hyo2.xml"))
        if not os.path.exists(xml_path):
            raise RuntimeError("Unable to locate %s" % xml_path)
        css_path = os.path.abspath(os.path.join(cls.media, "hyo2.css"))
        if not os.path.exists(css_path):
            raise RuntimeError("Unable to locate %s" % css_path)
        apply_stylesheet(app=app, theme=xml_path, invert_secondary=True, extra={'density_scale': '-2'},
                         css_file=css_path)

    @classmethod
    def html_css(cls) -> str:
        with open(os.path.join(cls.media, "html.css")) as fid:
            return fid.read()
