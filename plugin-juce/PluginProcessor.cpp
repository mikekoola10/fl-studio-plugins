#include "PluginProcessor.h"
#include "PluginEditor.h"

SpiralSynthAudioProcessor::SpiralSynthAudioProcessor()
{
}

SpiralSynthAudioProcessor::~SpiralSynthAudioProcessor()
{
}

void SpiralSynthAudioProcessor::prepareToPlay (double sampleRate, int samplesPerBlock)
{
}

void SpiralSynthAudioProcessor::releaseResources()
{
}

void SpiralSynthAudioProcessor::processBlock (juce::AudioBuffer<float>& buffer, juce::MidiBuffer& midiMessages)
{
    juce::ScopedNoDenormals noDenormals;
    auto totalNumInputChannels  = getTotalNumInputChannels();
    auto totalNumOutputChannels = getTotalNumOutputChannels();

    for (auto i = totalNumInputChannels; i < totalNumOutputChannels; ++i)
        buffer.clear (i, 0, buffer.getNumSamples());
}

juce::AudioProcessorEditor* SpiralSynthAudioProcessor::createEditor()
{
    return new SpiralSynthAudioProcessorEditor (*this);
}

void SpiralSynthAudioProcessor::getStateInformation (juce::MemoryBlock& destData)
{
}

void SpiralSynthAudioProcessor::setStateInformation (const void* data, int sizeInBytes)
{
}
