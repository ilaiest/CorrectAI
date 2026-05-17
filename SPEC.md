# CorrectAI Spec

## Objective

CorrectAI is an open source, local-first tool for correcting spelling, accents, and punctuation using AI. It should preserve the user's tone and wording as much as possible instead of rewriting text unnecessarily.

## Product Principles

- Correct only what is necessary.
- Preserve the user's tone.
- Avoid making text more formal unless explicitly requested.
- Keep user credentials local.
- Make the active provider and model visible to the user.
- Support multiple providers over time.
- Prefer safe behavior by default.
- Keep the code simple, readable, and auditable.

## Open Source Principles

CorrectAI should be safe and understandable for other users to run on their own machines.

- No hosted backend by default.
- No telemetry by default.
- No API keys committed to the repository.
- No hidden provider calls.
- Text should only be sent to the provider selected by the user.
- Local providers should be supported for users who prefer privacy or offline usage.

## v0.1 - Terminal Prototype

### Features

- Receive text from terminal input.
- Validate empty input before calling the model.
- Send text to Gemini.
- Return corrected text.
- Return a short list of important changes.
- Preserve tone and wording as much as possible.
- Show execution time.
- Handle basic API errors.

### Out of Scope

- GUI.
- Clipboard integration.
- Global hotkeys.
- Multiple providers.
- Persistent configuration.
- `.env` support.
- Automatic replacement of selected text in other apps.

## Current Architecture

```text
main.py
  terminal input
  input validation
  execution timing
  result display

corrector.py
  prompt construction
  Gemini API call
  basic API error handling
```

## Future Architecture

The project should move toward a provider-based design:

```text
CorrectAI core
  builds correction requests
  normalizes provider responses

Providers
  Gemini
  Bedrock
  Local/Ollama
  Mock

Interfaces
  Terminal
  Clipboard
  Hotkey background runner
  GUI settings panel
```

The correction flow should eventually look like:

```text
input text -> corrector core -> selected provider -> normalized result -> output target
```

## Planned Providers

### Gemini

Accessible cloud provider for early development and general users.

### AWS Bedrock

Enterprise/cloud provider for users who already have AWS credentials and approved model access.

### Local/Ollama

Private/offline option. This may have lower quality or higher hardware requirements depending on the selected model.

### Mock

Development provider for testing application flow without spending tokens or calling external APIs.

## Safety Modes

CorrectAI should support safe behavior before automatic behavior.

### Safe Clipboard Mode

The user copies text manually, CorrectAI corrects it, and the corrected version is copied back to the clipboard.

### Selection Mode

CorrectAI simulates copy, reads selected text, corrects it, and places the corrected text in the clipboard.

### Auto Replace Mode

CorrectAI corrects selected text and pastes the corrected version automatically. This should not be the default mode.

