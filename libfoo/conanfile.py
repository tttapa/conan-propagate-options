import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout


class LibFooConan(ConanFile):
    name = "libfoo"
    version = "1.0.0"
    package_type = "library"
    options = {"shared": [True, False], "fPIC": [True, False], "with_v2": [True, False]}
    default_options = {"shared": False, "fPIC": True, "with_v2": False}
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "src/*", "include/*", "CMakeLists.txt"
    generators = ("CMakeDeps",)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["FOO_WITH_V2"] = self.options.with_v2
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
