# Setup and Build Guide for FL Studio Plugins

This guide provides detailed instructions on how to set up your development environment and build your VST3 and CLAP plugins for FL Studio 25.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **C++ Compiler:** A modern C++ compiler such as GCC, Clang, or MSVC.
*   **CMake:** Version 3.10 or higher. CMake is used to manage the build process.
*   **VST3 SDK:** Download the VST3 SDK from the [Steinberg Developer website](https://www.steinberg.net/vst3sdk/).
*   **CLAP SDK:** Clone or download the CLAP SDK from its official GitHub repository: [github.com/free-audio/clap](https://github.com/free-audio/clap).
*   **IDE (Optional but Recommended):** An Integrated Development Environment like Visual Studio, CLion, or VS Code can significantly enhance your development workflow.

## Setting Up Your Project

1.  **Clone the repository:**

    If you haven't already, clone your plugin repository:

    ```bash
    git clone https://github.com/mikekoola10/fl-studio-plugins.git
    cd fl-studio-plugins
    ```

2.  **Place SDKs:**

    It is recommended to place the VST3 SDK and CLAP SDK in a known location on your system. You will need to reference these paths in your build configuration.

## Building Your Plugins

For C++ based plugins, CMake is a common choice for managing the build process. Here's a general workflow:

1.  **Create a `CMakeLists.txt`:**

    You will need a `CMakeLists.txt` file in your `src/` directory (or the root of your plugin project) that defines how your plugin is built. A basic example might look like this:

    ```cmake
    cmake_minimum_required(VERSION 3.10)
    project(MyFLStudioPlugin VERSION 1.0.0)

    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)

    # --- VST3 Plugin Example ---
    # Assuming VST3 SDK is at C:/SDKs/VST3_SDK or /Users/YourUser/SDKs/VST3_SDK
    # You might need to adjust these paths or use find_package if SDK is installed system-wide
    # include_directories(C:/SDKs/VST3_SDK/pluginterfaces/vst/)
    # add_library(MyVST3Plugin MODULE src/main.cpp)
    # target_link_libraries(MyVST3Plugin PRIVATE ...)

    # --- CLAP Plugin Example ---
    # Assuming CLAP SDK is at C:/SDKs/CLAP_SDK or /Users/YourUser/SDKs/CLAP_SDK
    # include_directories(C:/SDKs/CLAP_SDK/include)
    # add_library(MyCLAPPlugin MODULE src/main.cpp)
    # target_link_libraries(MyCLAPPlugin PRIVATE ...)
    ```

    *Note: The `CMakeLists.txt` from the initial setup was removed to simplify the repository structure. You will need to create a new one tailored to your specific plugin development.* 

2.  **Configure and Build:**

    Navigate to your project root and create a `build` directory (if you plan to use CMake for building):

    ```bash
    mkdir build
    cd build
    cmake ..
    cmake --build .
    ```

    This will compile your plugins. The output files (e.g., `.vst3`, `.clap`) will be generated in the `build` directory. You should then move these compiled plugins into the `plugins/` directory of this repository.

## Installing Plugins in FL Studio 25

Once your plugins are built, follow these steps to make them available in FL Studio 25:

1.  **Locate your compiled plugin files:** These will typically be `.vst3` files for VST3 plugins and `.clap` files for CLAP plugins.

2.  **Copy to FL Studio Plugin Folders:**

    *   **VST3 Plugins:** Copy your `.vst3` files to one of FL Studio's VST plugin scan paths. Common locations include:
        *   **Windows:** `C:\Program Files\Common Files\VST3`
        *   **macOS:** `/Library/Audio/Plug-Ins/VST3`

    *   **CLAP Plugins:** Copy your `.clap` files to a directory that FL Studio is configured to scan for CLAP plugins. Since there isn't a single standard location for CLAP plugins yet, you might need to:
        *   Create a dedicated folder (e.g., `C:\Program Files\Common Files\CLAP` or `~/Library/Audio/Plug-Ins/CLAP`).
        *   Add this new folder to FL Studio's plugin search paths.

3.  **Scan for plugins in FL Studio:**

    *   Open FL Studio 25.
    *   Go to `Options > Manage Plugins`.
    *   In the Plugin Manager, click the `Find plugins` button. Ensure that the directories where you copied your plugins are included in the scan paths. If not, add them using the 
