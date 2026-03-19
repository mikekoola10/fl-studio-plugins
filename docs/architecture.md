# SpiralSynth AI Architecture

The SpiralSynth AI system is designed as a two-layer architecture to provide immediate usability while building a long-term standalone asset.

## Layer 1: AI Control (Immediate Use)
- **Role:** Acts as the "brain + automation layer" for existing synths in FL Studio (e.g., Serum).
- **Functionality:**
  - Generates sound parameters from natural language prompts.
  - Controls synths via automation scripts.
  - Outputs presets and MIDI data.

## Layer 2: Custom Instrument (Standalone VST)
- **Role:** A custom-built synth engine using JUCE.
- **Functionality:**
  - Custom oscillators and sound identity.
  - Unique user interface.
  - Standalone VST3/CLAP plugin format.

## Unified Parameter Schema
Both layers communicate using a shared JSON schema, ensuring that AI-generated sounds can be applied to both existing synths and the custom SpiralSynth engine.

```json
{
  "osc_type": "saw",
  "detune": 0.12,
  "cutoff": 800,
  "resonance": 0.3,
  "attack": 0.01,
  "decay": 0.2,
  "sustain": 0.7,
  "release": 0.5,
  "reverb": 0.4,
  "distortion": 0.6
}
```

## Development Phases
1. **Phase 1:** AI Control Layer (Python + FL Studio scripts).
2. **Phase 2:** Core Synth Engine (JUCE-based oscillators, ADSR, filters).
3. **Phase 3:** AI Integration (Connecting the AI engine to the plugin UI).
4. **Phase 4:** Advanced Features (Wavetables, Mod Matrix, FX Rack).
