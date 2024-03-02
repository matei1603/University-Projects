#pragma once
#include "Song.h"
#include <vector>

class Playlist {
private:
    std::vector<Song> songs;

public:
    void add(const Song& song);
    void clear();
    void remove(const Song& song);
    void generateRandom(int n, const std::vector<Song>& availableSongs);
};


