#include "Song.h"
#include <cstring>
#include <iostream>
#pragma once
using namespace std;
Song::Song()
{}

Song::Song(string title, string artist, string lyrics,  string link):
	title{ title }, artist{ artist }, lyrics{ lyrics }, link{ link }
{
}


const string& Song::get_title()
{

	return this->title;
}

const string& Song::get_artist()
{
	return this->artist;
}

const string& Song::get_lyrics()
{
	return this->lyrics;
}

const string& Song::get_link()
{
	return this->link;
}



ostream& operator<<(ostream& output, const Song& t)
{
	output << t.title << " " << t.artist << " " << t.lyrics << " " << " " << t.link;
	return output;
}

istream& operator>>(istream& input, Song& t)
{
	input >> t.title >> t.artist >> t.lyrics >> t.link;
	return input;
}
bool Song::operator==(const Song& other) const {
	return title == other.title && artist == other.artist && lyrics == other.lyrics && link == other.link;
}
