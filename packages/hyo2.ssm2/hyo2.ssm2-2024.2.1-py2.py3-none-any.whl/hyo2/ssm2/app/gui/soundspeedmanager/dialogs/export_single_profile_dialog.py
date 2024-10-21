from PySide6 import QtCore, QtWidgets

import logging

from hyo2.abc2.lib.package.pkg_helper import PkgHelper
from hyo2.ssm2.app.gui.soundspeedmanager.dialogs.dialog import AbstractDialog
from hyo2.ssm2.app.gui.soundspeedmanager.dialogs.output_folders_dialog import OutputFoldersDialog
from hyo2.ssm2.lib.profile.dicts import Dicts

logger = logging.getLogger(__name__)


class ExportSingleProfileDialog(AbstractDialog):

    def __init__(self, main_win, lib, parent=None):
        AbstractDialog.__init__(self, main_win=main_win, lib=lib, parent=parent)

        # the list of selected writers passed to the library
        self.selected_writers = list()

        self.setWindowTitle("Export single profile")
        self.setMinimumWidth(160)

        settings = QtCore.QSettings()

        # outline ui
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        # label
        hbox = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(hbox)
        hbox.addStretch()
        label = QtWidgets.QLabel("Select output formats:")
        hbox.addWidget(label)
        hbox.addStretch()
        # buttons
        hbox = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(hbox)
        hbox.addStretch()
        # - fmt layout
        self.fmtLayout = QtWidgets.QHBoxLayout()
        hbox.addLayout(self.fmtLayout)
        # -- left
        self.leftButtonBox = QtWidgets.QDialogButtonBox(QtCore.Qt.Orientation.Vertical)
        self.leftButtonBox.setFixedWidth(100)
        self.fmtLayout.addWidget(self.leftButtonBox)
        # -- right
        self.rightButtonBox = QtWidgets.QDialogButtonBox(QtCore.Qt.Orientation.Vertical)
        self.rightButtonBox.setFixedWidth(100)
        self.fmtLayout.addWidget(self.rightButtonBox)
        hbox.addStretch()
        # add buttons (retrieving name, description and extension from the library)
        for idx, name in enumerate(self.lib.name_writers):

            if len(self.lib.ext_writers[idx]) == 0:
                continue

            btn = QtWidgets.QPushButton("%s" % self.lib.desc_writers[idx])
            btn.setCheckable(True)
            btn.setToolTip("Select %s format [*.%s]" % (self.lib.desc_writers[idx],
                                                        ", *.".join(self.lib.ext_writers[idx])))

            btn_settings = settings.value("export_single_%s" % name)
            if btn_settings is None:
                settings.setValue("export_single_%s" % name, False)
            if settings.value("export_single_%s" % name) == 'true':
                btn.setChecked(True)
                self.selected_writers.append(name)

            if (idx % 2) == 0:
                self.leftButtonBox.addButton(btn, QtWidgets.QDialogButtonBox.ButtonRole.ActionRole)
            else:
                self.rightButtonBox.addButton(btn, QtWidgets.QDialogButtonBox.ButtonRole.ActionRole)

        # noinspection PyUnresolvedReferences
        self.leftButtonBox.clicked.connect(self.on_select_writer_btn)
        # noinspection PyUnresolvedReferences
        self.rightButtonBox.clicked.connect(self.on_select_writer_btn)

        self.mainLayout.addSpacing(16)

        # option for selecting the output folder
        select_output_folder = settings.value("select_output_folder")
        if select_output_folder is None:
            settings.setValue("select_output_folder", False)
        hbox = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(hbox)
        hbox.addStretch()
        self.selectFolder = QtWidgets.QCheckBox('Select output folder', self)
        self.selectFolder.setChecked(settings.value("select_output_folder") == 'true')
        hbox.addWidget(self.selectFolder)
        hbox.addStretch()

        # option for opening the output folder
        export_open_folder = settings.value("export_open_folder")
        if export_open_folder is None:
            settings.setValue("export_open_folder", True)
        hbox = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(hbox)
        hbox.addStretch()
        self.openFolder = QtWidgets.QCheckBox('Open output folder', self)
        self.openFolder.setChecked(settings.value("export_open_folder") == 'true')
        hbox.addWidget(self.openFolder)
        hbox.addStretch()

        # export
        hbox = QtWidgets.QHBoxLayout()
        self.mainLayout.addLayout(hbox)
        hbox.addStretch()
        btn = QtWidgets.QPushButton("Export profile")
        btn.setMinimumHeight(32)
        hbox.addWidget(btn)
        # noinspection PyUnresolvedReferences
        btn.clicked.connect(self.on_export_profile_btn)
        hbox.addStretch()

    def on_select_writer_btn(self, btn):
        """Update the list of writers to pass to the library"""
        logger.debug("%s -> %s" % (btn.text(), btn.isChecked()))
        idx = self.lib.desc_writers.index(btn.text())
        name = self.lib.name_writers[idx]

        settings = QtCore.QSettings()

        if btn.isChecked():
            self.selected_writers.append(name)
            settings.setValue("export_single_%s" % name, True)

        else:
            settings.setValue("export_single_%s" % name, False)
            if name in self.selected_writers:
                self.selected_writers.remove(name)

    def on_export_profile_btn(self):
        logger.debug("export profile clicked")

        if len(self.selected_writers) == 0:
            msg = "Select output formats before data export!"
            # noinspection PyCallByClass,PyArgumentList
            QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
            return

        # special case for Fugro ISS format
        custom_writer_instrument = None

        # special case: synthetic profile and NCEI
        for writer in self.selected_writers:
            if writer != 'ncei':
                continue

            if self.lib.ssp.l[0].meta.sensor_type == Dicts.sensor_types['Synthetic']:
                msg = "Attempt to export a synthetic profile in NCEI format!"
                # noinspection PyCallByClass,PyArgumentList
                QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                return

            if self.lib.current_project == 'default':
                msg = "The 'default' project cannot be used for NCEI export.\n\n" \
                      "Rename the project in the Database tab!"
                if self.lib.setup.noaa_tools:
                    msg += "\n\nRecommend in project_survey format, e.g. OPR-P999-RA-17_H12345"
                # noinspection PyCallByClass,PyArgumentList
                QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                return

            if self.lib.setup.noaa_tools and self.lib.not_noaa_project(self.lib.current_project):
                current_project, accepted = self.lib.cb.ask_formatted_text(default=self.lib.noaa_project)
                if not accepted:
                    return
                if self.lib.not_noaa_project(current_project, accepted):
                    msg = "The project name cannot be used for NCEI export.\n\n" \
                          "Rename the project in the Database tab!\n\n" \
                          "Recommend \"project_survey\" format, e.g. OPR-P999-RA-17_H12345"
                    # noinspection PyCallByClass,PyArgumentList
                    QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                    return

            if not self.lib.ssp.cur.meta.survey or \
                    not self.lib.ssp.cur.meta.vessel or \
                    not self.lib.ssp.cur.meta.institution:
                msg = "Survey, vessel, and institution metadata are mandatory for NCEI export.\n\n" \
                      "To fix the issue:\n" \
                      "- Load the profile (if not already loaded)\n" \
                      "- Set the missing values using the Metadata button on the Editor tool bar\n"
                # noinspection PyCallByClass,PyArgumentList
                QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                return

            # special case for Fugro ISS format with NCEI format
            if self.lib.ssp.cur.meta.probe_type == Dicts.probe_types['ISS']:
                logger.info("special case: NCEI and ISS format")

                if custom_writer_instrument is None:

                    msg = "Enter the instrument type and model \n(if you don't know, leave it blank):"
                    instrument = self.lib.cb.ask_text("ISS for NCEI", msg)
                    # if empty, we just use the sensor type
                    if instrument is None or instrument == "":
                        instrument = self.lib.ssp.cur.meta.sensor
                    custom_writer_instrument = instrument

        settings = QtCore.QSettings()

        select_output_folder = self.selectFolder.isChecked()
        settings.setValue("select_output_folder", select_output_folder)
        output_folders = dict()
        # each writer may potentially have is own folder
        if select_output_folder:

            dlg = OutputFoldersDialog(main_win=self.main_win, lib=self.lib, writers=self.selected_writers, parent=self)
            dlg.exec_()
            output_folders = dlg.output_folders
            if len(output_folders) == 0:
                return

        # case where all the writers will write to the same folder
        if len(output_folders) == 0:
            for writer in self.selected_writers:
                output_folders[writer] = self.lib.outputs_folder
            settings.setValue("export_folder", self.lib.outputs_folder)
            logger.debug('output folder: %s' % self.lib.outputs_folder)

        # ask user for basename
        basenames = dict()
        # NCEI has special filename convention
        if (len(self.selected_writers) == 1) and (self.selected_writers[0] == 'ncei'):

            pass

        else:

            basename_msg = "Enter output basename (without extension):"
            while True:
                # noinspection PyCallByClass,PyArgumentList
                basename, ok = QtWidgets.QInputDialog.getText(self, "Output basename", basename_msg,
                                                              text=self.lib.cur_basename)
                if not ok:
                    return
                for writer in self.selected_writers:
                    basenames[writer] = basename
                break

        # actually do the export
        self.progress.start()
        try:
            self.lib.export_data(data_paths=output_folders, data_files=basenames,
                                 data_formats=self.selected_writers, custom_writer_instrument=custom_writer_instrument)
        except RuntimeError as e:
            self.progress.end()
            msg = "Issue in exporting the data.\nReason: %s" % e
            # noinspection PyCallByClass,PyArgumentList
            QtWidgets.QMessageBox.critical(self, "Export error", msg, QtWidgets.QMessageBox.StandardButton.Ok)
            return

        # opening the output folder
        export_open_folder = self.openFolder.isChecked()
        settings.setValue("export_open_folder", export_open_folder)
        if export_open_folder:

            opened_folders = list()
            for output_folder in output_folders.values():
                if output_folder not in opened_folders:
                    PkgHelper.explore_folder(output_folder)  # open the output folder
                    opened_folders.append(output_folder)
            self.progress.end()

        else:
            self.progress.end()
            msg = "Profile successfully exported!"
            # noinspection PyCallByClass,PyArgumentList
            QtWidgets.QMessageBox.information(self, "Export profile", msg, QtWidgets.QMessageBox.StandardButton.Ok)

        self.accept()
