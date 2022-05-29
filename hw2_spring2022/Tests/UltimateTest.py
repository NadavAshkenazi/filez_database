import unittest
import Solution
from Utility.Status import Status
from Tests.abstractTest import AbstractTest
from Business.File import File
from Business.RAM import RAM
from Business.Disk import Disk



class Test(unittest.TestCase):

    # before each test, setUp is executed
    def setUp(self) -> None:
        Solution.createTables()

        # Objects to play with in the coming tests
        self.file1 = File(1, "wav", 1)
        self.file2 = File(2, "wav", 2)
        self.file3 = File(3, "wav", 3)
        self.file4 = File(4, "mp4", 4)
        self.file5 = File(5, "txt", 5)
        self.file6 = File(6, "wav", 6)
        self.file7 = File(7, "wav", 11)

        self.disk1 = Disk(1, "DELL", 10, 10, 1)
        self.disk2 = Disk(2, "DELL", 20, 20, 2)
        self.disk3 = Disk(3, "DELL", 30, 30, 3)
        self.disk4 = Disk(4, "TRANSCEND", 40, 40, 4)
        self.disk5 = Disk(5, "TRANSCEND", 50, 50, 5)
        self.disk6 = Disk(6, "TRANSCEND", 60, 60, 6)
        self.disk7 = Disk(7, "TRANSCEND", 60, 4, 7)
        self.disk8 = Disk(8, "TRANSCEND", 60, 1, 8)

        self.RAM1 = RAM(1, "DELL", 1)
        self.RAM2 = RAM(2, "DELL", 2)
        self.RAM3 = RAM(3, "DELL", 3)
        self.RAM4 = RAM(4, "Kingston", 4)
        self.RAM5 = RAM(5, "Kingston", 5)
        self.RAM6 = RAM(6, "Kingston", 6)
        self.RAM7 = RAM(7, "Kingston", 7)

    # after each test, tearDown is executed
    def tearDown(self) -> None:
        Solution.dropTables()

    def testFile(self) -> None:
        self.assertEqual(Status.OK, Solution.addFile(self.file1), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(self.file2), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(self.file3), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(self.file4), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(self.file5), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(self.file6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addFile(self.file3), "FILE ID 3 already exists")
        self.assertEqual(6, Solution.getFileByID(6).getFileID(), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(self.file6), "Should work")
        self.assertEqual(None, Solution.getFileByID(6).getFileID(), "NO File ID 6")
        self.assertEqual(Status.OK, Solution.deleteFile(self.file6), "NO File ID 6")

    def testDisk(self) -> None:
        self.assertEqual(Status.OK, Solution.addDisk(self.disk1), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(self.disk2), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(self.disk3), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(self.disk4), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(self.disk5), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(self.disk6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDisk(self.disk1), "DISK ID 1 already exists")
        self.assertEqual(6, Solution.getDiskByID(6).getDiskID(), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(6), "Should work")
        self.assertEqual(None, Solution.getDiskByID(6).getDiskID(), "NO DISK ID 6")
        self.assertEqual(Status.NOT_EXISTS, Solution.deleteDisk(6), "NO DISK ID 6")

    def testRAM(self) -> None:
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM1), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM2), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM3), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM4), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM5), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAM(self.RAM2), "RAM ID 2 already exists")
        self.assertEqual(6, Solution.getRAMByID(6).getRamID(), "Should work")
        self.assertEqual(Status.OK, Solution.deleteRAM(6), "Should work")
        self.assertEqual(None, Solution.getRAMByID(6).getRamID(), "NO RAM ID 6")
        self.assertEqual(Status.NOT_EXISTS, Solution.deleteRAM(6), "NO RAM ID 6")

    def testFileAndDisk(self) -> None:
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk1, self.file1), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk2, self.file2), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk3, self.file3), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk4, self.file4), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk5, self.file5), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk6, self.file6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDiskAndFile(self.disk6, self.file6), "DISK ID 5 and FILE ID 5 already defined")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDiskAndFile(self.disk6, self.file7), "DISK ID 5 already defined")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDiskAndFile(self.disk7, self.file6), "FILE ID 5 already defined")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk7, self.file7), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file6, 6), "Should work")
        self.assertEqual(54, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(self.file6, 6), "Should work")
        self.assertEqual(60, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file6, 6), "Should work")
        self.assertEqual(54, Solution.getDiskByID(6).getFreeSpace(), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file4, 5), "Should work")
        self.assertEqual(46, Solution.getDiskByID(5).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file6, 5), "Should work")
        self.assertEqual(40, Solution.getDiskByID(5).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file6, 1), "Should work")
        self.assertEqual(Status.BAD_PARAMS, Solution.addFileToDisk(self.file5, 1), "Should not work as there is not enough free space on DISK 1")

        self.assertEqual(Status.OK, Solution.deleteFile(self.file6), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(self.file6, 6), "FILE 6 DELETED")
        self.assertEqual(60, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(46, Solution.getDiskByID(5).getFreeSpace(), "Should work")
        self.assertEqual(10, Solution.getDiskByID(1).getFreeSpace(), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file1, 6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addFileToDisk(self.file1, 6), "FILE 1 ALREADY ON DISK")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file3, 6), "Should work")
        self.assertEqual(Status.NOT_EXISTS, Solution.addFileToDisk(self.file6, 6), "FILE 6 DELETED")
        self.assertEqual(2, Solution.averageFileSizeOnDisk(6), "Should work - files 1,2,3")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file5, 6), "Should work")
        self.assertEqual(2.75, round(Solution.averageFileSizeOnDisk(6), 2), "Should work")
        self.assertEqual(4, Solution.averageFileSizeOnDisk(5), "Should work - files 4")
        self.assertEqual(0, Solution.averageFileSizeOnDisk(1), "NO FILES ON DISK 1")
        self.assertEqual(0, Solution.averageFileSizeOnDisk(9), "NO DISK 7")
        self.assertEqual(-1, Solution.averageFileSizeOnDisk("SIX"), "KEY MUST BE INTEGER")

        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file1, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file5, 4), "Should work")
        self.assertEqual(40, Solution.getCostForType("wav"), "Should work - 4*(1) + 6*(1+2+3) = 40")
        self.assertEqual(20, Solution.getCostForType("mp4"), "Should work - 5*(4) = 20")
        self.assertEqual(50, Solution.getCostForType("txt"), "Should work - 4*(5) + 6*(5) = 50")
        self.assertEqual(0, Solution.getCostForType("pdf"), "PDF does not exist")
        self.assertEqual(-1, Solution.getCostForType(1), "type should be string")

        self.assertEqual(Status.OK, Solution.addFile(self.file6), "Should work")
        self.assertEqual([7, 6, 5, 4, 3], Solution.getFilesCanBeAddedToDisk(6), "Should work")

        self.assertEqual([4, 3, 2, 1], Solution.getFilesCanBeAddedToDisk(7), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")

        self.assertEqual(Status.BAD_PARAMS, Solution.addFileToDisk(self.file7, 1), "NO SPACE")
        self.assertEqual(Status.OK, Solution.deleteFile(self.file7), "Should work")

        self.assertEqual(Status.OK, Solution.addDisk(self.disk8), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file1, 8), "Should work")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk(8), "NO FREE SPACE ON DISK 8")
        self.assertEqual(Status.OK, Solution.deleteDisk(8), "Should work")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk(9), "NO DISK 9")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk("SIX"), "KEY SHOULD BE INTEGER")

    def testRAMAndDisk(self) -> None:
        # Needed preparations
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk1, self.file1), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk2, self.file2), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk3, self.file3), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk4, self.file4), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk5, self.file5), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk6, self.file6), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(self.disk7, self.file7), "Should work")

        self.assertEqual(Status.OK, Solution.addRAM(self.RAM1), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM2), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM3), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM4), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM5), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(self.RAM6), "Should work")

        # Actual tests
        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(3, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(4, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(5, 6), "Should work")
        self.assertEqual(Status.NOT_EXISTS, Solution.addRAMToDisk(8, 6), "NO RAM ID 8")
        self.assertEqual(14, Solution.diskTotalRAM(6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(5, 6), "Should work")
        self.assertEqual(Status.NOT_EXISTS, Solution.removeRAMFromDisk(5, 6), "RAM ID 5 ALREADY REMOVED")
        self.assertEqual(Status.NOT_EXISTS, Solution.removeRAMFromDisk(8, 6), "NO RAM ID 8")
        self.assertEqual(9, Solution.diskTotalRAM(6), "Should work")
        self.assertEqual([1,2,3,4,5], Solution.getFilesCanBeAddedToDiskAndRAM(6), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(self.file1, 7), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(3, 6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(4, 6), "Should work")

        self.assertEqual(Status.OK, Solution.addRAMToDisk(1, 7), "Should work")
        self.assertEqual(1, Solution.diskTotalRAM(7), "Should work - RAM 1 ON DISK 7")
        self.assertEqual([1], Solution.getFilesCanBeAddedToDiskAndRAM(7), "Should work - free space = 3 & ram = 1 => file1 is the only fit")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 7), "Should work")
        self.assertEqual(3, Solution.diskTotalRAM(7), "Should work - RAM 1+2 ON DISK 7")
        self.assertEqual([1, 2, 3], Solution.getFilesCanBeAddedToDiskAndRAM(7), "Should work - free space 3 & ram = 3")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(3, 7), "Should work")
        self.assertEqual([1, 2, 3], Solution.getFilesCanBeAddedToDiskAndRAM(7), "Should work - free space 3 & ram = 6")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(1, 6), "Should work")
        self.assertEqual([1], Solution.getFilesCanBeAddedToDiskAndRAM(6), "Should work - free space = 60 & ram = 1 => file1 is the only fit")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 6), "Should work")
        self.assertEqual([1, 2, 3], Solution.getFilesCanBeAddedToDiskAndRAM(6), "Should work - free space = 60 & ram = 3")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(3, 6), "Should work")
        self.assertEqual([1, 2, 3, 4, 5], Solution.getFilesCanBeAddedToDiskAndRAM(6), "Should work - free space = 60 & ram = 6")
        self.assertEqual([], Solution.getFilesCanBeAddedToDiskAndRAM(1), "DISK 1 has no RAMs connected")
        self.assertEqual([], Solution.getFilesCanBeAddedToDiskAndRAM(11), "DISK 11 NOT EXISTS")

        self.assertEqual(Status.OK, Solution.addRAM(self.RAM7), "Should work")
        self.assertEqual(6, Solution.diskTotalRAM(7), "Should work - RAM 1+2+3 ON DISK 7")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(7, 7), "Should work - RAM 1+2+4 ON DISK 7")
        self.assertEqual(13, Solution.diskTotalRAM(7), "Should work - RAM 1+2+3+7 ON DISK 7")
        self.assertEqual(Status.OK, Solution.deleteRAM(7), "Should work")
        self.assertEqual(6, Solution.diskTotalRAM(7), "Should work - RAM 1+2+3 ON DISK 7")

        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAMToDisk(1, 7), "RAM 1 ON DISK 7 ALREADY")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(1, 5), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(1, 5), "Should work")

        self.assertEqual(Status.OK, Solution.addRAMToDisk(1, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(3, 1), "Should work")

        self.assertEqual(Status.OK, Solution.addRAMToDisk(4, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(5, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(6, 4), "Should work")
        self.assertEqual(True, Solution.isCompanyExclusive(1), "Should work - EXCLUSIVE")
        self.assertEqual(False, Solution.isCompanyExclusive(4), "NOT EXCLUSIVE")
        self.assertEqual(True, Solution.isCompanyExclusive(2), "Should work - NO RAMS ON 2")
        self.assertEqual(False, Solution.isCompanyExclusive(10), "NO DISK 10")

# *** DO NOT RUN EACH TEST MANUALLY ***
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)