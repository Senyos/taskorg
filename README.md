## Languages ​​of README

- [English](https://github.com/Senyos/taskorg/blob/master/README.md)
- [Russian](https://github.com/Senyos/taskorg/blob/master/README.ru.md)

# taskorg

## Briefly about the program

**taskorg** is a program for recording homework or other events scheduled for a certain date, with the ability to record events or tasks, change them, delete and receive them.

**taskorg** is divided into several programs: a backend for working with various clients (applications) and an official application with an interface.

A terminal (console) version of the program is also planned.

## How to build the program

The program builds are available in the repository on [github `taskorg`](https://github.com/Senyos/taskorg).

To build the program manually, `python 3.13.2` is loaded in the virtual environment directory `env`, and libraries for working with `Qt6`, `PyQt6`, `PysideQt6` are installed. The `nuitka` library is installed for compilation. [The `nuitka` manual](https://nuitka.net/) contains a more detailed schedule of all the instructions below.

To create a build of the program, you need to:

1. Check dependencies.
2. Boot into the virtual environment.
3. Compile the file `app/taskorg.py`.

### Dependencies

#### Linux

You must install the C compiler `gcc` or `clang` with your package manager if you do not have it. And you must also install `python3-devel`, `python` for developers.

#### Windows

You must have the `MingW64` or `Visual Studio` C compiler installed. And `python` for developers.

### Virtual environment and compilation

For details on virtual environments, see the [`python` documentation](https://docs.python.org/3/library/venv.html).

You must open a terminal (console), change to the directory with the `taskorg` program using the commands `cd /path/to/file`, where `cd` is "change directory" (or open a terminal directly in the folder with `taskorg`). Then you enter the commands described below.

Assuming you are now in the main directory `taskorg/`, then:

#### Linux

Boot into a virtual environment:

```sh
source env/bin/activate
```

Run compilation into one file:

```sh
python -m nuitka app/taskorg.py --onefile --enable-plugin=pyqt6
```

After these manipulations, 3 new directories and a file `taskorg.bin` will appear in the `taskorg` directory.

#### Windows

Boot into a virtual environment:

cmd

```sh
\env\bin\activate.bat
```

PowerShell

```sh
PS \env\bin\activate.ps1
```

Run compilation into one file:

```sh
python -m nuitka .\app\taskorg.py --onefile --enable-plugin=pyqt6 --assume-yes-for-downloads --windows-console-mode=disable
```

After these manipulations, 3 new directories and a file `taskorg.exe` will appear in the `taskorg` directory.

### Are there any problems with the build?

If you have any problems, please refer to the [`python venv`](https://docs.python.org/3/library/venv.html) and [`nuitka`](https://nuitka.net/) manuals, as well as [`Qt` for `python`](https://doc.qt.io/qtforpython-6/).

If your problem is not solved, create an `issue` in [github `taskorg` create new `issue`](https://github.com/Senyos/taskorg/issues/new)