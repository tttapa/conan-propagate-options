cmake_minimum_required(VERSION 3.28...4.1)
project(libfoo LANGUAGES CXX)
include(GenerateExportHeader)

add_library(libfoo foo.cpp)
generate_export_header(libfoo BASE_NAME foo)
target_sources(libfoo PUBLIC FILE_SET HEADERS
    BASE_DIRS include ${CMAKE_CURRENT_BINARY_DIR}
    FILES include/foo.hpp ${CMAKE_CURRENT_BINARY_DIR}/foo_export.h)

install(TARGETS libfoo EXPORT libfooTargets FILE_SET HEADERS)
install(EXPORT libfooTargets NAMESPACE libfoo:: DESTINATION lib/cmake/libfoo)
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/libfooConfig.cmake"
[=[
include("${CMAKE_CURRENT_LIST_DIR}/libfooTargets.cmake")
]=])
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/libfooConfig.cmake" DESTINATION lib/cmake/libfoo)
