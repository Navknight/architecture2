podman run --rm -it --userns=keep-id \
    -v "$(pwd)":/workspace \
    -w /workspace \
    gcc7_builder
