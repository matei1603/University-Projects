#include "SongControllerTest.h"
#include "exceptions.h"
void SongControllerTest::testSongController() const {
    Repo repo;
    Controller controller(repo);

    // test get_size() method
    assert(controller.get_size() == 0);

}

void SongControllerTest::testAddSong() const {
    Repo repo;
    Controller controller(repo);

    // test adding a song
    controller.add_s("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    assert(controller.get_size() == 1);

}

void SongControllerTest::testRemoveSong() const {
    Repo repo;
    Controller controller(repo);

    // add some songs to the repository
    controller.add_s("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    controller.add_s("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    controller.add_s("Song 3", "Artist 3", "Lyrics 3", "Link 3");

    // test removing a song
    controller.remove_s("Song 2", "Artist 2");
    assert(controller.get_size() == 2);

}

void SongControllerTest::testGenerateRandomPlaylist() const {
    Repo repo;
    Controller controller(repo);

    // add some songs to the repository
    controller.add_s("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    controller.add_s("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    controller.add_s("Song 3", "Artist 3", "Lyrics 3", "Link 3");

    // test generating a random playlist
    controller.generateRandomPlaylist(2);

}

void SongControllerTest::testFilterTutorials() const {
    Repo repo;
    Controller controller(repo);

    // add some songs to the repository
    controller.add_s("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    controller.add_s("Song 2", "Artist 2", "Lyrics 2", "Link 2");
    controller.add_s("Song 3", "Artist 1", "Lyrics 3", "Link 3");

    // test filtering songs by artist
    std::vector<Song> filteredSongs;
    controller.filter_tutorials(filteredSongs, "Artist 1");

}

void SongControllerTest::testUndo() const {
    Repo repo;
    Controller controller(repo);

    // add some songs to the repository
    controller.add_s("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    controller.add_s("Song 2", "Artist 2", "Lyrics 2", "Link 2");

    // test undoing the last action
    controller.undo();

}

void SongControllerTest::testRedo() const {
    Repo repo;
    Controller controller(repo);

    // add some songs to the repository
    controller.add_s("Song 1", "Artist 1", "Lyrics 1", "Link 1");
    controller.add_s("Song 2", "Artist 2", "Lyrics 2", "Link 2");

    // test redoing the last undone action
    controller.undo();
    controller.redo();

}
