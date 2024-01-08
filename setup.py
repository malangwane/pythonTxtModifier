from cx_Freeze import setup, Executable

# Specify the main script (replace 'your_main_script.py' with your script's filename)
main_script = 'ao.py'

executables = [Executable(main_script, base=None)]

setup(
    name="YourAppName",
    version="1.0",
    description="Your Application Description",
    executables=executables,
)
