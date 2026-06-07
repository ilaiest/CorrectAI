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
- [x] Verify prompt encoding in editor.
- [x] Move model name to a constant.
- [x] Improve variable names for clarity.

## v0.2 - Configuration Basics

- [x] Add `requirements.txt`.
- [x] Add `.gitignore`.
- [x] Add `.env` support.
- [x] Read model name from configuration.
- [x] Validate missing Gemini API key.
- [x] Add a mock provider for testing without API calls.

## v0.3 - Code Cleanup

- [x] Extract shared correction timing logic.
- [ ] Reduce duplicated input validation patterns.
- [ ] Improve terminal output formatting.

## v0.5 - Provider Design

- [x] Define a common provider interface.
- [x] Move Gemini logic into a provider module.
- [x] Add provider selection.
- [ ] Add provider-specific error messages.

- [ ] Document provider setup.

## v0.4 - Clipboard Workflow

- [x] Add `pyperclip`.
- [x] Read text from clipboard.
- [x] Correct clipboard text.
- [x] Copy corrected text back to clipboard.
- [x] Add safe mode as the default behavior.

## v0.6 - Local Provider Exploration

- [x] Test Ollama integration.
- [x] Try a small local model.
- [ ] Compare speed and correction quality.

## v0.7 - Hotkey Runner

- [x] Explore `pynput` or alternatives.
- [x] Add a background runner.
- [x] Configure a global hotkey.
- [x] Add safe clipboard hotkey mode.
- [ ] Consider optional auto-replace mode.

## v0.8 - Minimal GUI

- [x] Add a small settings window.
- [x] Configure provider.
- [x] Configure API key.
- [x] Configure model.
- [x] Configure hotkey.
