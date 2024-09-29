from pathlib import Path

def create_directory(dir_name):
    current_dir = Path(__file__).resolve().parent.parent.parent
    output_dir = current_dir / dir_name
    output_dir.mkdir(exist_ok=True)
    return output_dir
