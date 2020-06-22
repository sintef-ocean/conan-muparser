import os
from conans import ConanFile, tools, CMake


class MuparserConan(ConanFile):
    name = "muparser"
    version = "2.3.2"
    description = "Fast Math Parser Library"
    topics = ("conan", "muparser", "math", "parser")
    url = "https://github.com/sintef-ocean/conan-muparser"
    homepage = "https://beltoforion.de/en/muparser"
    author = "Jarle Ladstein jarle.ladstein@sintef.no"
    license = "MIT"
    exports = ["LICENSE"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    _source_subfolder = "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        tools.get("https://github.com/beltoforion/muparser/archive/v{}.zip".format(self.version),
                  sha256="ef303e5b842fa6e755ca7d4622ac1fd50a1f2e3df9069641c4d6eb5014cfe451")
        os.rename(self.name + "-" + self.version, self._source_subfolder)

        tools.replace_in_file(os.path.join(self._source_subfolder, 'CMakeLists.txt'),
                              'project(muParserProject)',
                              'project(muParserProject)\n'
                              'include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)\n'
                              'conan_basic_setup()')

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["ENABLE_SAMPLES"] = False
        cmake.definitions["ENABLE_OPENMP"] = False
        cmake.configure(source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="License.txt", src=self._source_subfolder, dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.defines.append("MUPARSER_DLL" if self.options.shared else "MUPARSER_STATIC")
