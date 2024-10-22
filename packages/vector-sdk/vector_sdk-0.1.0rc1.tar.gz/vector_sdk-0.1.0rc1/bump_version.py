import re
import sys
from pathlib import Path

VERSION_FILES = [
    Path("pyproject.toml"),
    Path("src/vector_sdk/__init__.py")
]

def read_version():
    with open(VERSION_FILES[0], 'r') as f:
        content = f.read()
    match = re.search(r'version\s*=\s*["\'](.+?)["\']', content)
    if not match:
        raise ValueError(f"Version not found in {VERSION_FILES[0]}")
    return match.group(1)

def update_version(new_version):
    for file_path in VERSION_FILES:
        with open(file_path, 'r') as f:
            content = f.read()
        if file_path.name == 'pyproject.toml':
            pattern = r'(version\s*=\s*["\'])(.+?)(["\'])'
        elif file_path.name == '__init__.py':
            pattern = r'(__version__\s*=\s*["\'])(.+?)(["\'])'
        else:
            continue  # Skip files we don't know how to handle
        updated_content = re.sub(pattern, r'\g<1>' + new_version + r'\g<3>', content)
        with open(file_path, 'w') as f:
            f.write(updated_content)

def bump_version(bump_type):
    current_version = read_version()
    version_parts = current_version.split('.')

    if bump_type == 'major':
        new_version = f"{int(version_parts[0]) + 1}.0.0"
    elif bump_type == 'minor':
        new_version = f"{version_parts[0]}.{int(version_parts[1]) + 1}.0"
    elif bump_type == 'patch':
        new_version = f"{version_parts[0]}.{version_parts[1]}.{int(version_parts[2].split('rc')[0]) + 1}"
    elif bump_type == 'rc':
        rc_part = version_parts[2].split('rc')
        if len(rc_part) == 1:
            new_version = f"{version_parts[0]}.{version_parts[1]}.{rc_part[0]}rc1"
        else:
            new_version = f"{version_parts[0]}.{version_parts[1]}.{rc_part[0]}rc{int(rc_part[1]) + 1}"
    elif bump_type == 'release':
        new_version = f"{version_parts[0]}.{version_parts[1]}.{version_parts[2].split('rc')[0]}"
    else:
        raise ValueError("Invalid bump type. Use 'major', 'minor', 'patch', 'rc', or 'release'.")

    update_version(new_version)
    print(f"Version bumped from {current_version} to {new_version}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bump_version.py <major|minor|patch|rc|release>")
        sys.exit(1)

    bump_type = sys.argv[1]
    bump_version(bump_type)