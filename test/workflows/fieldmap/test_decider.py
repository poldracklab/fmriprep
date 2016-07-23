import logging

from fmriprep.workflows.fieldmap import decider
from fmriprep.utils import misc

from test.workflows.utilities import TestWorkflow
import test.constant as c

class TestDecider(TestWorkflow):
    # ideally this would be a true unit test but in the interests of
    # time it is more like a smoke test
    # also it won't run in circle ci w/o some set up
    def test_decider_phasediff_and_mags(self):
        logging.basicConfig(level=logging.DEBUG)
        # SET UP INPUTS
        subject_data = misc.get_subject(c.DATASET, '100003')

        # RUN
        wf = decider.fieldmap_decider(subject_data, {})
#        wf.run()
