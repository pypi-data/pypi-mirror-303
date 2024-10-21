import logging
import os

from matplotlib import pyplot as plt

from hyo2.abc2.lib.logging import set_logging
from hyo2.ssm2.lib.base.callbacks.fake_callbacks import FakeCallbacks
from hyo2.ssm2.lib.base.testing import SoundSpeedTesting
from hyo2.ssm2.lib.soundspeed import SoundSpeedLibrary

set_logging(ns_list=["hyo2.abc2", "hyo2.ssm2"])

logger = logging.getLogger(__name__)

# create a project with test-callbacks
lib = SoundSpeedLibrary(callbacks=FakeCallbacks())

# set the current project name
lib.setup.current_project = 'test'

data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
testing = SoundSpeedTesting(root_folder=data_folder)

# retrieve data input/output folders
data_input = testing.input_data_folder()
logger.info('input folder: %s' % data_input)
data_output = testing.output_data_folder()
logger.info('output folder: %s' % data_output)

# test readers/writers
logger.info('test: *** START ***')
filters = ["aml", ]
tests = testing.input_dict_test_files(inclusive_filters=filters)
# print(tests)

first_done = False

# import each identified file
for idx, testfile in enumerate(tests.keys()):

    logger.debug("%d -> filename: %s" % (idx, testfile))

    if first_done:
        break
    else:
        first_done = True

    logger.info("test: * New profile: #%03d *" % idx)

    # import
    lib.import_data(data_path=testfile, data_format=tests[testfile].name)
    logger.debug("\n%s" % lib.cur)
    lib.plot_ssp(more=True, show=False)

    # store the current profile
    success = lib.store_data()
    logger.info("stored: %s" % success)

plt.show()

# retrieve all the id profiles from db
lst = lib.db_list_profiles()
logger.info("Profiles: %s" % len(lst))
for p in lst:
    logger.info(p)

# retrieve a specific profile and delete it
ssp_pk = lst[0][0]
ssp = lib.db_retrieve_profile(pk=ssp_pk)
logger.info("Retrieved profile:\n%s" % ssp)
ret = lib.delete_db_profile(pk=ssp_pk)
logger.info("Deleted profile: %s" % ret)

logger.info('test: *** END ***')
