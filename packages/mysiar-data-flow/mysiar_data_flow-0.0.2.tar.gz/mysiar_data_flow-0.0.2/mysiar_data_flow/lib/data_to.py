import fireducks.pandas as fd

from mysiar_data_flow.lib.FileType import FileType


def to_csv_from_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(tmp_filename).to_csv(filename)
        case FileType.feather:
            fd.read_feather(tmp_filename).to_csv(filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def to_feather_from_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(tmp_filename).to_feather(filename)
        case FileType.feather:
            fd.read_feather(tmp_filename).to_feather(filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def to_parquet_from_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(tmp_filename).to_parquet(filename)
        case FileType.feather:
            fd.read_feather(tmp_filename).to_parquet(filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def to_json_from_file(filename: str, tmp_filename: str, file_type: FileType) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(tmp_filename).to_json(filename)
        case FileType.feather:
            fd.read_feather(tmp_filename).to_json(filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def to_hdf_from_file(filename: str, tmp_filename: str, file_type: FileType, key: str = "key") -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(tmp_filename).to_hdf(path_or_buf=filename, key=key)
        case FileType.feather:
            fd.read_feather(tmp_filename).to_hdf(path_or_buf=filename, key=key)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")
