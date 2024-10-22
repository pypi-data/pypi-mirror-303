from typing import Any

import fireducks.pandas as fd

from mysiar_data_flow.lib.FileType import FileType
from mysiar_data_flow.lib.Operator import Operator


def data_get_columns(tmp_filename: str, file_type: FileType) -> list:
    match file_type:
        case FileType.parquet:
            return fd.read_parquet(tmp_filename).columns.to_list()
        case FileType.feather:
            return fd.read_feather(tmp_filename).columns.to_list()
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def data_delete_columns(tmp_filename: str, file_type: FileType, columns: list) -> None:
    match file_type:
        case FileType.parquet:
            data = fd.read_parquet(tmp_filename)
            data.drop(columns=columns, inplace=True)
            data.to_parquet(tmp_filename)
        case FileType.feather:
            data = fd.read_feather(tmp_filename)
            data.drop(columns=columns, inplace=True)
            data.to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def data_rename_columns(tmp_filename: str, file_type: FileType, columns_mapping: dict) -> None:
    match file_type:
        case FileType.parquet:
            fd.read_parquet(tmp_filename).rename(columns=columns_mapping).to_parquet(tmp_filename)
        case FileType.feather:
            fd.read_feather(tmp_filename).rename(columns=columns_mapping).to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def data_select_columns(tmp_filename: str, file_type: FileType, columns: list) -> None:
    match file_type:
        case FileType.parquet:
            data = fd.read_parquet(tmp_filename)[columns]
            data.to_parquet(tmp_filename)
        case FileType.feather:
            data = fd.read_feather(tmp_filename)[columns]
            data.to_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")


def data_filter_on_column(tmp_filename: str, file_type: FileType, column: str, value: Any, operator: Operator) -> None:
    match file_type:
        case FileType.parquet:
            data = fd.read_parquet(tmp_filename)
        case FileType.feather:
            data = fd.read_feather(tmp_filename)
        case _:
            raise ValueError(f"File type not implemented: {file_type} !")

    match operator:
        case Operator.Eq:
            data = data[data[column] == value]
        case Operator.Gte:
            data = data[data[column] >= value]
        case Operator.Lte:
            data = data[data[column] <= value]
        case Operator.Gt:
            data = data[data[column] > value]
        case Operator.Lt:
            data = data[data[column] < value]
        case Operator.Ne:
            data = data[data[column] != value]

    match file_type:
        case FileType.parquet:
            data.to_parquet(tmp_filename)
        case FileType.feather:
            data.to_feather(tmp_filename)
