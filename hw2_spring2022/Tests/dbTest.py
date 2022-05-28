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

    def test_avg(self) -> None:
        disk = Disk(1, "TRANSCEND", 40, 40, 4)

        file1 = File(1, "wav", 1)
        file2 = File(2, "wav", 2)
        file3 = File(3, "wav", 3)
        file4 = File(4, "mp4", 4)

        self.assertEqual(Status.OK, Solution.addDisk(disk), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file1), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file2), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file3), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file4), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file4, 1), "Should work")

        self.assertEqual(2.5, Solution.averageFileSizeOnDisk(1), "Should work")

    def test_all(self) -> None:
        # objects
        disk1 = Disk(1, "DELL", 10, 10, 1)
        disk2 = Disk(2, "DELL", 20, 20, 2)
        disk3 = Disk(3, "DELL", 30, 30, 3)
        disk4 = Disk(4, "TRANSCEND", 40, 40, 4)
        disk5 = Disk(5, "TRANSCEND", 50, 50, 5)
        disk6 = Disk(6, "TRANSCEND", 60, 60, 6)

        RAM1 = RAM(1, "DELL", 1)
        RAM2 = RAM(2, "DELL", 2)
        RAM3 = RAM(3, "DELL", 3)
        RAM4 = RAM(4, "Kingston", 4)
        RAM5 = RAM(5, "Kingston", 5)
        RAM6 = RAM(6, "Kingston", 6)

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
        self.assertEqual(Status.BAD_PARAMS, Solution.addDisk(Disk(7, "DELL", 0, 0, 0)), "free_space = 0")

        # rams
        self.assertEqual(Status.OK, Solution.addRAM(RAM1), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM2), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM3), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM4), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM5), "Should work")
        self.assertEqual(Status.OK, Solution.addRAM(RAM6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAM(RAM2),
                         "ID 2 already exists")
        self.assertEqual(Status.BAD_PARAMS, Solution.addRAM(RAM(7, "Kingston", 0)), "size = 0")

        # files
        self.assertEqual(Status.OK, Solution.addFile(file1), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file2), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file3), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file4), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file5), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addFile(file3),
                         "ID 3 already exists")
        self.assertEqual(Status.BAD_PARAMS, Solution.addFile(File(7, "wav", -1)), "size_needed = 0")

        # deletes
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
        self.assertEqual(Status.ERROR, Solution.deleteFile(Solution), "NO File 6")

        # disk and file relationship

        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk6, file6), "Should work")

        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDiskAndFile(disk5, file5),
                         "diskId 5 and fileId 5 already defined")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDiskAndFile(disk5, file6), "diskId 5 already defined")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addDiskAndFile(disk6, file5), "fileId 5 already defined")

        file7 = File(7, "wav", 7)
        self.assertEqual(Status.NOT_EXISTS, Solution.addFileToDisk(file7, 6), "NO FILE 7 IN FILES")

        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 6), "Should work")
        self.assertEqual(54, Solution.getDiskByID(6).getFreeSpace(), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file7, 6), "Should work - file 7 not on disk")
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
        self.assertEqual([6, 5, 4, 3, 2], Solution.getFilesCanBeAddedToDisk(6), "Should work")

        disk7 = Disk(7, "TRANSCEND", 60, 4, 7)
        self.assertEqual(Status.OK, Solution.addDisk(disk7), "Should work")
        self.assertEqual([4, 3, 2, 1], Solution.getFilesCanBeAddedToDisk(7), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")

        file11 = File(11, "wav", 11)
        self.assertEqual(Status.OK, Solution.addFile(file11), "Should work")
        self.assertEqual(Status.BAD_PARAMS, Solution.addFileToDisk(file11, 1), "NO SPACE")
        self.assertEqual(Status.OK, Solution.deleteFile(file11), "Should work")

        disk7 = Disk(7, "TRANSCEND", 60, 1, 7)
        self.assertEqual(Status.OK, Solution.addDisk(disk7), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 7), "Should work")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk(7), "NO FREE SPACE ON DISK 7")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk(8), "NO DISK 8")
        self.assertEqual([], Solution.getFilesCanBeAddedToDisk("SIX"), "KEY SHOULD BE INTEGER")

        pass

        # disk and ram relationship

        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(3, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(4, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(5, 6), "Should work")
        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAMToDisk(2, 5), "RAM 2 ON DISK 6 ALREADY")

        self.assertEqual(Status.NOT_EXISTS, Solution.addRAMToDisk(6, 6), "NO RAM 6")
        self.assertEqual(14, Solution.diskTotalRAM(6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(5, 6), "Should work")
        self.assertEqual(Status.NOT_EXISTS, Solution.removeRAMFromDisk(5, 6), "RAM 5 ALREADY REMOVED")
        self.assertEqual(Status.NOT_EXISTS, Solution.removeRAMFromDisk(6, 6), "NO RAM 6")
        self.assertEqual(9, Solution.diskTotalRAM(6), "Should work")
        self.assertEqual([1, 2, 3, 4, 5], Solution.getFilesCanBeAddedToDiskAndRAM(6), "Should work")

        disk7 = Disk(7, "TRANSCEND", 60, 1, 7)
        self.assertEqual(Status.OK, Solution.addDisk(disk7), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 7), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(2, 6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(3, 6), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(4, 6), "Should work")

        self.assertEqual(Status.OK, Solution.addRAMToDisk(1, 7), "Should work")
        self.assertEqual(1, Solution.diskTotalRAM(7), "Should work - RAM 1 ON DISK 7")
        self.assertEqual([1], Solution.getFilesCanBeAddedToDiskAndRAM(7), "Should work - free space + ram = 1")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(2, 7), "Should work")
        self.assertEqual(3, Solution.diskTotalRAM(7), "Should work - RAM 1+2 ON DISK 7")
        self.assertEqual([1, 2, 3], Solution.getFilesCanBeAddedToDiskAndRAM(7), "Should work - free space + ram = 3")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(4, 7), "Should work")
        self.assertEqual([1, 2, 3, 4, 5], Solution.getFilesCanBeAddedToDiskAndRAM(7),
                         "Should work - free space + ram = 7")

        RAM7 = RAM(7, "DELL", 7)
        self.assertEqual(Status.OK, Solution.addRAM(RAM7), "Should work")
        self.assertEqual(7, Solution.diskTotalRAM(7), "Should work - RAM 1+2+4 ON DISK 7")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(7, 7), "Should work - RAM 1+2+4 ON DISK 7")
        self.assertEqual(14, Solution.diskTotalRAM(7), "Should work - RAM 1+2+4+7 ON DISK 7")
        self.assertEqual(Status.OK, Solution.deleteRAM(7), "Should work")
        self.assertEqual(7, Solution.diskTotalRAM(7), "Should work - RAM 1+2+4 ON DISK 7")

        self.assertEqual(Status.ALREADY_EXISTS, Solution.addRAMToDisk(1, 5), "RAM 2 ON DISK 7 ALREADY")
        self.assertEqual(Status.OK, Solution.deleteDisk(7), "Should work")
        self.assertEqual(Status.OK, Solution.addRAMToDisk(1, 5), "Should work")
        self.assertEqual(Status.OK, Solution.removeRAMFromDisk(1, 5), "Should work")

        self.assertEqual(Status.OK, Solution.addRAM(RAM6), "Should work")

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

        # advanced API
        # conflicting disks
        self.assertEqual([4, 6], Solution.getConflictingDisks(), "Should work - file 1 on DISK 4 ,6")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file1, 4), "Should work")
        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file1, 6), "Should work")
        self.assertEqual([], Solution.getConflictingDisks(), "NO CONFLICTING DISKS")

        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file3, 6), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 2), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 2), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file5, 5), "Should work")
        self.assertEqual([1, 2, 4, 5, 6], Solution.getConflictingDisks(),
                         "Should work - (2->1,2,6), (3->1,2), (5->4,5)")

        file7 = File(7, "wav", 1)
        self.assertEqual(Status.OK, Solution.addFile(file7), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file7, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file7, 2), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file7, 3), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file7, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file7, 5), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file7, 6), "Should work")
        self.assertEqual([1, 2, 3, 4, 5, 6], Solution.getConflictingDisks(),
                         "Should work - (2->1,2,6), (3->1,2), (5->4,5), (7->1-6)")
        self.assertEqual(Status.OK, Solution.deleteFile(file7), "Should work")
        self.assertEqual([1, 2, 4, 5, 6], Solution.getConflictingDisks(),
                         "Should work - (2->1,2,6), (3->1,2), (5->4,5)")

        # available disks
        self.assertEqual(Status.OK, Solution.deleteFile(file1), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file2), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file3), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file4), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file5), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file6), "Should work")

        disk11 = Disk(11, "DELL", 1, 1, 1)
        disk12 = Disk(12, "DELL", 2, 2, 2)
        disk13 = Disk(13, "DELL", 3, 3, 3)
        disk14 = Disk(14, "DELL", 4, 4, 4)
        disk15 = Disk(15, "DELL", 5, 5, 5)
        disk16 = Disk(16, "DELL", 6, 6, 6)

        self.assertEqual(Status.OK, Solution.addFile(file1), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file2), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file3), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file4), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file5), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file6), "Should work")

        self.assertEqual(Status.OK, Solution.addDisk(disk11), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk12), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk13), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk14), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk15), "Should work")
        self.assertEqual(Status.OK, Solution.addDisk(disk16), "Should work")

        self.assertEqual([6, 5, 4, 3, 2], Solution.mostAvailableDisks(), "Should work")

        disk21 = Disk(21, "DELL", 6, 101, 1)
        disk22 = Disk(22, "DELL", 5, 90, 1)
        disk23 = Disk(23, "DELL", 4, 103, 1)
        disk24 = Disk(24, "DELL", 3, 104, 1)
        disk25 = Disk(25, "DELL", 2, 105, 1)
        disk26 = Disk(26, "DELL", 1, 106, 1)

        file21 = File(21, "wav", 80)
        file22 = File(22, "wav", 92)
        file23 = File(23, "wav", 93)
        file24 = File(24, "mp4", 94)
        file25 = File(25, "txt", 95)
        file26 = File(26, "wav", 101)

        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk21, file21), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk22, file22), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk23, file23), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk24, file24), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk25, file25), "Should work")
        self.assertEqual(Status.OK, Solution.addDiskAndFile(disk26, file26), "Should work")

        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 26), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 26), "Should work")  # disk 26 - 101
        self.assertEqual(Status.OK, Solution.addFileToDisk(file5, 25), "Should work")  # disk 25 - 100
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 21), "Should work")  # disk 21 - 100

        self.assertEqual([23, 24, 26, 21, 25], Solution.mostAvailableDisks(), "Should work")

        self.assertEqual(Status.OK, Solution.deleteFile(file21), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file22), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file23), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file24), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file25), "Should work")
        self.assertEqual(Status.OK, Solution.deleteFile(file26), "Should work")

        self.assertEqual(Status.OK, Solution.deleteDisk(21), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(22), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(23), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(24), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(25), "Should work")
        self.assertEqual(Status.OK, Solution.deleteDisk(26), "Should work")

        # closeset files

        # file 1 - disks 1,2,3,4,5,6
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 2), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 3), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 5), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 6), "Should work")

        # file 2 - disks 2,4,6
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 2), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file2, 6), "Should work")

        # file 3 - disks 1,3,5,6
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 3), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 5), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file3, 6), "Should work")

        # file 4 - disks 1,2,3
        self.assertEqual(Status.OK, Solution.addFileToDisk(file4, 1), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file4, 2), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file4, 3), "Should work")

        # file 5 - disks 4,5,6
        self.assertEqual(Status.OK, Solution.addFileToDisk(file5, 4), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file5, 5), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file5, 6), "Should work")

        # files 6 - not saves

        self.assertEqual([2, 3, 4, 5], Solution.getCloseFiles(1), "Should work")
        self.assertEqual([1, 2, 3, 4, 5], Solution.getCloseFiles(6), "Should work")
        self.assertEqual([1, 5], Solution.getCloseFiles(2), "Should work")

        # files 6 - disks 11

        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 16), "Should work")
        self.assertEqual([], Solution.getCloseFiles(6), "no shared disks")

        # files 6 - disks 16,17, file1 1-6, 17
        disk17 = Disk(17, "DELL", 100, 100, 100)
        self.assertEqual(Status.OK, Solution.addDisk(disk17), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file1, 17), "Should work")
        self.assertEqual(Status.OK, Solution.addFileToDisk(file6, 17), "Should work")
        self.assertEqual([1], Solution.getCloseFiles(6), "out of 2 disks sharing disk17 with file1")
        self.assertEqual([], Solution.getCloseFiles("SIX"), "KEY SHOULD BE INTEGER")
        self.assertEqual([], Solution.getCloseFiles(-1), "KEY SHOULD > 0")

        self.assertEqual(Status.OK, Solution.removeFileFromDisk(file1, 17), "Should work")

        file21 = File(21, "wav", 80)
        file22 = File(22, "wav", 92)
        file23 = File(23, "wav", 93)
        file24 = File(24, "mp4", 94)
        file25 = File(25, "txt", 95)
        file26 = File(26, "wav", 101)

        self.assertEqual(Status.OK, Solution.addFile(file21), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file22), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file23), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file24), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file25), "Should work")
        self.assertEqual(Status.OK, Solution.addFile(file26), "Should work")
        self.assertEqual([1, 2, 3, 4, 5, 6, 22, 23, 24, 25], Solution.getCloseFiles(21), "Should work")

        pass


# *** DO NOT RUN EACH TEST MANUALLY ***
if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
