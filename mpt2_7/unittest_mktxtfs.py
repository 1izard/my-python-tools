import unittest
import mktxtfs
import tempfile
import os
import glob
import shutil


class MktxtfsTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp_dirname = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dirname)

    def test_mktxtsfs_default(self):
        dirname = 'txts1'
        dirpath = os.path.join(self.tmp_dirname, dirname)
        argv = [dirpath]
        mktxtfs.main(argv)

        exist_txts = [os.path.basename(x) for x in glob.glob(os.path.join(dirpath, '*.txt'))]
        expected_txts = ['{}_{}.txt'.format(dirname, x) for x in range(1, 11)]

        actual = True
        for expected_txt in expected_txts:
            if not(expected_txt in exist_txts):
                actual = False
                break

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
