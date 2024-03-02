#include "exceptions.h"
#include "FileRepo.h"

vector<Song> FileRepo::read_data()
{
	ifstream in(this->file_name);
	vector<Song> objects;
	Song current;
	while (in >> current) {
		objects.push_back(current);
	}
	return objects;
}

void FileRepo::write_data(vector<Song> data)
{
	ofstream out(this->file_name);
	for (auto d : data)
		out << d << '\n';
}

Song FileRepo::get_entity(int pos)
{
	vector<Song>obj = read_data();

	return obj[pos];
}

FileRepo::FileRepo(string file)
{
	this->file_name = file;
	this->objects = read_data();
}

void FileRepo::store(string title, string artist, string lyrics, string link)
{
	int pos = find(title, artist);
	if (pos == -1) {
		Song temp(title, artist, lyrics, link);
		objects.push_back(temp);
		write_data(objects);
	}

	else
		throw RepoExceptions("The tutorial already exist in file repo");
}

void FileRepo::remove(string title, string artist)
{
	int pos = find(title, artist);
	if (pos != -1) {
		objects.erase(this->objects.begin() + pos);

	}
	else throw RepoExceptions("The tutorial doesn't exist in file repo");
}


int FileRepo::find(string title, string artist)
{
	for (int i = 0; i < objects.size(); i++)
		if (objects[i].get_title() == title && objects[i].get_artist() == artist)
			return i;

	return -1;
}

int FileRepo::get_size()
{
	return objects.size();
}

