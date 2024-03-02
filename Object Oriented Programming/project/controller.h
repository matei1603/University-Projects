#pragma once
#include <cstdlib>
#include "Song.h"
#include "repo.h"
#include "Action.h"
#include <vector>
#include <stack>
#include "Playlist.h"


class Controller {
private:
	Repo& repo;
	std::stack<Action*> undoStack;
	std::stack<Action*> redoStack;
	Playlist playlist;


public:

	Controller(Repo& repo);

	// adds to the service
	void add_s(string title, string artist, string lyrics, string link);
	//removes from the service
	void remove_s(string title, string artist);


	// returns the repository

	vector<Song>& get_repo();


	// gets the size of the service

	int get_size();
	void generateRandomPlaylist(int n);
	void filter_tutorials(vector<Song>& elements, string artist);
	void filter_tutorialss(vector<Song>& elements, string title);
	void undo();
	void redo();
	~Controller();
};