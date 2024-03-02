#pragma once
#include <string>
using namespace std;
class Song {
private:
	string title;
	string artist;
	string lyrics;
	string link;

public:
	Song();

	// constructor

	Song(string title, string artist, string lyrics, string link);

	// getter for title

	const string& get_title();

	// getter for artist

	const string& get_artist();

	// getter for duration

	const string& get_lyrics();

	// getter for link

	const string& get_link();


	friend	ostream& operator<<(ostream&, const Song&);
	friend istream& operator>>(istream&, Song&);
	bool operator==(const Song& other) const;
};