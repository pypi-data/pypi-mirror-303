###############################################################################
# (c) Copyright 2024 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
import argparse
import re
import sys
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from .cli_utils import log_error, log_info, log_warn  # type: ignore
from .options import Options

SUMMARY_XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<summary xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" xsi:noNamespaceSchemaLocation="$XMLSUMMARYBASEROOT/xml/XMLSummary.xsd">
    <success>True</success>
    <step>finalize</step>
    <usage><stat unit="KB" useOf="MemoryMaximum">0</stat></usage>
    <input>
{input_files}
    </input>
    <output>
{output_files}
    </output>
</summary>
"""
XML_FILE_TEMPLATE = '     <file GUID="" name="{name}" status="full">{n}</file>'


def read_xml_file_catalog(xml_file_catalog):
    """Lookup the LFN->PFN mapping from the XML file catalog."""
    if xml_file_catalog is None:
        return {}

    tree = ET.parse(xml_file_catalog)
    pfn_lookup: dict[str, list[str]] = {}  # type: ignore
    for file in tree.findall("./File"):
        lfns = [x.attrib.get("name") for x in file.findall("./logical/lfn")]
        pfns = [x.attrib.get("name") for x in file.findall("./physical/pfn")]
        if len(lfns) > 1:
            raise NotImplementedError(lfns)
        if lfns:
            lfn = lfns[0]
        elif len(pfns) > 1:
            raise NotImplementedError(pfns)
        else:
            lfn = pfns[0]
        pfn_lookup[f"LFN:{lfn}"] = pfns
    return pfn_lookup


def resolve_input_files(input_files, file_catalog):
    """Resolve LFNs to PFNs using what was returned from read_xml_file_catalog."""
    resolved = []
    for input_file in input_files:
        if input_file.startswith("LFN:"):
            if input_file in file_catalog:
                print("Resolved", input_file, "to", file_catalog[input_file][0])
                input_file = file_catalog[input_file][0]
            else:
                raise ValueError(f"Could not resolve {input_file}: {file_catalog}")
        resolved.append(input_file)
    return resolved


def write_summary_xml(options, output_files: set[str]):
    summary_xml = SUMMARY_XML_TEMPLATE.format(
        input_files="\n".join(
            XML_FILE_TEMPLATE.format(
                name=name if name.startswith("LFN:") else f"PFN:{name}", n=1
            )
            for name in options.input_files
        ),
        output_files="\n".join(
            XML_FILE_TEMPLATE.format(
                # assume that every input file contributed to each output file
                name=f"PFN:{name}",
                n=len(options.input_files),
            )
            for name in output_files
        ),
    )
    if options.xml_summary_file:
        log_info(f"Writing XML summary to {options.xml_summary_file}")
        Path(options.xml_summary_file).write_text(summary_xml)


def get_output_filename(key, options, extra_opts):
    if not extra_opts.write:
        # check outputs
        yield options.output_file
    for mapstr in extra_opts.write or []:
        fn, rex = mapstr.split("=")
        if re.match(rex, key):
            yield fn


def skim_and_merge(options: Options, *extra_args):
    """Take given input files, merge specified object keys from them and write to a corresponding output file."""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--write",
        action="append",
        help="Write to given file name the tree(s) matching a regular expression . e.g. --write XICP.ROOT='Xic.*/DecayTree'",
    )
    parser.add_argument(
        "--lumi-tuple",
        default="(GetIntegratedLuminosity|lumiTree)",
        help="Regular expression to match key containing Luminosity information. Set to 'none' to ignore.",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Allow trees in the input file(s) to be missing from the output files.",
    )
    parser.add_argument(
        "--allow-duplicates",
        action="store_true",
        help="Allow trees in the input file(s) to be copied to more than one output file.",
    )

    extra_opts = parser.parse_args(extra_args)

    if options.n_threads > 1:
        raise NotImplementedError

    import ROOT  # type: ignore

    compression_level = None
    if options.compression:
        # pylint: disable=no-member
        algorithms = {
            "ZLIB": ROOT.RCompressionSetting.EAlgorithm.kZLIB,
            "ZSTD": ROOT.RCompressionSetting.EAlgorithm.kZSTD,
            "LZ4": ROOT.RCompressionSetting.EAlgorithm.kLZ4,
            "LZMA": ROOT.RCompressionSetting.EAlgorithm.kLZMA,
        }
        algo = options.compression.algorithm
        level = options.compression.level
        if algo not in algorithms:
            log_error(f"Unknown compression algorithm {algo}")
            sys.exit(1)
        compression_level = algorithms[algo] * 100 + int(level)
        log_info(f"Compression specified as {algo}:{level} ({compression_level})")

    input_files = options.input_files
    if options.xml_file_catalog:
        file_catalog = read_xml_file_catalog(options.xml_file_catalog)
        input_files = resolve_input_files(options.input_files, file_catalog)

    output_files: set = set()
    all_trees: set = set()
    tree_keys = defaultdict(set)
    lumi_tree_key = None
    for input_file in input_files:
        rf = ROOT.TFile.Open(input_file)  # pylint: disable=no-member
        for key in rf.GetListOfKeys():
            key_name = key.GetName()
            if re.match(extra_opts.lumi_tuple, key_name) is None:
                no_match = True
                for out_fn in get_output_filename(key_name, options, extra_opts):
                    no_match = False
                    tree_keys[out_fn].add(key_name)
                if no_match:  # FIXME can we do better?!
                    tree_keys[None].add(key_name)
            else:
                lumi_tree_key = key_name
            all_trees.add(key_name)

    if not lumi_tree_key and extra_opts.lumi_tuple != "none":
        log_error(
            f"Luminosity info directory {extra_opts.lumi_tuple} was not found in any input file."
        )
        sys.exit(1)

    # check for duplication
    for tree_name in all_trees:
        found = 0
        for trees in tree_keys.values():
            if tree_name in trees:
                found += 1
            if found > 1 and not extra_opts.allow_duplicates:
                log_error(
                    f"Duplicates of directory {tree_name} across more than one file. Set --allow-duplicates if this is intended."
                )
                sys.exit(1)

    for stream, tree_names in tree_keys.items():
        if stream is None:
            for tree_name in tree_names:
                log_warn(f"Tree {tree_name} is missing from output file(s).")
            if extra_opts.allow_missing:
                continue
            log_error(
                "Some directories of the input files would not be copied to any output files. Set --allow-missing if this is intended."
            )
            sys.exit(1)

        op_time = time.time()
        merger = ROOT.TFileMerger(False, True)  # pylint: disable=no-member
        merger.SetPrintLevel(2)
        if options.compression:
            merger.SetFastMethod(not options.compression.optimise_baskets)

        for input_file in input_files:
            if not merger.AddFile(input_file):
                log_error(f"Couldn't add input file to merger: {input_file}")
                sys.exit(1)

        for tree_name in tree_names:
            log_info(
                f"SKIM directory {tree_name} FROM {len(input_files)} files ---> {options.get_output_file(stream)}"
            )
            merger.AddObjectNames(tree_name)
        log_info(
            f"SKIM directory {lumi_tree_key} FROM {len(input_files)} files ---> {options.get_output_file(stream)}"
        )
        merger.AddObjectNames(lumi_tree_key)

        merge_opts = (
            ROOT.TFileMerger.kAll  # pylint: disable=no-member
            | ROOT.TFileMerger.kOnlyListed  # pylint: disable=no-member
            | ROOT.TFileMerger.kIncremental  # pylint: disable=no-member
        )

        if compression_level:
            merger.OutputFile(
                options.get_output_file(stream),
                "RECREATE",
                compression_level,
            )
        else:
            # merge_opts |= ROOT.TFileMerger.kKeepCompression
            merger.OutputFile(options.get_output_file(stream), "RECREATE")
        output_files.add(options.get_output_file(stream))
        if not merger.PartialMerge(merge_opts):
            log_error("TFileMerger says: merging failed!")
            sys.exit(1)
        log_info(f"    ... took {time.time() - op_time:.1f} seconds")
    write_summary_xml(options, output_files)
    return options
