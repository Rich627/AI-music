# AI Music Generation

This project focuses on using deep learning techniques to generate music with the help of artificial intelligence.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Model Training](#model-training)
- [Inference and Music Generation](#inference-and-music-generation)
- [GUI Integration](#gui-integration)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

The goal of this project is to train a deep learning model using LSTM (Long Short-Term Memory) to generate music. The model is trained on a dataset of MIDI files obtained from the [Lakh MIDI Dataset](https://www.kaggle.com/datasets/imsparsh/lakh-midi-clean?resource=download). The generated music can be played, paused, and stopped using a GUI built with tkinter and pygame libraries.

## Dataset

The dataset used for training is the Lakh MIDI Dataset, which contains a large collection of MIDI files from various genres. You can download the dataset from the provided link and extract the MIDI files for further processing.

## Data Preprocessing

To prepare the MIDI files for training, the project involves the following steps:

1. Extract the MIDI files from each folder and remove the folder structure.
2. Rename the MIDI files for easier identification.
3. Use the `pretty_midi` library to extract the notes and velocities from each MIDI file.
4. Convert the extracted notes and velocities into NumPy arrays.
5. Normalize the arrays to bring the values within a specific range.
6. Combine the normalized notes and velocities arrays into a single array, which will serve as the input data for the model.

## Model Training

The deep learning model is built using TensorFlow and consists of an LSTM layer followed by two dense layers. The model is trained using the input and target data, which are split into training and validation sets. The training progress and loss are monitored and visualized to evaluate the model's performance.

## Inference and Music Generation

Once the model is trained, it can be used to generate new music. The model takes a sequence of input data as an initial seed and predicts the next notes and velocities in the sequence. This process can be repeated iteratively to generate longer music compositions. The generated music is then converted to MIDI format using the `music21` library.

## GUI Integration

A graphical user interface (GUI) is implemented using the `tkinter` library, allowing users to interact with the generated music. The GUI provides controls to play, pause, and stop the music. The `pygame` library is used to handle audio playback.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Acknowledgements

You can add reference to the following paper if need to use it somewhere:

Colin Raffel. "Learning-Based Methods for Comparing Sequences, with Applications to Audio-to-MIDI Alignment and Matching". PhD Thesis, 2016.
