# FL Studio Instruments and Plugins Development

This repository is dedicated to developing custom instruments and plugins compatible with FL Studio 25. It provides a basic structure and guidelines to help you create your own VST3 and CLAP plugins.

## Supported Formats

FL Studio 25 supports various plugin formats, with **VST3** and **CLAP** being modern and recommended choices for new development due to their advanced features and performance benefits.

*   **VST3 (Virtual Studio Technology 3)**: A widely adopted plugin standard offering features like dynamic I/O, event-based automation, and improved CPU efficiency.
*   **CLAP (Clever Audio Plugin API)**: A newer, open-source plugin API designed for modern plugin development, focusing on performance, stability, and extensibility.

## Project Structure

```
fl-studio-plugins/
├── README.md               # This file
├── plugins/                # Compiled plugin files (e.g., .vst3, .clap)
│   └── (your plugin files go here)
├── src/                    # Source code for your plugins
│   └── main.cpp            # Example plugin source file
├── presets/                # Presets for instruments and effects
│   └── patcher-presets/    # Patcher presets
└── docs/                   # Documentation and guides
    └── setup-guide.md      # Setup and build guide
```

## Getting Started

### Prerequisites

To develop VST3/CLAP plugins, you will need:

*   A C++ compiler (e.g., GCC, Clang, MSVC)
*   CMake (version 3.10 or higher) - *Note: CMakeLists.txt was removed for a simpler structure, but CMake is still recommended for complex C++ projects.*
*   VST3 SDK (available from [Steinberg](https://www.steinberg.net/vst3sdk/))
*   CLAP SDK (available from [github.com/free-audio/clap](https://github.com/free-audio/clap))
*   An IDE (e.g., Visual Studio, CLion, VS Code) is recommended for a better development experience.

### Setup and Build Instructions

Detailed setup and build instructions can be found in `docs/setup-guide.md`.

### Installing Plugins in FL Studio 25

1.  **Locate your plugin files:** After building, find your `.vst3` and/or `.clap` files in the `plugins/` directory.

2.  **Copy to FL Studio Plugin Folders:**

    *   **VST3:** Copy your `.vst3` plugin to one of FL Studio\`s VST plugin scan paths. A common location is `C:\Program Files\Common Files\VST3` (Windows) or `/Library/Audio/Plug-Ins/VST3` (macOS).
    *   **CLAP:** Copy your `.clap` plugin to a folder that FL Studio scans for CLAP plugins. There isn\`t a single standard location yet, so you might need to create a dedicated folder and add it to FL Studio\`s plugin search paths.

3.  **Scan for plugins in FL Studio:**

    *   Open FL Studio 25.
    *   Go to `Options > Manage Plugins`.
    *   Click `Find plugins` to scan for new plugins. Ensure that the directories where you copied your plugins are included in the scan paths.

4.  **Add to your project:** Your new instruments or effects should now appear in the plugin database and be available for use in your FL Studio projects.

## Contributing

Feel free to fork this repository, create your own plugins, and submit pull requests with improvements or new examples.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details. (Note: A `LICENSE` file will be added later.)
