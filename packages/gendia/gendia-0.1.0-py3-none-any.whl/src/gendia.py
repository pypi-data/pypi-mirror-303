import os
import argparse

# ANSI escape codes for coloring
COLOR_BLUE = '\033[94m'  # Blue for directories
COLOR_GREEN = '\033[92m'  # Green for Python files
COLOR_YELLOW = '\033[93m'  # Yellow for compiled Python files
COLOR_RESET = '\033[0m'  # Reset to default color
COLOR_ORANGE = '\033[33m'  # Orange for JavaScript files
COLOR_RED = '\033[31m'  # Red for C files
COLOR_LIGHT_BLUE = '\033[36m'  # Light blue for C++ files
COLOR_PURPLE = '\033[35m'  # Purple for Java files
COLOR_PINK = '\033[95m'  # Pink for Ruby files
COLOR_WHITE = '\033[97m'  # White for text files
COLOR_GRAY = '\033[90m'  # Gray for other files
COLOR_MAGENTA = '\033[95m'  # Magenta for image files
COLOR_CYAN = '\033[96m'  # Cyan for audio files
COLOR_LIGHT_GREEN = '\033[92m'  # Light green for video files
COLOR_LIGHT_YELLOW = '\033[93m'  # Light yellow for compressed files
COLOR_LIGHT_RED = '\033[91m'  # Light red for executable files
COLOR_LIGHT_PURPLE = '\033[95m'  # Light purple for library directories


def get_color(entry):
    """Returns color based on file type."""
    if os.path.isdir(entry):
        return COLOR_BLUE
    elif entry.endswith('.py'):
        return COLOR_GREEN
    elif entry.endswith('.pyc'):
        return COLOR_YELLOW
    elif entry.endswith('.js'):
        return COLOR_ORANGE
    elif entry.endswith('.c'):
        return COLOR_RED
    elif entry.endswith('.cpp'):
        return COLOR_LIGHT_BLUE
    elif entry.endswith('.java'):
        return COLOR_PURPLE
    elif entry.endswith('.rb'):
        return COLOR_PINK
    elif entry.endswith('.txt'):
        return COLOR_WHITE
    elif entry.endswith('.jpg') or entry.endswith('.png') or entry.endswith('.gif'):
        return COLOR_MAGENTA
    elif entry.endswith('.mp3') or entry.endswith('.wav'):
        return COLOR_CYAN
    elif entry.endswith('.mp4') or entry.endswith('.avi') or entry.endswith('.mkv'):
        return COLOR_LIGHT_GREEN
    elif entry.endswith('.zip') or entry.endswith('.tar') or entry.endswith('.gz'):
        return COLOR_LIGHT_YELLOW
    elif entry.endswith('.exe'):
        return COLOR_LIGHT_RED
    elif os.path.islink(entry):
        return COLOR_GRAY
    else:
        return COLOR_RESET

def print_tree(directory, prefix=''):
    # List all entries in the directory, sorting them so that directories come first
    entries = sorted(os.listdir(directory), key=lambda x: (not os.path.isdir(os.path.join(directory, x)), x))

    for index, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = index == len(entries) - 1
        color = get_color(path)

        # Print the current item with the appropriate prefix
        if is_last:
            print(f"{prefix}└── {color}{entry}{COLOR_RESET}")
            new_prefix = f"{prefix}    "
        else:
            print(f"{prefix}├── {color}{entry}{COLOR_RESET}")
            new_prefix = f"{prefix}│   "

        # If the current item is a directory, recursively print its contents
        if os.path.isdir(path):
            print_tree(path, new_prefix)

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Display a color-coded tree-like directory structure")
    parser.add_argument('directory', type=str, help='The directory to display')
    args = parser.parse_args()

    # Get the absolute path of the directory and print the tree
    directory = os.path.abspath(args.directory)
    if os.path.isdir(directory):
        print(directory)
        print_tree(directory)
    else:
        print(f"{directory} is not a valid directory")

if __name__ == '__main__':
    main()
