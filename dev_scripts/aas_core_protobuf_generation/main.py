"""Generate the Protobuf definitions for AAS meta-models."""

import argparse
import os
import pathlib
import sys

import aas_core_codegen.main
import aas_core_meta.v3


def module_basename(name: str) -> str:
    """
    Extract the last name in a qualified module name.

    >>> module_basename("aas_core_meta.v3")
    'v3'
    """
    return name.split(".")[-1]


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    this_path = pathlib.Path(os.path.realpath(__file__))

    for meta_model in [aas_core_meta.v3]:
        assert meta_model.__file__ is not None
        model_path = pathlib.Path(meta_model.__file__)
        meta_model_basename = module_basename(meta_model.__name__)

        print(f"Generating the definitions for meta-model: {meta_model_basename}")

        codegen_params = aas_core_codegen.main.Parameters(
            model_path=model_path,
            target=aas_core_codegen.main.Target.PROTOBUF,
            snippets_dir=this_path.parent.parent / "snippets" / meta_model_basename,
            output_dir=this_path.parent.parent.parent / meta_model_basename,
        )

        aas_core_codegen.main.execute(
            params=codegen_params, stdout=sys.stdout, stderr=sys.stderr
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
