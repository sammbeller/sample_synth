Current tasks:
- [ ] Install script
  - [ ] setup virtualenv
  - [ ] Download sms-tools and add to python path

- [x] STFT
  - [ ] Improve error
    - [ ] Different window type?
      - [ ] Hamming windows and related are POA at 50%
    - [ ] No windowing?
  - [ ] More Tests?
    - [X] Peak consistency
    - [ ] Add new parameters
  - [ ] Infer length of synthesized sound from spectrum

- [ ] Harmonic Analysis
  - [ ] Parabolic Interpolation
  - [ ] Variables
    - [ ] Minimum amplitude threshold (based on sidelobe level, paramterized for now)
    - [ ] Minimum duration threshold
    - [ ] Maximum number of tracks?
  - [ ] Tests
    - [ ] Parabolic Interpolation
    - [ ] Shape
    - [ ] Accuracy (number of tracks??)
    - [ ] Fundamental??

- [ ] Stochastic Analysis

- [ ] Pitch shift
  - [ ] Read wav file
  - [ ] Perform stft
  - [ ] Identify Peaks
    - [ ] Window size (might be depentdent on fundamental frequency detection)
    - [ ] Frequency variability
    - [ ] Duration threshold
    - [ ] Min amplitude
    - [ ] Parabolic interpolation
  - [ ] Identify fundamental fq
  - [ ] Stochastic analysis
  - [ ] Adjust harmonics to new fundamental
  - [ ] Synthesize
  - [ ] write wav

- [ ] Variables
  - [ ] DFT size (parameterized for now, but should be inferred from fundamental)
  - [X] Window type (Hanning)
  - [ ] Frequency delta threshold
  - [ ] Minimum amplitude threshold
  - [ ] Minimum duration threshold
  - [X] Window size (same as DFT size duh)
