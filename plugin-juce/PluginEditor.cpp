#include "PluginProcessor.h"
#include "PluginEditor.h"

SpiralSynthAudioProcessorEditor::SpiralSynthAudioProcessorEditor (SpiralSynthAudioProcessor& p)
    : AudioProcessorEditor (&p), audioProcessor (p)
{
    setSize (400, 300);
}

SpiralSynthAudioProcessorEditor::~SpiralSynthAudioProcessorEditor()
{
}

void SpiralSynthAudioProcessorEditor::paint (juce::Graphics& g)
{
    g.fillAll (getLookAndFeel().findColour (juce::ResizableWindow::backgroundColourId));
    g.setColour (juce::Colours::white);
    g.setFont (15.0f);
    g.drawFittedText ("SpiralSynth AI", getLocalBounds(), juce::Justification::centred, 1);
}

void SpiralSynthAudioProcessorEditor::resized()
{
}
