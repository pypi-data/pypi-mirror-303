"""Module with CMIP/CORDEX-like path and filename utilities."""

import pathlib
import re

from gordias.util import time_string

FREQUENCY_KEYWORDS = ["day"]
HISTORICAL_KEYWORDS = ["hist", "historical"]
SCENARIO_KEYWORDS = [r"rcp\d{2}", r"ssp\d{3}"]


def get_stem_base_part(path: pathlib.Path | str) -> str:
    """Get base part of filename stem.

    The base part of the stem is the CMIP/CORDEX-like filename
    stem without the first part, generally a variable name, and
    the last part, if the last part is a time range.

    Parameters
    ----------
    path : pathlib.Path | str
        Filename to get the stem base from.

    Returns
    -------
    str
        Stem base.
    """
    stem_parts = pathlib.Path(path).stem.split("_")
    if time_string.is_valid_time_range(stem_parts[-1]) or time_string.is_valid_time(
        stem_parts[-1]
    ):
        return "_".join(stem_parts[1:-1])
    else:
        return "_".join(stem_parts[1:])


def get_stem_time_range_part(path: pathlib.Path | str) -> str:
    """Get the time range part from a filename.

    Parameters
    ----------
    path : pathlib.Path
        Filename to get the stem time range from.

    Returns
    -------
    str
        Stem time range.
    """
    stem_parts = pathlib.Path(path).stem.split("_")
    if time_string.is_valid_time_range(stem_parts[-1]) or time_string.is_valid_time(
        stem_parts[-1]
    ):
        return stem_parts[-1]
    else:
        return ""


def get_stem_time_range(path: pathlib.Path | str) -> time_string.TimeRange:
    """Get the time range from a filename.

    Tries to extract a time range from the filename. If there is no time
    range, but only a single time, this function will still return a range,
    with the filename time as start and end.

    Parameters
    ----------
    path : pathlib.Path | str
        Filename to extract time range from.

    Returns
    -------
    time_string.TimeRange
        Extracted time range.

    Raises
    ------
    ValueError
        If a time range could not be extracted.
    """
    time_range_str = get_stem_time_range_part(path)
    try:
        return time_string.parse_time_range(time_range_str)
    except ValueError:
        try:
            start = time_string.parse_time(time_range_str)
            return time_string.TimeRange(start, start, False)
        except ValueError:
            raise ValueError("Filename stem does not include time range")


def _add_frequency_placeholder_to_stem(stem: str) -> str:
    """Add frequency placeholder to stem, or replace current frequency keyword.

    Adds frequency placeholder (`"_{frequency}"`) to the end of string,
    or, if a frequency keyword is discovered in the string, replaces
    the frequency keyword with the placeholder.

    Parameters
    ----------
    stem : str
        Filename stem string.

    Returns
    -------
    str
        Stem with frequency placeholder added at the end, or with frequency
        keyword replaced with frequency placeholder.
    """
    freq_re = re.compile(rf"_({'|'.join(FREQUENCY_KEYWORDS)})(?=_|$)")
    if freq_re.search(stem):
        stem = freq_re.sub("_{frequency}", stem)
    else:
        stem += "_{frequency}"
    return stem


def _stem_base_merger(stem_bases: list[str]) -> str:
    """Merge multiple stem bases into one.

    Helper function to merge multiple stem bases into one. In particular, it looks
    for different scenario keywords. If two different scenario keywords are found,
    and the corresponding stem bases are identical elsewhere, the resulting base
    will hold both scenario key words concatenated with a hyphen.
    For example,
    `["e1_historical_e3", "e1_rcp45_e3"]` will result in `"e1_historical-rcp45_e3"`.

    Parameters
    ----------
    stem_bases : list[str]
        List of stem bases to merge.

    Returns
    -------
    str | None
        Merged stem base, or empty string if merge failed.
    """
    unique_bases = set(stem_bases)
    if len(unique_bases) == 1:
        return unique_bases.pop()
    elif len(unique_bases) == 2:
        # Possible combination of historical and scenario data.
        hist_re = re.compile(rf"_({r'|'.join(HISTORICAL_KEYWORDS)})_")
        scen_re = re.compile(rf"_({r'|'.join(SCENARIO_KEYWORDS)})_")
        # Figure out which base is historical and which is scenario.
        hist_base = [b for b in unique_bases if hist_re.search(b)]
        scen_base = [b for b in unique_bases if scen_re.search(b)]
        if len(hist_base) == 1 and len(scen_base) == 1:
            hist_parts = hist_re.split(hist_base[0])
            scen_parts = scen_re.split(scen_base[0])
            if (
                len(hist_parts) == 3
                and len(scen_parts) == 3
                and hist_parts[0] == scen_parts[0]
                and hist_parts[2] == scen_parts[2]
            ):
                concat_keywords = hist_parts[1] + "-" + scen_parts[1]
                return f"{hist_parts[0]}_{concat_keywords}_{hist_parts[2]}"
    return ""


def build_cmip_like_filename_template(
    files: list[pathlib.Path] | list[str],
    include_time_range: bool = True,
    time_range_placeholder: bool = False,
) -> str:
    """
    Form a CMIP/CORDEX style filename template based on the given file names.

    A CMIP or CORDEX filename has a well-defined structure, adhering to the
    DRS (Data Reference Syntax) rules. This means that several of the data
    attributes are included in the filename. It generally starts with a
    variable name and, unless containing a dataset with no associated
    time dimension, also ends with a time range. In the case of CORDEX
    files, the frequency is also included in the filename.

    This function takes a number of filenames (or file paths) and tries
    to combine them into a single filename template, suitable for using as
    output filename when combining the files or storing the result of an
    analysis of the data in the files.

    For example, the two CORDEX-like filenames

    `tas_element1_element2_element3_day_19710101-19751231.nc`,
    `tas_element1_element2_element3_day_19760101-19801231.nc`

    can generate the following filename templates, depending on settings:

    `{var_name}_element1_element2_element3_{frequency}_19710101-19801231.nc`,
    `{var_name}_element1_element2_element3_{frequency}_{start}-{end}.nc`,
    `{var_name}_element1_element2_element3_{frequency}.nc`.

    Note that if the input filenames contains folder paths, those will be
    stripped in the returned filename template.

    The frequency placeholder will always be added
    to the template, even though in the case of CMIP-like filenames, the
    frequency generally is not included.

    If the input filenames represent both historical and scenario data,
    the corresponding attributes will be combined with a hyphen in the
    template, e.g. `historical` and `rcp45` will be combined into
    `historical-rcp45` in the filename template.

    If the code fails to create an unambiguous filename template, the template
    fallback `{var_name}_{frequency}.nc` will be returned.

    Parameters
    ----------
    files : list[pathlib.Path] | list[str]
        Input file names. Note: no wildcard expansion is run.
    include_time_range : bool, optional
        If True, time range will be included in the template.
        The time period of the template will always represent the whole period
        as covered by all files, given that the time periods can be parsed from
        the input filenames. Default True.
    time_range_placeholder : bool, optional
        If True, a time range placeholder will be added instead of extracting
        the time range from the input files, i.e. the template will end with
        `_{start}-{end}.nc`. Default False.

    Returns
    -------
    filename_template : str
        A format string suitable for use in the construction of an output
        filename.
    """
    files = [pathlib.Path(p) for p in files]
    stem_base = _stem_base_merger([get_stem_base_part(f) for f in files])
    if stem_base == "":
        return "{var_name}_{frequency}.nc"

    stem_base_with_freq = _add_frequency_placeholder_to_stem(stem_base)

    if not include_time_range:
        return f"{{var_name}}_{stem_base_with_freq}.nc"
    elif time_range_placeholder:
        return f"{{var_name}}_{stem_base_with_freq}_{{start}}-{{end}}.nc"
    else:
        try:
            stem_time_range_parts = [get_stem_time_range_part(f) for f in files]
            starts = [int(s.split("-")[0]) for s in stem_time_range_parts]
            ends = [int(s.split("-")[-1]) for s in stem_time_range_parts]
            start = str(min(starts))
            end = str(max(ends))
            return f"{{var_name}}_{stem_base_with_freq}_{start}-{end}.nc"

        except ValueError:
            return f"{{var_name}}_{stem_base_with_freq}.nc"
