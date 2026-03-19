import json

class PresetGenerator:
    def __init__(self, schema_path):
        with open(schema_path, 'r') as f:
            self.schema = json.load(f)

    def generate_preset(self, parameters, preset_name="new_preset"):
        # In a real scenario, this would format parameters into a specific
        # preset file format (e.g., .fst for FL Studio, or a custom format).
        # For now, we'll just save the JSON parameters as a 'preset'.
        preset_data = {
            "name": preset_name,
            "parameters": parameters
        }
        output_path = f"../presets/generated/{preset_name}.json"
        with open(output_path, 'w') as f:
            json.dump(preset_data, f, indent=2)
        print(f"Preset '{preset_name}' generated at {output_path}")
        return output_path

if __name__ == "__main__":
    # Example usage
    from prompt_parser import PromptParser
    from parameter_mapper import ParameterMapper

    parser = PromptParser()
    mapper = ParameterMapper("../shared/parameter_schema.json")
    generator = PresetGenerator("../shared/parameter_schema.json")

    prompt = "dark ambient pad"
    parsed_params = parser.parse(prompt)
    mapped_params = mapper.map_to_spiralsynth(parsed_params)
    generator.generate_preset(mapped_params, preset_name="dark_ambient_pad")
