cmake_minimum_required(VERSION 3.28...4.1)
project(myapp LANGUAGES CXX)

find_package(libwrapper REQUIRED)

add_executable(myapp "src/main.cpp")
target_link_libraries(myapp PRIVATE libwrapper::libwrapper)
