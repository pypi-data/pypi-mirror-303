import os
from hyo2.abc2 import pkg_info

app_path = os.path.abspath(os.path.dirname(__file__))
app_media_path = os.path.join(app_path, "media")

app_info = pkg_info.app_info(
    app_path=app_path,
    app_media_path=app_media_path,
    app_icon_path=os.path.join(app_media_path, "noaa_support.png"),
    app_tabs_icon_size=36,
    app_toolbars_icon_size=28
)
