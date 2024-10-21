import logging

import numpy as np

from hyo2.ssm2.lib.profile.oceanography import Oceanography as Oc
from hyo2.abc2.lib.logging import set_logging

set_logging(ns_list=["hyo2.abc2", "hyo2.ssm2"])

logger = logging.getLogger(__name__)

# gold ref using the matlab script: generate_gsw_trusted_values.m and GSW 3.05

# - @ 1000m

# absolute salinity
sa = np.array([34.7118, 34.8915, 35.0256, 34.8472, 34.7366, 34.7324])
# conservative temperature
ct = np.array([28.8099, 28.4392, 22.7862, 10.2262,  6.8272,  4.3236])
# sea pressure
p = np.array([10.0, 50.0, 125.0, 250.0, 600.0, 1000.0])
p_ref = 1000.0
# golden reference values
gold_ref = np.array([17.0392, 14.6659, 10.9129, 7.5679, 3.3935, 0])

calc_out = Oc.geo_strf_dyn_height(sa=sa, ct=ct, p=p, p_ref=p_ref)
print("@1000")
print("gold: %s" % gold_ref)
print("calc: %s" % calc_out)
print("diff: %s" % (calc_out - gold_ref))

# - @ 500m

# absolute salinity
sa = np.array([34.7118, 34.8915, 35.0256, 34.8472, 34.7366, 34.7324])
# conservative temperature
ct = np.array([28.8099, 28.4392, 22.7862, 10.2262,  6.8272,  4.3236])
# sea pressure
p = np.array([10.0, 50.0, 125.0, 250.0, 600.0, 1000.0])
p_ref = 500.0
# golden reference values
gold_ref = np.array([12.5588, 10.1854, 6.4324, 3.0875, -1.0869, -4.4804])

calc_out = Oc.geo_strf_dyn_height(sa=sa, ct=ct, p=p, p_ref=p_ref)
print("\n@500")
print("gold: %s" % gold_ref)
print("calc: %s" % calc_out)
print("diff: %s" % (calc_out - gold_ref))

# - @ 0m

# absolute salinity
sa = np.array([34.7118, 34.8915, 35.0256, 34.8472, 34.7366, 34.7324])
# conservative temperature
ct = np.array([28.8099, 28.4392, 22.7862, 10.2262,  6.8272,  4.3236])
# sea pressure
p = np.array([10.0, 50.0, 125.0, 250.0, 600.0, 1000.0])
p_ref = 0.0
# golden reference values
gold_ref = np.array([-0.6008, -2.9742, -6.7272, -10.0721, -14.2465, -17.6400])

calc_out = Oc.geo_strf_dyn_height(sa=sa, ct=ct, p=p, p_ref=p_ref)
print("\n@0")
print("gold: %s" % gold_ref)
print("calc: %s" % calc_out)
print("diff: %s" % (calc_out - gold_ref))
