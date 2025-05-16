# Custom Project Documentation AI

This tool creates a custom AI model trained on your project's documentation, allowing you to query and discuss project-specific details. The AI will respond to questions based on your documentation and indicate when queries are outside the project's scope.

## Prerequisites

- Python 3.8 or higher
- A Linux-based system
- Project documentation in Markdown format (.md files)

## Setup

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your HuggingFace API token:
   ```
   HUGGINGFACE_API_TOKEN=your_token_here
   ```

4. Place your project's markdown documentation files in a `docs` directory:
   ```bash
   mkdir docs
   # Copy your .md files into the docs directory
   ```

## Usage

1. Run the training script:
   ```bash
   python train_model.py
   ```

2. Once training is complete, you can start asking questions about your project.

3. The AI will:
   - Answer questions based on your documentation
   - Indicate when a question is outside the project's scope
   - Provide relevant information from your documentation

## Notes

- The model uses HuggingFace's FLAN-T5 base model for generating responses
- Documentation is processed and stored in a vector database for efficient retrieval
- The system uses semantic search to find relevant documentation sections
- All responses are based solely on the provided documentation

## Customization

You can modify the following parameters in `train_model.py`:
- Chunk size for document splitting (default: 1000)
- Chunk overlap (default: 200)
- Model temperature (default: 0.5)
- Maximum response length (default: 512)

## Troubleshooting

If you encounter any issues:
1. Ensure all documentation files are in proper Markdown format
2. Verify that the `docs` directory contains your documentation files
3. Check that your HuggingFace API token is correctly set in the `.env` file
4. Make sure you have sufficient system resources for training