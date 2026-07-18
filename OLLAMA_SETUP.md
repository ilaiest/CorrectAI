# Ollama Setup SOP

This guide explains how to install Ollama and download the recommended local model for CorrectAI.

Use this if you want CorrectAI to correct text locally instead of using a cloud provider.

## 1. Install Ollama

Download Ollama from:

```text
https://ollama.com/download
```

Choose the installer for your operating system and follow the installation steps.

On Windows, Ollama usually keeps running in the background after installation.

## 2. Open A Terminal

On Windows:

1. Open the Start menu.
2. Search for `PowerShell`.
3. Open PowerShell.

## 3. Check That Ollama Works

Run:

```powershell
ollama --version
```

If this prints a version number, Ollama is installed correctly.

## 4. Download The Recommended Model

CorrectAI currently recommends:

```text
qwen2.5:7b
```

Download it with:

```powershell
ollama pull qwen2.5:7b
```

This may take a while because the model is several GB.

## 5. Confirm The Model Is Installed

Run:

```powershell
ollama list
```

You should see:

```text
qwen2.5:7b
```

## 6. Test The Model

Run:

```powershell
ollama run qwen2.5:7b
```

Then type a short test:

```text
Corrige este texto: ola como estas espero estes bien
```

If the model responds, Ollama is ready.

To exit the chat, type:

```text
/bye
```

## 7. Configure CorrectAI

In CorrectAI, use:

```text
Provider: ollama
Model: qwen2.5:7b
Hotkey: F8
```

The API key can be empty when using Ollama.

## 8. Common Issues

### CorrectAI Says Ollama Is Not Running

Open Ollama from your Start menu, then try again.

You can also test from PowerShell:

```powershell
ollama list
```

If that command fails, Ollama is not available yet.

### CorrectAI Says The Model Is Missing

Run:

```powershell
ollama pull qwen2.5:7b
```

Then try CorrectAI again.

### The Computer Feels Slow

Local models use CPU, GPU, RAM, and disk space.

For most users, `qwen2.5:7b` is a good balance between quality and resource usage. If it is too slow, try a smaller model:

```powershell
ollama pull llama3.2:3b
```

Then configure CorrectAI with:

```text
Model: llama3.2:3b
```

Quality may be lower with smaller models.

## 9. Remove Models You Do Not Use

Check installed models:

```powershell
ollama list
```

Remove a model:

```powershell
ollama rm llama3.2:3b
```

Replace `llama3.2:3b` with the model name you want to remove.
