#include "controller.h"
#include <vector>
#include <algorithm>
#include "Song.h"


Controller::Controller(Repo& repo) :
	repo{ repo } {}

void Controller::add_s(string title, string artist, string lyrics, string link)
{
	this->repo.store(title, artist, lyrics, link);
}

void Controller::remove_s(string title, string artist)
{
	this->repo.remove(title, artist);

}
void Controller::generateRandomPlaylist(int n) {
    playlist.generateRandom(n, repo.getVector());
}

vector<Song>&Controller::get_repo() { 
	return this->repo.getVector(); }



int Controller::get_size()
{
	return this->repo.get_size();
}


void Controller::filter_tutorials(vector<Song>& elements, string artist)
{
	auto it = copy_if(this->get_repo().begin(), this->get_repo().end(), elements.begin(),
		[artist](Song song) {
			if (artist == "")
				return true;
			return song.get_artist() == artist; });
	elements.resize(it - elements.begin());

}
void Controller::filter_tutorialss(vector<Song>& elements, string title)
{
	auto it = copy_if(this->get_repo().begin(), this->get_repo().end(), elements.begin(),
		[title](Song song) {
			if (title == "")
				return true;
			return song.get_title() == title; });
	elements.resize(it - elements.begin());

}

void Controller::undo() {
    if (!undoStack.empty()) {
        Action* action = undoStack.top();
        undoStack.pop();
        action->apply(repo);
        redoStack.push(action);
    }
}

void Controller::redo() {
    if (!redoStack.empty()) {
        Action* action = redoStack.top();
        redoStack.pop();
        action->apply(repo);
        undoStack.push(action);
    }
}

Controller::~Controller() {
    while (!undoStack.empty()) {
        delete undoStack.top();
        undoStack.pop();
    }

    while (!redoStack.empty()) {
        delete redoStack.top();
        redoStack.pop();
    }
}

