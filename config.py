# Configuration settings for the custom AI model

# Document processing settings
DOC_SETTINGS = {
    'chunk_size': 1000,  # Size of text chunks for processing
    'chunk_overlap': 200,  # Overlap between chunks to maintain context
    'encoding': 'utf-8'  # Default encoding for reading files
}

# Model settings
MODEL_SETTINGS = {
    'model_name': 'google/flan-t5-base',  # Base model to use
    'temperature': 0.5,  # Controls randomness in generation (0.0-1.0)
    'max_length': 512,  # Maximum length of generated responses
    'top_p': 0.95,  # Nucleus sampling parameter
    'top_k': 50  # Top-k sampling parameter
}

# Vector store settings
VECTOR_STORE = {
    'similarity_metric': 'cosine',  # Similarity metric for vector search
    'k_neighbors': 4  # Number of nearest neighbors to consider
}

# Response settings
RESPONSE_SETTINGS = {
    'min_confidence_score': 0.7,  # Minimum confidence score for valid responses
    'max_context_length': 2000,  # Maximum context length for responses
    'out_of_scope_threshold': 0.4  # Threshold for determining out-of-scope questions
}