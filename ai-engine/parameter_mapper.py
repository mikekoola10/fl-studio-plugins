import json

class ParameterMapper:
    def __init__(self, schema_path):
        with open(schema_path, 'r') as f:
            self.schema = json.load(f)

    def map_to_serum(self, params):
        """
        Maps the unified parameter schema to Serum's macro indices.
        Example: Macro 1 = Cutoff, Macro 2 = Resonance, etc.
        """
        serum_mapping = {
            "Macro 1": params.get("cutoff", 500),
            "Macro 2": params.get("resonance", 0.2),
            "Macro 3": params.get("distortion", 0.1),
            "Macro 4": params.get("detune", 0.1)
        }
        return serum_mapping

    def map_to_spiralsynth(self, params):
        """
        Maps the unified parameter schema directly to the custom SpiralSynth engine.
        """
        return params

if __name__ == "__main__":
    mapper = ParameterMapper("../shared/parameter_schema.json")
    sample_params = {
        "cutoff": 800,
        "resonance": 0.4,
        "distortion": 0.6,
        "detune": 0.12
    }
    print("Serum Mapping:", mapper.map_to_serum(sample_params))
    print("SpiralSynth Mapping:", mapper.map_to_spiralsynth(sample_params))
