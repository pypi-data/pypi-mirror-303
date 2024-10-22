import fireducks.pandas as fd
import pandas as pd

from mysiar_data_flow.lib.FileType import FileType


def from_pandas_2_file(df: pd.DataFrame, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.from_pandas(df).to_parquet(tmp_filename)
        case FileType.feather:
            fd.from_pandas(df).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")
