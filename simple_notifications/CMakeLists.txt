cmake_minimum_required(VERSION 3.5)
project(notification)

set(CMAKE_CXX_STANDARD 14)

set (CMAKE_CXX_FLAGS "-flto")

#set(PYBIND11_PYTHON_VERSION 2.7)


add_subdirectory(src/pybind11)
pybind11_add_module(injectionSupport src/main.cpp)
target_link_libraries(injectionSupport PRIVATE "-framework Foundation")

