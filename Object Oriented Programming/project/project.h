#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_project.h"

class project : public QMainWindow
{
    Q_OBJECT

public:
    project(QWidget *parent = nullptr);
    ~project();

private:
    Ui::projectClass ui;
};
