import fireducks.pandas as fd

from mysiar_data_flow.lib.FileType import FileType


def from_fireducks_2_file(df: fd.DataFrame, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            df.to_parquet(tmp_filename)
        case FileType.feather:
            df.to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def to_fireducks_from_file(tmp_filename: str, file_type: FileType) -> fd.DataFrame:
    match file_type:
        case FileType.parquet:
            return fd.read_parquet(tmp_filename)
        case FileType.feather:
            return fd.read_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")
