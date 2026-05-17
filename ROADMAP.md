# CorrectAI Roadmap

## v0.1 - Terminal Prototype

- [x] Create `main.py`.
- [x] Create `corrector.py`.
- [x] Receive text from terminal.
- [x] Validate empty input.
- [x] Connect to Gemini.
- [x] Return corrected text and important changes.
- [x] Add basic API error handling.
- [x] Measure execution time.
- [ ] Fix prompt encoding if needed.
- [x] Move model name to a constant.
- [x] Improve variable names for clarity.

## v0.2 - Configuration Basics

- [ ] Add `requirements.txt`.
- [ ] Add `.gitignore`.
- [ ] Add `.env` support.
- [ ] Read model name from configuration.
- [ ] Add a mock provider for testing without API calls.

## v0.3 - Provider Design

- [ ] Define a common provider interface.
- [ ] Move Gemini logic into a provider module.
- [ ] Add provider selection.
- [ ] Add provider-specific error messages.
- [ ] Document provider setup.

## v0.4 - Clipboard Workflow

- [ ] Add `pyperclip`.
- [ ] Read text from clipboard.
- [ ] Correct clipboard text.
- [ ] Copy corrected text back to clipboard.
- [ ] Add safe mode as the default behavior.

## v0.5 - Local Provider Exploration

- [ ] Test Ollama integration.
- [ ] Try a small local model.
- [ ] Compare speed and correction quality.
- [ ] Document local setup limitations.

## v0.6 - Hotkey Runner

- [ ] Explore `pynput` or alternatives.
- [ ] Add a background runner.
- [ ] Configure a global hotkey.
- [ ] Add safe clipboard hotkey mode.
- [ ] Consider optional auto-replace mode.

## v0.7 - Minimal GUI

- [ ] Add a small settings window.
- [ ] Configure provider.
- [ ] Configure API key.
- [ ] Configure model.
- [ ] Test provider connection.
- [ ] Configure hotkey.
