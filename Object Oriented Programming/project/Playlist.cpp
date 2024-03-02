#include "Playlist.h"
#include <algorithm>
#include <random>
#include <ctime>

void Playlist::add(const Song& song) {
    songs.push_back(song);
}

void Playlist::clear() {
    songs.clear();
}

void Playlist::remove(const Song& song) {
    songs.erase(std::remove(songs.begin(), songs.end(), song), songs.end());
}

void Playlist::generateRandom(int n, const std::vector<Song>& availableSongs) {
    if (n <= 0 || availableSongs.empty()) {
        return;
    }
    // random number generator
    std::mt19937 rng(static_cast<unsigned int>(std::time(nullptr))); 
    std::vector<Song> shuffledSongs = availableSongs;
    std::shuffle(shuffledSongs.begin(), shuffledSongs.end(), rng);

    songs.clear();
    for (int i = 0; i < n && i < shuffledSongs.size(); ++i) {
        songs.push_back(shuffledSongs[i]);
    }
}
