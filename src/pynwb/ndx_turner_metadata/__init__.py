import os

from pynwb import load_namespaces, get_class

spec_path = os.path.abspath(os.path.dirname(__file__))
ns_path = os.path.join(spec_path, "spec", "ndx-turner-metadata.namespace.yaml")

load_namespaces(ns_path)
LabMetaDataExtension = get_class("LabMetaDataExtension", "ndx-turner-metadata")
