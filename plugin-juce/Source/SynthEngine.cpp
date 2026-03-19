#include <iostream>
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

class SynthEngine {
public:
    struct Parameters {
        std::string osc_type = "sine";
        float detune = 0.1f;
        float cutoff = 1000.0f;
        float resonance = 0.2f;
        float attack = 0.01f;
        float decay = 0.3f;
        float reverb = 0.2f;
        float distortion = 0.2f;
    };

    SynthEngine() : phase(0.0f), sampleRate(44100.0f) {}

    void setParameters(const Parameters& newParams) {
        params = newParams;
        std::cout << "SynthEngine: Parameters updated." << std::endl;
    }

    float process(float frequency) {
        // Apply detune to frequency
        float detunedFreq = frequency * (1.0f + params.detune * 0.05f);
        
        phase += detunedFreq / sampleRate;
        if (phase >= 1.0f) phase -= 1.0f;

        float sample = 0.0f;
        if (params.osc_type == "sine") {
            sample = std::sin(phase * 2.0f * M_PI);
        } else if (params.osc_type == "saw") {
            sample = 2.0f * (phase - 0.5f);
        } else if (params.osc_type == "square") {
            sample = (phase < 0.5f) ? 1.0f : -1.0f;
        }

        // Simple distortion (clipping)
        if (params.distortion > 0.5f) {
            float drive = params.distortion * 2.0f;
            sample = std::tanh(sample * drive);
        }

        // Simple low-pass filter (mock)
        // In a real JUCE plugin, this would be a proper IIR/FIR filter
        float filterEffect = params.cutoff / 20000.0f;
        sample *= filterEffect;

        return sample;
    }

    void setSampleRate(float newSampleRate) {
        sampleRate = newSampleRate;
    }

private:
    float phase;
    float sampleRate;
    Parameters params;
};

int main() {
    SynthEngine engine;
    engine.setSampleRate(44100.0f);

    SynthEngine::Parameters darkBassParams;
    darkBassParams.osc_type = "saw";
    darkBassParams.cutoff = 200.0f;
    darkBassParams.distortion = 0.8f;
    darkBassParams.detune = 0.3f;

    engine.setParameters(darkBassParams);
    
    std::cout << "Generating 10 samples of 'dark bass' at 55Hz (A1):" << std::endl;
    for (int i = 0; i < 10; ++i) {
        std::cout << "Sample " << i << ": " << engine.process(55.0f) << std::endl;
    }
    
    return 0;
}
