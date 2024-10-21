import time
from datetime import datetime as dt
import logging
from enum import IntEnum
from PySide6 import QtWidgets

from hyo2.abc2.app.qt_progress import QtProgress
from hyo2.abc2.lib.logging import set_logging
from hyo2.ssm2.lib.soundspeed import SoundSpeedLibrary
from hyo2.ssm2.app.gui.soundspeedmanager.qt_callbacks import QtCallbacks


set_logging(ns_list=["hyo2.abc2", "hyo2.ssm2"])

logger = logging.getLogger(__name__)


class ModelOptions(IntEnum):
    # World Models
    WOA09 = 1
    WOA13 = 2
    RTOFS = 3
    WOA18 = 4

    # Regional Models
    # East Coast
    CBOFS = 10  # RG = True     # Format is GoMOFS
    DBOFS = 11  # RG = True     # Format is GoMOFS
    GoMOFS = 12  # RG = True     # Format is GoMOFS
    NYOFS = 13  # RG = False
    SJROFS = 14  # RG = False

    # Gulf of Mexico
    NGOFS2 = 20  # RG = True     # Format is GoMOFS
    TBOFS = 21  # RG = True     # Format is GoMOFS

    # Great Lakes
    LEOFS = 30  # RG = True     # Format is GoMOFS
    LMHOFS = 31  # RG = False
    LOOFS = 33  # RG = False
    LSOFS = 34  # RG = False

    # Pacific Coast
    SSCOFS = 40  # RG = True     # Format is GoMOFS
    SFBOFS = 41  # RG = True     # Format is GoMOFS
    WCOFS = 42  # RG = True     # Format is GoMOFS


# Choose Model
switch = ModelOptions.WCOFS  # Choose a ModelOptions Value to test

app = QtWidgets.QApplication([])  # PySide stuff (start)
mw = QtWidgets.QMainWindow()
mw.show()

lib = SoundSpeedLibrary(progress=QtProgress(parent=mw), callbacks=QtCallbacks(parent=mw))

# Choose test location
tests = [

    # (-19.1, 74.16, dt.utcnow()),              # Indian Ocean
    # (72.852028, -67.315431, dt.utcnow())      # Baffin Bay
    # (18.2648113, 16.1761115, dt.utcnow()),    # in land -> middle of Africa
    # (39.725989, -104.967745, dt.utcnow())     # in land -> Denver, CO
    # (37.985427, -76.311156, dt.utcnow()),     # Chesapeake Bay
    # (39.162802, -75.278057, dt.utcnow()),     # Deleware Bay
    # (43.026480, -70.318824, dt.utcnow()),     # offshore Portsmouth
    # (40.662218, -74.049306, dt.utcnow())      # New York Harbor
    # (30.382518, -81.573615, dt.utcnow())      # Mill Cove, St. Johns River
    # (28.976225, -92.078882, dt. utcnow())     # Offshore Louisiana
    # (27.762904, -82.557280, dt.utcnow())      # Tampa Bay
    # (41.806023, -82.393283, dt.utcnow())      # Lake Erie
    # (44.564914, -82.845794, dt.utcnow())      # Lake Huron
    # (43.138573, -86.832183, dt.utcnow())      # Lake Michigan
    # (43.753190, -76.826818, dt.utcnow())      # Lake Ontario
    # (47.457546, -89.347715, dt.utcnow())      # Lake Superior
    # (46.161403, -124.107396, dt.utcnow())     # Offshore of Colombia River
    # (37.689510, -122.298514, dt.utcnow())     # San Francisco Bay
    (37.779088, -124.209048, dt.utcnow())     # Offshore San Francisco (West Coast)
]

if switch is ModelOptions.WOA09:

    # download the woa09 if not present
    if not lib.has_woa09():
        success = lib.download_woa09()
        if not success:
            raise RuntimeError("unable to download")
    logger.info("has WOA09: %s" % lib.has_woa09())

elif switch is ModelOptions.WOA13:

    # download the woa13 if not present
    if not lib.has_woa13():
        success = lib.download_woa13()
        if not success:
            raise RuntimeError("unable to download")
    logger.info("has WOA13: %s" % lib.has_woa13())

elif switch is ModelOptions.WOA18:

    # download the woa18 if not present
    if not lib.has_woa18():
        success = lib.download_woa18()
        if not success:
            raise RuntimeError("unable to download")
    logger.info("has WOA18: %s" % lib.has_woa18())

elif switch is ModelOptions.RTOFS:

    # download the current-time rtofs
    if not lib.has_rtofs():
        lib.download_rtofs()
    logger.info("has RTOFS: %s" % lib.has_rtofs())

elif switch is ModelOptions.CBOFS:

    # download the current-time cbofs
    if not lib.has_cbofs():
        lib.download_cbofs()
    logger.info("has CBOFS: %s" % lib.has_cbofs())

elif switch is ModelOptions.DBOFS:

    # download the current-time dbofs
    if not lib.has_dbofs():
        lib.download_dbofs()
    logger.info("has DBOFS: %s" % lib.has_dbofs())

elif switch is ModelOptions.GoMOFS:

    # download the current-time gomofs
    if not lib.has_gomofs():
        lib.download_gomofs()
    logger.info("has GoMOFS: %s" % lib.has_gomofs())

elif switch is ModelOptions.NYOFS:

    # download the current-time nyofs
    if not lib.has_nyofs():
        lib.download_nyofs()
    logger.info("has NYOFS: %s" % lib.has_nyofs())

elif switch is ModelOptions.SJROFS:

    # download the current-time sjrofs
    if not lib.has_sjrofs():
        lib.download_sjrofs()
    logger.info("has SJROFS: %s" % lib.has_sjrofs())

elif switch is ModelOptions.NGOFS2:

    # download the current-time ngofs2
    if not lib.has_ngofs2():
        lib.download_ngofs2()
    logger.info("has NGOFS2: %s" % lib.has_ngofs2())

elif switch is ModelOptions.TBOFS:

    # download the current-time tbofs
    if not lib.has_tbofs():
        lib.download_tbofs()
    logger.info("has TBOFS: %s" % lib.has_tbofs())

elif switch is ModelOptions.LEOFS:

    # download the current-time leofs
    if not lib.has_leofs():
        lib.download_leofs()
    logger.info("has LEOFS: %s" % lib.has_leofs())

elif switch is ModelOptions.LMHOFS:

    # download the current-time lmhofs
    if not lib.has_lmhofs():
        lib.download_lmhofs()
    logger.info("has LMHOFS: %s" % lib.has_lmhofs())

elif switch is ModelOptions.LOOFS:

    # download the current-time loofs
    if not lib.has_loofs():
        lib.download_loofs()
    logger.info("has LOOFS: %s" % lib.has_loofs())

elif switch is ModelOptions.LSOFS:

    # download the current-time lmhofs
    if not lib.has_lmhofs():
        lib.download_lmhofs()
    logger.info("has LMHOFS: %s" % lib.has_lmhofs())

elif switch is ModelOptions.SSCOFS:

    # download the current-time sscofs
    if not lib.has_sscofs():
        lib.download_sscofs()
    logger.info("has SSCOFS: %s" % lib.has_sscofs())

elif switch is ModelOptions.SFBOFS:

    # download the current-time sfbofs
    if not lib.has_sfbofs():
        lib.download_sfbofs()
    logger.info("has SFBOFS: %s" % lib.has_sfbofs())

elif switch is ModelOptions.WCOFS:

    # download the current-time wcofs
    if not lib.has_wcofs():
        lib.download_wcofs()
    logger.info("has WCOFS: %s" % lib.has_wcofs())

else:
    raise RuntimeError("invalid switch value: %s" % switch)

# # more stuff
# if switch == "RTOFS":
#
#     # test today urls
#     # noinspection PyProtectedMember
#     temp_url, sal_url = lib.atlases.rtofs._build_check_urls(dt.utcnow())
#     # noinspection PyProtectedMember
#     logger.info("urls:\n- %s [%s]\n%s [%s]"
#                 % (temp_url, lib.atlases.rtofs._check_url(temp_url), sal_url, lib.atlases.rtofs._check_url(sal_url)))
#     # test yesterday urls
#     # noinspection PyProtectedMember
#     temp_url, sal_url = lib.atlases.rtofs._build_check_urls(dt.utcnow() - timedelta(days=1))
#     # noinspection PyProtectedMember
#     logger.info("urls:\n- %s [%s]\n%s [%s]"
#                 % (temp_url, lib.atlases.rtofs._check_url(temp_url), sal_url, lib.atlases.rtofs._check_url(sal_url)))
#
# elif switch == "GoMOFS":
#
#     # test today urls
#     # noinspection PyProtectedMember
#     url = lib.atlases.gomofs._build_check_url(dt.utcnow())
#     # noinspection PyProtectedMember
#     logger.info("url:\n- %s [%s]"
#                 % (url, lib.atlases.gomofs._check_url(url)))
#     # test yesterday urls
#     # noinspection PyProtectedMember
#     url = lib.atlases.gomofs._build_check_url(dt.utcnow() - timedelta(days=1))
#     # noinspection PyProtectedMember
#     logger.info("url:\n- %s [%s]"
#                 % (url, lib.atlases.gomofs._check_url(url)))


# test for a few locations
for test in tests:

    start_time = time.time()
    # just the ssp (there are also ssp_min and ssp_max)
    if switch is ModelOptions.WOA09:
        logger.info("WOA09 profiles:\n%s" % lib.atlases.woa09.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.WOA13:
        logger.info("WOA13 profiles:\n%s" % lib.atlases.woa13.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.WOA18:
        logger.info("WOA18 profiles:\n%s" % lib.atlases.woa18.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.RTOFS:
        logger.info("RTOFS profiles:\n%s" % lib.atlases.rtofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.CBOFS:
        logger.info("CBOFS profiles:\n%s" % lib.atlases.cbofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.DBOFS:
        logger.info("DBOFS profiles:\n%s" % lib.atlases.dbofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.GoMOFS:
        logger.info("GoMOFS profiles:\n%s" % lib.atlases.gomofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.NYOFS:
        logger.info("NYOFS profiles:\n%s" % lib.atlases.nyofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.SJROFS:
        logger.info("SJROFS profiles:\n%s" % lib.atlases.sjrofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.NGOFS2:
        logger.info("NGOFS2 profiles:\n%s" % lib.atlases.ngofs2.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.TBOFS:
        logger.info("TBOFS profiles:\n%s" % lib.atlases.tbofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.LEOFS:
        logger.info("LEOFS profiles:\n%s" % lib.atlases.leofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.LMHOFS:
        logger.info("LMHOFS profiles:\n%s" % lib.atlases.lmhofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.LOOFS:
        logger.info("LOOFS profiles:\n%s" % lib.atlases.loofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.LSOFS:
        logger.info("LSOFS profiles:\n%s" % lib.atlases.lsofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.SSCOFS:
        logger.info("SSCOFS profiles:\n%s" % lib.atlases.sscofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.SFBOFS:
        logger.info("SFBOFS profiles:\n%s" % lib.atlases.sfbofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    elif switch is ModelOptions.WCOFS:
        logger.info("WCOFS profiles:\n%s" % lib.atlases.wcofs.query(lat=test[0], lon=test[1], dtstamp=test[2]))
    else:
        raise RuntimeError("invalid switch value: %s" % switch)
    logger.info("execution time: %.3f s" % (time.time() - start_time))

app.exec()  # no need to actually run the message loop
