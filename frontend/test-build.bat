@echo off
echo Simulando build do Render.com localmente

echo Limpando instalacao anterior...
rd /s /q node_modules 2>nul
del package-lock.json 2>nul

echo Instalando dependencias...
call npm install --legacy-peer-deps

echo Fazendo build...
call npm run build

echo Build completo! Verifique a pasta 'build' para os resultados.
pause