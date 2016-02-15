with import <nixpkgs> {};

(python.buildEnv.override {
  extraLibs = with pythonPackages;
    [ pyyaml
    ];
}).env
