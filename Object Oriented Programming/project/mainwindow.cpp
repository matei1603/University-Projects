#pragma once
#include "mainwindow.h"
#include "controller.h"


MainWindow::MainWindow(QWidget* parent) : QWidget(parent) {
    QHBoxLayout* ly = new QHBoxLayout{};
    this->listWidget = new QListWidget{};
    QListWidget* listWidget1 = new QListWidget{};
    setLayout(ly);

    // Left column: All song list
    QVBoxLayout* leftLayout = new QVBoxLayout{};
    leftLayout->addWidget(new QLabel{ "All Songs:" });
    leftLayout->addWidget(listWidget);
    leftLayout->addSpacing(10);
    ly->addLayout(leftLayout);
    ly->addSpacing(10);

    QFormLayout* formLayout = new QFormLayout();
QLineEdit* titleLineEdit = new QLineEdit;
titleLineEdit->setObjectName("titleLineEdit");

QLineEdit* artistLineEdit = new QLineEdit;
artistLineEdit->setObjectName("artistLineEdit");

QLineEdit* linkLineEdit = new QLineEdit;
linkLineEdit->setObjectName("linkLineEdit");
    formLayout->addRow(new QLabel{ "Title:" }, titleLineEdit);
    formLayout->addRow(new QLabel{ "Artist:" }, artistLineEdit);
    formLayout->addRow(new QLabel{ "Link:" }, linkLineEdit);
    formLayout->setObjectName("formLayout");

    leftLayout->addLayout(formLayout);
    leftLayout->addSpacing(10);

    QHBoxLayout* buttonsLayout = new QHBoxLayout{};
    QPushButton* addButton = new QPushButton{ "Add" };
    connect(addButton, SIGNAL(clicked()), this, SLOT(addButtonClicked()));
    buttonsLayout->addWidget(addButton);
    QPushButton* removeButton = new QPushButton{ "Remove" };
    buttonsLayout->addWidget(removeButton);
    connect(removeButton, SIGNAL(clicked()), this, SLOT(removeButtonClicked()));
    buttonsLayout->addWidget(new QPushButton{ "View Lyrics" });

    leftLayout->addLayout(buttonsLayout);

    leftLayout->addWidget(new QPushButton{ "Sort by title" });
    leftLayout->addWidget(new QPushButton{ "Sort by artist" });


    // Middle column: > button
    QVBoxLayout* middleLayout = new QVBoxLayout{};
    QPushButton* addplaylistButton = new QPushButton{ "Remove" };
    middleLayout->addWidget(new QPushButton{ "Add to playlist" });
    ly->addLayout(middleLayout);
    ly->addSpacing(10);

    // Right column: Playlist list
    QVBoxLayout* rightLayout = new QVBoxLayout{};
    rightLayout->addWidget(new QLabel{ "Playlist:" });
    rightLayout->addWidget(listWidget1);
    rightLayout->addSpacing(10);
    ly->addLayout(rightLayout);

    QHBoxLayout* buttonsLayout1 = new QHBoxLayout{};
    buttonsLayout1->addWidget(new QPushButton{ "Create Random Playlist" });
    buttonsLayout1->addWidget(new QPushButton{ "Remove from Playlist" });
    rightLayout->addLayout(buttonsLayout1);
    rightLayout->addSpacing(20);

    // Create the controller with the repository
    Repo* repo = new Repo();
    repo->init_repo();
    controller = new Controller(*repo);

    this->populate_list();
}

void MainWindow::populate_list()
{
    this->listWidget->clear();
    vector<Song>elements = controller->get_repo();
    for (auto& element : elements)
        this->listWidget->addItem(QString::fromStdString(element.get_title() + " " + element.get_artist() + " " + element.get_link()));


}

void MainWindow::addButtonClicked() {
    // Retrieve the line edits using their object names
    QLineEdit* titleLineEdit = findChild<QLineEdit*>("titleLineEdit");
    QLineEdit* artistLineEdit = findChild<QLineEdit*>("artistLineEdit");
    QLineEdit* linkLineEdit = findChild<QLineEdit*>("linkLineEdit");

    // Check if any of the line edits are null
    if (!titleLineEdit || !artistLineEdit || !linkLineEdit) {
        // Handle the error appropriately (e.g., show an error message)
        return;
    }

    // Get the text from the line edits
    QString title = titleLineEdit->text();
    QString artist = artistLineEdit->text();
    QString link = linkLineEdit->text();

    // Clear the line edits
    titleLineEdit->clear();
    artistLineEdit->clear();
    linkLineEdit->clear();

    // Create a new song and add it to the repository
    controller->add_s(title.toStdString(), artist.toStdString(), "", link.toStdString());
    this->populate_list();
}
void MainWindow::removeButtonClicked() {
    // Retrieve the line edits using their object names
    QLineEdit* titleLineEdit = findChild<QLineEdit*>("titleLineEdit");
    QLineEdit* artistLineEdit = findChild<QLineEdit*>("artistLineEdit");
    QLineEdit* linkLineEdit = findChild<QLineEdit*>("linkLineEdit");

    // Check if any of the line edits are null
    if (!titleLineEdit || !artistLineEdit || !linkLineEdit) {
        // Handle the error appropriately (e.g., show an error message)
        return;
    }

    // Get the text from the line edits
    QString title = titleLineEdit->text();
    QString artist = artistLineEdit->text();
    QString link = linkLineEdit->text();

    // Clear the line edits
    titleLineEdit->clear();
    artistLineEdit->clear();
    linkLineEdit->clear();

    // Create a new song and add it to the repository
    controller->remove_s(title.toStdString(), artist.toStdString());
    this->populate_list();
}









