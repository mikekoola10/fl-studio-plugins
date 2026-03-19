import json
import random

class PromptParser:
    def __init__(self, style_map_path="../shared/style_map.json", schema_path="../shared/parameter_schema.json"):
        with open(style_map_path, 'r') as f:
            self.style_map = json.load(f)
        with open(schema_path, 'r') as f:
            self.default_params = json.load(f)

    def parse(self, prompt):
        print(f"Parsing prompt: {prompt}")
        params = self.default_params.copy()
        
        words = prompt.lower().split()
        for word in words:
            if word in self.style_map:
                style_traits = self.style_map[word]
                for param, value_config in style_traits.items():
                    if isinstance(value_config, dict) and "min" in value_config and "max" in value_config:
                        # Randomly pick a value within the defined range, or use default
                        params[param] = random.uniform(value_config["min"], value_config["max"])
                    else:
                        # Direct value assignment (e.g., osc_type)
                        params[param] = value_config
        
        return params

if __name__ == "__main__":
    parser = PromptParser()
    test_prompts = [
        "dark bass",
        "ambient pad",
        "rage lead",
        "bright pluck"
    ]
    for prompt in test_prompts:
        result = parser.parse(prompt)
        print(f"\nParameters for \'{prompt}\':")
        print(json.dumps(result, indent=2))
