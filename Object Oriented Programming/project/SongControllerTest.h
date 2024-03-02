#pragma once

#include <iostream>
#include <cassert>
#include "controller.h"

class SongControllerTest {
public:
    void testSongController() const;
    void testAddSong() const;
    void testRemoveSong() const;
    void testGenerateRandomPlaylist() const;
    void testFilterTutorials() const;
    void testUndo() const;
    void testRedo() const;
};

