#include <iostream>
#include <cmath>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

class Oscillator {
public:
    Oscillator() : phase(0.0f), sampleRate(44100.0f) {}

    float process(float frequency) {
        phase += frequency / sampleRate;
        if (phase >= 1.0f) phase -= 1.0f;

        // Basic sine wave implementation
        return std::sin(phase * 2.0f * M_PI);
    }

    void setSampleRate(float newSampleRate) {
        sampleRate = newSampleRate;
    }

private:
    float phase;
    float sampleRate;
};

int main() {
    Oscillator osc;
    osc.setSampleRate(44100.0f);
    
    std::cout << "Generating 10 samples of a 440Hz sine wave:" << std::endl;
    for (int i = 0; i < 10; ++i) {
        std::cout << "Sample " << i << ": " << osc.process(440.0f) << std::endl;
    }
    
    return 0;
}
