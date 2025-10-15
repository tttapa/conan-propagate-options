cmake_minimum_required(VERSION 3.28...4.1)
project(myapp LANGUAGES CXX)

find_package(libbar REQUIRED)

add_executable(myapp main.cpp)
target_link_libraries(myapp PRIVATE libbar::libbar)
