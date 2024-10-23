param(
    [Parameter(Mandatory=$true)]
    [string]$version_type
)

# Get current branch name
$current_branch = git rev-parse --abbrev-ref HEAD

# Run the bump version script
python bump_version.py $version_type

# Get the new version from pyproject.toml
$version = (Select-String -Path "pyproject.toml" -Pattern 'version = "(.*?)"').Matches.Groups[1].Value

# Check if this is a pre-release (contains 'rc')
$isPrerelease = $version -match "rc"

# Create a git tag
git add .
git commit -m "Bump version to $version"
git tag -a "v$version" -m "Release version $version"
git push origin $current_branch --tags

# Create a GitHub release with prerelease flag if it's an RC
if ($isPrerelease) {
    gh release create "v$version" --prerelease --title "Pre-release v$version" --notes "Release candidate version $version"
} else {
    gh release create "v$version" --title "Release v$version" --notes "Release version $version"
}