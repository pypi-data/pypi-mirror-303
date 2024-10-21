{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    naersk.url = "github:nix-community/naersk";
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = {
    self,
    flake-utils,
    naersk,
    nixpkgs,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = (import nixpkgs) {
          inherit system;
        };

        naersk' = pkgs.callPackage naersk {};

        # List of libraries to include in LD_LIBRARY_PATH
        libraries = with pkgs; [
          xorg.libX11
          libxkbcommon
          xorg.libXi
          stdenv.cc.cc.lib
          freetype
        ];

        # Build the LD_LIBRARY_PATH by concatenating the lib paths
        ld_library_path = builtins.concatStringsSep ":" (map (lib: "${lib}/lib") libraries);
      in rec {
        # For `nix build` & `nix run`:
        defaultPackage = naersk'.buildPackage {
          src = ./.;
        };

        # For `nix develop`:
        devShell = pkgs.mkShell {
          nativeBuildInputs = with pkgs; [
            rustc
            pkg-config
            cargo
            alsaLib
            xorg.libX11
            udev
            xorg.libXi
            libxkbcommon
            openssl
            openssl.dev
            awscli2
            python312Full
            python312Packages.uv
            python312Packages.tkinter
          ];

          PKG_CONFIG_PATH = "${pkgs.openssl.dev}/lib/pkgconfig";

          shellHook = ''
            export RUST_BACKTRACE=1
            export WINIT_UNIX_BACKEND=wayland
            export OPENSSL_DIR="${pkgs.openssl.out}"
            export OPENSSL_INCLUDE_DIR=$OPENSSL_DIR/include
            export OPENSSL_LIB_DIR=$OPENSSL_DIR/lib/pkgconfig
            export LD_LIBRARY_PATH=${ld_library_path}:$LD_LIBRARY_PATH
            exec fish
          '';
        };
      }
    );
}
