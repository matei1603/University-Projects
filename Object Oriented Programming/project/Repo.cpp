#include "repo.h"
#include "exceptions.h"
#pragma once

Repo::Repo() {
}


void Repo::init_repo()
{
	store("In the club", "50cent", "xsxsxs", "www.a");
	store("Template", "charlie", "xs sxs", "www.b");
	store("Candy shop", "50cent", "xsxsxs ada", "www.c");
	store("Ref", "Andrew", " dsadadsdas  sda", "www.d");
	store("lil bit", "50cent", "dasdas as sadasda", "www.e");
	store("Refer", "Cndrew", "sdas asd saadsa", "www.f");
	store("window shopper", "50cent", "sdas asdsadas a", "www.g");
	store("tho", "Endrew", "das a dsadsad", "www.h");
	store("songs", "50cent", "dsada d adasda", "www.i");
	store("song", "50cent", "dasdsdd adsa dasdsa", "www.o");
}

int Repo::get_size()
{
	return this->objects.size();
}

vector<Song>& Repo::getVector() {
	return this->objects;
}

void Repo::store(string title, string artist, string lyrics, string link)
{
	int pos = find(title, link);
	if (pos == -1) {
		Song temp(title, artist, lyrics, link);
		this->objects.push_back(temp);
	}

	else
		throw RepoExceptions("The song already exists");
}

void Repo::remove(string title, string artist)
{
	int pos = find(title, artist);
	if (pos != -1) {
		this->objects.erase(this->objects.begin() + pos);

	}
	else throw RepoExceptions("The song doesn't exists");
}


int Repo::find(string title, string artist)
{
	for (int i = 0; i < this->objects.size(); i++)
		if (objects[i].get_title() == title && objects[i].get_artist() == artist)
			return i;
	return -1;
}
