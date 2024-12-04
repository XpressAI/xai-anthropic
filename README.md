<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>





<p align="center"><i>Xircuits Component Library to interface with 
Anthropic AI! Build AI-powered solutions.</i></p>

---
## Xircuits Component Library for Anthropic

This library allows Xircuits to use Anthropic's models for direct AI interactions. It manages API keys and simplifies executing custom text generation tasks.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:
![anthropic_example](https://github.com/user-attachments/assets/3cbda704-5dbb-4886-b40a-3281ac7d7c20)

### The Result:
![Anthropic_Example_Result](https://github.com/user-attachments/assets/b557707c-4b42-408a-884f-13516300866d)


## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.

## Main Xircuits Components

### Anthropic Authorize Component:
Sets the API key for the Anthropic client.

<img src="https://github.com/user-attachments/assets/6fe98f7e-1cb2-4527-adee-5b5699c6ac23" alt="Anthropic Authorize" width="200" />

### Anthropic Generate Component:
Generates text using an Anthropic model, with options to customize length and randomness.

<img src="https://github.com/user-attachments/assets/3cf68c9c-859c-4e6d-a61b-dd77ea5f831f" alt="AnthropicGenerate" width="200" />


## Try The Examples

We have provided an example workflow to help you get started with the Anthropic component library. Give it a try and see how you can create custom Anthropic components for your applications.

### Anthropic Example
Check out the anthropic_example.xircuits workflow. This example uses the AnthropicGenerate component to listen for specific prompts and generates customized responses based on the detected keywords in a conversation.

## Installation
To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the Anthropic library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install anthropic
```
You can also do it manually by cloning and installing it:
```
# base Xircuits directory
git clone https://github.com/XpressAI/xai-anthropic xai_components/xai_anthropic
pip install -r xai_components/xai_anthropic/requirements.txt 
```
