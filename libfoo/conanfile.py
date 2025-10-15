import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout


class LibFooConan(ConanFile):
    name = "libfoo"
    version = "1.0.0"
    package_type = "library"
    options = {"shared": [True, False], "fPIC": [True, False], "single_precision": [True, False]}
    default_options = {"shared": False, "fPIC": True, "single_precision": False}
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "*.hpp", "*.cpp", "CMakeLists.txt"
    generators = ("CMakeDeps",)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["FOO_WITH_SINGLE_PRECISION"] = self.options.single_precision
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("lib", "cmake", "libfoo"))
