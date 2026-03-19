# FL Studio Plugins by MikeKoola10

This repository contains custom plugins, tools, and presets for FL Studio, with a focus on the **SpiralSynth AI** project.

## SpiralSynth AI Project Overview

**Objective:** To build an AI-assisted sound generation system for FL Studio, comprising two main layers:

1.  **AI Control Layer (Python):** Provides immediate usability within FL Studio by generating sound parameters from text prompts and controlling existing synths via automation.
2.  **Custom Instrument Layer (JUCE VST/CLAP):** A long-term asset, a standalone VST instrument with custom oscillators, UI, and sound identity.

Both layers utilize a **Unified Parameter Schema** (`shared/parameter_schema.json`) for consistent control.

## Repository Structure

```
fl-studio-plugins/
├── README.md                   # Project overview and instructions
├── ai-engine/                  # Python scripts for AI sound generation
│   ├── prompt_parser.py        # Parses text prompts into parameters
│   ├── parameter_mapper.py     # Maps parameters to target systems (FL Studio, JUCE)
│   ├── preset_generator.py     # Generates presets from parameters
│   ├── main_ai_orchestrator.py # Main script to run AI sound generation
│   └── test_prompts.txt        # Example prompts for testing the AI engine
├── fl-integration/             # Python scripts for FL Studio integration
│   └── fl_controller.py        # Applies parameters to FL Studio (mocked for now)
├── plugin-juce/                # JUCE project for the custom VST/CLAP instrument
│   └── Source/                 # C++ source files for the JUCE plugin
│       └── SynthEngine.cpp     # Basic synth engine (sine wave oscillator)
├── shared/                     # Shared resources and configurations
│   ├── parameter_schema.json   # Unified parameter definition
│   └── style_map.json          # Deterministic mapping for prompt parsing
├── presets/                    # Generated presets and Patcher presets
│   └── generated/              # AI-generated presets
│   └── patcher-presets/        # User-created Patcher presets
└── docs/                       # Project documentation
    ├── setup-guide.md          # Detailed setup and build instructions
    ├── architecture.md         # Overview of the SpiralSynth AI architecture
    └── milestone_v0.md         # Definition of Milestone v0 requirements
```

## Types of Tools
- **AI Engine (Python):** For generating sound parameters from text prompts.
- **VST Plugins (C++ / JUCE):** For developing custom instruments and effects.
- **FL Studio Patcher Presets:** For complex routing and instrument chains.
- **Python Scripts (Automation tools):** For controlling FL Studio and other tasks.

## Installation & Usage

### AI Engine (Python)

1.  **Navigate to the `ai-engine` directory:**
    ```bash
    cd fl-studio-plugins/ai-engine
    ```
2.  **Run the main orchestrator script:**
    ```bash
    python3 main_ai_orchestrator.py
    ```
    This will process the `test_prompts.txt` and simulate applying parameters to FL Studio, generating presets in `presets/generated/`.

### VST Plugins (C++ / JUCE)

Detailed setup and build instructions for the JUCE plugin can be found in `docs/setup-guide.md`.

1.  **Build the JUCE plugin:** Follow the instructions in `docs/setup-guide.md` to compile your `.vst3` or `.clap` files.
2.  **Copy .vst3 files** to your VST folder (e.g., `C:\Program Files\Common Files\VST3`).
3.  **Open FL Studio** and go to `Options → Manage Plugins → Scan`.

### Patcher Presets

1.  **Drop your `.fst` files** into:
    `Documents/Image-Line/FL Studio/Presets/Patcher`

### Scripts

1.  **Place your Python scripts** inside:
    `FL Studio/System/Hardware specific/` (or other designated script folders within FL Studio).

## Goal

Build powerful, creative tools for producers and creators, starting with an AI-assisted sound design system that evolves into a unique, sellable instrument.

## Milestone v0 Status

Refer to `docs/milestone_v0.md` for the current requirements and definition of done for the initial working prototype. The current focus is on completing the parameter mapping logic, connecting the AI to the FL Studio script, and making the JUCE plugin produce sound.
