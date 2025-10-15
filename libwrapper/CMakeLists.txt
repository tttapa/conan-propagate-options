cmake_minimum_required(VERSION 4.1)
project(libwrapper LANGUAGES CXX)

find_package(libfoo REQUIRED)

add_library(libwrapper "src/wrapper.cpp")
target_sources(libwrapper PUBLIC FILE_SET HEADERS
               BASE_DIRS include FILES include/libwrapper/wrapper.hpp)
target_link_libraries(libwrapper PUBLIC libfoo::libfoo)

install(TARGETS libwrapper EXPORT libwrapperTargets FILE_SET HEADERS)
install(EXPORT libwrapperTargets NAMESPACE libwrapper:: DESTINATION lib/cmake/libwrapper)
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/libwrapperConfig.cmake"
[=[
include(CMakeFindDependencyMacro)
find_dependency(libfoo REQUIRED)
include("${CMAKE_CURRENT_LIST_DIR}/libwrapperTargets.cmake")
]=])
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/libwrapperConfig.cmake" DESTINATION lib/cmake/libwrapper)
