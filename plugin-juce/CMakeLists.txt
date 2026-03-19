cmake_minimum_required(VERSION 3.10)
project(SpiralSynth VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# This is a placeholder for a real JUCE project setup.
# In a full JUCE project, you would typically use the Projucer to generate
# the CMake files, or include the JUCE CMake modules.
# For Milestone v0, we are just ensuring a basic C++ file can compile.

add_executable(SynthEngine Source/SynthEngine.cpp)

# To simulate exposing parameters, we would need a more complex JUCE setup.
# For now, the C++ file simply demonstrates sound generation.
