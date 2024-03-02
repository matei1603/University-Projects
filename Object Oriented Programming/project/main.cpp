#include <QApplication>
#include "mainwindow.h"
#include <iostream>
#include "RepositoryTest.h"
#include "FileRepositoryTest.h"
#include "SongControllerTest.h"

int main(int argc, char* argv[]) {
    QApplication a(argc, argv);
    MainWindow w;
   
    RepositoryTest repoTest;
    repoTest.testRepository();

    FileRepositoryTest fileRepoTest;
    fileRepoTest.testFileRepository();

    SongControllerTest songControllerTest;
    songControllerTest.testSongController();
    w.show();
    std::cout << "All tests passed successfully!\n";
    return a.exec();
}
