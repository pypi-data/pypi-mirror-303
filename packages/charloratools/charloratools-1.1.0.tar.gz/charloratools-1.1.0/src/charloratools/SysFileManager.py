"""
> Provides classes and functions for **managing and processing image
files.**

Functionalities
---------------
  - Validating image files
  - Resizing
  - Copying
  - Deleting duplicates
  - Generating HTML galleries.

Classes
-------
ImgManager
    Manages individual images, including validation, comparison,
    and processing.
GalleryManager
    Manages collections of images using ImgManager for validation
    and processing.
TmpManager
    Handles temporary directories for image operations.

Functions
---------
refresh_decorator(func)
    A decorator for refreshing the image manager's state before and
    after method execution.

Examples
--------
```py
from charloratools.SysFileManager import GalleryManager
gm1 = GalleryManager(path='path/to/dir1')
gm2 = GalleryManager(path='path/to/dir2')
# Add images and create a new directory
gm3 = gm1 + gm2
```
"""

import logging
import shutil
from pathlib import Path
import base64
from typing import Union, Self
from collections.abc import Iterator
from typing import Callable
from typing import ParamSpec, TypeVar
from typing import Optional, Type
import concurrent
from concurrent.futures import ThreadPoolExecutor
# External Libs
import PIL
from PIL import Image
from tqdm import tqdm
import numpy as np
import imagehash
from imagehash import ImageHash, ImageMultiHash
import hashlib
import tempfile
# Scripts
from . import errors
from . import utils


class ImgManager:
    """
    Handles image files for easier validation, comparison, and processing
    when using OpenCV or PIL.

    This class allows comparing images by numpy array correspondence
    instead of hashes using the `arr_equals` method, while the operator
    defaults to the specified hash comparison.
    """
    OPERATION_ON_DELETED = "Trying to perform operation on deleted image"
    logger = logging.getLogger(__name__)

    def __init__(self, path: str | Path, hashtype: str = 'sha256'):
        """
        Initializes the ImgManager with the specified
        image path and hash type.

        Parameters
        ----------
        path : str or Path
            Path to the image file.
        hashtype : str, optional
            Type of hashing to be used for comparisons. Defaults to 'sha256'.
            Supported hashing types include:
              - sha256
              - phash
              - dhash
              - avg_hash
              - crop_resistant

        Raises
        ------
        errors.InvalidPathError
            If the provided path does not exist.
        errors.InvalidInputError
            If the provided path is not a file.
        errors.ImageTypeNotSupportedError
            If the image type is not supported.
        errors.ImageIsUnopenableError
            If Pillow cannot open the image.
        """
        if isinstance(path, str):
            path = Path(path).resolve()
        elif isinstance(path, Path):
            path = path
        else:
            raise errors.InvalidInputError("Path must be str or Path")
        # Checking if image path is valid
        if not path.exists():
            raise errors.InvalidPathError("Path doesn't exist")
        if not path.is_file():
            raise errors.InvalidInputError(
                "Image path does not exist or is not a file!")
        # Cheking if image extension is supported
        if not path.suffix.endswith(('.png',
                                     '.jpg',
                                     '.jpeg',
                                     '.tiff',
                                     '.bmp',
                                     '.gif')):
            raise errors.ImageTypeNotSupportedError(
                'Image type is not supported!')
        else:
            self.ext = path.suffix
        # Checking if pillow can open the image
        try:
            with Image.open(path) as img:
                self.array = np.array(img)
                self.dim = img.size
        except PIL.UnidentifiedImageError:
            raise errors.ImageIsUnopenableError(
                "Pillow can't open the image,check path")
        # End Validation
        self.path = path
        self.basename = path.stem+self.ext
        self.fname = path.stem
        self.hashtype = hashtype
        self.deleted = False
        self.hash = self.to_hash(hashtype)
        self.width = self.dim[0]
        self.height = self.dim[1]

    def __str__(self) -> str:
        """
        Returns a string representation of the ImgManager object.

        Returns
        -------
        str
            The string representation of the ImgManager, including the path,
            size, deletion status, and hash.
        """
        p = f"Path:{self.path};"
        s = f"Size:{self.dim[0]}x{self.dim[1]};"
        d = f"Deleted:{self.deleted};"
        h = f"Hash:{str(self.hash)};"
        return f"ImgManager[{p} {s} {d} {h}]"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the ImgManager instance.

        Returns
        -------
        str
            A representation string for the ImgManager instance.
        """
        return f"ImgManager(path={self.path},hashtype={self.hashtype})"

    def __bool__(self) -> bool:
        """
        Checks if the image is not marked as deleted.

        Returns
        -------
        bool
            True if the image is not deleted, False otherwise.
        """
        if not self.deleted:
            return True
        else:
            return False

    def __eq__(self, other: Self) -> bool:
        """
        Compares two ImgManager instances based on their hashes.

        Parameters
        ----------
        other : ImgManager
            Another ImgManager instance to compare with.

        Returns
        -------
        bool
            True if the hashes of both instances are equal, False otherwise.
        """

        return self.hash == other.hash

    def delete(self) -> None:
        """
        Deletes the image from the directory.

        Raises
        ------
        errors.ImageIsDeletedError
            If attempting to delete an image that is already marked as deleted.
        errors.ImgDeleteError
            If the deletion operation fails for any reason.
        """
        if not self:
            raise errors.ImageIsDeletedError(self.OPERATION_ON_DELETED)
        try:
            self.path.unlink()
            self.logger.info(f"Deleted Image {self.path}")
            self.deleted = True
        except FileNotFoundError:
            self.deleted = False
            es = f"Image not found for deletion: {self.path}"
            raise errors.ImgDeleteError(es)
        except PermissionError:
            es = f"Permission denied to delete image: {self.path}"
            self.deleted = False
            raise errors.ImgDeleteError(es)
        except OSError as e:
            es = f"Failed to delete image due to OS error: {str(e)}"
            self.deleted = False
            raise errors.ImgDeleteError(es)

    def to_html_base64(self, no_html_tag: bool = False) -> str:
        """
        Converts the image to base64 and returns an HTML img tag.

        Reads the image in binary mode, encodes it to base64,
        and returns an HTML img tag.

        Parameters
        ----------
        no_html_tag : bool, optional
            If True, returns only the base64 string without the HTML img tag.
            Defaults to False.

        Returns
        -------
        str
            The base64 image string or an HTML img tag depending on the
            `no_html_tag` parameter.

        Raises
        ------
        errors.ImageIsDeletedError
            If attempting to convert an image that has been deleted.
        errors.ImgOperationError
            If the conversion to base64 fails.
        """
        if not self:
            raise errors.ImageIsDeletedError(self.OPERATION_ON_DELETED)
        try:
            with open(self.path, 'rb') as binary_img:
                base64_img = base64.b64encode(binary_img.read())
            data_uri = base64_img.decode('utf-8')
            mime_type = f'image/{self.ext[1:]}'
            if no_html_tag:
                return data_uri
            return f'<img src="data:{mime_type};base64,{data_uri}"/>'
        except (FileNotFoundError, OSError) as e:
            raise errors.ImgOperationError(
                f"Failed to convert image to base64: {str(e)}")

    def arr_equals(self, other: np.ndarray) -> bool:
        """
        Compares the image array with another numpy array.

        Parameters
        ----------
        other : np.ndarray
            The numpy array to be compared with.

        Returns
        -------
        bool
            True if the arrays are equal, False otherwise.

        Raises
        ------
        errors.InvalidInputError
            If `other` is not a numpy array.
        """
        if not isinstance(other, np.ndarray):
            raise errors.InvalidInputError("other must be numpy array")
        return np.array_equal(self.array, other)

    def copy_to(self,
                path: str | Path,
                name: str | None = None) -> None:
        """
        Copies the image to a new directory.

        Appends a datetime.now unique suffix if a file of the same name
        already exists.

        Parameters
        ----------
        path : str or Path
            The destination path where the image will be copied.
        name : str or None, optional
            The name for the copied image without the suffix
            for example 'img1', if instance's file type is JPG
            will be saved as 'img1.jpg'. Defaults to None.

        Raises
        ------
        errors.ImageIsDeletedError
            If attempting to copy an image that has been deleted.
        errors.InvalidInputError
            If the destination path is not valid or is not a directory.
        errors.ImgOperationError
            If the copy operation fails for any reason.
        """
        if not self:
            raise errors.ImageIsDeletedError(self.OPERATION_ON_DELETED)
        # Check dir
        if isinstance(path, str):
            path = Path(path).resolve()
        elif isinstance(path, Path):
            path = path.resolve()
        else:
            raise errors.InvalidInputError(
                "path must be string or Path object")
        if not path.is_dir():
            raise errors.InvalidInputError("Path must be a directory")
        if not path.exists():
            raise errors.InvalidPathError("Path Doesn't exist")

        if name:
            if not isinstance(name, str):
                raise errors.InvalidInputError("Name must be str")
            else:
                copy_path = path / (name + self.ext)

        elif self.basename in [i.stem+i.suffix for i in path.iterdir()]:
            s = f"{self.fname}_{utils.GetUniqueDtStr()}{self.ext}"
            copy_path = path / s
        else:
            copy_path = path/self.basename
        if copy_path.exists():
            self.logger.warning("Image will be overwritten")
        try:
            shutil.copyfile(self.path, copy_path)
            self.logger.info(f"Copied Image {self.path} to {copy_path}")
        except Exception as e:
            raise errors.ImgOperationError(
                f"Failed to copy image to {copy_path}: {str(e)}")

    def resize(self,
               max_size: int,
               keep_aspect_ratio=True,
               size: tuple | None = None,
               inplace: bool = True,
               output_dir: str | Path | None = None) -> Path | None:
        """
        Resizes the image to a specified maximum size if
        `keep_aspect_ratio=True` or to the specific size
        defined in the `size` argument.

        ??? info
            - Uses `Image.Resampling.Lanczos` as the resizing
              method.
            - When `keep_aspect_ratio` is `False`, the `max_int`,
              parameter is ignored and only the `size` parameter
              is condidered.


        Parameters
        ----------
        max_size : int
            The maximum size for the resized image.
        keep_aspect_ratio : bool, optional
            If True, maintains the aspect ratio during resizing.
            Defaults to True.
        size : tuple or None, optional
            The desired size if `keep_aspect_ratio` is False. Defaults to None.
        inplace : bool, optional
            If True, modifies the original image. If False, saves a new image.
            Defaults to True.
        output_dir : str or Path or None, optional
            The directory where to output the resized image if `inplace` is
            False. Defaults to None.

        Returns
        -------
        Path or None
            returns the newly resized and saved image's
            path if inplace=False, returns None otherwise.

        Raises
        ------
        errors.InvalidInputError
            If invalid parameters are provided.
        errors.ImgOperationError
            If the resizing operation fails.
        """
        if not inplace and output_dir is None:
            raise errors.InvalidInputError(
                "output_dir must be provided if inplace=False")
        if not keep_aspect_ratio and size is None:
            raise errors.InvalidInputError(
                "size must be provided if keep_aspect_ratio=False")
        if isinstance(output_dir, str):
            output_dir = Path(output_dir).resolve()
        elif isinstance(output_dir, Path):
            output_dir = output_dir.resolve()
        else:
            if not inplace:
                raise errors.InvalidInputError("output_dir is not str or Path")
        if not inplace:
            if not output_dir.exists():
                raise errors.InvalidInputError("output path doesn't exist")
            elif not output_dir.is_dir():
                raise errors.InvalidInputError("output path is not dir.")
        try:
            with Image.open(self.path) as img:
                if keep_aspect_ratio:
                    aspect_ratio = img.width / img.height
                    if aspect_ratio > 1:
                        # Image is wider than it is tall
                        new_width = max_size
                        new_height = int(max_size / aspect_ratio)
                    else:
                        # Image is taller than it is wide
                        new_height = max_size
                        new_width = int(max_size * aspect_ratio)
                    img_resized = img.resize(
                        (new_width, new_height), Image.LANCZOS)
                else:
                    img_resized = img.resize(size, Image.LANCZOS)
                if inplace:
                    self.delete()
                    img_resized.save(self.path, quality=95)
                    rw = img_resized.width
                    rh = img_resized.height
                    self.width = rw
                    self.height = rh
                    self.logger.debug(
                        f"Resized Image {self.basename} to {rw}x{rh}")
                    self.deleted = False
                else:
                    fn = self.fname
                    rw = img_resized.width
                    rh = img_resized.height
                    sp = output_dir/f"{fn}_{rw}_{rh}.{self.ext}"
                    img_resized.save(sp, quality=95)
                    return sp
        except Exception as e:
            raise errors.ImgOperationError(
                f"Failed to resize image : {str(e)}")

    def to_hash(self,
                hashtype: str = 'sha256') -> str | ImageHash | ImageMultiHash:
        """
        Generates a hash for the image using the specified hash type.

        Parameters
        ----------
        hashtype : str, optional
            The hashing algorithm to use. Defaults to 'sha256'.

        Returns
        -------
        str or ImageHash or ImageMultiHash
            The resulting hash.
            If `hashtype='sha256'` the resulting hash is returned
            as a string. If  `hashtype='crop_resistant'` the
            resulting hash is a `imagehash.ImageMultiHash` instance,
            otherwise it is a `imagehash.ImageHash` instance.

        Raises
        ------
        errors.ImgHashNotSupportedError
            If the specified hash type is not supported.
        errors.ImageIsDeletedError
            If attempting to generate a hash for a deleted image.
        """
        if hashtype not in ['sha256', 'phash', 'crop_resistant', 'avg_hash',
                            'dhash']:
            raise errors.ImgHashNotSupportedError()
        if not self:
            raise errors.ImageIsDeletedError(self.OPERATION_ON_DELETED)
        if hashtype == 'sha256':
            with open(self.path, "rb") as f:
                hash = hashlib.sha256(f.read()).hexdigest()
        elif hashtype == 'phash':
            with Image.open(self.path) as img:
                hash = imagehash.phash(img)
        elif hashtype == 'crop_resistant':
            with Image.open(self.path) as img:
                hash = imagehash.crop_resistant_hash(img)
        elif hashtype == 'avg_hash':
            with Image.open(self.path) as img:
                hash = imagehash.average_hash(img)
        elif hashtype == 'dhash':
            with Image.open(self.path) as img:
                hash = imagehash.dhash(img)
        return hash

    def __hash__(self) -> int:
        """
        Generates a hash value for the ImgManager instance.

        Returns
        -------
        int
            The hash value of the image.
        """
        if self.hashtype == "sha256":
            return int(self.hash, 16)
        else:
            return hash(self.hash)


# Refresh decorator type hinting
P = ParamSpec("P")
R = TypeVar("R")


def refresh_decorator(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator to refresh the image manager's state before and after
    method execution.

    Parameters
    ----------
    func : callable
        The function to be wrapped.

    Returns
    -------
    callable
        A wrapper function that executes the original function
        and refreshes the state.
    """
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        self = args[0]
        prev_img_count = len(self.images)
        self.path, self.images = utils.dirisvalid(
            self.path,
            return_info=True,
            hashtype=self.hashtype,
            show_tqdm=self.show_tqdm)
        self.basename = self.path.stem
        self.ext_dir = self.path.parent
        self.ext_dir_name = self.path.parent.stem
        self.img_managers = [v for v in self.images.values()]
        self.image_paths = [k for k in self.images.keys()]
        self.logger.debug(
            f"Refreshed images {prev_img_count}->{len(self.images)}")
        result = func(*args, **kwargs)
        prev_img_count = len(self.images)
        self.path, self.images = utils.dirisvalid(
            self.path,
            return_info=True,
            hashtype=self.hashtype,
            show_tqdm=self.show_tqdm)
        self.basename = self.path.stem
        self.ext_dir = self.path.parent
        self.ext_dir_name = self.path.parent.stem
        self.img_managers = [v for v in self.images.values()]
        self.image_paths = [k for k in self.images.keys()]
        self.logger.debug(
            f"Refreshed images {prev_img_count}->{len(self.images)}")
        return result
    return wrapper


class GalleryManager:
    """
    Handles management and validation of a directory of images using
    the ImgManager class.

    This class supports operations with other instances and paths to
    facilitate image management.
    """
    logger = logging.getLogger(__name__)

    def __init__(self, path: str | Path,
                 hashtype: str = 'sha256',
                 show_tqdm: bool = False):
        """
        Initializes the GalleryManager with the specified
        path and hash type.

        Parameters
        ----------
        path : str or Path
            Path to the gallery directory.
        hashtype : str, optional
            Type of hash used for image comparisons. Defaults to sha256.
            Supported hashing types include:
              - sha256
              - phash
              - dhash
              - avg_hash
              - crop_resistant
        show_tqdm : bool, optional
            If True, enables progress showing during operations.
            Defaults to False.

        Raises
        ------
        errors.InvalidPathError
            If the provided path is not a string or path-like object.
        """
        if isinstance(path, str):
            self.path = Path(path).resolve()
        elif isinstance(path, Path):
            self.path = path
        else:
            raise errors.InvalidPathError(
                "path must be string or path-like object")
        self.basename = self.path.stem
        self.ext_dir = self.path.parent
        self.ext_dir_name = self.path.parent.stem
        self.hashtype = hashtype
        self.show_tqdm = show_tqdm
        self.path, self.images = utils.dirisvalid(
            self.path,
            return_info=True,
            hashtype=self.hashtype,
            show_tqdm=self.show_tqdm)
        self.img_managers = [v for v in self.images.values()]
        self.image_paths = [k for k in self.images.keys()]

    @refresh_decorator
    def change_hashtype(self, hashtype: str) -> None:
        """
        Changes the hash type used for image comparisons.

        Parameters
        ----------
        hashtype : str
            The new type of hash to use for comparing images.

        Raises
        ------
        errors.ImgHashNotSupportedError
            If the specified hash type is not supported.
        """
        self.hashtype = hashtype

    @refresh_decorator
    def __str__(self) -> str:
        """
        Returns a string representation of the GalleryManager.

        Returns
        -------
        str
            A string representation of the GalleryManager.
        """
        return f"GalleryManager[hash = {self.hashtype}, imgs = {len(self)}]"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the GalleryManager
        instance.

        Returns
        -------
        str
            A representation string for the GalleryManager instance.
        """
        sp = f"path={self.path}"
        st = f"show_tqdm={self.show_tqdm}"
        sh = f"hashtype={self.hashtype}"
        crepr = f"GalleryManager({sp}, {sh}, {st})"
        return crepr

    @refresh_decorator
    def __len__(self) -> str:
        """
        Returns the number of images in the gallery.

        Returns
        -------
        int
            The number of images in the gallery.
        """
        return len(self.images)

    @refresh_decorator
    def __getitem__(self,
                    key: Union[str, ImgManager, int, Path]) -> ImgManager:
        """
        Gets an ImgManager instance from the gallery by key.

        Parameters
        ----------
        key : str or Path or ImgManager or int
              The key to retrieve the ImgManager, can be a string, path,
              ImgManager instance or index.

        Returns
        -------
        ImgManager
            The requested ImgManager instance.

        Raises
        ------
        KeyError
            If the provided key does not match any image in the gallery.
        """
        if isinstance(key, str):
            path_value = Path(key).resolve()
            if not path_value.exists():
                e = f"Couldn't resolve path from string: {key}"
                raise errors.InvalidPathError(e)
            imgmanager = ImgManager(
                path=Path(key).resolve(), hashtype=self.hashtype)
            if imgmanager in self:
                index = self.get_img_manager_index(imgmanager)

                return self.img_managers[index]
            else:
                raise KeyError(
                    "Path isn't valid or Image doesn't match any in gallery")
        elif isinstance(key, Path):
            imgmanager = ImgManager(path=key, hashtype=self.hashtype)
            if imgmanager in self:
                index = self.get_img_manager_index(imgmanager)
                return self.img_managers[index]
            else:
                raise KeyError(
                    "Path isn't valid or Image doesn't match any in gallery")

        elif isinstance(key, ImgManager):
            if key in self:
                index = self.get_img_manager_index(key)
                return self.img_managers[index]
            else:
                raise KeyError(
                    "Image doesn't match any image present in gallery")

        elif isinstance(key, int):
            try:
                return self.img_managers[key]
            except IndexError:
                raise KeyError("Index out of range for GalleryManager")
        else:
            ke = f"""Key must be a string with the image file name,
                     path-like object of image path,or ImgManager object,
                     got {type(key)}"""
            raise KeyError(ke)

    @refresh_decorator
    def __setitem__(self, key: Union[str, Path, ImgManager, str],
                    value: Union[str, Path, ImgManager]) -> None:
        """
        Sets an image in the gallery at the specified key.

        Parameters
        ----------
        key : str or Path or ImgManager
              The key at which to set the image. Can be a string with the
              image file name,
              a path-like object of the image path, or an ImgManager instance.
        value : str or Path or ImgManager
                The image to set at the specified key. Can be a string, path,
                or ImgManager instance.

        Raises
        ------
        KeyError
            If the key does not match any existing images in the gallery.
        errors.InvalidInputError
            If the value is not a string, path, or ImgManager object.
        errors.OperationNotSupportedError
            If the operation is not supported for the provided value type.
        """
        if isinstance(value, str):
            path_value = Path(value).resolve()
            if not path_value.exists():
                e = f"Couldn't resolve path from string: {value}"
                raise errors.InvalidPathError(e)
            oldimgmanager = self[key]
            nimg = ImgManager(Path(value).resolve(), hashtype=self.hashtype)
            nimg.copy_to(self.path, name=oldimgmanager.fname)

        elif isinstance(value, ImgManager):
            oldimgmanager = self[key]
            value.copy_to(self.path, name=oldimgmanager.fname)

        elif isinstance(value, Path):
            oldimgmanager = self[key]
            nimg = ImgManager(path=value.resolve(), hashtype=self.hashtype)
            nimg.copy_to(self.path, name=oldimgmanager.fname)
        else:
            raise errors.OperationNotSupportedError("Operation not supported")

    @refresh_decorator
    def __iter__(self) -> Iterator[ImgManager]:
        """
        Returns an iterator over the ImgManager instances in the gallery.

        Returns
        -------
        iterator
            An iterator of ImgManager instances.
        """
        return iter(tuple(self.img_managers))

    @refresh_decorator
    def __contains__(self, item: Union[Self,
                                       ImgManager,
                                       list[str | ImgManager], str]) -> bool:
        """
        Checks if a given item is present in the gallery.

        Parameters
        ----------
        item : GalleryManager or ImgManager or list or str
               The item to check for presence in the gallery. This can be an
               ImgManager instance, a list of ImgManager instances,
               or a file path string.

        Returns
        -------
        bool
            True if the item or any image from the item is found in the
            gallery, False otherwise.

        Raises
        ------
        errors.OperationNotSupportedError
            If the provided item type is not supported for the operation.
        errors.InvalidPathError
            if the provided string path is invalid.
        """
        gallery_hashes = np.array([img.hash for img in self.img_managers])

        if isinstance(item, ImgManager):
            if item.hashtype != self.hashtype:
                item_hash = item.to_hash(self.hashtype)
            else:
                item_hash = item.hash
            return np.isin(item_hash, gallery_hashes)

        elif isinstance(item, (str, Path)):
            path = Path(item).resolve()
            if not path.exists():
                raise errors.InvalidPathError(f"Path '{path}' does not exist")
            img = ImgManager(path=path, hashtype=self.hashtype)
            return np.isin(img.hash, gallery_hashes)

        elif isinstance(item, GalleryManager):
            # Check if all images in the other GalleryManager exist in this one
            o_hashes = []
            for i in item.img_managers:
                if i.hashtype != self.hashtype:
                    o_hashes.append(i.to_hash(self.hashtype))
                else:
                    o_hashes.append(i.hash)

            other_hashes = np.array(o_hashes)
            return np.all(np.isin(other_hashes, gallery_hashes))

        elif isinstance(item, list):
            return all(self.__contains__(element) for element in item)

        else:
            es = f"Operation not supported for type {type(item)}"
            raise errors.OperationNotSupportedError(es)

    @refresh_decorator
    def __eq__(self, other: Self) -> bool:
        """
        Checks equality between this instance and another
        GalleryManager instance.

        ??? info
            If `other` parameter is not a GalleryManager instance
            returns False.

        Parameters
        ----------
        other : GalleryManager
            The other GalleryManager instance to compare with.

        Returns
        -------
        bool
            True if both instances contain the same images and have the
            same hash type, False otherwise.
        """
        if isinstance(other, self.__class__):
            if len(self) != len(other):
                return False
            if self.hashtype != other.hashtype:
                other.change_hashtype(self.hashtype)

            # If the number of images is different, they can't be equal
            if len(self) != len(other):
                return False

            # Convert the list of hashes to sets for fast comparison
            self_hashes = {i.hash for i in self}
            other_hashes = {i.hash for i in other}

            # Compare the two sets
            return self_hashes == other_hashes

        else:
            return False

    @refresh_decorator
    def __ne__(self, other: Self) -> bool:
        """
        Checks inequality between this instance and another
        GalleryManager instance.

        Parameters
        ----------
        other : GalleryManager
            The other GalleryManager instance to compare with.

        Returns
        -------
        bool
            True if the instances are not equal, False otherwise.
        """
        return not self.__eq__(other)

    @refresh_decorator
    def __gt__(self, other: Self) -> bool:
        """
        Compares this instance with another GalleryManager instance.

        Parameters
        ----------
        other : GalleryManager
            The other GalleryManager instance to compare with.

        Returns
        -------
        bool
            True if this instance has more images than the other,
            False otherwise.
        """
        return len(self) > len(other)

    @refresh_decorator
    def __lt__(self, other: Self) -> bool:
        """
        Compares this instance with another GalleryManager instance.

        Parameters
        ----------
        other : GalleryManager
            The other GalleryManager instance to compare with.

        Returns
        -------
        bool
            True if this instance has fewer images than the other,
            False otherwise.
        """
        return len(self) < len(other)

    @refresh_decorator
    def __add__(self, other: Union[Self, str, ImgManager]) -> Self:
        """
        Adds another GalleryManager instance or image to this instance
        by creating a new directory.

        ??? info
            - The new directory will be created in the **parent folder**
              of the calling instance's (left of the operator) path.
            - The new directory's name will follow the following structure
              ```py
              f"{this_instance}_add_{other_object}"
              ```
        ??? note
            When adding images, if there are **repeating file names**,
            an **unique datetime string** will be appended to one of
            the repeating files and, if images are the same, they
            **will be duplicated**.

        Parameters
        ----------
        other : GalleryManager or str or ImgManager
            The GalleryManager instance or image path/ImgManager to add
            to this instance.

        Returns
        -------
        GalleryManager
            A new GalleryManager instance containing images from both this
            instance and the other.

        Raises
        ------
        errors.OperationNotSupportedError
            If the operation is not supported for the provided other type.
        """
        if isinstance(other, self.__class__):
            # Addings two instances
            # Creating new dir
            if other.hashtype != self.hashtype:
                other.change_hashtype(self.hashtype)
            s_base = self.basename
            nn = f"{s_base}_add_{other.basename}_{utils.GetUniqueDtStr()}"
            new_dir_name = Path(f"{self.ext_dir}") / Path(nn)
            new_dir_name = utils.dirisvalid(
                new_dir_name,
                create_if_not_found=True,
                show_tqdm=self.show_tqdm)
            for imgmanager in tqdm(self, desc='Copying 1st instance images'):
                imgmanager.copy_to(new_dir_name.resolve())
            for oimgmanager in tqdm(other, desc='Copying 2nd instance images'):
                oimgmanager.copy_to(new_dir_name.resolve())
            # Hashtype returned is the left instance's one
            return GalleryManager(new_dir_name.resolve(),
                                  hashtype=self.hashtype)
        # Subtracting instance from str
        elif isinstance(other, str):
            path = Path(other).resolve()
            if not path.exists():
                e = f"Couldn't resolve path from string: {other}"
                raise errors.InvalidPathError(e)
            nimgmanager = ImgManager(other, hashtype=self.hashtype)
            fn = Path(f"{self.basename}_add_{nimgmanager.basename}")
            new_dir_name = Path(f"{self.ext_dir}")/fn
            new_dir_name = utils.dirisvalid(
                new_dir_name, create_if_not_found=True,
                show_tqdm=self.show_tqdm)
            for imgmanager in self:
                imgmanager.copy_to(new_dir_name.resolve())
            nimgmanager.copy_to(new_dir_name.resolve())
            return GalleryManager(new_dir_name.resolve(),
                                  hashtype=self.hashtype)
        elif isinstance(other, ImgManager):
            if other.hashtype != self.hashtype:
                other = ImgManager(other.path)
            s = f"{self.basename}_add_{other.basename}"
            new_dir_name = Path(f"{self.ext_dir}") / Path(s)
            new_dir_name = utils.dirisvalid(
                new_dir_name, create_if_not_found=True,
                show_tqdm=self.show_tqdm)
            for imgmanager in self:
                imgmanager.copy_to(new_dir_name.resolve())
            other.copy_to(new_dir_name.resolve())
            return GalleryManager(new_dir_name.resolve(),
                                  hashtype=self.hashtype)
        else:
            raise errors.OperationNotSupportedError("Operation not supported")

    @refresh_decorator
    def __sub__(self, other: Union[Self, str, ImgManager]) -> Self:
        """
        Removes images from this instance based on another GalleryManager
        instance or image.

        ??? info
            - If `other` is a GalleryManager instance, it
              finds all images present in the calling instance
              (left of the operator) which are **not** present
              in the `other` instance (right of the operator)
              and copies them to a new directory
            - The newly created directory will be **located in
              the parent directory** of the calling instance's
              directory.
            - The new directory's name will follow the following structure
              ```py
              f"{this_instance}_add_{other_object}"
              ```


        Parameters
        ----------
        other : GalleryManager or str or ImgManager
            The images to remove from this instance.

        Returns
        -------
        GalleryManager
            A new GalleryManager instance containing images left
            after subtraction.

        Raises
        ------
        errors.OperationResultsInEmptyDirectoryError
            If the resulting operation would lead to an empty directory.
        errors.OperationNotSupportedError
            If the operation is not supported for the provided other type.
        """
        def _compare_multihash(im1, im2):
            return im1.hash - im2.hash

        # Subtracting two GalleryManager instances
        if isinstance(other, self.__class__):
            # Ensure the hash types are the same
            if other.hashtype != self.hashtype:
                other.change_hashtype(self.hashtype)

            # Subtract based on hash type
            other_hashes = {oimg.hash for oimg in other}

            imgs_to_add = [i for i in self if i.hash not in other_hashes]
            es = "Operation would result in empty directory"
            if len(imgs_to_add) == 0:
                raise errors.OperationResultsInEmptyDirectoryError(es)
            dstr = f"{self.basename}_sub_{other.basename}"
            new_dir_name = Path(self.ext_dir) / dstr
            new_dir_name = utils.dirisvalid(new_dir_name,
                                            create_if_not_found=True,
                                            show_tqdm=self.show_tqdm)

            for imgmanager in tqdm(imgs_to_add, desc='Copying images'):
                imgmanager.copy_to(new_dir_name.resolve())

            return GalleryManager(new_dir_name.resolve(),
                                  hashtype=self.hashtype)

        # Subtracting a string (file path)
        elif isinstance(other, str):
            path = Path(other).resolve()
            if not path.exists():
                es = f"Couldn't resolve path from string: {other}"
                raise errors.InvalidPathError(es)

            nimgmanager = ImgManager(other, hashtype=self.hashtype)
            return self - nimgmanager

        # Subtracting an ImgManager instance
        elif isinstance(other, ImgManager):
            imgs_to_add = [img for img in self if img.hash != other.hash]

            if len(imgs_to_add) == 0:
                es = "Operation would result in empty directory"
                raise errors.OperationResultsInEmptyDirectoryError(es)

            dstr = f"{self.basename}_sub_{other.basename}"
            new_dir_name = Path(self.ext_dir) / dstr
            new_dir_name = utils.dirisvalid(new_dir_name,
                                            create_if_not_found=True,
                                            show_tqdm=self.show_tqdm)

            for imgmanager in imgs_to_add:
                imgmanager.copy_to(new_dir_name.resolve())

            return GalleryManager(new_dir_name.resolve(),
                                  hashtype=self.hashtype)

        else:
            es = "Operation not supported for this type"
            raise errors.OperationNotSupportedError(es)

    @refresh_decorator
    def __iadd__(self, other: Union[Self, str, ImgManager]) -> Self:
        """
        Inserts images from another GalleryManager instance or image
        into this instance.

        ??? info
            Performs the same operation as `GalleryManager.__add__`
            but inplace.

        Parameters
        ----------
        other : GalleryManager or str or ImgManager
            The images to insert.

        Returns
        -------
        GalleryManager
            This instance, updated with the new images.

        Raises
        ------
        errors.OperationNotSupportedError
            If the operation is not supported for the provided other type.
        """
        if isinstance(other, self.__class__):
            if other.hashtype != self.hashtype:
                other.change_hashtype(self.hashtype)
            for imgmanager in tqdm(other, desc='Copying Images'):
                imgmanager.copy_to(self.path)
            return self
        elif isinstance(other, str):
            path = Path(other).resolve()
            if not path.exists():
                e = f"Couldn't resolve path from string: {other}"
                raise errors.InvalidPathError(e)
            nimgmanager = ImgManager(other, hashtype=self.hashtype)
            nimgmanager.copy_to(self.path)
            return self
        elif isinstance(other, ImgManager):
            other.copy_to(self.path)
            return self
        else:
            raise errors.OperationNotSupportedError("Operation not supported")

    @refresh_decorator
    def __isub__(self, other: Union[Self, str, ImgManager]) -> Self:
        """
        Removes images from this instance based on another GalleryManager
        instance or image.

        ??? info
            Performs the same operation as the `GalleryManager.__sub__`
            but inplace. Meaning **images in the calling instance's
            (left of the operator) will be deleted**

        Parameters
        ----------
        other : GalleryManager or str or ImgManager
            The images to remove.

        Returns
        -------
        GalleryManager
            This instance, updated with the remaining images after removal.

        Raises
        ------
        errors.OperationNotSupportedError
            If the operation is not supported for the provided other type.
        """
        if isinstance(other, self.__class__):
            if other.hashtype != self.hashtype:
                other.change_hashtype(self.hashtype)
            if other == self:
                raise errors.OperationResultsInEmptyDirectoryError(
                    "Operation would result in an empty directory")
            for imgmanager in tqdm(self, desc="Checking Hashes"):
                if imgmanager in other:
                    if len(self) == 1:
                        raise errors.OperationResultsInEmptyDirectoryError
                    imgmanager.delete()
            return self
        elif isinstance(other, str):
            path = Path(other).resolve()
            if not path.exists():
                e = f"Couldn't resolve path from string: {other}"
                raise errors.InvalidPathError(e)
            nimgmanager = ImgManager(other, hashtype=self.hashtype)
            for imgmanager in self:
                if imgmanager == nimgmanager:
                    if len(self) == 1:
                        raise errors.OperationResultsInEmptyDirectoryError
                    imgmanager.delete()
            return self
        elif isinstance(other, ImgManager):
            for imgmanager in self:
                if imgmanager == other:
                    if len(self) == 1:
                        raise errors.OperationResultsInEmptyDirectoryError
                    imgmanager.delete()
            return self
        else:
            raise errors.OperationNotSupportedError(
                f'Operation not supported for type {type(other)}')

    @refresh_decorator
    def __hash__(self) -> int:
        """
         Returns a hash value for the GalleryManager instance.

        Returns
        -------
        int
            The hash value calculated from the hashes of the images
            in the gallery.
        """
        img_hashes = tuple([hash(manager) for manager in self.img_managers])
        return hash(img_hashes)

    @refresh_decorator
    def to_html_img_gallery(self,
                            output_dir: str,
                            separate_elements: bool = False
                            ) -> tuple[str | Path]:
        """
        Creates a standalone HTML image gallery for preview from the current
        directory's images.

        Parameters
        ----------
        output_dir : str
            The directory in which to create the .html file.
        separate_elements : bool, optional
            If True, return only the image gallery HTML div and necessary
            elements instead of a fully formatted website. Defaults to False.

        Returns
        -------
        tuple
            The path to the generated HTML file and the
            formatted HTML file's content as a string if
            `separate_elements` is False, otherwise returns a
            tuple containing the head and body elements of the HTML.

        Raises
        ------
        errors.InvalidPathError
            If the specified output directory does not exist or is not valid.
        errors.ImgOperationError
            If the image gallery generation fails.
        """
        output_dir = utils.dirisvalid(
            output_dir, create_if_not_found=True, show_tqdm=self.show_tqdm)
        website_template = """<!doctype html><html><head><meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Preview Image Gallery</title>
        <link rel="icon"
         href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.6.0/svgs/solid/images.svg"/>
        <script
         src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js">
        </script>
        <link
         href="https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.css"
         rel="stylesheet">
        <script
         src="https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.js"></script>
        <link
         href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
         crossorigin="anonymous">
        </head><body style="background-color:#024950;">
        <div class="container text-center"><div class="row">
        <div class="col"><h1 style="color:#AFDDE5">Image Gallery</h1></div>
        </div>
        <div class="row"><div class="fotorama col"
         data-allowfullscreen="native"
         data-width="100%" data-ratio="4/3">{0}</div></div></div>
         <div class="container text-center">
        <p style="color:#AFDDE5">
        Photo Gallery Credits:<a href="https://fotorama.io/">Fotoroma</a></p>
        </div>
        <script
         src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
         integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
          crossorigin="anonymous"></script>
        </body></html>
        """
        body_template = """<div class="container text-center"><div class="row">
                     <div class="fotorama col" data-allowfullscreen="native"
                      data-width="100%" data-ratio="4/3">{0}</div>
                     </div></div>
                     <script
                      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
                      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
                       crossorigin="anonymous"></script>
                     """
        head_template = """<meta charset="utf-8">
                     <meta name="viewport" content="width=device-width,
                      initial-scale=1">
                     <script
                      src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
                     <link
                      href="https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.css"
                       rel="stylesheet">
                     <script
                     src="https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.js"></script>
                     <link
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                      rel="stylesheet"
                      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
                      crossorigin="anonymous">
                   """

        html_tags = ''
        for i in self:
            img_tag = i.to_html_base64()
            html_tags += img_tag
        template_with_img = website_template.format(html_tags)
        body_template_with_img = body_template.format(html_tags)
        if separate_elements:
            self.logger.info("html body formatted sucessfully")
            return head_template, body_template_with_img
        else:
            s = f'generated_img_gallery_{utils.GetUniqueDtStr()}.html'
            save_path = output_dir / s
            with open(save_path, 'w') as f:
                f.write(template_with_img)
            self.logger.info('.html image gallery saved sucessfully')
            return save_path, template_with_img

    @refresh_decorator
    def delete_duplicates(self) -> None:
        """
         Deletes duplicate images in the gallery based on their hashes.

        This method checks for duplicate images and removes them from
        the gallery, maintaining only one instance of each unique image.

        Raises
        ------
        errors.ImgDeleteError
            If any errors occur during the deletion of duplicate images.
        """
        seen_hashes = {}
        duplicates = []

        # Iterate over each image and check if its hash is already seen
        for img in self:
            try:
                img_hash = img.hash
                if img_hash in seen_hashes:
                    duplicates.append(img)
                else:
                    seen_hashes[img_hash] = img
            except Exception as e:
                es = f"Error processing image {img.path}: {str(e)}"
                self.logger.error(es)
                raise

        # Delete all duplicate images
        for img in duplicates:
            try:
                img.delete()
            except Exception as e:
                es = f"Error deleting duplicate image {img.path}: {str(e)}"
                self.logger.error(es)
                raise

    @refresh_decorator
    def resize_all(self,
                   max_size: int,
                   keep_aspect_ratio: bool = True,
                   size: tuple | None = None,
                   inplace: bool = True,
                   output_dir: str | Path | None = None) -> Self | None:
        """
        Resizes all images in the gallery according to specified parameters
        for more information on parameters, see the `ImgManager.resize`
        method documentation.

        ??? info
            As of version `1.1.0` images are resized concurrently
            using multithreading.

        Parameters
        ----------
        max_size : int
            The maximum size for the resized images.
        keep_aspect_ratio : bool, optional
            If True, maintains the aspect ratio during resizing.
            Defaults to True.
        size : tuple or None, optional
            The desired size if `keep_aspect_ratio` is False. Defaults to None.
        inplace : bool, optional
            If True, modifies the original images. If False, saves resized
            images in `output_dir`. Defaults to True.
        output_dir : str or Path or None, optional
            The directory where to output the resized images if `inplace` is
            False. Defaults to None.

        Returns
        -------
        GalleryManager or None
            If inplace is false, returns the GalleryManager for the
            created output directory, otherwise returns this instance
            with resized images.

        Raises
        ------
        errors.InvalidInputError
            If invalid parameters are provided.
        errors.ImgOperationError
            If the resizing operation fails.
        """
        if not inplace:
            output_dir = utils.dirisvalid(output_dir,
                                          create_if_not_found=True,
                                          show_tqdm=self.show_tqdm)

        def _resize_im(im: ImgManager) -> None:
            try:
                im.resize(max_size,
                          keep_aspect_ratio,
                          size,
                          inplace,
                          output_dir)
            except Exception as e:
                # Log the error for the current image and re-raise
                es = f"Error resizing image {im.path}: {str(e)}"
                self.logger.error(es)
                raise

        with ThreadPoolExecutor() as executor:
            imlst = self.img_managers
            futures = [executor.submit(_resize_im, im) for im in imlst]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    # Handle the exception raised in any of the threads
                    es = f"Error during concurrent resizing: {str(e)}"
                    self.logger.error(es)
        if not inplace:
            return GalleryManager(path=output_dir,
                                  hashtype=self.hashtype,
                                  show_tqdm=self.show_tqdm)

    @refresh_decorator
    def get_img_manager_index(self, img_manager: ImgManager) -> int:
        """
        Returns the index of the specified ImgManager in the gallery.

        Parameters
        ----------
        img_manager : ImgManager
            The ImgManager instance to search for in the gallery.

        Returns
        -------
        int
            The index of the specified ImgManager.

        Raises
        ------
        KeyError
            If the specified ImgManager is not found in the gallery.
        """
        if img_manager not in self:
            raise KeyError("Image isn't in gallery")
        else:
            for i, smanager in enumerate(self.img_managers):
                if img_manager == smanager:
                    return i


class TmpManager(GalleryManager):
    """
    Handles creation and deletion of a temporary
    directory for image operations.

    This class extends the GalleryManager to use a temporary directory,
    providing methods to manage images within that directory.
    """

    def __init__(self,
                 hashtype: str,
                 save_content_on_deletion: bool = False,
                 output_dir: str | Path | None = None):
        """
        Initializes the TmpManager with hash type and other parameters.

        Parameters
        ----------
        hashtype : str
            The type of hash to use for image comparisons.
        save_content_on_deletion : bool, optional
            If True, saves the contents of the temporary directory upon
            deletion. Defaults to False.
        output_dir : str or Path, optional
            The output directory where contents might be saved. If None, uses
            a default temporary path.

        Raises
        ------
        errors.InvalidInputError
            If output_dir is not a string or path-like object, or if it does
            not exist.
        """
        self.temp_dir = None
        # initializing gallery manager attrs
        if output_dir is None:
            output_dir = None
        elif isinstance(output_dir, str):
            output_dir = Path(output_dir).resolve()
            if not output_dir.exists():
                raise errors.InvalidInputError("Output Dir Doesn't Exist")
        elif isinstance(output_dir, Path):
            output_dir = output_dir.resolve()
            if not output_dir.exists():
                raise errors.InvalidInputError("Output Dir Doesn't Exist")
        else:
            raise errors.InvalidInputError(
                "output_dir must be str or path-like object")
        self.prev_tmp_dir = None
        self.path = None
        self.basename = None
        self.ext_dir = None
        self.ext_dir_name = None
        self.show_tqdm = None
        self.images = None
        self.img_managers = None
        self.image_paths = None
        # --
        self.prev_tempdir_var = None
        self.tmp_path = None
        self.hashtype = hashtype
        self.save_content_on_deletion = save_content_on_deletion
        self.output_dir = Path(output_dir).resolve(
        ) if output_dir else self.tmp_path
        self.is_open = False

    def __str__(self) -> str:
        """
        Returns a string representation of the TmpManager instance.

        Returns
        -------
        str
            A string describing the temporary directory name and
            its open status.
        """
        p = f"Path:{self.tmp_path};"
        o = f"Opened:{self.is_open}"
        return f"TmpManager[{p} {o}]"

    def __repr__(self) -> str:
        """
         Returns a detailed string representation of the TmpManager instance.

        Returns
        -------
        str
            A representation string for the TmpManager, including
            hash type and save content status.
        """
        ht = f"hashtype={self.hashtype}"
        sc = f"save_content_on_deletion={self.save_content_on_deletion}"
        return f"TmpManager({ht},{sc},output_dir={self.output_dir})"

    def __enter__(self) -> Self:
        """
        Enters the context of the temporary directory manager.

        Creates a temporary directory and initializes the gallery
        manager parameters.

        Returns
        -------
        TmpManager
            The instance of TmpManager.
        """
        self.prev_tempdir_var = tempfile.tempdir
        self.temp_dir = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.temp_dir.name).resolve()
        logging.debug(f"Created tmp dir at {self.tmp_path}")
        placeholder = Image.fromarray(np.reshape(
            np.arange(0, 100, 1, dtype=np.uint8), (10, 10)))
        placeholder.save(self.tmp_path / 'placeholder.jpg')
        super().__init__(path=self.tmp_path, hashtype=self.hashtype)
        self.is_open = True
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[object]) -> Optional[bool]:
        """
        Exits the context of the temporary directory manager.

        Cleans up the temporary directory and optionally
        saves contents if required.

        Parameters
        ----------
        exc_type : type
            The type of exception that triggered the exit.
        exc_val : Exception
            The exception instance that triggered the exit.
        exc_tb : traceback
            The traceback object.

        Raises
        ------
        Exception
            Propagates any exceptions that occur during the cleaning process.
        """
        # Transfer contents to a permanent location if needed
        if self.save_content_on_deletion and len(self) != 0:
            for img in self:
                if img.basename != "placeholder.jpg":
                    img.copy_to(self.output_dir)
        if self.temp_dir is not None:
            self.temp_dir.cleanup()
        self.is_open = False
        return False

    def __del__(self) -> None:
        """
        Ensures cleanup of the temporary directory when the instance
        is deleted.

        This method is called when the instance is about to be destroyed.
        It cleans up the temporary directory if it hasn't
        already been cleaned up.
        """
        # Ensure cleanup if not already done
        if self.temp_dir is not None:
            self.temp_dir.cleanup()
