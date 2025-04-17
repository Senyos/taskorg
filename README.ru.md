## Languages of README

- [English](https://github.com/Senyos/taskorg/blob/master/README.md)
- [Russian](https://github.com/Senyos/taskorg/blob/master/README.ru.md)

# taskorg

## Коротко о программе

**taskorg** это программа для записи домашнего задания или других событий, назначенных на какую-либо дату, с возможностью записывать события или задания, изменять их, удалять и получать.

**taskorg** разбивается на несколько программ: бэкэнд для работы с различным клиентам (приложениям) и официальное приложение с интерфейсом.

Также планируется терминальная (консольная) версия программы.

## Как собрать программу (build)

Build-ы программы доступны в репозитории на [github `taskorg`](https://github.com/Senyos/taskorg).

Чтобы собрать программу вручную, в директории виртуального окружения `env` загружен `python 3.13.2`, а также установлены библиотеки для работы с `Qt6`, `PyQt6`, `PysideQt6`. Для компиляции установлена библиотека `nuitka`. [Руководство `nuitka`](https://nuitka.net/) содержит более подробное расписание всех инструкций ниже.

Чтобы создать build программы, вам нужно:

1. Проверить зависимости.
2. Загрузиться в виртуальном окружении.
3. Скомпилировать файл `app/taskorg.py`.

### Зависимости

#### Linux

Вы должны установить C компилятор `gcc` или `clang` своим пакетным менеджером, если у вас его нет. А также вы должны установить `python3-devel`, `python` для разработчиков.

#### Windows

У вас должен быть установлен C компилятор `MingW64` или `Visual Studio`. А также `python` для разработчиков.

### Виртуальное окружение и компиляция

Для подробностей о виртуальных окружениях смотреть [`python` документацию](https://docs.python.org/3/library/venv.html).

Вы должны открыть терминал (консоль), перейти в директорию с программой `taskorg` с помощью команд `cd /path/to/file`, где `cd` -- "change directory" (или открыть терминал сразу в папке с `taskorg`). Затем вы вводите команды, описанные далее.

Предполагаемо вы сейчас находитесь в главной директории `taskorg/`, тогда:

#### Linux

Загружаемся в виртуальном окружении:

```sh
source env/bin/activate
```

Запускаем компиляцию в один файл:

```sh
python -m nuitka app/taskorg.py --onefile --enable-plugin=pyqt6
```

После этих манипуляций в директории `taskorg` появятся 3 новые директории и файл `taskorg.bin`.

#### Windows

Загружаемся в виртуальном окружении:

cmd

```sh
\env\bin\activate.bat
```

PowerShell

```sh
PS \env\bin\activate.ps1
```

Запускаем компиляцию в один файл:

```sh
python -m nuitka .\app\taskorg.py --onefile --enable-plugin=pyqt6 --assume-yes-for-downloads --windows-console-mode=disable
```

После этих манипуляций в директории `taskorg` появятся 3 новые директории и файл `taskorg.exe`.


### Возникли проблемы при сборе build-а?

Если возникли проблемы, то обращайтесь к руководствам [`python venv`](https://docs.python.org/3/library/venv.html) и [`nuitka`](https://nuitka.net/), а также [`Qt` for `python`](https://doc.qt.io/qtforpython-6/).

Если ваша проблема не решена, создайте `issue` в [github `taskorg` создать новый `issue`](https://github.com/Senyos/taskorg/issues/new)