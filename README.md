# SpiralSynth AI

SpiralSynth AI is a project that bridges AI-driven sound design with real-time plugin control, specifically designed for FL Studio.

## Architecture

- **ai-engine (Python)**: Natural language processing for prompt-to-parameter mapping.
- **fl-integration (Python)**: Logic for communicating with FL Studio automation.
- **plugin-juce (C++ / JUCE)**: The VST3 synthesizer engine and UI.
- **shared (JSON Schema)**: Unified parameter definitions used by both the AI and the plugin.
- **presets/generated**: A folder for storing AI-generated sound presets.
- **docs**: Project documentation and guides.

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **CMake 3.15+**
- **JUCE Framework**
- **FL Studio 25+** (for integration testing)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mikekoola10/fl-studio-plugins.git
    cd fl-studio-plugins
    ```

2.  **Build the VST3 Plugin:**
    ```bash
    cd plugin-juce
    mkdir build && cd build
    cmake ..
    cmake --build .
    ```

3.  **Run the AI Engine:**
    ```bash
    cd ai-engine
    # Example usage (stub)
    python3 parameter_mapper.py
    ```

## Roadmap

- [ ] Complete AI prompt parsing with LLM integration.
- [ ] Implement advanced DSP in the JUCE synthesizer.
- [ ] Develop real-time FL Studio automation bridge.
- [ ] Create a library of predefined style maps.
- [ ] Add preset export/import via JSON schema.

## Goal

Provide a seamless experience where producers can describe a sound in plain English and have the plugin adjust its parameters in real-time within FL Studio.
