cmake_minimum_required(VERSION 3.15)

project(SpiralSynthAI VERSION 0.1.0)

# ------------------------------------------------------------------------------
# JUCE Setup
# ------------------------------------------------------------------------------
# In a real environment, you'd find_package(JUCE) or add_subdirectory(JUCE).
# We're providing a structured scaffold for Manus.

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# If JUCE was already found, this would be:
# juce_add_plugin(SpiralSynthAI
#     COMPANY_NAME "SpiralSynth"
#     IS_SYNTH TRUE
#     NEEDS_MIDI_INPUT TRUE
#     FORMATS VST3
# )

# For a basic CMake scaffold:
add_library(SpiralSynthAI MODULE
    PluginProcessor.cpp
    PluginProcessor.h
    PluginEditor.cpp
    PluginEditor.h
)

target_include_directories(SpiralSynthAI PRIVATE .)

# ------------------------------------------------------------------------------
# Build Notes for Manus:
# 1. Ensure JUCE is available.
# 2. Link against necessary JUCE modules (audio_processors, gui_basics, etc.).
# 3. Update juce_add_plugin configuration as needed.
# ------------------------------------------------------------------------------
