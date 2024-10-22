cmake_minimum_required(VERSION 3.29)
project(gmpwrap)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

find_package(GMP REQUIRED)

add_library(gmpwrap SHARED gmpwrap.cpp gmpwrap.h)
target_link_libraries(gmpwrap PUBLIC ${GMP_LIBRARIES})
target_include_directories(gmpwrap PUBLIC ${GMP_INCLUDES} .)
