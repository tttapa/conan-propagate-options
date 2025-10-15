cmake_minimum_required(VERSION 3.28...4.1)
project(libfoo LANGUAGES CXX)

option(FOO_WITH_SINGLE_PRECISION "Use single precision instead of double" OFF)

add_library(libfoo foo.cpp)
target_sources(libfoo PUBLIC FILE_SET HEADERS BASE_DIRS . FILES foo.hpp)
target_compile_definitions(libfoo PUBLIC
    FOO_REAL_TYPE=$<IF:$<BOOL:${FOO_WITH_SINGLE_PRECISION}>,float,double>)

install(TARGETS libfoo EXPORT libfooTargets FILE_SET HEADERS)
install(EXPORT libfooTargets NAMESPACE libfoo:: DESTINATION lib/cmake/libfoo)
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/libfooConfig.cmake"
[=[
include("${CMAKE_CURRENT_LIST_DIR}/libfooTargets.cmake")
]=])
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/libfooConfig.cmake" DESTINATION lib/cmake/libfoo)
