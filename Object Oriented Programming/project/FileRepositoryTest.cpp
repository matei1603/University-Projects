#include "FileRepositoryTest.h"
#include "FileRepo.h"
#include "exceptions.h"


void FileRepositoryTest::testFileRepository() const {
    FileRepo fileRepo("test_file.txt");



    // test store() method
    fileRepo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");


    // test remove() method
    fileRepo.remove("Song 1", "Artist 1");

}

void FileRepositoryTest::testReadData() const {
    FileRepo fileRepo("test_file.txt");

    // test reading data from a file
    std::vector<Song> songs = fileRepo.read_data();
    assert(songs.size() == 0);

}

void FileRepositoryTest::testWriteData() const {
    FileRepo fileRepo("test_file.txt");

    // test writing data to a file
    std::vector<Song> songs;
    songs.push_back(Song("Song 1", "Artist 1", "Lyrics 1", "Link 1"));
    songs.push_back(Song("Song 2", "Artist 2", "Lyrics 2", "Link 2"));
    fileRepo.write_data(songs);

}

void FileRepositoryTest::testStore() const {
    FileRepo fileRepo("test_file.txt");

    // test storing songs in the file repository
    fileRepo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    fileRepo.store("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    assert(fileRepo.get_size() == 2);

    // test storing duplicate song
    try {
        fileRepo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
        // the above line should throw an exception, so the below assert is not reached
        assert(false);
    }
    catch (const Exceptions& e) {
        // the exception should be caught and the size should remain the same
        assert(fileRepo.get_size() == 2);
    }
}

void FileRepositoryTest::testRemove() const {
    FileRepo fileRepo("test_file.txt");

    // add some songs to the file repository
    fileRepo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    fileRepo.store("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    fileRepo.store("Song 3", "Artist 3", "Lyrics 3", "Link 3");

    // test removing a song from the file repository
    fileRepo.remove("Song 2", "Artist 2");
    assert(fileRepo.get_size() == 2);

    // test removing a non-existent song
    try {
        fileRepo.remove("Song 4", "Artist 4");
        /// the above line should throw an exception, so the below assert is not reached
        assert(false);
    }
    catch (const RepoExceptions& e) {
        // the exception should be caught and the size should remain the same
        assert(fileRepo.get_size() == 2);
    }
}
