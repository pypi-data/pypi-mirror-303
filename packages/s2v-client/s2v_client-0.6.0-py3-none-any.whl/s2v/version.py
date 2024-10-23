__version = "v0.6.0"

version: str = "v0.0.0" if __version == "{{STABLE_GIT_DESCRIPTION}}" else __version
