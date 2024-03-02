#pragma once
#include <fstream>
#include "repo.h"

class FileRepo : public Repo {
private:
	string file_name;
	Song get_entity(int pos);
public:
	void write_data(vector<Song> data);
	vector<Song> read_data();
	FileRepo(string file);
	void store(string title, string artist, string lyrics, string link) override;
	void remove(string title, string artist) override;
	int find(string title, string artist) override;
	int get_size() override;

};