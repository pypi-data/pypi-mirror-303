import os
import sys
import argparse
import subprocess
from pynput.keyboard import Listener
import time

print("\033[032m", end="")

def pause(func="sys.exit"):
    """Pause the execution and wait for a key press."""
    def on_press(*args):
        if callable(func):
            func()
        else:
            sys.exit()

    with Listener(on_press=on_press) as L:
        L.join()

def load_keywords(file_path):
    """Load keywords from a specified text file."""
    try:
        with open(file_path, 'r') as f:
            return {line.strip() for line in f if line.strip()}  # Return a set of keywords
    except FileNotFoundError:
        print(f"Keyword file not found: {file_path}. Please ensure it exists.")
        pause(sys.exit)
    except Exception as e:
        print(f"Error loading keywords: {e}")
        pause(sys.exit)

def changeBracks(line):
    """Change braces to colons in the given line."""
    while '{' in line:
        bracIndex = line.index("{")
        line = line[:bracIndex] + ":" + line[bracIndex + 1:]
        while bracIndex > 0 and line[bracIndex - 1] == " ":
            line = line[:bracIndex - 1] + line[bracIndex:]
    while '}' in line:
        bracIndex = line.index("}")
        line = line[:bracIndex] + line[bracIndex + 1:]
        while bracIndex < len(line) and line[bracIndex] == " ":
            line = line[:bracIndex] + line[bracIndex + 1:]
    return line

def get_file_path(file_name):
    """Get the absolute file path."""
    if not file_name.endswith(".by"):
        print("Please provide a file with the '.by' extension.")
        print("Press Enter to exit...")
        pause()

    if os.path.basename(file_name) == file_name:
        return os.path.join(os.getcwd(), file_name)
    return file_name

def read_code(code, keywords):
    """Read and process the code, converting braces to colons as needed."""
    processed_code = ''
    firstBrac = 0
    
    for line in code.splitlines():
        is_dict = (line.count('=') == 1) and ("{" in line)

        if any(line.lstrip().startswith(keyword) for keyword in keywords):
            processed_code += f"{changeBracks(line)}\n"
            continue

        
        if is_dict:
            if "{" in line and "}" not in line:
                firstBrac += 1
            processed_code += f"{line}\n"
            continue

        if firstBrac and "}" in line:
            processed_code += f"{line}\n"
            firstBrac -= 1
            continue
        
        processed_code += changeBracks(line) + "\n"
    
    return processed_code

def read_file(file_path):
    """Read the content of a file."""
    try:
        with open(file_path, 'r') as code_file:
            return code_file.read()
    except FileNotFoundError:
        print("File not found!")
        pause()
    except Exception as e:
        print(f"An error occurred: {e}")
        pause()

def execute(code, file_name, keep_file):
    """Execute the processed code."""
    base_name = os.path.splitext(file_name)[0] + ".py"
    
    if os.path.exists(base_name):
        os.remove(base_name)

    with open(base_name, 'w') as file:
        file.write(f"import sys\n__exe__ = sys.executable\n\n{code}")

    start = time.time()
    result = os.system(f"python {base_name}")
    end = time.time()
    
    timeElapsed = (end - start) * 1000
    
    if not keep_file:
        os.remove(base_name)

    print("------------")
    print("Exit code:", result)
    print(f"Elapsed time: {timeElapsed:.2f} ms")

def translate_only(code, file_name):
    """Translate the code and save it to a file."""
    base_name = os.path.splitext(file_name)[0] + ".py"
    
    if os.path.exists(base_name):
        os.remove(base_name)
    
    with open(base_name, 'w') as file:
        file.write(code)
    
    print(f"Translated file saved as: {base_name}")
    pause()

def main():
    """Main function to handle command line arguments and processing."""
    parser = argparse.ArgumentParser(description="Translate and optionally execute a file.")
    parser.add_argument('file', type=str, help='Path to the file to be processed.')
    parser.add_argument('--keep', action='store_true', help='Keep the translated file after execution.')
    parser.add_argument('--translate-only', action='store_true', help='Only translate the file without executing it.')
    args = parser.parse_args()

    file_path = get_file_path(args.file)
    code = read_file(file_path)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    keyword_file_path = os.path.join(script_dir, 'data', 'keywords.txt')

    keywords = load_keywords(keyword_file_path)

    processed_code = read_code(code, keywords)

    if args.translate_only:
        translate_only(processed_code, file_path)
    else:
        execute(processed_code, file_path, args.keep)

if __name__ == '__main__':
    main()
    pause(sys.exit)
