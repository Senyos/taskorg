############################################################
#                                                          #
# A program licensed by The MIT License. 2025 DjBlooky (c) #
#           https://github.com/Senyos/taskorg              #
#                                                          #
############################################################

import sys
import os
from datetime import date, timedelta

from PyQt6 import QtCore, QtGui, QtWidgets

from backend.jsonstore import JSONStore
from backend.taskmanage import TaskManage
from ui.py.main_window import Ui_MainWindow
from ui.py.find_note_window import Ui_FindWindow
from ui.py.delete_note_window import Ui_DeleteWindow
from ui.py.write_note_window import Ui_WriteWindow

# Объявляем QApplication
app = QtWidgets.QApplication(sys.argv)

# Путь относительно запускаемого файла
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Файл хранения JSON
JStore = JSONStore("./tasks.json")
TManage = TaskManage()

try:
    JStore.read_json()
except:
    JStore.write_json([])

# Главное окно
MainWindow = QtWidgets.QMainWindow()
ui_MainWindow = Ui_MainWindow()
ui_MainWindow.setupUi(MainWindow)

# Окно удаления заметок
DeleteWindow = QtWidgets.QMainWindow()
ui_DeleteWindow = Ui_DeleteWindow()
ui_DeleteWindow.setupUi(DeleteWindow)
# DeleteWindow.show()

# Окно написания заметок
WriteWindow = QtWidgets.QMainWindow()
ui_WriteWindow = Ui_WriteWindow()
ui_WriteWindow.setupUi(WriteWindow)
# WriteWindow.show()

# Окно нахождения заметок
FindWindow = QtWidgets.QMainWindow()
ui_FindWindow = Ui_FindWindow()
ui_FindWindow.setupUi(FindWindow)
# FindWindow.show()


def today_button():
    _today = str(date.today())
    ui_MainWindow.t_title.setText(f"Заметки на сегодня, {_today}.")
    ui_MainWindow.t_content.setText("")
    
    # Read json file
    _data = JStore.read_json()

    if _data:

        TManage.set_tasks(_data)

        # Get indexes of the tasks of today's day
        _indexes = TManage.find_tasks_indexes(by="Date", value=_today)

        # Save only tasks by indexes
        TManage.save_tasks(_indexes)

        # Get text pretty if task list isn't empty
        if TManage.get_all_tasks():
            _text = TManage.get_all_tasks_pretty()
            ui_MainWindow.t_content.setText(_text)
        else:
            ui_MainWindow.t_content.setText("На сегодня нет задач.")
    else:
            ui_MainWindow.t_content.setText("На сегодня нет задач.")

def tomorrow_button():
    # print(date.today() + timedelta(days=1)) # завтра
    _tomorow = str(date.today() + timedelta(days=1))
    ui_MainWindow.t_title.setText(f"Заметки на завтра, {_tomorow}.")
    ui_MainWindow.t_content.setText("")
    
    # Read json file
    _data = JStore.read_json()

    if _data:
        TManage.set_tasks(_data)

        # Get indexes of the tasks of tomorrow's day
        _indexes = TManage.find_tasks_indexes(by="Date", value=_tomorow)

        # Save only tasks by indexes
        TManage.save_tasks(_indexes)

        # Get text pretty if task list isn't empty
        if TManage.get_all_tasks():
            _text = TManage.get_all_tasks_pretty()
            ui_MainWindow.t_content.setText(_text)
        else:
            ui_MainWindow.t_content.setText("На завтра нет задач.")
    else:
            ui_MainWindow.t_content.setText("На завтра нет задач.")

def date_button():
    _datefilter = ui_MainWindow.t_datenote.date()
    _date = str(_datefilter.toPyDate())

    ui_MainWindow.t_title.setText(f"Заметки на дату, {_date}.")
    ui_MainWindow.t_content.setText("")
    
    # Read json file
    _data = JStore.read_json()

    if _data:

        TManage.set_tasks(_data)

        # Get indexes of the tasks of today's day
        _indexes = TManage.find_tasks_indexes(by="Date", value=_date)

        # Save only tasks by indexes
        TManage.save_tasks(_indexes)

        # Get text pretty if task list isn't empty
        if TManage.get_all_tasks():
            _text = TManage.get_all_tasks_pretty()
            ui_MainWindow.t_content.setText(_text)
        else:
            ui_MainWindow.t_content.setText("На эту дату нет задач.")
    else:
            ui_MainWindow.t_content.setText("На эту дату нет задач.")

# Write button of MainWindow
def write_note_button():
    ui_WriteWindow.t_date.setDate(date.today())
    # Показывает окно записи заметки
    WriteWindow.show()

# Find button of MainWindow
def find_note_button():

    # Устанавливаем сегодняшнюю дату для виджета даты
    ui_FindWindow.t_datefilter.setDate(date.today())

    _chb_themefilter = ui_FindWindow.chb_themefilter.isChecked()
    _chb_contentfilter = ui_FindWindow.chb_contentfilter.isChecked()
    _chb_datefilter = ui_FindWindow.chb_datefilter.isChecked()

    if _chb_themefilter:
        ui_FindWindow.t_themefilter.setEnabled(True)
    else:
        ui_FindWindow.t_themefilter.setEnabled(False)

    if _chb_contentfilter:
        ui_FindWindow.t_contentfilter.setEnabled(True)
    else:
        ui_FindWindow.t_contentfilter.setEnabled(False)

    if _chb_datefilter:
        ui_FindWindow.t_datefilter.setEnabled(True)
    else:
        ui_FindWindow.t_datefilter.setEnabled(False)

    # Показывает окно поиска заметок
    FindWindow.show()

# Delete button of MainWindow
def delete_note_button():
    # Устанавливаем сегодняшнюю дату для виджета даты
    ui_DeleteWindow.t_datefilter.setDate(date.today())

    _chb_themefilter = ui_DeleteWindow.chb_themefilter.isChecked()
    _chb_contentfilter = ui_DeleteWindow.chb_contentfilter.isChecked()
    _chb_datefilter = ui_DeleteWindow.chb_datefilter.isChecked()

    if _chb_themefilter:
        ui_DeleteWindow.t_themefilter.setEnabled(True)
    else:
        ui_DeleteWindow.t_themefilter.setEnabled(False)

    if _chb_contentfilter:
        ui_DeleteWindow.t_contentfilter.setEnabled(True)
    else:
        ui_DeleteWindow.t_contentfilter.setEnabled(False)

    if _chb_datefilter:
        ui_DeleteWindow.t_datefilter.setEnabled(True)
    else:
        ui_DeleteWindow.t_datefilter.setEnabled(False)

    # Показывает окно удаления заметок
    DeleteWindow.show()


# Note finding of FindWindow
def find_note_filter_button():
    _themefilter = ui_FindWindow.t_themefilter.text()
    _contentfilter = ui_FindWindow.t_contentfilter.text()
    _datefilter = ui_FindWindow.t_datefilter.date()

    _datefilter = str(_datefilter.toPyDate())

    _chb_themefilter = ui_FindWindow.chb_themefilter.isChecked()
    _chb_contentfilter = ui_FindWindow.chb_contentfilter.isChecked()
    _chb_datefilter = ui_FindWindow.chb_datefilter.isChecked()

    _themeprint = ''
    _contentprint = ''
    _dateprint = ''

    _data = JStore.read_json()

    _text = 'Пусто'

    _filtered_by = 'Все заметки:'

    if _data:
        TManage.set_tasks(_data)

        if _chb_themefilter and _themefilter:
            _indexes = TManage.find_tasks_indexes(by='Theme', 
                                                  value=_themefilter)
            TManage.save_tasks(_indexes)
            _themeprint = _themefilter + ' | '
            _filtered_by = 'Фильтр по: '

        if _chb_contentfilter and _contentfilter:
            _indexes = TManage.find_tasks_indexes(by='Note',
                                                  value=_contentfilter)
            TManage.save_tasks(_indexes)
            _contentprint = _contentfilter + ' | '
            _filtered_by = 'Фильтр по: '

        if _chb_datefilter and _datefilter:
            _indexes = TManage.find_tasks_indexes(by='Date',
                                                  value=_datefilter)
            TManage.save_tasks(_indexes)
            _dateprint = _datefilter
            _filtered_by = 'Фильтр по: '

        # if ((not _chb_themefilter and not _chb_contentfilter
        # and not _chb_datefilter) or (not _themefilter and not _contentfilter
        # and not _chb_datefilter)):
        #     TManage.clear_tasks()

        if TManage.get_all_tasks():
            _text = TManage.get_all_tasks_pretty()

            _titletext = _filtered_by + _themeprint + _contentprint + _dateprint
            ui_MainWindow.t_title.setText(_titletext)
            ui_MainWindow.t_content.setText(_text)

            if ((not _chb_themefilter and not _chb_contentfilter
            and not _chb_datefilter) and (not _themefilter and not _contentfilter)):
                ui_MainWindow.t_title.setText(_filtered_by)
                ui_MainWindow.t_content.setText(TManage.get_all_tasks_pretty())
        else:
            ui_MainWindow.t_title.setText("По этому фильтру ничего не найдено.")
            ui_MainWindow.t_content.setText("Пусто.")
        
    else:
        ui_MainWindow.t_title.setText("По этому фильтру ничего не найдено.")
        ui_MainWindow.t_content.setText("Пусто.")

def find_chb_theme_clicked():
    _chb_themefilter = ui_FindWindow.chb_themefilter.isChecked()

    if _chb_themefilter:
        ui_FindWindow.t_themefilter.setEnabled(True)
    else:
        ui_FindWindow.t_themefilter.setEnabled(False)

def find_chb_content_clicked():
    _chb_contentfilter = ui_FindWindow.chb_contentfilter.isChecked()

    if _chb_contentfilter:
        ui_FindWindow.t_contentfilter.setEnabled(True)
    else:
        ui_FindWindow.t_contentfilter.setEnabled(False)

def find_chb_date_clicked():
    _chb_datefilter = ui_FindWindow.chb_datefilter.isChecked()

    if _chb_datefilter:
        ui_FindWindow.t_datefilter.setEnabled(True)
    else:
        ui_FindWindow.t_datefilter.setEnabled(False)

# Note deletion of DeleteWindow
# FIXME: Deleting with typing "OR", not "AND".
def delete_note_filter_button():
    _themefilter = ui_DeleteWindow.t_themefilter.text()
    _contentfilter = ui_DeleteWindow.t_contentfilter.text()
    _datefilter = ui_DeleteWindow.t_datefilter.date()

    _datefilter = str(_datefilter.toPyDate())

    _chb_themefilter = ui_DeleteWindow.chb_themefilter.isChecked()
    _chb_contentfilter = ui_DeleteWindow.chb_contentfilter.isChecked()
    _chb_datefilter = ui_DeleteWindow.chb_datefilter.isChecked()

    _themeprint = ''
    _contentprint = ''
    _dateprint = ''

    _data = JStore.read_json()

    _text = 'Пусто'

    _filtered_by = 'Удалено по фильтру: '

    _indexes_theme = ()
    _indexes_content = ()
    _indexes_date = ()
    _indexes = ()

    if _data:
        TManage.set_tasks(_data)

        if _chb_themefilter and _themefilter:
            _indexes_theme = TManage.find_tasks_indexes(by='Theme', 
                                                  value=_themefilter)
            _themeprint = _themefilter + ' | '

        if _chb_contentfilter and _contentfilter:
            _indexes_content = TManage.find_tasks_indexes(by='Note',
                                                  value=_contentfilter)
            _contentprint = _contentfilter + ' | '

        if _chb_datefilter and _datefilter:
            _indexes_date = TManage.find_tasks_indexes(by='Date',
                                                  value=_datefilter)
            _dateprint = _datefilter

        if ((not _indexes_theme and not _themefilter or not _chb_themefilter) 
            and (_indexes_content and _contentfilter and _chb_contentfilter) 
            and (_indexes_date and _datefilter and _chb_contentfilter)):
            _indexes = list(set(_indexes_content).intersection(_indexes_date))
        elif ((not _indexes_content and not _contentfilter or not _chb_contentfilter) 
               and (_indexes_theme and _themefilter and _chb_themefilter) 
               and (_indexes_date and _datefilter and _chb_contentfilter)):
            _indexes = list(set(_indexes_theme).intersection(_indexes_date))
        elif ((not _indexes_date and not _datefilter or not _chb_datefilter) 
               and (_indexes_content and _contentfilter and _chb_contentfilter) 
               and (_indexes_theme and _themefilter and _chb_themefilter)):
            _indexes = list(set(_indexes_theme).intersection(_indexes_content))

        elif ((_indexes_date and _datefilter or _chb_datefilter) 
               and (_indexes_content and _contentfilter and _chb_contentfilter) 
               and (_indexes_theme and _themefilter and _chb_themefilter)):
            _indexes = set(_indexes_theme).intersection(
                    set(_indexes_content).intersection(_indexes_date))
            _indexes = list(_indexes)
        elif ((_indexes_theme and _themefilter and _chb_themefilter)
                ):
            _indexes = _indexes_theme
        elif ((_indexes_content and _contentfilter and _chb_contentfilter)
                ):
            _indexes = _indexes_content
        elif ((_indexes_date and _datefilter or _chb_datefilter)
                ):
            _indexes = _indexes_date
        else:
            _indexes = []

        print(_indexes, _indexes_theme, _indexes_content, _indexes_date)

        TManage.delete_tasks(_indexes)

        if TManage.get_all_tasks():
            _text = 'Удалены некоторые данные'

        _titletext = _filtered_by + _themeprint + _contentprint + _dateprint
        ui_MainWindow.t_title.setText(_titletext)
        ui_MainWindow.t_content.setText(_text)

        JStore.write_json(TManage.get_all_tasks())
        
    else:
        ui_MainWindow.t_title.setText("По этому фильтру ничего не найдено.")
        ui_MainWindow.t_content.setText("Пусто.")

def delete_chb_theme_clicked():
    _chb_themefilter = ui_DeleteWindow.chb_themefilter.isChecked()

    if _chb_themefilter:
        ui_DeleteWindow.t_themefilter.setEnabled(True)
    else:
        ui_DeleteWindow.t_themefilter.setEnabled(False)

def delete_chb_content_clicked():
    _chb_contentfilter = ui_DeleteWindow.chb_contentfilter.isChecked()

    if _chb_contentfilter:
        ui_DeleteWindow.t_contentfilter.setEnabled(True)
    else:
        ui_DeleteWindow.t_contentfilter.setEnabled(False)

def delete_chb_date_clicked():
    _chb_datefilter = ui_DeleteWindow.chb_datefilter.isChecked()

    if _chb_datefilter:
        ui_DeleteWindow.t_datefilter.setEnabled(True)
    else:
        ui_DeleteWindow.t_datefilter.setEnabled(False)

def delete_all_button():
    JStore.write_json([])


# Note creation of WriteWindow
def create_note_button():
    _theme = ui_WriteWindow.t_theme.text()
    _note = ui_WriteWindow.t_note.text()
    _date = ui_WriteWindow.t_date.date()

    _date = str(_date.toPyDate())

    _data = JStore.read_json()

    if _data:
        TManage.set_tasks(_data)
    
    else:
        TManage.clear_tasks()
    
    TManage.create_task(_theme, _note, _date)
    JStore.write_json(TManage.get_all_tasks())

    ui_MainWindow.t_title.setText("Заметка успешно добавлена:")
    ui_MainWindow.t_content.setText(f'Тема: {_theme}\nЗаметка: {_note}\nДата: {_date}\n\n')

    TManage.clear_tasks()
