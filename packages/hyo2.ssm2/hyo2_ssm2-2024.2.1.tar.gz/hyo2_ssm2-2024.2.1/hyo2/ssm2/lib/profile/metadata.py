import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

from hyo2.ssm2.lib.profile.dicts import Dicts


class Metadata:
    def __init__(self):
        self.sensor_type = Dicts.sensor_types['Unknown']
        self.probe_type = Dicts.probe_types['Unknown']
        self.latitude = None
        self.longitude = None
        self.utc_time = None
        self.original_path = str()
        self._institution = str()
        self._survey = str()
        self._vessel = str()
        self._sn = str()  # serial number
        self.proc_time = None  # last processing time
        self.proc_info = str()  # info about processing
        self.surveylines = str()
        self.comments = str()
        self.pressure_uom = 'dbar'
        self.depth_uom = 'm'
        self.speed_uom = 'm/s'
        self.temperature_uom = 'deg C'
        self.conductivity_uom = 'S/m'
        self.salinity_uom = 'PSU'

    @property
    def sensor(self):
        return Dicts.first_match(Dicts.sensor_types, self.sensor_type)

    @property
    def probe(self):
        return Dicts.first_match(Dicts.probe_types, self.probe_type)

    @property
    def institution(self):
        return self._institution

    @institution.setter
    def institution(self, value):
        self.update_proc_time()
        self._institution = value.strip()

    @property
    def survey(self):
        return self._survey

    @survey.setter
    def survey(self, value):
        self.update_proc_time()
        self._survey = value.strip()

    @property
    def vessel(self):
        return self._vessel

    @vessel.setter
    def vessel(self, value):
        self.update_proc_time()
        self._vessel = value.strip()

    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self.update_proc_time()
        self._sn = value.strip()

    def update_proc_time(self):
        self.proc_time = datetime.utcnow()

    def __repr__(self):
        msg = "  <Meta>\n"
        msg += "    <sensor:%s[%s]>\n" % (self.sensor, self.probe)
        msg += "    <time:%s,lat:%s,long:%s>\n" % (self.utc_time, self.latitude, self.longitude)
        msg += "    <path:%s>\n" % self.original_path
        msg += "    <institution:%s>\n" % self.institution
        msg += "    <survey:%s,vessel:%s>\n" % (self.survey, self.vessel)
        msg += "    <sn:%s>\n" % self.sn
        msg += "    <proc_time:%s>\n" % self.proc_time
        msg += "    <proc_info:%s>\n" % self.proc_info
        msg += "    <surveylines:%s>\n" % self.comments
        msg += "    <comments:%s>\n" % self.comments
        msg += "    <pressure_uom:%s>\n" % self.pressure_uom
        msg += "    <depth_uom:%s>\n" % self.depth_uom
        msg += "    <speed_uom:%s>\n" % self.speed_uom
        msg += "    <temperature_uom:%s>\n" % self.temperature_uom
        msg += "    <conductivity_uom:%s>\n" % self.conductivity_uom
        msg += "    <salinity_uom:%s>\n" % self.salinity_uom

        return msg

    def debug_info(self):
        msg = "Sensor: %s\n" % Dicts.first_match(Dicts.sensor_types, self.sensor_type)
        msg += "Probe: %s\n" % Dicts.first_match(Dicts.probe_types, self.probe_type)
        msg += "Location: %s, %s\n" % (self.latitude, self.longitude)
        msg += "Time: %s\n" % self.utc_time
        if self.original_path:
            msg += "Basename: %s\n" % os.path.basename(self.original_path)
        msg += "Survey: %s, Vessel: %s\n" % (self.survey, self.vessel)
        msg += "S/N: %s\n" % self.sn
        msg += "Last proc. time: %s\n" % self.proc_time
        msg += "Last proc. info: %s\n" % self.proc_info
        return msg
