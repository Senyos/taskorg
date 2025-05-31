############################################################
#                                                          #
# A program licensed by The MIT License. 2025 DjBlooky (c) #
#           https://github.com/Senyos/taskorg              #
#                                                          #
############################################################


from button_functions import *

if __name__ == "__main__":
    
    # Главное окно
    MainWindow.show()

    # MainWindow buttons connect
    ui_MainWindow.b_todaynote.clicked.connect(today_button)
    ui_MainWindow.b_tommorownote.clicked.connect(tomorrow_button)
    ui_MainWindow.b_writenote.clicked.connect(write_note_button)
    ui_MainWindow.b_findnote.clicked.connect(find_note_button)
    ui_MainWindow.b_deletenote.clicked.connect(delete_note_button)
    ui_MainWindow.b_datenote.clicked.connect(date_button)
    ui_MainWindow.t_datenote.setDate(date.today())

    # FindWindow buttons connect
    ui_FindWindow.b_findnote.clicked.connect(find_note_filter_button)
    ui_FindWindow.chb_themefilter.clicked.connect(find_chb_theme_clicked)
    ui_FindWindow.chb_contentfilter.clicked.connect(find_chb_content_clicked)
    ui_FindWindow.chb_datefilter.clicked.connect(find_chb_date_clicked)

    # WriteWindow buttons connect
    ui_WriteWindow.b_createnote.clicked.connect(create_note_button)

    # DeleteWindow buttons connect
    ui_DeleteWindow.b_deletenote.clicked.connect(delete_note_filter_button)
    ui_DeleteWindow.chb_themefilter.clicked.connect(delete_chb_theme_clicked)
    ui_DeleteWindow.chb_contentfilter.clicked.connect(delete_chb_content_clicked)
    ui_DeleteWindow.chb_datefilter.clicked.connect(delete_chb_date_clicked)
    ui_DeleteWindow.b_deleteall.clicked.connect(delete_all_button)


    sys.exit(app.exec())