{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    fenix = {
      url = "github:nix-community/fenix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    nixpkgs,
    fenix,
    ...
  }: let
    systems = ["x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin"];
    eachSystem = systems: f: let
      op = attrs: system: let
        ret = f system;
        op = attrs: key:
          attrs
          // {
            ${key} =
              (attrs.${key} or {})
              // {${system} = ret.${key};};
          };
      in
        builtins.foldl' op attrs (builtins.attrNames ret);
    in
      builtins.foldl' op {} systems;
  in
    eachSystem systems (system: let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [fenix.overlays.default];
      };
      toolchain = pkgs.fenix.default.withComponents [
        "cargo"
        "clippy"
        "rustc"
        "rustfmt"
      ];
    in rec {
      packages.default = pkgs.python3Packages.buildPythonPackage rec {
        pname = "cimulate";
        version = "0.1.2";
        pyproject = true;
        src = ./.;

        nativeBuildInputs = with pkgs; [
          toolchain
          rustPlatform.cargoSetupHook
          python3Packages.setuptools
          python3Packages.setuptools-scm
          python3Packages.setuptools-rust
        ];

        cargoDeps = pkgs.rustPlatform.fetchCargoTarball {
          src = ./.;
          name = "${pname}-${version}";
          hash = "sha256-4PQTYbyYPGdaTIGXTDeRIWMZv8ja92TQPNfK/34HFEw=";
        };
      };

      devShells.default = pkgs.mkShell {
        packages = with pkgs; [
          (python3.withPackages (p: [
            packages.default
            p.build
            p.twine
            p.pip
            p.pytest
            p.pdoc
            p.matplotlib
            p.numpy
          ]))
          ruff
          toolchain
          rust-analyzer-nightly
        ];
      };
    });
}
