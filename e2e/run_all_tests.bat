@echo off
echo [1/3] Running CREATE tests...
pytest -m create -v -rA --capture=no
IF ERRORLEVEL 1 (
    echo Create tests failed. Aborting...
    exit /b 1
)
echo [2/3] Running SEND tests...
pytest -m send -n auto -v -rA --capture=no
IF ERRORLEVEL 1 (
    echo Send tests failed. Aborting...
    exit /b 1
)

echo [3/3] Running DOWNLOAD tests...
pytest -m download -n auto -v -rA --capture=no
IF ERRORLEVEL 1 (
    echo Download tests failed. Aborting...
    exit /b 1
)

echo All tests passed successfully.
pause