# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [ pkgs.python3
               pkgs.poetry
               pkgs.python311Packages.uvicorn ];
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" "rangav.vscode-thunder-client"  "KnisterPeter.vscode-github" "ms-python.debugpy"];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        # install = "python -m venv .venv && curl -sSL https://install.python-poetry.org | python -";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
      # Runs when a workspace is (re)started
      onStart = { run-server = "./devserver.sh"; };
    };
  };
}
