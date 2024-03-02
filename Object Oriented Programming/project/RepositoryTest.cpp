#include "RepositoryTest.h"
#include "exceptions.h"

void RepositoryTest::testRepository() const {
    Repo repo;

    // test get_size() method
    assert(repo.get_size() == 0);

    // test store() method
    repo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    assert(repo.get_size() == 1);

    // test remove() method
    repo.remove("Song 1", "Artist 1");
    assert(repo.get_size() == 0);
}

void RepositoryTest::testInitRepo() const {
    Repo repo;

    // test init_repo() method
    repo.init_repo();
    assert(repo.get_size() == 10);
}

void RepositoryTest::testStore() const {
    Repo repo;

    // test storing songs in the repository
    repo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    repo.store("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    assert(repo.get_size() == 2);

    // test storing duplicate song
    try {
        repo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
        // the above line should throw an exception, so the below assert is not reached
        assert(false);
    }
    catch (const Exceptions& e) {
        // the exception should be caught and the size should be the same
        assert(repo.get_size() == 2);
    }
}

void RepositoryTest::testRemove() const {
    Repo repo;

    // add some songs to the repository
    repo.store("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    repo.store("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    repo.store("Song 3", "Artist 3", "Lyrics 3", "Link 3");

    // test removing a song from the repository
    repo.remove("Song 2", "Artist 2");
    assert(repo.get_size() == 2);

    // test removing a non-existent song
    try {
        repo.remove("Song 4", "Artist 4");
        // The above line should throw an exception, so the below assert is not reached
        assert(false);
    }
    catch (const Exceptions& e) {
        // the exception should be caught and the size should be the same
        assert(repo.get_size() == 2);
    }
}
