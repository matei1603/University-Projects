#include <QWidget>
#include "controller.h"
#include "Playlist.h"
#include "qlistwidget.h"
#include <QWidget>
#include <QHBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include <QFormLayout>
class MainWindow : public QWidget {
    Q_OBJECT
public:
    MainWindow(QWidget* parent = nullptr);
    void populate_list();
private slots:
    void addButtonClicked();
    void removeButtonClicked();
   
private:
    Controller* controller;
    QListWidget* listWidget;


};
