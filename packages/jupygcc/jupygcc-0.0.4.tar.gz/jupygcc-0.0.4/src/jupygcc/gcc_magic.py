from IPython.core.magic import Magics, cell_magic, magics_class

from .utils import compile_run_c, handle_metadata


@magics_class
class GccMagic(Magics):
    @cell_magic
    def gcc(self, line, cell):
        """Compile and run C code using gcc."""
        metadata_dict, code = handle_metadata(cell)
        compile_run_c(code, metadata_dict)
