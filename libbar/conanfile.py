import os
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class LibBarConan(ConanFile):
    name = "libbar"
    version = "1.0.0"
    package_type = "library"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "*.hpp", "*.cpp", "CMakeLists.txt"
    generators = "CMakeDeps", "CMakeToolchain"
    build_requires = "cmake/[>=3.28 <5]"

    def requirements(self):
        self.requires("libfoo/1.0.0", transitive_headers=True)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("lib", "cmake", "libbar"))
