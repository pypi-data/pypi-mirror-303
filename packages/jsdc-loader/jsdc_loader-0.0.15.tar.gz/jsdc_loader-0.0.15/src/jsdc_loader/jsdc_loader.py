from typing import Optional, get_args, get_type_hints, TypeVar, Any, get_origin, Union, TextIO
from enum import Enum
from dataclasses import dataclass, is_dataclass
import json

T = TypeVar('T', bound=dataclass)

def jsdc_load(fp: Union[str, TextIO], data_class: T, encoding: str = 'utf-8') -> T:
    """
    Deserialize a file-like object containing a JSON document to a Python dataclass object.

    :param fp: A .read()-supporting file-like object containing a JSON document
    :param data_class: The dataclass type to deserialize into
    :param encoding: The encoding to use when reading the file (if fp is a string)
    :return: An instance of the data_class
    """
    if isinstance(fp, str):
        with open(fp, 'r', encoding=encoding) as f:
            return jsdc_loads(f.read(), data_class)
    else:
        return jsdc_loads(fp.read(), data_class)

def jsdc_loads(s: str, data_class: T) -> T:
    """
    Deserialize a string containing a JSON document to a Python dataclass object.

    :param s: A string containing a JSON document
    :param data_class: The dataclass type to deserialize into
    :return: An instance of the data_class
    """
    def validate_dataclass(cls: Any) -> None:
        if not is_dataclass(cls):
            raise ValueError('data_class must be a dataclass')

    def convert_dict_to_dataclass(data: dict, cls: T) -> T:
        root_obj: T = cls()
        __dict_to_dataclass(root_obj, data)
        return root_obj

    def __dict_to_dataclass(c_obj: Any, c_data: dict) -> None:
        t_hints: dict = get_type_hints(type(c_obj))
        for key, value in c_data.items():
            if hasattr(c_obj, key):
                e_type = t_hints.get(key)
                if e_type is not None:
                    setattr(c_obj, key, convert_value(key, value, e_type))
            else:
                raise ValueError(f'Unknown data key: {key}')

    def convert_value(key: str, value: Any, e_type: Any) -> Any:
        if isinstance(e_type, type) and issubclass(e_type, Enum):
            return convert_enum(key, value, e_type)
        elif is_dataclass(e_type):
            return convert_dict_to_dataclass(value, e_type)
        elif get_origin(e_type) is list and is_dataclass(get_args(e_type)[0]):
            return convert_list_of_dataclasses(value, get_args(e_type)[0])
        else:
            return convert_other_types(key, value, e_type)

    def convert_enum(key: str, value: Any, enum_type: Any) -> Any:
        try:
            return enum_type[value]
        except KeyError:
            raise ValueError(f'Invalid Enum value for key {key}: {value}')

    def convert_list_of_dataclasses(value: list, item_type: Any) -> list:
        return [item_type(**item) for item in value]

    def convert_other_types(key: str, value: Any, e_type: Any) -> Any:
        try:
            origin = get_origin(e_type)
            if origin is Union:
                return convert_union_type(key, value, e_type)
            else:
                return convert_simple_type(key, value, e_type)
        except (ValueError, KeyError) as ex:
            raise ValueError(f'Invalid type for key {key}, expected {e_type}, got {type(value).__name__}') from ex

    def convert_union_type(key: str, value: Any, union_type: Any) -> Any:
        args = get_args(union_type)
        non_none_args = [arg for arg in args if arg is not type(None)]
        if len(non_none_args) == 1:
            actual_type = non_none_args[0]
            if isinstance(actual_type, type) and issubclass(actual_type, Enum):
                return actual_type[value]
            else:
                return actual_type(value)
        else:
            raise TypeError(f'Unsupported Union type for key {key}: {union_type}')

    def convert_simple_type(_: str, value: Any, e_type: Any) -> Any:
        if isinstance(e_type, type) and issubclass(e_type, Enum):
            return e_type[value]
        else:
            return e_type(value)

    data = json.loads(s)
    validate_dataclass(data_class)
    return convert_dict_to_dataclass(data, data_class)


def jsdc_dump(obj: T, output_path: str, encoding: str = 'utf-8', indent: int = 4) -> None:
    """Serialize a dataclass instance to a JSON file.

    This function takes a dataclass instance and writes its serialized 
    representation to a specified file in JSON format. The output file 
    can be encoded in a specified character encoding, and the JSON 
    output can be formatted with a specified indentation level.

    Args:
        obj (T): The dataclass instance to serialize.
        output_path (str): The path to the output file where the JSON 
                           data will be saved.
        encoding (str, optional): The character encoding to use for the 
                                  output file. Defaults to 'utf-8'.
        indent (int, optional): The number of spaces to use for indentation 
                                in the JSON output. Defaults to 4.

    Raises:
        ValueError: If the provided object is not a dataclass.
    """
    def save_json_file(file_path: str, data: dict, encoding: str, indent: int) -> None:
        with open(file_path, 'w', encoding=encoding) as f:
            json.dump(obj=data, fp=f, indent=indent)

    def validate_dataclass(cls: Any) -> None:
        if not is_dataclass(cls):
            raise ValueError('obj must be a dataclass')

    def convert_dataclass_to_dict(obj: Any) -> Any:
        if isinstance(obj, Enum):
            return obj.name
        elif isinstance(obj, list):
            return [convert_dataclass_to_dict(item) for item in obj]
        elif is_dataclass(obj):
            result = {}
            t_hints = get_type_hints(type(obj))
            for key, value in vars(obj).items():
                e_type = t_hints.get(key)
                if e_type is not None:
                    validate_type(key, value, e_type)
                result[key] = convert_dataclass_to_dict(value)
            return result
        return obj
        

    def validate_type(key: str, value: Any, e_type: Any) -> None:
        o_type = get_origin(e_type)
        if o_type is Union:
            if not any(isinstance(value, t) for t in get_args(e_type)):
                raise TypeError(f'Invalid type for key {key}: expected {e_type}, got {type(value)}')
        elif o_type is not None:
            if not isinstance(value, o_type):
                raise TypeError(f'Invalid type for key {key}: expected {o_type}, got {type(value)}')
        else:
            if not isinstance(value, e_type):
                raise TypeError(f'Invalid type for key {key}: expected {e_type}, got {type(value)}')

    validate_dataclass(obj)
    data_dict = convert_dataclass_to_dict(obj)
    save_json_file(output_path, data_dict, encoding, indent)



if __name__ == '__main__':
    from dataclasses import field
    from enum import auto
    @dataclass
    class DatabaseConfig:
        host: str = 'localhost'
        port: int = 3306
        user: str = 'root'
        password: str = 'password'
        ips: list[str] = field(default_factory=lambda: ['127.0.0.1'])
        primary_user: Optional[str] = field(default_factory=lambda: None)

    jsdc_dump(DatabaseConfig(), 'config.json')
    data = jsdc_load('config.json', DatabaseConfig)
    print(data.host)


    data = DatabaseConfig()
    jsdc_dump(data, 'config.json')

    loaded_data = jsdc_load('config.json', DatabaseConfig)
    print(loaded_data.host)

    @dataclass
    class UserType(Enum):
        ADMIN = auto()
        USER = auto()

    @dataclass
    class UserConfig:
        name: str = 'John Doe'
        age: int = 30
        married: bool = False
        user_type: UserType = field(default_factory=lambda: UserType.USER)

    @dataclass
    class AppConfig:
        user: UserConfig = field(default_factory=lambda: UserConfig())
        database: DatabaseConfig = field(default_factory=lambda: DatabaseConfig())

    app_data = AppConfig()
    jsdc_dump(app_data, 'config.json')

    loaded_app_data = jsdc_load('config.json', AppConfig)
    print(loaded_app_data.user.name)

    loaded_app_data.user.name = 'Jane Doe'
    jsdc_dump(loaded_app_data, 'config.json')
    print(loaded_app_data.user.name)

    @dataclass
    class ControllerConfig:
        controller_id: str = 'controller_01'
        controller_type: str = 'controller_type_01'
        controller_version: str = 'controller_version_01'
        utc_offset: float = 0.0
        app: AppConfig = field(default_factory=lambda: AppConfig())

    controller_data = ControllerConfig()
    controller_data.utc_offset = 9.0
    jsdc_dump(controller_data, 'config.json')

    loaded_controller_data = jsdc_load('config.json', ControllerConfig)
    loaded_controller_data.app.database.ips.append('127.0.0.2')

    jsdc_dump(loaded_controller_data, 'config.json')
    controller_data = jsdc_load('config.json', ControllerConfig)
    print(controller_data.app.database.ips)

    @dataclass
    class File_Hash:
        sha512: str = field(default_factory=lambda: "")
        xxhash: str = field(default_factory=lambda: "")

    @dataclass
    class Files_Hash:
        file_hashes: list[File_Hash] = field(default_factory=lambda: [])

    file_hashes = Files_Hash()
    file_hashes.file_hashes.append(File_Hash(sha512='123', xxhash='456'))
    file_hashes.file_hashes.append(File_Hash(sha512='789', xxhash='101'))
    jsdc_dump(file_hashes, 'config.json')

    loaded_file_hashes = jsdc_load('config.json', Files_Hash)
    print(loaded_file_hashes.file_hashes)

    import os
    os.remove('config.json')
