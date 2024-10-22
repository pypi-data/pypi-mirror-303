# **POLESTAR**
- A Python Project Managemnet

## **Specification**

### **Development Environment**
- **Operating System**: Windows
- **Python Version**: Python 3.10.11
- **Editor**: Visual Studio Code (VSCode)

### **Supported Environments**
- **Operating Systems**: Windows, Linux, macOS
- **Python Version**: Python 3.7+
- **Editor**: Any editor (VSCode, PyCharm, etc.)

## **Manual**

### **Installation**
To install `polestar`, use the following pip command:
```cmd
pip install polestar
```


### **Commands**
- Create New Project:
> Creates a `{name}.polestar` file where the project name is the same as the directory name.
```cmd
:: Creates a project at the specified absolute path.
polestar new "{projectfullpath}"

:: Creates a project in the current working directory by making a new directory named `{name}` and generating the project there.
polestar new "{name}"

:: Creates a project in the current working directory.
polestar new
```

- Build Project:
```cmd
:: Builds the executable file for the project.
polestar build exec

:: Builds the project as a library (e.g., a wheel package).
polestar build library
```

- Run Source Code:
```cmd
:: Runs the source code for the project in the current directory.
polestar run
```

- Remove Temporary Project Files:
```cmd
:: Removes temporary files from the project directory.
polestar clean
```

- Update Project:
```cmd
:: Automatically updates the project, handling package management and other necessary tasks.
polestar update
```

- Create Configuration:
```cmd
:: Creates a new configuration.
polestar config create "{name}"
```

- Set Configuration:
```cmd
:: Sets the current configuration.
polestar config set "{name}"
```

- Remove Configuration:
```cmd
:: Removes an existing configuration.
polestar config remove "{name}"
```

- List Configuration:
```cmd
:: Lists all available configurations.
polestar config list
```