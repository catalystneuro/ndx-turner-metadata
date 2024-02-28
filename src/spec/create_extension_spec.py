# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec


def main():
    ns_builder = NWBNamespaceBuilder(
        name="""ndx-turner-metadata""",
        version="""0.1.0""",
        doc="""The NWB extension for storing Turner lab specific metadata""",
        author=["Szonja Weigl", "Ben Dichter"],
        contact=["ben.dichter@catalystneuro.com"],
    )

    ns_builder.include_type('LabMetaData', namespace='core')

    lab_meta_data_extension = NWBGroupSpec(
        doc="type for storing metadata for Turner lab",
        neurodata_type_def="TurnerLabMetaData",
        neurodata_type_inc="LabMetaData",
    )

    lab_meta_data_extension.add_attribute(
        name="MPTP_status",
        doc="Indicates whether the subject was treated with MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine; a chemical compound known to induce Parkinsonism) "
            "with values 'pre-MPTP' or 'post-MPTP', reflecting the treatment status of the subject.",
        dtype="text",
    )

    new_data_types = [lab_meta_data_extension]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "spec"))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
