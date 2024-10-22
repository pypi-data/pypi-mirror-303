import os
import tempfile
from typing import Any

import fireducks.pandas as fd
import pandas as pd
import polars as pl
from pyarrow import feather

from mysiar_data_flow.lib import FileType, Operator
from mysiar_data_flow.lib.data_columns import (
    data_get_columns,
    data_delete_columns,
    data_rename_columns,
    data_select_columns,
    data_filter_on_column,
)
from mysiar_data_flow.lib.data_from import (
    from_csv_2_file,
    from_feather_2_file,
    from_parquet_2_file,
    from_json_2_file,
    from_hdf_2_file,
)
from mysiar_data_flow.lib.data_to import (
    to_csv_from_file,
    to_feather_from_file,
    to_parquet_from_file,
    to_json_from_file,
    to_hdf_from_file,
)
from mysiar_data_flow.lib.fireducks import from_fireducks_2_file, to_fireducks_from_file
from mysiar_data_flow.lib.pandas import from_pandas_2_file
from mysiar_data_flow.lib.tools import generate_temporary_filename, delete_file


class DataFlow:
    class DataFrame:
        __in_memory: bool
        __file_type: FileType
        __data: fd.DataFrame = None
        __filename: str = None

        def __init__(self, in_memory: bool = True, file_type: FileType = FileType.parquet, tmp_file: str = None):
            self.__in_memory = in_memory
            self.__file_type = file_type
            if not in_memory and tmp_file is not None:
                self.__filename = tmp_file
            if not in_memory and tmp_file is None:
                self.__filename = os.path.join(tempfile.gettempdir(), generate_temporary_filename(ext=file_type.name))

        def __del__(self):
            if not self.__in_memory:
                delete_file(self.__filename)

        def from_csv(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.read_csv(filename)
            else:
                from_csv_2_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_feather(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.from_pandas(feather.read_feather(filename))
            else:
                from_feather_2_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_fireducks(self, df: fd.DataFrame) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = df
            else:
                from_fireducks_2_file(df=df, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_hdf(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.read_hdf(filename)
            else:
                from_hdf_2_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_json(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.read_json(filename)
            else:
                from_json_2_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_pandas(self, df: pd.DataFrame) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.from_pandas(df)
            else:
                from_pandas_2_file(df=df, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_parquet(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.read_parquet(filename)
            else:
                from_parquet_2_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def from_polars(self, df: pl.DataFrame) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data = fd.from_pandas(df.to_pandas())
            else:
                from_pandas_2_file(df=df.to_pandas(), tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def to_csv(self, filename: str, index=False) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data.to_csv(filename, index=index)
            else:
                to_csv_from_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def to_feather(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data.to_feather(filename)
            else:
                to_feather_from_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def to_fireducks(self) -> fd.DataFrame:
            if self.__in_memory:
                return self.__data
            else:
                return to_fireducks_from_file(tmp_filename=self.__filename, file_type=self.__file_type)

        def to_hdf(self, filename: str, key: str = "key") -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data.to_hdf(path_or_buf=filename, key=key)
            else:
                to_hdf_from_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type, key=key)
            return self

        def to_json(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data.to_json(filename)
            else:
                to_json_from_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def to_pandas(self) -> pd.DataFrame:
            if self.__in_memory:
                return self.__data.to_pandas()
            else:
                return to_fireducks_from_file(tmp_filename=self.__filename, file_type=self.__file_type).to_pandas()

        def to_parquet(self, filename: str) -> "DataFlow.DataFrame":
            if self.__in_memory:
                self.__data.to_parquet(filename)
            else:
                to_parquet_from_file(filename=filename, tmp_filename=self.__filename, file_type=self.__file_type)
            return self

        def to_polars(self) -> pl.DataFrame:
            if self.__in_memory:
                return pl.from_pandas(self.__data.to_pandas())
            else:
                return pl.from_pandas(
                    to_fireducks_from_file(tmp_filename=self.__filename, file_type=self.__file_type).to_pandas()
                )

        def columns(self) -> list:
            """
            lists columns in data frame

            :return: list - list of columns in data frame
            """
            if self.__in_memory:
                return self.__data.columns.to_list()
            else:
                return data_get_columns(tmp_filename=self.__filename, file_type=self.__file_type)

        def columns_delete(self, columns: list) -> "DataFlow.DataFrame":
            """
            deletes columns from data frame

            :param columns: list - list of columns to delete
            :return: self
            """
            if self.__in_memory:
                self.__data.drop(columns=columns, inplace=True)
            else:
                data_delete_columns(tmp_filename=self.__filename, file_type=self.__file_type, columns=columns)

            return self

        def columns_rename(self, columns_mapping: dict) -> "DataFlow.DataFrame":
            """
            rename columns

            :param columns_mapping: dict - old_name: new_name pairs ex. {"Year": "year", "Units": "units"}
            :return: self
            """
            if self.__in_memory:
                self.__data.rename(columns=columns_mapping, inplace=True)
            else:
                data_rename_columns(
                    tmp_filename=self.__filename,
                    file_type=self.__file_type,
                    columns_mapping=columns_mapping,
                )
            return self

        def columns_select(self, columns: list) -> "DataFlow.DataFrame":
            """
            columns select - columns to keep in data frame

            :param columns: list - list of columns to select
            :return: self
            """
            if self.__in_memory:
                self.__data = self.__data[columns]
            else:
                data_select_columns(tmp_filename=self.__filename, file_type=self.__file_type, columns=columns)
            return self

        def filter_on_column(self, column: str, value: Any, operator: Operator) -> "DataFlow.DataFrame":
            """
            filters data on column

            :param column: str - column name
            :param value: Any - value
            :param operator: mysiar_data_flow.lib.Operator - filter operator
            :return: self
            """
            if self.__in_memory:
                match operator:
                    case Operator.Eq:
                        self.__data = self.__data[self.__data[column] == value]
                    case Operator.Gte:
                        self.__data = self.__data[self.__data[column] >= value]
                    case Operator.Lte:
                        self.__data = self.__data[self.__data[column] <= value]
                    case Operator.Gt:
                        self.__data = self.__data[self.__data[column] > value]
                    case Operator.Lt:
                        self.__data = self.__data[self.__data[column] < value]
                    case Operator.Ne:
                        self.__data = self.__data[self.__data[column] != value]
            else:
                data_filter_on_column(
                    tmp_filename=self.__filename,
                    file_type=self.__file_type,
                    column=column,
                    value=value,
                    operator=operator,
                )
            return self
