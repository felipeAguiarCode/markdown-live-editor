@echo off
cd /d "%~dp0"

where python >nul 2>&1
if not errorlevel 1 (
  python "%~dp0servidor.py"
  if errorlevel 1 pause
  exit /b 0
)

where npx >nul 2>&1
if errorlevel 1 (
  echo Nao encontrei python nem node nesta maquina.
  echo Instale um dos dois, ou sirva esta pasta com qualquer servidor HTTP.
  pause
  exit /b 1
)
echo.
echo   markdown-live-editor  -^>  http://localhost:8123/index.html
echo   Deixe esta janela aberta. Fechar a janela para o servidor.
echo.
start "" /b powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Seconds 3; Start-Process 'http://localhost:8123/index.html'"
npx --yes serve -l 8123 .
