from typing import Any

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QAction, QCloseEvent, QColor, QDesktopServices, QResizeEvent
from PySide6.QtWidgets import QApplication, QGraphicsColorizeEffect, QMainWindow, QWidget

from pyside_app_core.app import AppMetadata
from pyside_app_core.services import platform_service
from pyside_app_core.ui.standard.about_dialog import AboutDialog
from pyside_app_core.ui.standard.base_window import BaseMixin
from pyside_app_core.ui.widgets.menu_ctx import MenuBarContext
from pyside_app_core.ui.widgets.tool_bar_ctx import ToolBarContext
from pyside_app_core.ui.widgets.window_settings_mixin import WindowSettingsMixin


class MainWindow(WindowSettingsMixin, BaseMixin, QMainWindow):
    def __init__(self, *, primary: bool = False) -> None:
        super().__init__(parent=None)

        # primary window will quit app when closed
        self._primary = primary

        self._about_dialog = AboutDialog()

        self._central = QWidget(parent=self)
        self.setCentralWidget(self._central)

        # must call in order to show grab handle
        self.statusBar().show()

        self._menu_bar = MenuBarContext(self)
        self._menu_bar.setNativeMenuBar(platform_service.is_macos)
        self.setMenuBar(self._menu_bar)

        with (
            self._menu_bar.menu("File") as file_menu,
            file_menu.action("Quit") as exit_action,
        ):
            exit_action.setMenuRole(QAction.MenuRole.QuitRole)
            exit_action.triggered.connect(self.close)

        self._build_menus()

        with self._menu_bar.menu("Window") as window_menu:
            with window_menu.action("Minimize") as min_action:
                min_action.setShortcut("Ctrl+M")
                min_action.triggered.connect(self.showMinimized)
            with window_menu.action("Zoom") as zoom_action:
                zoom_action.triggered.connect(self.showMaximized)

        with self._menu_bar.menu("Help") as help_menu:
            with help_menu.action("About") as about_action:
                about_action.setMenuRole(QAction.MenuRole.AboutRole)
                about_action.triggered.connect(self._about_dialog.exec)

            if AppMetadata.help_url:
                with help_menu.action("Get Help") as help_action:
                    help_action.triggered.connect(lambda: QDesktopServices.openUrl(QUrl(AppMetadata.help_url)))

            if AppMetadata.bug_report_url:
                with help_menu.action("Report Bug") as help_action:
                    help_action.triggered.connect(lambda: QDesktopServices.openUrl(QUrl(AppMetadata.bug_report_url)))

    @property
    def menu_bar(self) -> MenuBarContext:
        return self._menu_bar

    def _build_menus(self) -> None:
        pass

    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        QApplication.quit()


class MainToolbarWindow(MainWindow):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._tool_bar = ToolBarContext(area="top", parent=self, movable=False)
        self._tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self._build_toolbar()

    @property
    def tool_bar(self) -> ToolBarContext:
        return self._tool_bar

    def _build_toolbar(self) -> None:
        pass
