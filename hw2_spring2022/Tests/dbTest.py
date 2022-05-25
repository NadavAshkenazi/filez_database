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
        disk1 = Disk(1, "DELL", 10, 10, 10)
        disk2 = Disk(2, "DELL", 10, 10, 10)
        disk3 = Disk(3, "DELL", 10, 10, 10)
        disk4 = Disk(4, "TRANSCEND", 20, 10, 10)
        disk5 = Disk(5, "TRANSCEND", 30, 20, 20)
        disk6 = Disk(6, "TRANSCEND", 40, 30, 30)

        RAM1 = RAM(1, "Kingston", 10)
        RAM2 = RAM(2, "Kingston", 10)
        RAM3 = RAM(3, "Kingston", 10)
        RAM4 = RAM(4, "DELL", 10)
        RAM5 = RAM(5, "DELL", 10)
        RAM6 = RAM(6, "DELL", 10)

        file1 = File(1, "wav", 1)
        file2 = File(2, "wav", 2)
        file3 = File(3, "wav", 3)
        file4 = File(4, "mp4", 4)
        file5 = File(5, "mp4", 5)
        file6 = File(6, "mp4", 6)

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

        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk6, file6), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 6), "Should work")
        self.assertEqual(24, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file6, 6), "Should work")
        self.assertEqual(30, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        pass



# *** DO NOT RUN EACH TEST MANUALLY ***
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)