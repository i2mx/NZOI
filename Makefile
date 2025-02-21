gcc = C:\tools\msys64\usr\bin\g++
name = NotSudoku

default: build run
build: 
	$(gcc) -O3 -Wall -Wextra -std=c++23 -o $(name) $(name).cpp 
run:
	.\$(name)