Current tasks:
- [ ] Install script
  - [ ] setup virtualenv
  - [ ] Download sms-tools and add to python path

- [x] STFT
  - [ ] Improve error
    - [ ] Different window type?
    - [ ] No windowing?
  - [ ] More Tests?
    - [ ] Peak consistency

- [ ] Harmonic Analysis
  - [ ] Use side-lobe height to determine min-amplitude threshhold

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
