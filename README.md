# langchain_playGround

Welcome to the `langchain_playGround` repository! This repository is a collection of experiments and examples built using LangChain, a powerful framework for developing applications with large language models (LLMs).

## Overview

The goal of this repository is to explore different use cases of LangChain and showcase how LLMs can be integrated into applications for tasks like conversation history management, prompt chaining, parallel execution, and much more.

The two main components in this repository are:

1. **Chat History Management with LangChain:**
   - A persistent chat history feature using a JSON file to store and retrieve conversation messages. This allows for more natural interactions with the model as it "remembers" past exchanges.
2. **Code and Test Generation:**
   - A prompt-based tool that generates short code snippets in the specified language based on a task description and generates tests for the generated code.

## Features

- **Persistent Chat History:**  
  The `JSONChatMessageHistory` class manages chat history across sessions using a JSON file. This allows users to interact with a LangChain model while maintaining state across different conversational turns.

- **Code Generation and Testing:**  
  A simple CLI tool that generates code based on user input. The tool writes a function for a specified task, creates a test for the function, and prints the results.

- **Flexible Prompt Templates:**  
  Utilizes LangChain’s `PromptTemplate` to dynamically generate prompts for different tasks, such as code generation or test creation.

- **Parallel Execution of Tasks:**  
  The repository demonstrates parallel task execution using LangChain's `RunnableParallel`, which allows running multiple tasks simultaneously (e.g., generating code and writing tests in parallel).

## Requirements

- Python 3.7+
- LangChain (`pip install langchain`)
- OpenAI API key (for using the `ChatOpenAI` model)

You can also set up environment variables using a `.env` file for your OpenAI API key.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/********
   cd langchain_playGround
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the examples:
   ```bash
   python chat_with_history.py
   python generate_code_and_test.py --task "print the first 10 numbers" --language python
   ```

## Example Usage

### Chat with History Example:

This script demonstrates maintaining a conversation with the AI across multiple turns, where the context is preserved throughout the session.

### Code and Test Generation Example:

This script takes a description of a task and generates a code snippet in the specified language. It also generates a test for the generated code.

## Contributing

Feel free to fork the repository, submit issues, and contribute via pull requests. Suggestions and improvements are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
