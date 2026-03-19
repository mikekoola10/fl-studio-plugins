import json
from prompt_parser import PromptParser
from parameter_mapper import ParameterMapper
from preset_generator import PresetGenerator
import sys
import os

# Add the fl-integration directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../fl-integration"))
from fl_controller import apply_parameters_to_fl

def run_ai_sound_generation(prompt):
    print(f"\n--- Running AI Sound Generation for: \"{prompt}\" ---")
    
    # 1. Parse Prompt
    parser = PromptParser(
        style_map_path=os.path.join(os.path.dirname(__file__), "../shared/style_map.json"),
        schema_path=os.path.join(os.path.dirname(__file__), "../shared/parameter_schema.json")
    )
    parsed_params = parser.parse(prompt)
    print("Parsed Parameters:", json.dumps(parsed_params, indent=2))

    # 2. Map Parameters
    mapper = ParameterMapper(
        schema_path=os.path.join(os.path.dirname(__file__), "../shared/parameter_schema.json")
    )
    # For Milestone v0, we are primarily interested in the SpiralSynth mapping
    mapped_params_spiralsynth = mapper.map_to_spiralsynth(parsed_params)
    print("Mapped Parameters (SpiralSynth):", json.dumps(mapped_params_spiralsynth, indent=2))

    # 3. Apply to FL Studio (mock for now)
    print("\n--- Simulating FL Studio Integration ---")
    apply_parameters_to_fl(mapped_params_spiralsynth)

    # 4. Generate Preset
    generator = PresetGenerator(
        schema_path=os.path.join(os.path.dirname(__file__), "../shared/parameter_schema.json")
    )
    preset_path = generator.generate_preset(mapped_params_spiralsynth, preset_name=prompt.replace(" ", "_"))
    print(f"Preset saved to: {preset_path}")
    print("--- AI Sound Generation Complete ---")

if __name__ == "__main__":
    test_prompts_path = os.path.join(os.path.dirname(__file__), "test_prompts.txt")
    with open(test_prompts_path, "r") as f:
        prompts = f.readlines()
    
    for p in prompts:
        run_ai_sound_generation(p.strip())

    # Example for a single prompt
    # run_ai_sound_generation("dark ambient pad")
