cmake_minimum_required(VERSION 3.29)
project(mincostpmatch)

set(CMAKE_CXX_STANDARD 14)

add_library(mincostpmatch SHARED BinaryHeap.cpp
        BinaryHeap.h
        Example.cpp
        Globals.h
        Graph.cpp
        Graph.h
        Matching.cpp
        Matching.h
        types.h library.h)
