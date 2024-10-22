import os

# Model configurations
REPO_ID = "InshaM/my-mistral-seekh-qna"
REVISION = "main"
BASE_MODEL_NAME = "Llama-2-13B"
REMOVE_FP16 = True
LOCAL_MODEL_DIR = "../finetune_and_upload/InshaM/my-mistral-seekh-qna"
INPUT_DIR = "InshaM/my-mistral-seekh-qna"
OUTPUT_DIR = "quantized-v3"
LLAMA_CPP_DIR = "/home/ubuntu/llama.cpp"

# Quantization configurations
QUANT_TYPES = ["q4_0", "q4_1", "q5_0", "q5_1", "q8_0", "q2_K", "q3_K_S", "q3_K_M", "q3_K_L", "q4_K_S", "q4_K_M", "q5_K_S", "q5_K_M", "q6_K"]
QUANT_THREADS = 8
CONTEXT_SIZE = 2048
CONVERT_BATCH_SIZE = 512
VERBOSE = True

# Hugging Face configurations
HF_REPO_ID = 'InshaM/my-mistral-seekh-qna'
HF_TOKEN = os.getenv('HF_API_TOKEN')

# Model specifics
FINETUNING_TYPE = None  # or "lora" if applicable
MODEL_TYPE = "llama"  # or "mistral", "falcon", etc.

# Warning message
WARNING_MESSAGE = "WARNING: This script is designed to run on a system with 1x80GB A100 GPU. Ensure your system meets these requirements before proceeding."

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

# Create necessary directories
create_directory(INPUT_DIR)
create_directory(OUTPUT_DIR)

print("All necessary directories for quantization have been created.")