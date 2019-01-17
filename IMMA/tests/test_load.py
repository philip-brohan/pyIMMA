import unittest

import IMMA
import pickle
import os
 
# Need to find the test files
thisdir=os.path.dirname(os.path.abspath(__file__))

class TestLoad(unittest.TestCase):
 
    # Start simple
    def test_load_simple(self):
        with open("%s/pickled_samples/basic.pkl" % thisdir,"rb" ) as pf:
            target=pickle.load(pf)
        with open("%s/sample_files/basic.imma" % thisdir,"rt") as imf:
            loaded=IMMA.read(imf)
        self.assertEqual(loaded,target)

    # Variable sets of attachments
    def test_load_mixed(self):
        with open("%s/pickled_samples/mixed_attachments.pkl" % thisdir,
                            "rb" ) as pf:
            target=pickle.load(pf)
        with open("%s/sample_files/mixed_attachments.imma" % thisdir) as imf:  
            loaded=IMMA.read(imf)
        self.assertEqual(loaded,target)

    # Unusual attachments
    def test_load_unusual(self):
        with open("%s/pickled_samples/IMMA1_0+1+5+6+7+8+9+98+99.pkl" % thisdir,
                            "rb" ) as pf:
            target=pickle.load(pf)
        with open("%s/sample_files/IMMA1_0+1+5+6+7+8+9+98+99.imma" % thisdir) as imf: 
            loaded=IMMA.read(imf)
        self.assertEqual(loaded,target)
  
if __name__ == '__main__':
    unittest.main()
