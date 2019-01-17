import unittest

import IMMA
import pickle
import tempfile
import filecmp
import os
 
# Need to find the test files
thisdir=os.path.dirname(os.path.abspath(__file__))

class TestWrite(unittest.TestCase):
 
    # Start simple
    def test_write_simple(self):
        with open("%s/pickled_samples/basic.pkl" % thisdir,
                            "rb" ) as pf:
            obs=pickle.load(pf)
        tmfn=tempfile.NamedTemporaryFile(delete=False)
        for o in obs:
           IMMA.write(o,tmfn)
        tmfn.close()
        self.assertTrue(filecmp.cmp(tmfn.name,
                                    "%s/sample_files/basic.imma" % thisdir,
                                    shallow=False))
        os.unlink(tmfn.name)

    # Variable sets of attachments
    def test_write_variable(self):
        with open("%s/pickled_samples/mixed_attachments.pkl" % thisdir,
                            "rb" ) as pf:
            obs=pickle.load(pf)
        tmfn=tempfile.NamedTemporaryFile(delete=False)
        for o in obs:
           IMMA.write(o,tmfn)
        tmfn.close()
        self.assertTrue(filecmp.cmp(tmfn.name,
                                    "%s/sample_files/mixed_attachments.imma" % thisdir,
                                    shallow=False))
        os.unlink(tmfn.name)

    # Unusual attachments
    def test_write_unusual(self):
        with open("%s/pickled_samples/IMMA1_0+1+5+6+7+8+9+98+99.pkl" % thisdir,
                            "rb" ) as pf:
            obs=pickle.load(pf)
        tmfn=tempfile.NamedTemporaryFile(delete=False)
        for o in obs:
           IMMA.write(o,tmfn)
        tmfn.close()
        self.assertTrue(filecmp.cmp(tmfn.name,
                                    "%s/sample_files/IMMA1_0+1+5+6+7+8+9+98+99.imma" % thisdir,
                                    shallow=False))
        os.unlink(tmfn.name)
  
if __name__ == '__main__':
    unittest.main()
