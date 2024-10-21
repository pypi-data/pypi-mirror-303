from typing import Optional, get_args, get_type_hints, TypeVar, Any, get_origin, Union
from enum import Enum
from dataclasses import dataclass, is_dataclass
import json

T = TypeVar('T', bound=dataclass) # type hinting for dataclass
def jsdc_load(data_path: str, data_class: T, encoding: str = 'utf-8') -> T:
    # Recursive function to convert a dictionary to a dataclass
    def __dict_to_dataclass(c_obj: Any, c_data: dict):
        t_hints: dict = get_type_hints(type(c_obj))
        for key, value in c_data.items():
            if hasattr(c_obj, key):
                e_type = t_hints.get(key)
                if e_type is not None:
                    # Handle Enum types first
                    if isinstance(e_type, type) and issubclass(e_type, Enum):
                        try:
                            enum_value = e_type[value]
                            setattr(c_obj, key, enum_value)
                        except KeyError:
                            raise ValueError(f'Invalid Enum value for key {key}: {value}')
                    # Handle nested dataclasses
                    elif is_dataclass(e_type):
                        n_obj = e_type()
                        __dict_to_dataclass(n_obj, value)
                        setattr(c_obj, key, n_obj)
                    # Handle lists of dataclasses
                    elif get_origin(e_type) is list and is_dataclass(get_args(e_type)[0]):
                        item_type = get_args(e_type)[0]
                        n_list = [item_type(**item) for item in value]
                        setattr(c_obj, key, n_list)
                    else:
                        try:
                            origin = get_origin(e_type)
                            if origin is Union:
                                args = get_args(e_type)
                                # Handle Optional types (e.g., Union[Type, NoneType])
                                non_none_args = [arg for arg in args if arg is not type(None)]
                                if len(non_none_args) == 1:
                                    actual_type = non_none_args[0]
                                    if isinstance(actual_type, type) and issubclass(actual_type, Enum):
                                        value = actual_type[value]
                                    else:
                                        value = actual_type(value)
                                else:
                                    raise TypeError(f'Unsupported Union type for key {key}: {e_type}')
                            else:
                                if isinstance(e_type, type) and issubclass(e_type, Enum):
                                    value = e_type[value]
                                else:
                                    value = e_type(value)
                        except (ValueError, KeyError) as ex:
                            raise ValueError(f'Invalid type for key {key}, expected {e_type}, got {type(value).__name__}') from ex
                        setattr(c_obj, key, value)
            else:
                raise ValueError(f'Unknown data key: {key}')

    with open(data_path, 'r', encoding=encoding) as f:
        try:
            data: dict = json.load(f)
        except json.JSONDecodeError:
            raise ValueError('not supported file format, only json is supported')
    if not is_dataclass(data_class):
        raise ValueError('data_class must be a dataclass')
    
    root_obj: T = data_class()
    __dict_to_dataclass(root_obj, data)

    return root_obj


def jsdc_dump(obj: T, output_path: str, encoding: str = 'utf-8', indent: int = 4) -> None:
    # Recursive function to convert a dataclass to a dictionary
    def __dataclass_to_dict(obj: Any) -> Any:
        if isinstance(obj, Enum):
            return obj.name
        elif isinstance(obj, list):
            return [__dataclass_to_dict(item) for item in obj]
        elif is_dataclass(obj):
            result = {}
            t_hints = get_type_hints(type(obj))
            for key, value in vars(obj).items():
                e_type = t_hints.get(key)
                if e_type is not None:
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
                result[key] = __dataclass_to_dict(value)
            return result
        return obj

    if not is_dataclass(obj):
        raise ValueError('obj must be a dataclass')
    data_dict = __dataclass_to_dict(obj)
    with open(output_path, 'w', encoding=encoding) as f:
        json.dump(obj=data_dict, fp=f, indent=indent)



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
