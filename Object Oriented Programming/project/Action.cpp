#include "Action.h"
#include "Repo.h"

ActionAdd::ActionAdd(const Song& song) : song(song) {}

void ActionAdd::apply(Repo& repo) {
    repo.store(song.get_title(), song.get_artist(), song.get_lyrics(), song.get_link());
}

ActionDelete::ActionDelete(const Song& song) : song(song) {}

void ActionDelete::apply(Repo& repo) {
    repo.remove(song.get_title(), song.get_artist());
}
