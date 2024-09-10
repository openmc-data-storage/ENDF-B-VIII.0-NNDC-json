
import openmc_data_to_json as odj
from pathlib import Path

odj.cross_section_h5_files_to_json_files(
    filenames = list(Path('nuclear_data/endfb-viii.0-hdf5/neutron').glob('*.h5')),
    output_dir = 'ENDF-B-VIII.0_json',
    library='ENDFB-8.0',
    index_filename='ENDFB-8.0_index.json',
    indent=None,
    temperature='294K',
)
