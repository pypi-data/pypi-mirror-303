import collections
import hashlib
import json
from typing import Any, Callable
from pathlib import Path
from modeltasks.util.serializer import normalize_object


default_hash_algorithm = 'sha1'


def get_hash_algorithm(algorithm: str = default_hash_algorithm) -> Callable:
    if algorithm.lower() == 'md5':
        return hashlib.md5
    elif algorithm.lower() == 'sha1':
        return hashlib.sha1
    elif algorithm.lower() == 'sha256':
        return hashlib.sha256
    else:
        return hashlib.sha1


def get_hash(o: Any, algorithm: str = default_hash_algorithm) -> str:
    o = normalize_object(o)
    bytes_value = json.dumps(o, sort_keys=True, ensure_ascii=True, default=str)
    hash_method = get_hash_algorithm(algorithm)
    try:
        return hash_method(bytes_value.encode()).hexdigest()
    except AttributeError:
        return ''


def get_file_hash(f: Path, algorithm: str = default_hash_algorithm) -> str:
    """Creates a hash for a file by looking at filename and size"""
    if isinstance(f, Path) and f.exists() and f.is_file():
        try:
            hash_method = get_hash_algorithm(algorithm)
            file_hash = hash_method()
            file_stat = f.stat()
            file_hash.update(f'{file_stat.st_size}{f.absolute()}'.encode('UTF-8'))
            return file_hash.hexdigest()
        except AttributeError as e:
            return ''
    else:
        return ''


def get_file_hash_checksum(f: Path, algorithm: str = default_hash_algorithm) -> str:
    """Creates a hash for a file by looking at its content"""
    if isinstance(f, Path) and f.exists() and f.is_file():
        try:
            hash_method = get_hash_algorithm(algorithm)
            file_hash = hash_method()
            with open(f, 'rb') as fh:
                while chunk := fh.read(8192):
                    file_hash.update(chunk)
            return file_hash.hexdigest()
        except AttributeError as e:
            return ''
    else:
        return ''


def get_folder_hash(f: Path, algorithm: str = default_hash_algorithm) -> str:
    """Creates a hash for a folder by creating simple hashes for all its contained files"""
    if isinstance(f, Path) and f.exists() and f.is_dir():
        hash_method = get_hash_algorithm(algorithm)
        folder_hash = hash_method()
        try:
            for p in sorted(f.rglob('*')):
                if p.is_file():
                    folder_hash.update(get_file_hash(p).encode('UTF-8'))
            return folder_hash.hexdigest()
        except AttributeError:
            return ''
    else:
        return ''


def get_folder_hash_checksum(f: Path, algorithm: str = default_hash_algorithm) -> str:
    """Creates a hash for a folder by creating checksums for all its contained files"""
    if isinstance(f, Path) and f.exists() and f.is_dir():
        hash_method = get_hash_algorithm(algorithm)
        folder_hash = hash_method()
        try:
            for p in sorted(f.rglob('*')):
                if p.is_file():
                    folder_hash.update(get_file_hash_checksum(p).encode('UTF-8'))
            return folder_hash.hexdigest()
        except AttributeError:
            return ''
    else:
        return ''
