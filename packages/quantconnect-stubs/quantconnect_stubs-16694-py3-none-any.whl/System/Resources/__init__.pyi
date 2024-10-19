from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.Globalization
import System.IO
import System.Reflection
import System.Resources
import System.Runtime.Serialization


class SatelliteContractVersionAttribute(System.Attribute):
    """Instructs a ResourceManager object to ask for a particular version of a satellite assembly."""

    @property
    def version(self) -> str:
        ...

    def __init__(self, version: str) -> None:
        ...


class IResourceReader(System.Collections.IEnumerable, System.IDisposable, metaclass=abc.ABCMeta):
    """Abstraction to read streams of resources."""

    def close(self) -> None:
        ...


class ResourceReader(System.Object, System.Resources.IResourceReader):
    """This class has no documentation."""

    @overload
    def __init__(self, fileName: str) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    def get_resource_data(self, resource_name: str, resource_type: typing.Optional[str], resource_data: typing.Optional[typing.List[int]]) -> typing.Union[None, str, typing.List[int]]:
        ...


class MissingSatelliteAssemblyException(System.SystemException):
    """The exception that is thrown when the satellite assembly for the resources of the default culture is missing."""

    @property
    def culture_name(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, cultureName: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class ResourceSet(System.Object, System.IDisposable, System.Collections.IEnumerable):
    """This class has no documentation."""

    @property
    def reader(self) -> System.Resources.IResourceReader:
        """This field is protected."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, fileName: str) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, reader: System.Resources.IResourceReader) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def dispose(self) -> None:
        ...

    def get_default_reader(self) -> typing.Type:
        ...

    def get_default_writer(self) -> typing.Type:
        ...

    def get_enumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    @overload
    def get_object(self, name: str) -> System.Object:
        ...

    @overload
    def get_object(self, name: str, ignore_case: bool) -> System.Object:
        ...

    @overload
    def get_string(self, name: str) -> str:
        ...

    @overload
    def get_string(self, name: str, ignore_case: bool) -> str:
        ...

    def read_resources(self) -> None:
        """This method is protected."""
        ...


class UltimateResourceFallbackLocation(Enum):
    """Specifies whether a ResourceManager object looks for the resources of the app's default culture in the main assembly or in a satellite assembly."""

    MAIN_ASSEMBLY = 0

    SATELLITE = 1


class NeutralResourcesLanguageAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def culture_name(self) -> str:
        ...

    @property
    def location(self) -> System.Resources.UltimateResourceFallbackLocation:
        ...

    @overload
    def __init__(self, cultureName: str) -> None:
        ...

    @overload
    def __init__(self, cultureName: str, location: System.Resources.UltimateResourceFallbackLocation) -> None:
        ...


class ResourceManager(System.Object):
    """This class has no documentation."""

    @property
    def base_name_field(self) -> str:
        """This field is protected."""
        ...

    @property
    def main_assembly(self) -> System.Reflection.Assembly:
        """This field is protected."""
        ...

    MAGIC_NUMBER: int = ...

    HEADER_VERSION_NUMBER: int = 1

    @property
    def base_name(self) -> str:
        ...

    @property
    def ignore_case(self) -> bool:
        ...

    @property.setter
    def ignore_case(self, value: bool) -> None:
        ...

    @property
    def resource_set_type(self) -> typing.Type:
        ...

    @property
    def fallback_location(self) -> System.Resources.UltimateResourceFallbackLocation:
        """This property is protected."""
        ...

    @property.setter
    def fallback_location(self, value: System.Resources.UltimateResourceFallbackLocation) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, baseName: str, assembly: System.Reflection.Assembly) -> None:
        ...

    @overload
    def __init__(self, baseName: str, assembly: System.Reflection.Assembly, usingResourceSet: typing.Type) -> None:
        ...

    @overload
    def __init__(self, resourceSource: typing.Type) -> None:
        ...

    @staticmethod
    def create_file_based_resource_manager(base_name: str, resource_dir: str, using_resource_set: typing.Type) -> System.Resources.ResourceManager:
        ...

    @staticmethod
    def get_neutral_resources_language(a: System.Reflection.Assembly) -> System.Globalization.CultureInfo:
        """This method is protected."""
        ...

    @overload
    def get_object(self, name: str) -> System.Object:
        ...

    @overload
    def get_object(self, name: str, culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    def get_resource_file_name(self, culture: System.Globalization.CultureInfo) -> str:
        """This method is protected."""
        ...

    def get_resource_set(self, culture: System.Globalization.CultureInfo, create_if_not_exists: bool, try_parents: bool) -> System.Resources.ResourceSet:
        ...

    @staticmethod
    def get_satellite_contract_version(a: System.Reflection.Assembly) -> System.Version:
        """This method is protected."""
        ...

    @overload
    def get_stream(self, name: str) -> System.IO.UnmanagedMemoryStream:
        ...

    @overload
    def get_stream(self, name: str, culture: System.Globalization.CultureInfo) -> System.IO.UnmanagedMemoryStream:
        ...

    @overload
    def get_string(self, name: str) -> str:
        ...

    @overload
    def get_string(self, name: str, culture: System.Globalization.CultureInfo) -> str:
        ...

    def internal_get_resource_set(self, culture: System.Globalization.CultureInfo, create_if_not_exists: bool, try_parents: bool) -> System.Resources.ResourceSet:
        """This method is protected."""
        ...

    def release_all_resources(self) -> None:
        ...


class MissingManifestResourceException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


