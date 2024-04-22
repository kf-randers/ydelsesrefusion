:: To run 
:: 
:: NB: If your python alias is 'py' instead of 'python', then run "DOSKEY python=py $1" before running the script

@echo off

set "command=python --version"
set "output="

for /f "tokens=* USEBACKQ" %%F in (`%command% 2^>^&1`) do (set "output=%%F")

echo "%output%" | findstr /C:"Python was not found" 1>nul

if errorlevel 1 ( 
    setlocal enabledelayedexpansion

    for /f "tokens=1,2" %%a in ('python -c "import sys; print(sys.version_info[0], sys.version_info[1])"') do (
        set "major=%%a"
        set "minor=%%b"
    )

    if %major% GEQ 3 (
        if %minor% GEQ 10 (
            set install_python=false
        ) else (
            set install_python=true
        )
    ) else (
        set install_python=true
    )

    endlocal
    
    if %install_python% == true (
        echo. ERROR: install python min version 3.10 and run script again
        GOTO :EOF
    ) else (
        GOTO :create_venv
    )

    

) else ( 
    echo. ERROR: install python min version 3.10 and run script again - check comment in file for alias issue
    GOTO :EOF
)

setlocal enabledelayedexpansion

:check_virtualenv
    python -c "import virtualenv" 2>nul
    if errorlevel 1 (
        echo. virtualenv is not installed. Installing...
        python -m pip install --user virtualenv
        echo. virtualenv installation complete.
    )

:create_venv
    set "env_name=%~1"
    if not "%env_name%" == "" (
        if exist "%env_name%" (
            echo. Virtual environment '%env_name%' already exists. Aborting.
            exit /b 1
        )
    ) else (
        set "env_name=.venv"
    )

    python -m venv "%env_name%"
    call "%env_name%\Scripts\activate"
    python -m pip install -U pip

endlocal

:activate_venv
    set "env_name=%~1"
    if not "%env_name%" == "" (
        if not exist "%env_name%" (
            echo. Virtual environment '%env_name%' not found. Use '%~nx0 create [env_name]' to create one.
            exit /b 1
        )
    ) else (
        set "env_name=.venv"
    )

    call "%env_name%\Scripts\activate"

:install_deps
    set "env_name=%~1"
    if not "%env_name%" == "" (
        if not exist "%env_name%" (
            echo Virtual environment '%env_name%' not found. Use '%~nx0 create [env_name]' to create one.
            exit /b 1
        )
    ) else (
        set "env_name=.venv"
    )

    call "%env_name%\Scripts\activate"

    if exist "app\requirements.txt" (
        python -m pip install -Ir app\requirements-dev.txt
    )

    if exist "requirements-dev.txt" (
        python -m pip install -Ir requirements-dev.txt
    )

:end