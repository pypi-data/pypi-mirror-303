import os
import logging

from PySide6 import QtCore, QtWidgets

from hyo2.abc2.lib.package.pkg_helper import PkgHelper
from hyo2.ssm2.app.gui.soundspeedmanager.dialogs.dialog import AbstractDialog
from hyo2.ssm2.app.gui.soundspeedmanager.dialogs.output_folders_dialog import OutputFoldersDialog
from hyo2.ssm2.lib.profile.dicts import Dicts

logger = logging.getLogger(__name__)


class ExportMultiProfileDialog(AbstractDialog):

    def __init__(self, main_win, lib, pks, parent=None):
        AbstractDialog.__init__(self, main_win=main_win, lib=lib, parent=parent)

        # check the passed primary keys
        if type(pks) is not list:
            raise RuntimeError("The dialog takes a list of primary keys, not %s" % type(pks))
        if len(pks) < 2:
            raise RuntimeError("The dialog takes a list of at least 2 primary keys, not %s" % len(pks))
        self._pks = pks

        # the list of selected writers passed to the library
        self.selected_writers = list()

        self.setWindowTitle("Export multiple profiles")
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
        btn = QtWidgets.QPushButton("Export profiles")
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
        logger.debug("export profiles clicked")

        if len(self.selected_writers) == 0:
            msg = "Select output formats before data export!"
            # noinspection PyCallByClass,PyArgumentList
            QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
            return

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

        # CARIS-specific check for file concatenation
        for writer in self.selected_writers:

            if writer == 'caris':
                caris_path = os.path.join(output_folders[writer], "CARIS", self.lib.current_project + ".svp")
                if os.path.exists(caris_path):
                    msg = "An existing CARIS file is present in the output folder.\n\n" \
                          "Do you want to remove it to avoid possible profile duplications?"
                    # noinspection PyCallByClass,PyArgumentList
                    ret = QtWidgets.QMessageBox.question(
                        self, "CARIS export", msg,
                        QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
                    if ret == QtWidgets.QMessageBox.StandardButton.Yes:
                        os.remove(caris_path)
                break

        # special case for Fugro ISS format
        force_writer_instrument_for_next_casts = None
        custom_writer_instrument = None

        # actually do the export
        current_project = None
        format_ok = False
        opened_folders = list()
        export_open_folder = self.openFolder.isChecked()
        settings.setValue("export_open_folder", export_open_folder)
        all_exported = True
        for pk in self._pks:

            success = self.lib.load_profile(pk, skip_atlas=True)
            if not success:
                # noinspection PyCallByClass,PyArgumentList
                QtWidgets.QMessageBox.warning(self, "Database", "Unable to load profile #%02d!" % pk,
                                              QtWidgets.QMessageBox.StandardButton.Ok)
                continue

            # special case: synthetic profile and NCEI
            skip_export = False
            for writer in self.selected_writers:

                if writer != 'ncei':
                    continue

                if self.lib.ssp.l[0].meta.sensor_type == Dicts.sensor_types['Synthetic']:
                    msg = "Attempt to export a synthetic profile in NCEI format!"
                    # noinspection PyCallByClass,PyArgumentList
                    QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                    skip_export = True
                    continue

                if self.lib.current_project == 'default':

                    msg = "The 'default' project cannot be used for NCEI export.\n\n" \
                          "Rename the project in the Database tab!"
                    if self.lib.setup.noaa_tools:
                        msg += "\n\nRecommend in project_survey format, e.g. OPR-P999-RA-17_H12345"
                    # noinspection PyCallByClass,PyArgumentList
                    QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                    skip_export = True
                    continue

                if self.lib.setup.noaa_tools and self.lib.not_noaa_project(self.lib.current_project):
                    if self.lib.not_noaa_project(current_project, format_ok):
                        current_project, accepted = self.lib.cb.ask_formatted_text(default=self.lib.noaa_project)
                        if not accepted:
                            continue
                        if self.lib.not_noaa_project(current_project, accepted):
                            msg = "The project name cannot be used for NCEI export.\n\n" \
                                  "Rename the project in the Database tab!\n\n" \
                                  "Recommend \"project_survey\" format, e.g. OPR-P999-RA-17_H12345"
                            # noinspection PyCallByClass,PyArgumentList
                            QtWidgets.QMessageBox.warning(self, "Export warning", msg,
                                                          QtWidgets.QMessageBox.StandardButton.Ok)
                            skip_export = True
                            continue

                if not self.lib.ssp.cur.meta.survey or \
                        not self.lib.ssp.cur.meta.vessel or \
                        not self.lib.ssp.cur.meta.institution:
                    msg = "Survey, vessel, and institution metadata are mandatory for NCEI export.\n\n" \
                          "To fix the issue:\n" \
                          "- Load the profile (if not already loaded)\n" \
                          "- Set the missing values using the Metadata button on the Editor tool bar\n"
                    # noinspection PyCallByClass,PyArgumentList
                    QtWidgets.QMessageBox.warning(self, "Export warning", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                    skip_export = True
                    continue

                # special case for Fugro ISS format with NCEI format
                if self.lib.ssp.cur.meta.probe_type == Dicts.probe_types['ISS']:
                    logger.info("special case: NCEI and ISS format")

                    if force_writer_instrument_for_next_casts is None:

                        msg = "Enter the instrument type and model \n(if you don't know, leave it blank):"
                        instrument, flag = self.lib.cb.ask_text_with_flag("ISS for NCEI", msg,
                                                                          flag_label="Apply to all the next profiles")
                        logger.debug("user input for ISS: %s, %r" % (instrument, flag))
                        # if empty, we just use the sensor type
                        if instrument is None or instrument == "":
                            instrument = self.lib.ssp.cur.meta.sensor
                        if flag:  # to skip the user dialog for next casts
                            force_writer_instrument_for_next_casts = instrument
                        else:
                            force_writer_instrument_for_next_casts = None
                        custom_writer_instrument = instrument

                    else:  # user asked to apply to all the next profiles
                        custom_writer_instrument = force_writer_instrument_for_next_casts

            if skip_export:
                all_exported = False
                continue

            self.progress.start(text="Exporting profile #%02d" % pk)
            try:
                self.progress.update(value=60)
                self.lib.export_data(data_paths=output_folders, data_formats=self.selected_writers,
                                     custom_writer_instrument=custom_writer_instrument)

            except RuntimeError as e:
                self.progress.end()
                msg = "Issue in exporting the data for profile #%02d.\nReason: %s" % (pk, e)
                # noinspection PyCallByClass,PyArgumentList
                QtWidgets.QMessageBox.critical(self, "Export error", msg, QtWidgets.QMessageBox.StandardButton.Ok)
                continue
            self.progress.end()

            # opening the output folder
            if export_open_folder:

                for output_folder in output_folders.values():
                    if output_folder not in opened_folders:
                        PkgHelper.explore_folder(output_folder)
                        opened_folders.append(output_folder)

        if all_exported:
            msg = "Profiles successfully exported!"
            # noinspection PyCallByClass,PyArgumentList
            QtWidgets.QMessageBox.information(self, "Export profile", msg, QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            msg = "At least one profile had issues in being exported!"
            # noinspection PyCallByClass,PyArgumentList
            QtWidgets.QMessageBox.warning(self, "Export profile", msg, QtWidgets.QMessageBox.StandardButton.Ok)

        self.accept()
