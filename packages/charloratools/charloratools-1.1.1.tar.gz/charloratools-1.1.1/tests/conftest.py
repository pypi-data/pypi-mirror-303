from PIL import Image
import numpy as np
import tempfile
import urllib.request
from typing import Generator
from pathlib import Path
import sys
import logging
import pytest
from unittest.mock import patch, MagicMock
from pytest import FixtureRequest

sys.path.append('./src')

# Setup Logging

logging.basicConfig(level="INFO", style="{",
                    format="{name} - {levelname} - {message}")

# Cloudfare Image CDN account hash
CLOUDFARE_ACC_HASH = "YCQ3OFRYiR1R_AeUslNHiw"


class TempDirFactory:
    """
    Creates temporary directories used for testing OS
    file system functionalities.
    """

    def __init__(self):
        """
        Initializes an instance of the TempDirFactory class by
        creating an initial empty dictionary which will contain
        the created temporary directories

        Returns
        -------
        TempDirFactory
        """

        self.directories = {}

    def new_temp(self, name: str) -> Path:
        """
        Generates a new temporary directory and adds it to the
        instance's directories attribute

        Parameters
        ----------
        name : str
               The dictionary key to be used when appending
               to the instance's 'directories' attribute.

        Returns
        -------
        Path
            The newly created temporary directory's path.
        """
        temp = tempfile.TemporaryDirectory()
        path = Path(temp.name).resolve()
        self.directories[name] = {'dir': temp,
                                  'path': path}
        return path

    def cleanup(self) -> None:
        """
        Deletes all temporary directories in instance's
        'directories' attribute and all of their content.
        Also resets the attribute to an empty dictionary.
        """
        for d in self.directories.values():
            d['dir'].cleanup()
        logging.info(f"Sucessfully Cleaned Up {len(self.directories)} dirs")
        self.directories = {}

    def create_random_image(self, name: str, fname: str) -> Path:
        """
        Creates a randomly generated 100x100 .jpg image in the
        directory attributed to the 'name' key in the
        instance's 'directories' attribute.

        Parameters
        ----------
        name : str
               The dictionary key attributed to the
               temporary directory in the instance's
               'directories' attribute.
        fname : str
                The name of the image file to be created
                before the '.jpg' suffix.

        Returns
        -------
        Path
            The path to the newly created random
            image.

        Raises
        ------
        KeyError
            If the 'name' parameter provided is not an
            existent key in the 'directories' attribute
        """
        imarray = np.random.rand(100, 100, 3) * 255
        im = Image.fromarray(imarray.astype('uint8'))
        try:
            temp = self.directories[name]
        except KeyError:
            er = "The name provided is not an instance temporary directory"
            raise KeyError(er)
        im_fpath = fname + '.jpg'
        save_path = temp['path'] / im_fpath
        im.save(save_path)
        return save_path

    def create_txt_file(self, name: str, fname: str) -> Path:
        """
        Creates an empty text file in the
        directory attributed to the 'name' key in the
        instance's 'directories' attribute.

        Parameters
        ----------
        name : str
               The dictionary key attributed to the
               temporary directory in the instance's
               'directories' attribute.
        fname : str
                The name of the image file to be created
                before the '.txt' suffix.

        Returns
        -------
        Path
            The path to the newly created empty
            text file.

        Raises
        ------
        KeyError
            If the 'name' parameter provided is not an
            existent key in the 'directories' attribute
        """
        try:
            temp = self.directories[name]
        except KeyError:
            er = "The name provided is not an instance temporary directory"
            raise KeyError(er)

        txt_fpath = fname + '.txt'
        save_path = temp['path'] / txt_fpath
        with open(save_path, 'w') as n_txt:
            n_txt.write(" ")

        return save_path

    def download_from_cloudfare(self, img_id: str, name: str,
                                fname: str, acc_hash: str,
                                size: str = '400x400', **kwargs) -> Path:
        """
        Downloads an image from cloudfare's CDN  into the
        directory attributed to the 'name' key in the
        instance's 'directories' attribute.

        Parameters
        ----------
        img_id : str
                 The id defined by cloudfare when storing
                 the image to be delivered.
        name : str
               The dictionary key attributed to the
               temporary directory in the instance's
               'directories' attribute.
        fname : str
                The name of the image file to be created
                before the '.jpg' suffix.
        acc_hash : str
                   The unique cloudfare account id hash
                   which is used in the delivered
                   image's url.
        size : str
               The delivered image's size (cloudfare variants)
               which is also part of the url. Defaults to 400x400

        Returns
        -------
        Path
            The path to the downloaded image.

        Raises
        ------
        KeyError
            If the 'name' parameter provided is not an
            existent key in the 'directories' attribute
        TypeError
            If any of the parameters provided are not a
            string.
        RuntimeError
            If there's an error downlaoding the image from
            the CDN.
        """
        if not isinstance(img_id, str):
            raise TypeError("img_id must be a str")

        if not isinstance(name, str):
            raise TypeError("name must be a str")

        if not isinstance(fname, str):
            raise TypeError("fn must be a str")

        if not isinstance(size, str):
            raise TypeError("size must be a str")

        if not isinstance(acc_hash, str):
            raise TypeError("acc_hash must be a str")

        try:
            temp = self.directories[name]
        except KeyError:
            er = "The name provided is not an instance temporary directory"
            raise KeyError(er)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Chrome')]
        urllib.request.install_opener(opener)

        base_url = "https://imagedelivery.net"

        img_url = f"{base_url}/{acc_hash}/{img_id}/{size}"

        im_fpath = fname + '.jpg'
        save_path = temp['path'] / im_fpath

        # Retry logic for downloading
        for attempt in range(3):
            try:
                urllib.request.urlretrieve(img_url, save_path)
                logging.info(f"Download successful, saved to {save_path}")
                return save_path
            except Exception as e:
                logging.warning(f"Failed on attempt {attempt + 1}:{e}")
        es = "Failed to download image from Cloudflare after 3 attempts."
        raise RuntimeError(es)


@pytest.fixture
def mock_webdriver() -> Generator[MagicMock, None, None]:
    """
    Function to simulate a selenium webdriver to test
    the 'Scrapers' classes logic by using unittest's
    MagicMock.

    Yields
    ------
    MagicMock
        The mocked selenium webdriver
    """
    with patch('selenium.webdriver.Chrome') as mock_driver:
        mock_instance = MagicMock()
        mock_driver.return_value = mock_instance
        yield mock_instance


@pytest.fixture(scope="session")
def tfactory(request: type[FixtureRequest]) -> TempDirFactory:
    """
    Pytest fixture function to make the same instance
    of TempDirFactory available during the test
    session and clean up the temporary directories
    created at the end of it

    Parameters
    ----------
    request : type[FixtureRequest]
        gives access to the requesting test context as
        explained in pytest's documentation.

    Returns
    -------
    TempDirFactory
        the TempDirFactory instance to be made available
        to the requesting test.
    """
    tfactory = TempDirFactory()

    # Register cleanup to run after the session ends
    request.addfinalizer(tfactory.cleanup)

    return tfactory
