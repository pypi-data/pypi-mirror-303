import os
import datetime
import shutil

try:
    # TODO: winreg is windows-only, use QSettings instead
    import winreg  # python 3+
except Exception:
    pass
import traceback
import logging

from PySide6 import QtGui, QtWidgets

from hyo2.ssm2.app.gui.soundspeedmanager.dialogs.dialog import AbstractDialog
from hyo2.ssm2.app.gui.soundspeedmanager.dialogs.seacat import add_btn, get_last_comport, AutoSeacat, SelectCastsDlg, \
    save_last_comport, sbe_serialcomms, get_setting_string

logger = logging.getLogger(__name__)


class SeacatDialog(AbstractDialog):
    here = os.path.abspath(os.path.join(os.path.dirname(__file__)))  # to be overloaded
    media = os.path.join(here, os.pardir, 'media')

    def __init__(self, main_win, lib, parent=None):
        AbstractDialog.__init__(self, main_win=main_win, lib=lib, parent=parent)

        self.setWindowTitle("Import data from Sea-Bird SeaCAT CTD")
        self.setMinimumWidth(220)

        # create the overall layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)

        # info box
        hbox = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(hbox)
        hbox.addStretch()
        self.group_box = QtWidgets.QGroupBox("SeaCAT")
        self.group_box.setMaximumHeight(120)
        self.group_box.setFixedWidth(500)
        hbox.addWidget(self.group_box)
        hbox.addStretch()

        # image and text
        group_layout = QtWidgets.QHBoxLayout()
        self.group_box.setLayout(group_layout)
        group_layout.addStretch()
        # - image
        img_label = QtWidgets.QLabel()
        img = QtGui.QImage(os.path.join(self.media, 'seacat.png'))
        if img.isNull():
            raise RuntimeError("unable to open seacat image")
        # noinspection PyArgumentList
        img_label.setPixmap(QtGui.QPixmap.fromImage(img))
        group_layout.addWidget(img_label)
        # - text
        info_label = QtWidgets.QLabel(
            "This tool allows to directly interact with a SeaCAT instrument.\n\n"
            "The tool communicates by serial port with the sensor and makes\n"
            "possible to directly download the collected profiles."
        )
        info_label.setStyleSheet("color: #96A8A8;")
        info_label.setWordWrap(True)
        group_layout.addWidget(info_label)
        group_layout.addStretch()

        hbox4 = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(hbox4)
        hbox4.addStretch()  # spacer on left
        add_btn("Download All", self.on_download_all, "Retrieve and convert all casts in memory", hbox4)
        add_btn("Download Selected", self.on_download_selected, "Retrieve and convert selected casts in memory", hbox4)
        add_btn("Download Last Cast", self.on_download_last, "Retrieve and convert last cast in memory", hbox4)

        hbox4.addStretch()  # spacer on right

        hbox2 = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(hbox2)
        hbox2.addStretch()  # spacer on left
        add_btn("COMPORT", self.on_choose_comport, "Select a COM port to use with seacat", hbox2)
        add_btn("Status", self.on_status, "Retrieve and display Seacat status", hbox2)
        add_btn("Headers", self.on_headers, "Retrieve and display Seacat stored cast summary information", hbox2)
        add_btn("Set UTC Time", self.on_settime, "Set the clock on Seacat with current time in UTC", hbox2)
        add_btn("Precast Setup", self.on_precast, "Clear the seacat memory and reset clock (if needed)", hbox2)

        hbox2.addStretch()  # spacer on right

        hbox3 = QtWidgets.QHBoxLayout()
        self.main_layout.addLayout(hbox3)
        hbox3.addStretch()  # spacer on left
        lbl = QtWidgets.QLabel("Last used COM port info:", self)
        hbox3.addWidget(lbl)
        self.com_label = QtWidgets.QLabel("", self)
        hbox3.addWidget(self.com_label)
        hbox3.addStretch()  # spacer on right

        self.main_layout.addStretch()

    def set_com_label(self):
        self.com_label.setText(get_last_comport())

    def on_download_selected(self, event=None):
        self.download(selected=[])

    def on_download_last(self):
        self.download(selected=[-1])

    def on_download_all(self):
        logger.debug('downloading all ...')
        self.download(get_all=True)

    def download(self, get_all=False, selected=None):
        """if get_all==True then will download and convert all casts and will ignore the selected parameter.
        otherwise:
        selected=[-1] will get last cast (or whatever numbers are supplied
        selected=[] --empty list will prompt user for selected casts
        """
        if selected is None:
            selected = list()

        logger.debug('downloading last ...')
        output_path = self.lib.cb.ask_directory(key_name="Seacat/DownloadHex",
                                                title="Choose Directory to Store Seacat Files in")

        if output_path:
            with AutoSeacat(progbar=self.progress) as cat:  # with auto-closes port even if an exception is thrown
                if cat.isOpen():
                    self.com_label.setText(cat.get_com_str())
                    headers = list(cat.get_headers().items())
                    headers.sort()  # list of [cast#, header info]
                    if headers:
                        if get_all:
                            download_list = [h[0] for h in headers]
                        else:
                            if selected:
                                download_list = [headers[v][0] for v in selected]
                            else:
                                cast_descriptions = ["%d: %s" % hd for hd in headers]
                                dlg = SelectCastsDlg(cast_descriptions)
                                dlg_return = dlg.exec()
                                if dlg_return:  # user pressed OK
                                    download_list = dlg.get_selected()
                                else:
                                    download_list = []

                        succeeded, _failed = self.download_from_seacat(cat, download_list, output_path)
                        for pth in succeeded:
                            try:
                                self.lib.import_data(data_path=pth, data_format="seabird")
                                self.lib.store_data()
                                try:
                                    self.lib.filter_cur_data()
                                    self.lib.store_data()
                                except Exception:
                                    # noinspection PyCallByClass
                                    QtWidgets.QMessageBox.warning(self, "Error",
                                                                  "Filtering failed on the file below\n  "
                                                                  "The raw data was loaded instead\n\n%s" % (pth,))
                                    self.reject()
                            except Exception:
                                # noinspection PyCallByClass
                                QtWidgets.QMessageBox.information(self, "Notice",
                                                                  "File downloaded from the Seacat instrument\n  "
                                                                  "but failed to load in SoundSpeedManager\n\n%s" % (
                                                                  pth,))
                                self.reject()
                    else:
                        # noinspection PyCallByClass
                        QtWidgets.QMessageBox.information(self, "Notice", "No casts in the device")
                        self.reject()

        self.accept()

    def download_from_seacat(self, cat, casts, hexpath):
        """casts is an iterable of cast numbers to download from the open seacat device "cat"
        hexpath will default to the CATFILES user preference if it is not specified, it is where the downloaded HEX
        data files are stored
        """
        paths = cat.download(hexpath, casts, progbar=self.progress)
        failed = []
        succeeded = []
        if paths:
            is_ok, confile_path_or_messages = self.get_confile_for_hexfile(paths[0])
            if is_ok:
                conpath = confile_path_or_messages
                seabird_datacnv = self.get_seabird_datacnv()
                if seabird_datacnv:
                    for hexpath in paths:
                        logger.info('Trying to convert:\n' + hexpath + '\n')
                        is_ok, output = sbe_serialcomms.convert_hexfile(hexpath, conpath,
                                                                        os.path.dirname(seabird_datacnv))  # import Hex
                        if is_ok:
                            succeeded.append(output)
                        else:
                            failed.append(hexpath)
                    if failed:
                        # noinspection PyCallByClass
                        QtWidgets.QMessageBox.information(self, "Error in Conversion",
                                                          "The following casts failed to convert:\n\n" + "\n".join(
                                                              failed))
                else:
                    logger.info('Seabird DataCNV.exe not found\n')
            else:
                # noinspection PyCallByClass
                QtWidgets.QMessageBox.information(self, confile_path_or_messages[0], confile_path_or_messages[1])
        else:
            logger.info('No hex files downloaded, nothing to import\n')
        return succeeded, failed

    def on_choose_comport(self):
        """Changes the comport on which to try communicating with a Seacat"""
        logger.debug('choosing comport ...')
        ports = sbe_serialcomms.scan_for_comports()
        old = get_last_comport()
        port, ok = QtWidgets.QInputDialog.getItem(self, 'Choose COM', "Choose COM port to use, %s last used" % old,
                                                  ports)
        if ok:
            save_last_comport(port)

    def on_status(self):
        """Connects to seacat and shows the status message from the seacat to the user"""
        logger.debug('getting status ...')
        with AutoSeacat(progbar=self.progress) as cat:  # with auto-closes port even if an exception is thrown
            if cat.isOpen():
                self.com_label.setText(cat.get_com_str())
                msg = cat.get_status() + '\n'
            else:
                msg = "Seacat not found"
            logger.info(msg)
            # noinspection PyCallByClass
            QtWidgets.QMessageBox.information(self, "SBE SeaCAT", msg)

    def on_headers(self):
        """Connects to seacat and shows the header information to the user"""
        logger.debug('Showing header info from Seacat ...')
        with AutoSeacat(progbar=self.progress) as cat:  # with auto-closes port even if an exception is thrown
            if cat.isOpen():
                self.com_label.setText(cat.get_com_str())
                headers = list(cat.get_headers().items())
                if headers:
                    headers.sort()
                    msg = '\n'.join(["%d: %s" % hd for hd in headers]) + '\n'
                else:
                    msg = 'No headers received\n'
                logger.info(msg)
                # noinspection PyCallByClass
                QtWidgets.QMessageBox.information(self, "SBE SeaCAT", msg)

    def on_settime(self):
        """Set the clock with current CPU time on UTC"""
        logger.debug('setting clock to current UTC ...')
        with AutoSeacat(progbar=self.progress) as cat:  # with auto-closes port even if an exception is thrown
            if cat.isOpen():
                self.com_label.setText(cat.get_com_str())
                try:
                    msg = "Do you want to set the clock to " + datetime.datetime.utcnow().isoformat()
                    # noinspection PyCallByClass
                    ret = QtWidgets.QMessageBox.question(self, "Confirm Seacat Time Change", msg,
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.StandardButton.No)
                    if ret == QtWidgets.QMessageBox.Yes:
                        cat.set_datetime(datetime.datetime.utcnow())
                except Exception:
                    traceback.print_exc()

    def on_precast(self):
        """Precast setup checks (and resets seacat clock if more than 3 minutes off) and clears memory"""
        logger.debug('precast setup ...')
        with AutoSeacat(progbar=self.progress) as cat:  # with auto-closes port even if an exception is thrown
            if cat.isOpen():
                try:
                    dt_now = datetime.datetime.utcnow()
                    dt = cat.get_datetime()  # Get time refreshes the Status message -- voltages are included in status
                    diff = dt_now - dt
                    # see if time is more than 3 minutes off
                    bSetTime = False
                    if diff > datetime.timedelta(0, 3 * 60) or diff < datetime.timedelta(0, -3 * 60):
                        msg = """The Seacat time is %s
                            CPU time UTC is %s
                            They differ by more than three minutes.

                            Do you want to reset the Seacat time when initializing?""" % (dt.isoformat(),
                                                                                          dt_now.isoformat())
                        # noinspection PyCallByClass
                        ret = QtWidgets.QMessageBox.question(self, "Time Mismatch", msg,
                                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.StandardButton.No)
                        if ret == QtWidgets.QMessageBox.Yes:
                            bSetTime = True

                    # Getting the time refreshes the Status message -- voltages are included in status
                    volt_messages = cat.get_voltages()
                    # noinspection PyCallByClass
                    ret = QtWidgets.QMessageBox.question(self, "Confirm Seacat Init",
                                                         "Do you want to clear the Seacat memory now" +
                                                         "\nAnd set the clock" * bSetTime + "?"
                                                                                            "\n\nAlso - note the battery voltages:\n\n" + volt_messages,
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.StandardButton.No)
                    if ret == QtWidgets.QMessageBox.Yes:
                        if bSetTime:
                            cat.set_datetime(datetime.datetime.utcnow())
                        cat.init_logging()

                except Exception:
                    traceback.print_exc()

    def get_seabird_datacnv(self):
        seabird_utils_dir = get_setting_string("Seacat/DataCNV", '')
        if seabird_utils_dir:
            seabird_utils_exe = os.path.join(seabird_utils_dir, "datcnvw.exe")
            if not os.path.exists(seabird_utils_exe):
                seabird_utils_exe = ""
        else:
            seabird_utils_exe = ""

        if not seabird_utils_exe:
            try:
                rootkey = winreg.HKEY_CLASSES_ROOT
                xmlconkey = winreg.CreateKey(rootkey, "xmlconFile\\shell\\edit\\command")
                xmlcon_val = winreg.QueryValue(xmlconkey, "")
                path_to_seabird_exe = xmlcon_val[:xmlcon_val.lower().find(".exe") + 4].replace("'", "").replace('"', "")
                seabird_utils_exe = os.path.join(os.path.dirname(path_to_seabird_exe), "datcnvw.exe")
                if seabird_utils_exe:
                    if not os.path.exists(seabird_utils_exe):
                        raise Exception("datcnv not found - asking user to supply location")

            except Exception:
                seabird_utils_exe = self.lib.cb.ask_filename(saving=False, key_name="Seacat/DataCNV",
                                                             title="Find the Seabird Data Processing executable",
                                                             file_filter="DataCNVw.exe|datcnvw.exe")
                # rcode, seabird_utils_dir = RegistryHelpers.GetDirFromUser(None, RegistryKey="UserSpecifiedSeabird",
                #                               Title="Find the Seabird Data Processing executable",
                #                               bLocalMachine=0, DefaultVal="",
                #                               Message="Plese locate the seabird data processing directory.\n"
                #                               "It's probably under Program files(x86).")
        return seabird_utils_exe

    def get_confile_for_hexfile(self, hexfile_path):
        serial_num = sbe_serialcomms.get_serialnum(hexfile_path)
        if serial_num is None:
            msg = "Unable to get serial number.\nCheck raw data file %s" % hexfile_path
            title = "INCORRECT RAW DATA FILE"
            return False, [title, msg]

        else:
            # Make sure that calibration file is present.  Ask user if it's not
            # local first
            datadirec = os.path.dirname(hexfile_path)
            conname = sbe_serialcomms.get_confile_name(serial_num, datadirec)
            if not conname:
                loc = get_setting_string("Seacat/AlternateConFilePath", '')
                conname = sbe_serialcomms.get_confile_name(serial_num, loc)
                if not conname:
                    conname = self.lib.cb.ask_filename(saving=False, key_name="Seacat/AlternateConFilePath",
                                                       title="Find the config file for %s" % str(serial_num),
                                                       file_filter="Seacat Config Files (*.con *.xmlcon)")
                    if conname:
                        matches_convention = sbe_serialcomms.get_confile_name(serial_num, os.path.dirname(conname))
                        if not matches_convention:
                            better_name = os.path.join(datadirec, (serial_num + ".con"))
                            msg = "The config file selected doesn't fit the automatically recognized pattern.  " \
                                  "Do you want Sound Speed Manager to make a copy of the config with a name that  " \
                                  "will automatically be found next time?\n\nCopy+Rename to: %s" % better_name
                            # noinspection PyCallByClass
                            ret = QtWidgets.QMessageBox.question(self, "Copy and Rename?", msg,
                                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.StandardButton.No)
                            if ret == QtWidgets.QMessageBox.Yes:
                                shutil.copyfile(conname, better_name)
                    else:
                        title = "User Cancelled"
                        msg = "No seabird config file selected."
                        return False, [title, msg]

            return True, conname
