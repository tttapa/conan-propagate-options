cmake_minimum_required(VERSION 3.28...4.1)
project(libbar LANGUAGES CXX)

find_package(libfoo REQUIRED)

add_library(libbar bar.cpp)
target_sources(libbar PUBLIC FILE_SET HEADERS BASE_DIRS . FILES bar.hpp)
target_link_libraries(libbar PUBLIC libfoo::libfoo)

install(TARGETS libbar EXPORT libbarTargets FILE_SET HEADERS)
install(EXPORT libbarTargets NAMESPACE libbar:: DESTINATION lib/cmake/libbar)
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/libbarConfig.cmake"
[=[
include(CMakeFindDependencyMacro)
find_dependency(libfoo REQUIRED)
include("${CMAKE_CURRENT_LIST_DIR}/libbarTargets.cmake")
]=])
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/libbarConfig.cmake" DESTINATION lib/cmake/libbar)
