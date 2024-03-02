#pragma once

#include <iostream>
#include <cassert>
#include "FileRepo.h"

class FileRepositoryTest {
public:
    void testFileRepository() const;
    void testReadData() const;
    void testWriteData() const;
    void testStore() const;
    void testRemove() const;
};
