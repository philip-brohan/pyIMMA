#!/usr/bin/env python

# This is not part of the test suite. 

# It recreates the pickle files from the IMMA files. Run it when
#  changes to the package have changed the internal representation
#  of an IMMA record. Possibly also when changes to Python have
#  changed the pickle format.

# Don't run it otherwise - it will invalidate the tests.

import os
import IMMA
import pickle

thisdir=os.path.dirname(os.path.abspath(__file__))

o=IMMA.read("%s/../sample_files/basic.imma" % thisdir)
pickle.dump(o,open("%s/../pickled_samples/basic.pkl" % thisdir, "wb" ) )

o=IMMA.read("%s/../sample_files/mixed_attachments.imma" % thisdir)
pickle.dump(o,open("%s/../pickled_samples/mixed_attachments.pkl" % thisdir, "wb" ) )

o=IMMA.read("%s/../sample_files/IMMA1_0+1+5+6+7+8+9+98+99.imma" % thisdir)
pickle.dump(o,open("%s/../pickled_samples/IMMA1_0+1+5+6+7+8+9+98+99.pkl" % thisdir, "wb" ) )

