cmake_minimum_required(VERSION 4.1)
project(libfoo LANGUAGES CXX)

option(FOO_WITH_V2 "Enable foo_v2" OFF)

add_library(libfoo "src/foo.cpp")
target_sources(libfoo PUBLIC FILE_SET HEADERS
               BASE_DIRS include FILES include/libfoo/foo.hpp)
target_compile_definitions(libfoo PUBLIC $<$<BOOL:${FOO_WITH_V2}>:FOO_WITH_V2>)

install(TARGETS libfoo EXPORT libfooTargets FILE_SET HEADERS)
install(EXPORT libfooTargets NAMESPACE libfoo:: DESTINATION lib/cmake/libfoo)
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/libfooConfig.cmake"
[=[
include("${CMAKE_CURRENT_LIST_DIR}/libfooTargets.cmake")
]=])
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/libfooConfig.cmake" DESTINATION lib/cmake/libfoo)
