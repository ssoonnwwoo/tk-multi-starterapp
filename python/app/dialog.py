# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog
from .ui.iomanager_ui import IOManagerWidget

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)


def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("IO Manager", app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        # self.ui = Ui_Dialog()
        # self.ui.setupUi(self)
        layout = QtGui.QVBoxLayout()
        self.io_widget = IOManagerWidget()
        layout.addWidget(self.io_widget)
        self.setLayout(layout)
        self.resize(1400, 800)

        # self._app = sgtk.platform.current_bundle()
        # context = self._app.context
        # project_name = context.project.get("name")
        # if project_name:
        #     self.io_widget.project_cb.setCurrentText(project_name)
        #     self.io_widget.on_project_selected(project_name)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        #self._app = sgtk.platform.current_bundle()

        # logging happens via a standard toolkit logger
        logger.info("Launching IO Manager...")

        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk

        # lastly, set up our very basic UI
        #self.ui.context.setText("Current Context: %s" % self._app.context)
        #self.ui.context_user.setText("Current User: %s" % self._app.context.user['name'])
        #self.ui.project_dir.setText("Project Dir: %s" % self._app.context.filesystem_locations)

        #context = self._app.context
        #print("Project :", context.project)
        #print("User    :", context.user['name'])
        # print("Filesystem Locations:", context.filesystem_locations)
        # print("Human-readable str :", str(context))
