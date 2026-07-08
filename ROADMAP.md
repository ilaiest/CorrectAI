# CorrectAI Roadmap

## Product Focus

CorrectAI v1 has one clear job:

```text
Select text in any app -> press the hotkey -> CorrectAI corrects and replaces the selected text.
```

The first public version should stay focused on fast in-place correction. Chatbot-style writing, email drafting, tone rewriting, and advanced composition features are intentionally out of scope for v1.

## Completed Foundation

- [x] Create terminal correction prototype.
- [x] Add empty text validation.
- [x] Add execution timing for terminal mode.
- [x] Add `.env` configuration.
- [x] Add `.gitignore`.
- [x] Add `requirements.txt`.
- [x] Define a shared provider interface.
- [x] Add Gemini provider.
- [x] Add Ollama provider.
- [x] Add provider selection through configuration.
- [x] Add clipboard correction workflow.
- [x] Add global hotkey runner.
- [x] Add minimal settings GUI.
- [x] Document Gemini and Ollama setup.

## v1 - In-Place Text Correction

- [x] Simulate copy from selected text.
- [x] Read selected text from the clipboard.
- [x] Correct selected text with the active provider.
- [x] Copy corrected text back to the clipboard.
- [x] Paste corrected text into the active application.
- [x] Use a stable default hotkey for replacement mode.
- [x] Keep the correction prompt focused on direct corrected output.
- [x] Refactor hotkey runner into copy, correct, and paste steps.
- [x] Polish hotkey runner messages.
- [ ] Test replacement flow in common apps.
- [ ] Finalize recommended local model.
- [x] Update README around the v1 scope.
- [ ] Add basic release notes for v1.

## v1 GUI Scope

The GUI should support configuration only. It should not become a chatbot in v1.

- [x] Configure provider.
- [x] Configure API key.
- [x] Configure model.
- [x] Configure hotkey.
- [x] Make the GUI feel like a simple main menu for v1.
- [ ] Keep provider/model settings easy to understand.
- [x] Add a Start CorrectAI action for the hotkey workflow.
- [ ] Add Start/Stop behavior to the main action button.
- [ ] Display hotkeys in a user-friendly format.

## Post-v1 Ideas

These are useful ideas, but they should not block v1.

- [ ] Compose mode for drafting messages, emails, or replies.
- [ ] Chatbot-style writing assistant.
- [ ] Tone adjustment modes.
- [ ] Optional explanation of corrections.
- [ ] Provider connection test.
- [ ] More detailed provider-specific error messages.
- [ ] Speed and quality comparison between Gemini and local models.
- [ ] Screenshots or demo GIF for the README.
