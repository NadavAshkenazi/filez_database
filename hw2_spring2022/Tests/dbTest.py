import unittest
import Solution
from Utility.Status import Status
from Tests.abstractTest import AbstractTest
from Business.File import File
from Business.RAM import RAM
from Business.Disk import Disk

'''
    Simple test, create one of your own
    make sure the tests' names start with test_
'''


class Test(AbstractTest):
    def test_Disk(self) -> None:
        self.assertEqual(Status.OK, Solution.addDisk(Disk(1, "DELL", 10, 10, 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(Disk(2, "DELL", 10, 10, 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(Disk(3, "DELL", 10, 10, 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(Disk(4, "TRANSCEND", 20, 10, 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(Disk(5, "TRANSCEND", 30, 20, 20)), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(Disk(6, "TRANSCEND", 40, 30, 30)), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDisk(Disk(1, "DELL", 10, 10, 10)),
                         "ID 1 already exists")

    def test_RAM(self) -> None:
        self.assertEqual(Status.OK, Solution.addRAM(RAM(1, "Kingston", 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM(2, "Kingston", 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM(3, "Kingston", 10)), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAM(RAM(2, "Kingston", 10)),
                         "ID 2 already exists")

    def test_File(self) -> None:
        self.assertEqual(Status.OK, Solution.addFile(File(1, "wav", 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(File(2, "wav", 10)), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(File(3, "wav", 10)), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addFile(File(3, "wav", 10)),
                         "ID 3 already exists")

    def test_all(self) -> None:
        # objects
        disk1 = Disk(1, "DELL", 10, 10, 1)
        disk2 = Disk(2, "DELL", 20, 20, 2)
        disk3 = Disk(3, "DELL", 30, 30, 3)
        disk4 = Disk(4, "TRANSCEND", 40, 40, 4)
        disk5 = Disk(5, "TRANSCEND", 50, 50, 5)
        disk6 = Disk(6, "TRANSCEND", 60, 60, 6)

        RAM1 = RAM(1, "Kingston", 10)
        RAM2 = RAM(2, "Kingston", 20)
        RAM3 = RAM(3, "Kingston", 30)
        RAM4 = RAM(4, "DELL", 40)
        RAM5 = RAM(5, "DELL", 50)
        RAM6 = RAM(6, "DELL", 60)

        file1 = File(1, "wav", 1)
        file2 = File(2, "wav", 2)
        file3 = File(3, "wav", 3)
        file4 = File(4, "mp4", 4)
        file5 = File(5, "txt", 5)
        file6 = File(6, "wav", 6)

        # disks
        self.assertEqual(Status.OK, Solution.addDisk(disk1), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk2), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk3), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk4), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk5), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDisk(disk1),
                         "ID 1 already exists")
        # rams
        self.assertEqual(Status.OK, Solution.addRAM(RAM1), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM2), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM3), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM4), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM5), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAM(RAM2),
                         "ID 2 already exists")
        # files
        self.assertEqual(Status.OK, Solution.addFile(file1), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file2), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file3), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file4), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file5), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addFile(file3),
                         "ID 3 already exists")

        #deletes
        self.assertEqual(6, Solution.getDiskByID(6).getDiskID(), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(6), "Should work")
        self.assertEqual(Disk.badDisk().getDiskID(), Solution.getDiskByID(6).getDiskID(), "NO DISK 6")
        self.assertEqual(Status.NOT_EXISTS, Solution.deleteDisk(6), "NO DISK 6")


        self.assertEqual(6, Solution.getRAMByID(6).getRamID(), "Should work")
        self.assertEqual(Status.OK, Solution.deleteRAM(6), "Should work")
        self.assertEqual(RAM.badRAM().getRamID(), Solution.getRAMByID(6).getRamID(), "NO RAM 6")
        self.assertEqual(Status.NOT_EXISTS, Solution.deleteRAM(6), "NO RAM 6")

        self.assertEqual(6, Solution.getFileByID(6).getFileID(), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file6), "Should work")
        self.assertEqual(File.badFile().getFileID(), Solution.getFileByID(6).getFileID(), "NO File 6")
        self.assertEqual(Status.ERROR, Solution.deleteFile(6), "NO File 6")

        #disk and file relationaship

        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk6, file6), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 6), "Should work")
        self.assertEqual(54, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file6, 6), "Should work")
        self.assertEqual(60, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 6), "Should work")
        self.assertEqual(54, Solution.getDiskByID(6).getFreeSpace(), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(file4, 5), "Should work")
        self.assertEqual(46, Solution.getDiskByID(5).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 5), "Should work")
        self.assertEqual(40, Solution.getDiskByID(5).getFreeSpace(), "Should work")

        self.assertEqual(Status.OK, Solution.deleteFile(file6), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file6, 6), "FILE 6 DELETED")
        self.assertEqual(60, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(46, Solution.getDiskByID(5).getFreeSpace(), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 6), "Should work")

        self.assertEqual(Status.ALREADY_EXISTS, Solution.addFileToDisk(file1, 6), "FILE 1 ALREADY ON DISK")
        self.assertEqual(Status.NOT_EXISTS, Solution.addFileToDisk(file6, 6), "FILE 6 DELETED")
        self.assertEqual(2, Solution.averageFileSizeOnDisk(6), "Should work - files 1,2,3")
        self.assertEqual(4, Solution.averageFileSizeOnDisk(5), "Should work - files 4")
        self.assertEqual(0, Solution.averageFileSizeOnDisk(1), "NO FILES ON DISK 1")
        self.assertEqual(0, Solution.averageFileSizeOnDisk(7), "NO DISK 7")
        self.assertEqual(-1, Solution.averageFileSizeOnDisk("SIX"), "KEY MUST BE INTEGER")

        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file5, 4), "Should work")
        self.assertEqual(40, Solution.getCostForType("wav"), "Should work - 4*(1) + 6*(1+2+3) = 40")
        self.assertEqual(20, Solution.getCostForType("mp4"), "Should work - 5*(4) = 20")
        self.assertEqual(20, Solution.getCostForType("txt"), "Should work - 4*(5) = 20")
        self.assertEqual(0, Solution.getCostForType("pdf"), "PDF does not exist")
        self.assertEqual(-1, Solution.getCostForType(1), "type should be string")

        self.assertEqual(Status.OK, Solution.addFile(file6), "Should work")
        self.assertEqual([6,5,4,3,2], Solution.getFilesCanBeAddedToDisk(6), "Should work")

        disk7 = Disk(7, "TRANSCEND", 60, 4, 7)
        self.assertEqual(Status.OK, Solution.addDisk(disk7), "Should work")
        self.assertEqual([4,3,2,1], Solution.getFilesCanBeAddedToDisk(7), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")


        disk7 = Disk(7, "TRANSCEND", 60, 1, 7)
        self.assertEqual(Status.OK, Solution.addDisk(disk7), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 7), "Should work")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk(7), "NO FREE SPACE ON DISK 7")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk(8), "NO DISK 8")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk("SIX"), "KEY SHOULD BE INTEGER")





        pass

        #disk and ram relationaship

        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(3, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(4, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(5, 6), "Should work")
        self.assertEqual(Status.NOT_EXISTS, Solution.addRAMToDisk(6, 6), "NO RAM 6")
        self.assertEqual(140, Solution.diskTotalRAM(6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(5, 6), "Should work")
        self.assertEqual(Status.NOT_EXISTS, Solution.removeRAMFromDisk(5, 6), "RAM 5 ALREADY REMOVED")
        self.assertEqual(Status.NOT_EXISTS, Solution.removeRAMFromDisk(6, 6), "NO RAM 6")
        self.assertEqual(90, Solution.diskTotalRAM(6), "Should work")


        # self.assertEqual([1,2,3,4,5], Solution.getFilesCanBeAddedToDiskAndRAM(6), "Should work")

        #disk and ram relationaship

        pass







# *** DO NOT RUN EACH TEST MANUALLY ***
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)