# SpiralSynth AI – Milestone v0

## Goal
Working AI-assisted sound generation inside FL Studio.

## Requirements

1. AI Engine
- Input: text prompt
- Output: parameter JSON

2. Parameter System
- Must follow parameter_schema.json
- Deterministic mapping using style_map.json

3. FL Studio Integration
- Script runs without error
- Applies parameters to active plugin (mock acceptable)

4. JUCE Plugin
- Builds successfully
- Produces sound (sine wave is enough)
- Exposes 8 parameters:
  osc_type, detune, cutoff, resonance, attack, decay, reverb, distortion

5. End-to-End Test
- Input: "dark ambient pad"
- Output: audible sound change

## Definition of Done
User can:
- Run script
- Generate parameters
- Hear sound change in FL Studio or plugin
