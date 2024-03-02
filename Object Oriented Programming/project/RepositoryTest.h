#pragma once

#include <iostream>
#include <cassert>
#include "repo.h"

class RepositoryTest {
public:
    void testRepository() const;
    void testInitRepo() const;
    void testStore() const;
    void testRemove() const;
};
