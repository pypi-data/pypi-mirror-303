import fireducks.pandas as fd
from pyarrow import feather

from mysiar_data_flow.lib.FileType import FileType


def from_csv_2_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_csv(filename).to_parquet(tmp_filename)
        case FileType.feather:
            fd.read_csv(filename).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def from_feather_2_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.from_pandas(feather.read_feather(filename)).to_parquet(tmp_filename)
        case FileType.feather:
            fd.from_pandas(feather.read_feather(filename)).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def from_parquet_2_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(filename).to_parquet(tmp_filename)
        case FileType.feather:
            fd.read_parquet(filename).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def from_json_2_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_json(filename).to_parquet(tmp_filename)
        case FileType.feather:
            fd.read_json(filename).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def from_hdf_2_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_hdf(filename).to_parquet(tmp_filename)
        case FileType.feather:
            fd.read_hdf(filename).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")
