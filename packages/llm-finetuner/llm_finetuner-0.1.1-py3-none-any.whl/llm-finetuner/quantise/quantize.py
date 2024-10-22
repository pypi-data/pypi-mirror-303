import os
import subprocess
import logging
from config import *
from huggingface_hub import snapshot_download

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ensure_model_files(repo_id, local_dir):
    if not os.path.isdir(local_dir) or not os.path.isfile(f"{local_dir}/config.json"):
        logging.info(f"Model files not found locally. Downloading from {repo_id} to {local_dir}")
        snapshot_download(repo_id=repo_id, local_dir=local_dir, local_dir_use_symlinks=False)
    else:
        logging.info(f"Model files found locally at {local_dir}")

def quantize(model, outbase, outdir):
    if not os.path.isdir(model):
        raise FileNotFoundError(f"Could not find model dir at {model}")
    if not os.path.isfile(f"{model}/config.json"):
        raise FileNotFoundError(f"Could not find config.json in {model}")
    
    create_directory(outdir)
    fp16 = f"{outdir}/{outbase}.fp16.gguf"
    
    logging.info(f"Making unquantized GGUF at {fp16}")
    if not os.path.isfile(fp16):
        subprocess.run(f"python {LLAMA_CPP_DIR}/convert_hf_to_gguf.py {model} --outtype f16 --outfile {fp16} --batch-size {CONVERT_BATCH_SIZE}", shell=True, check=True)
    else:
        logging.info(f"Unquantized GGUF already exists at: {fp16}")
    
    logging.info("Making quants")
    for q_type in QUANT_TYPES:
        outfile = f"{outdir}/{outbase}.{q_type}.gguf"
        logging.info(f"Making {q_type} : {outfile}")
        cmd = f"{LLAMA_CPP_DIR}/llama-quantize -t {QUANT_THREADS} -c {CONTEXT_SIZE} {fp16} {outfile} {q_type}"
        if VERBOSE:
            cmd += " -v"
        subprocess.run(cmd, shell=True, check=True)
    
    if REMOVE_FP16:
        os.remove(fp16)

if __name__ == "__main__":
    setup_logging()
    try:
        print(WARNING_MESSAGE)
        ensure_model_files(INPUT_DIR, LOCAL_MODEL_DIR)
        quantize(LOCAL_MODEL_DIR, BASE_MODEL_NAME, OUTPUT_DIR)
    except Exception as e:
        logging.error(f"Quantization failed: {e}")