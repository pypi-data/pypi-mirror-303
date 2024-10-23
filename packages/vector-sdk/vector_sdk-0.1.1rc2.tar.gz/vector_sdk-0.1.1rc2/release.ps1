param(
    [Parameter(Mandatory=$true)]
    [string]$version_type
)

# Run the bump version script
python bump_version.py $version_type

# Get the new version from pyproject.toml
$version = (Select-String -Path "pyproject.toml" -Pattern 'version = "(.*?)"').Matches.Groups[1].Value

# Create a git tag
git add .
git commit -m "Bump version to $version"
git tag -a "v$version" -m "Release version $version"
git push origin main --tags

# Create a GitHub release
gh release create "v$version" --title "Release v$version" --notes "Release version $version"