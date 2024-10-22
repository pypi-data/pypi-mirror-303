import torch
import subprocess

_is_cuda_available_ = None
def is_cuda_available() -> bool:
    global _is_cuda_available_
    if _is_cuda_available_ is None:
        from torch.cuda import is_available as is_cuda_available_
        _is_cuda_available_ = is_cuda_available_
    return _is_cuda_available_()

def available_vram_nvidia_smi():
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=memory.total,memory.free', '--format=csv,noheader,nounits'],
            stdout=subprocess.PIPE,
            encoding='utf-8'
        )
        output = result.stdout.strip()
        total_mem, free_mem = map(int, output.split(','))
        return free_mem * 1024 * 1024, total_mem * 1024 * 1024  # Convert MB to bytes
    except FileNotFoundError:
        pass

    raise RuntimeError("nvidia-smi not found. Ensure NVIDIA drivers are installed.")

def available_vram_torch():
    if torch.cuda.is_available():
        torch.cuda.synchronize()
        total_mem = torch.cuda.get_device_properties(0).total_memory
        allocated_mem = torch.cuda.memory_allocated(0)  # Memory currently allocated by tensors
        reserved_mem = torch.cuda.memory_reserved(0)  # Memory reserved by the CUDA allocator
        free_mem = reserved_mem - allocated_mem  # Available memory from reserved pool
        return free_mem, total_mem
    else:
        raise RuntimeError("CUDA is not available.")
    
def get_available_vram():
    try:
        return available_vram_nvidia_smi()
    except Exception as ex:
        pass
    
    try:
        return available_vram_torch()
    except Exception as ex:
        pass
    
    raise RuntimeError("Coudlnt get available memory.")
