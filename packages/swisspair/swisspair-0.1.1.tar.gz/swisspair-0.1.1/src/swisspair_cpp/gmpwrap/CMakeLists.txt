cmake_minimum_required(VERSION 3.29)
project(gmpwrap)

set(CMAKE_CXX_STANDARD 20)

add_library(gmpwrap SHARED gmpwrap.cpp gmpwrap.h)
