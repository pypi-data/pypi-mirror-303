# **Lify**
- A Python cross-platform project management toolkit.

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
To install `lify`, use the following pip command:
```cmd
pip install lify
```

### **Command Examples**
- Create New Project:
```cmd
:: Creates a project at the specified absolute path.
lify new "{projectfullpath}"

:: Creates a project in the current working directory by making a new directory named `{name}` and generating the project there.
lify new "{name}" # make {name}

:: Creates a project in the current working directory.
lify new
```

- Build Executable Binary Project:
```cmd
lify build "{buildfilepath}" # build output file path in project.
lify new "{name}" # make {name} project in dir makes in current workspace.
lify build # 프로젝트는 현재 작업경로에 생성됩니다.current workspace.
```