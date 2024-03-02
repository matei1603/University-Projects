#pragma once
#include <cstdlib>
#include "Song.h"
#include <vector>
class Repo {
protected:
	vector<Song> objects;
public:
	Repo();


	// initialize the repo with the certain entities

	void init_repo();

	//returns the size of the repo
	virtual int get_size();


	// returns the vector

	vector<Song>& getVector();


	// adds to the repo

	virtual void store(string title, string artist, string lyrics, string link);

	// removes from the repo if the entity exists

	virtual void remove(string title, string artist);
	// returns the position of the found enitity 

	virtual int find(string title, string artist);

	//delete update;

	Song& operator [] (int pos) {
		return(this->objects)[pos];
	}


};