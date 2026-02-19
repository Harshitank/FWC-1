This directory is intended for project specific (private) libraries. 
PlatformIO will compile them to static libraries and link into the executable file.

The source code of each library should be placed in a separate directory:

lib/your_library_name/[Code]

For example, see the structure of the following example libraries Foo and Bar:

|-- lib
|   |-- Bar
|   |   |-- docs
|   |   |-- examples
|   |   |-- src
|   |   |   |- Bar.c
|   |   |   |- Bar.h
|   |   |   |- library.json (optional)
|   |
|   |-- Foo
|   |   |- Foo.c
|   |   |- Foo.h
|
|-- platformio.ini
|-- src
|   |- main.c


Example contents of src/main.c using Foo and Bar:

#include <Foo.h>
#include <Bar.h>

int main (void)
{
  ...
}

The PlatformIO Library Dependency Finder will automatically detect
dependent libraries by scanning project source files.

More information:

https://docs.platformio.org/page/librarymanager/config.html
https://docs.platformio.org/page/librarymanager/ldf.html
