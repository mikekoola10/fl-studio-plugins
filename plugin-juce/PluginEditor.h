#pragma once

#include <juce_gui_basics/juce_gui_basics.h>
#include "PluginProcessor.h"

class SpiralSynthAudioProcessorEditor  : public juce::AudioProcessorEditor
{
public:
    SpiralSynthAudioProcessorEditor (SpiralSynthAudioProcessor&);
    ~SpiralSynthAudioProcessorEditor() override;

    void paint (juce::Graphics&) override;
    void resized() override;

private:
    SpiralSynthAudioProcessor& audioProcessor;

    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR (SpiralSynthAudioProcessorEditor)
};
