"""Version Management Script for Vector SDK

This script manages version numbers across the Vector SDK project files. It updates version numbers
in both pyproject.toml and __init__.py files consistently.

Usage:
    python bump_version.py <command> [version]

Commands:
    major     - Bump major version (X.y.z -> X+1.0.0)
    minor     - Bump minor version (x.Y.z -> x.Y+1.0)
    patch     - Bump patch version (x.y.Z -> x.y.Z+1)
    rc        - Bump/add release candidate (x.y.z -> x.y.zrc1 or x.y.zrcN -> x.y.zrcN+1)
    release   - Convert RC to release version (x.y.zrcN -> x.y.z)
    set       - Set to specific version (requires version argument)

Examples:
    # Bump major version (1.0.0 -> 2.0.0)
    python bump_version.py major

    # Bump minor version (1.1.0 -> 1.2.0)
    python bump_version.py minor

    # Create/bump release candidate (1.1.0 -> 1.1.0rc1 or 1.1.0rc1 -> 1.1.0rc2)
    python bump_version.py rc

    # Convert RC to release (1.1.0rc1 -> 1.1.0)
    python bump_version.py release

    # Set specific version
    python bump_version.py set 1.1.0

Files Modified:
    - pyproject.toml
    - src/vector_sdk/__init__.py

Version Format:
    - Must follow semantic versioning (X.Y.Z or X.Y.ZrcN)
    - X = Major version
    - Y = Minor version
    - Z = Patch version
    - rcN = Release candidate number (optional)

Notes:
    - Version numbers are synchronized across all project files
    - The script validates version format before making changes
    - Use 'set' command with caution as it allows direct version manipulation
"""

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

def parse_version(version_str):
    """Parse version string into parts."""
    parts = version_str.split('.')
    if len(parts) != 3:
        raise ValueError("Version must be in format X.Y.Z or X.Y.ZrcN")
    major, minor = int(parts[0]), int(parts[1])
    patch_parts = parts[2].split('rc')
    patch = int(patch_parts[0])
    rc = int(patch_parts[1]) if len(patch_parts) > 1 else None
    return major, minor, patch, rc

def bump_version(bump_type, target_version=None):
    current_version = read_version()
    
    if target_version:
        # Direct version setting
        try:
            parse_version(target_version)  # Validate format
            new_version = target_version
        except ValueError as e:
            raise ValueError(f"Invalid target version format: {e}")
    else:
        # Regular version bumping
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
            raise ValueError("Invalid bump type. Use 'major', 'minor', 'patch', 'rc', 'release', or 'set'")

    update_version(new_version)
    print(f"Version {'set' if target_version else 'bumped'} from {current_version} to {new_version}")

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python bump_version.py <major|minor|patch|rc|release>")
        print("   or: python bump_version.py set <version>")
        sys.exit(1)

    bump_type = sys.argv[1]
    if bump_type == 'set' and len(sys.argv) == 3:
        target_version = sys.argv[2]
        bump_version(bump_type, target_version)
    else:
        bump_version(bump_type)