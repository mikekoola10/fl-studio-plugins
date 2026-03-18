cmake_minimum_required(VERSION 3.10)
project(FLStudioPlugins VERSION 1.0.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add source and include directories
add_subdirectory(src)
include_directories(include)

# Find VST3 SDK (assuming it's installed or provided)
# You would typically add logic here to find the VST3 SDK
# For example: find_package(VST3 REQUIRED)

# Find CLAP SDK (assuming it's installed or provided)
# You would typically add logic here to find the CLAP SDK
# For example: find_package(CLAP REQUIRED)

# Example for a simple VST3 plugin (replace with actual plugin logic)
# add_library(MyVST3Plugin MODULE src/MyVST3Plugin.cpp)
# target_link_libraries(MyVST3Plugin PRIVATE VST3::SDK)

# Example for a simple CLAP plugin (replace with actual plugin logic)
# add_library(MyCLAPPlugin MODULE src/MyCLAPPlugin.cpp)
# target_link_libraries(MyCLAPPlugin PRIVATE CLAP::SDK)

# Install targets (optional)
# install(TARGETS MyVST3Plugin DESTINATION "${CMAKE_INSTALL_PREFIX}/VST3")
# install(TARGETS MyCLAPPlugin DESTINATION "${CMAKE_INSTALL_PREFIX}/CLAP")
