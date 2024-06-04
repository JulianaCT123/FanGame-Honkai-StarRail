# pip intall cx_Freeze
import cx_Freeze
executaveis = [cx_Freeze.Executable(script="main.py", icon = "assets/icon.ico")]

cx_Freeze.setup(
    name ="IronMan",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    },executables = executaveis
)

# python setup.py build
# python setup.py build_msi