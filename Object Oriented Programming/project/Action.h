#include "Repo.h"
#include "Song.h"

class Action {
public:
    virtual void apply(Repo& repo) = 0;
};

class ActionAdd : public Action {
private:
    Song song;

public:
    ActionAdd(const Song& song);

    void apply(Repo& repo) override;
};

class ActionDelete : public Action {
private:
    Song song;

public:
    ActionDelete(const Song& song);

    void apply(Repo& repo) override;
};

