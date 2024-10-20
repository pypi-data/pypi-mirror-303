from typing import Final

from PySide6.QtCore import QCoreApplication
from PySide6.QtCore import Qt
from PySide6.QtQuick import QQuickWindow
from PySide6.QtQuick import QSGRendererInterface
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QWidget

from _support.staticfixtures import BaseTest
from _support.staticfixtures import static_setup
from _support.staticfixtures import static_teardown


class BaseGuiTest(BaseTest):
    app: QApplication
    widgets: Final[list[QWidget]] = []

    @static_setup
    @classmethod
    def start_application(cls) -> None:
        QCoreApplication.setAttribute(
            Qt.ApplicationAttribute.AA_ShareOpenGLContexts
        )
        QQuickWindow.setGraphicsApi(
            QSGRendererInterface.GraphicsApi.OpenGLRhi  # @UndefinedVariable
        )

        cls.app = QApplication([])

    @static_teardown
    @classmethod
    def quit_application(cls) -> None:
        for widget in cls.widgets:
            widget.show()
        cls.app.exec()
