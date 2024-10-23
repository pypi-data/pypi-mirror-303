from pathlib import Path
import pytest
import torch
import pandas as pd
from cv2 import imread
from cv2 import cvtColor
from cv2 import COLOR_BGR2RGB
from charloratools.SysFileManager import ImgManager
from charloratools.utils import dirisvalid
from charloratools.utils import distance_function
from charloratools.utils import InfoDict2Pandas
from charloratools.utils import split_matched
from charloratools.utils import img_path_to_tensor
from charloratools.utils import dir_path_to_img_batch
from charloratools.errors import InvalidPathError
from charloratools.errors import InvalidInputError
from charloratools.errors import InfoDictFormatError
from charloratools.FilterAI import FaceRecognizer
from charloratools.errors import NoImagesInDirectoryError
from charloratools.errors import InvalidTypeError
from charloratools.facenet_pytorch import MTCNN
from charloratools.facenet_pytorch import InceptionResnetV1
from charloratools.SysFileManager import GalleryManager
from conftest import TempDirFactory
from conftest import CLOUDFARE_ACC_HASH


def setup_img_dir(tfactory: TempDirFactory, name: str) -> Path:
    """
    Sets up a new temporary directory in an
    instance of 'TempDirFactory' with test images
    downloaded from cloudfare.

    Parameters
    ----------
    tfactory : TempDirFactory
        the 'TempDirFactory' instance.
    name : str
        the dictionary key that will be set in the
        instance's directories attribute for the
        new temporary directory.

    Returns
    -------
    Path
        the path to the temporary directory.
    """
    path = tfactory.new_temp(name)
    test_face1_id = "4cb492db-609f-4b30-20dd-f21c71a9a300"
    test_face2_id = "aecfc808-015d-4731-60d3-26a77f840f00"
    test_filler = "d86b8943-68c1-4f43-702f-db0633f98000"
    test_multiple = "479facfa-0358-47d6-b7c2-e5813f4e5f00"
    size = "400x400"

    tfactory.download_from_cloudfare(test_face2_id,
                                     name,
                                     "test_face2",
                                     CLOUDFARE_ACC_HASH,
                                     size)

    tfactory.download_from_cloudfare(test_face1_id,
                                     name,
                                     "test_face1",
                                     CLOUDFARE_ACC_HASH,
                                     size)

    tfactory.download_from_cloudfare(test_filler,
                                     name,
                                     "filler",
                                     CLOUDFARE_ACC_HASH,
                                     size)
    tfactory.download_from_cloudfare(test_multiple,
                                     name,
                                     "multiple",
                                     CLOUDFARE_ACC_HASH,
                                     size)
    return path


def test_dirisvalid(tfactory: TempDirFactory) -> None:
    """
    Tests the 'dirisvalid' function from the utils module.

    Parameters
    ----------
    tfactory : TempDirFactory
        the instance of 'TempDirFactory' initalized as
        a pytest fixture.
    """
    imgs_path = setup_img_dir(tfactory, "test_dirisvalid1")
    empty_path = tfactory.new_temp("test_dirisvalid2")
    no_images_path = tfactory.new_temp("test_dirisvalid3")
    tfactory.create_txt_file('test_dirisvalid3', "randomt")
    # Test return_info=True and hashtype is None
    with pytest.raises(InvalidInputError):
        dirisvalid(path=imgs_path,
                   check_images=False,
                   return_info=True,
                   hashtype=None,
                   create_if_not_found=False,
                   show_tqdm=False)
    # Test path is not str or path
    with pytest.raises(InvalidTypeError):
        dirisvalid(path=True,
                   check_images=False,
                   return_info=True,
                   hashtype='sha256',
                   create_if_not_found=False,
                   show_tqdm=False)

    # Test invalid path
    with pytest.raises(InvalidPathError):
        dirisvalid(path='invalid/path',
                   check_images=False,
                   return_info=True,
                   hashtype='sha256',
                   create_if_not_found=False,
                   show_tqdm=False)

    # Test dir without images
    with pytest.raises(NoImagesInDirectoryError):
        dirisvalid(path=no_images_path,
                   check_images=True,
                   return_info=True,
                   hashtype='sha256',
                   create_if_not_found=False,
                   show_tqdm=False)

    # Test empty dir without checking images
    dcheck = dirisvalid(path=empty_path,
                        check_images=False,
                        return_info=False,
                        hashtype='sha256',
                        create_if_not_found=False,
                        show_tqdm=False)
    assert dcheck
    # Test dir with images, return info is False
    dimg_check = dirisvalid(path=imgs_path,
                            check_images=True,
                            return_info=False,
                            hashtype='sha256',
                            create_if_not_found=False,
                            show_tqdm=False)
    dimg_check2 = dirisvalid(path=imgs_path,
                             check_images=True,
                             return_info=False,
                             hashtype='sha256',
                             create_if_not_found=False,
                             show_tqdm=True)
    assert dimg_check
    assert dimg_check2

    # Test dir with images, return info is True
    (path, images) = dirisvalid(path=imgs_path,
                                check_images=True,
                                return_info=True,
                                hashtype='sha256',
                                create_if_not_found=False,
                                show_tqdm=False)
    (path2, images2) = dirisvalid(path=imgs_path,
                                  check_images=True,
                                  return_info=True,
                                  hashtype='sha256',
                                  create_if_not_found=False,
                                  show_tqdm=True)
    assert isinstance(path, Path)
    assert isinstance(path2, Path)
    assert isinstance(images, dict)
    assert isinstance(images2, dict)
    assert len(images) == 4
    assert len(images2) == 4
    for k, v in images.items():
        assert isinstance(k, Path)
        assert isinstance(v, ImgManager)

    # Test creating dir
    sys_temp_folder = imgs_path.parent
    ndir = sys_temp_folder / "test_dirisvalid_dir_creation"
    ndir_path = dirisvalid(path=ndir,
                           check_images=False,
                           return_info=False,
                           hashtype=None,
                           create_if_not_found=True,
                           show_tqdm=False)
    assert isinstance(ndir_path, Path)
    assert ndir_path.exists()
    assert ndir_path.is_dir()
    assert ndir_path.parent == sys_temp_folder


def test_distance_f(tfactory: TempDirFactory) -> None:
    """
    Tests the 'distance_function' function from the utils module.

    Parameters
    ----------
    tfactory : TempDirFactory
        the instance of 'TempDirFactory' initalized as
        a pytest fixture.
    """
    imgs_path = setup_img_dir(tfactory, "test_dfunction")
    # Getting embeddings
    mtcnn = MTCNN(keep_all=False,
                  selection_method='probability')
    resnet = InceptionResnetV1(pretrained='vggface2').eval()
    gm = GalleryManager(path=imgs_path,
                        hashtype='sha256',
                        show_tqdm=False)
    face2_path = gm[0].path
    face1_path = gm[1].path
    img1 = imread(face1_path)
    img2 = imread(face2_path)
    img1 = cvtColor(img1, COLOR_BGR2RGB)
    img2 = cvtColor(img2, COLOR_BGR2RGB)
    aligned1 = mtcnn(img1).unsqueeze(0)
    aligned2 = mtcnn(img2).unsqueeze(0)
    emb1 = resnet(aligned1)
    emb2 = resnet(aligned2)

    # Test unsupported method
    with pytest.raises(InvalidInputError):
        distance_function(embedding1=emb1,
                          embedding2=emb2,
                          method='invalid_method',
                          classify=False,
                          threshold=None
                          )

    # Test threshold not set
    with pytest.raises(InvalidInputError):
        distance_function(embedding1=emb1,
                          embedding2=emb2,
                          method='cosine',
                          classify=True,
                          threshold=None
                          )

    # Test cosine
    d = distance_function(embedding1=emb1,
                          embedding2=emb2,
                          method='cosine',
                          classify=False,
                          threshold=None
                          ).item()
    assert isinstance(d, float)
    thresh1 = d - 0.1
    cb = distance_function(embedding1=emb1,
                           embedding2=emb2,
                           method='cosine',
                           classify=True,
                           threshold=thresh1)
    assert isinstance(cb, bool)
    assert cb

    # Test euclidean
    de = distance_function(embedding1=emb1,
                           embedding2=emb2,
                           method='euclidean',
                           classify=False,
                           threshold=None
                           ).item()
    assert isinstance(de, float)
    thresh2 = de + 0.1
    eb = distance_function(embedding1=emb1,
                           embedding2=emb2,
                           method='euclidean',
                           classify=True,
                           threshold=thresh2)
    assert isinstance(cb, bool)
    assert eb


def test_dir_to_tensor(tfactory: TempDirFactory) -> None:
    """
    Tests the 'dir_to_tensor' function from the utils module.

    Parameters
    ----------
    tfactory : TempDirFactory
        the instance of 'TempDirFactory' initalized as
        a pytest fixture.
    """
    imgs_path = setup_img_dir(tfactory, "test_dir_to_tensor")
    gm = GalleryManager(path=imgs_path,
                        hashtype='sha256',
                        show_tqdm=False)
    im1_path = gm[0].path
    # test invalid path
    with pytest.raises(InvalidInputError):
        dir_path_to_img_batch(path=True)
    with pytest.raises(InvalidInputError):
        dir_path_to_img_batch(path=im1_path)
    with pytest.raises(InvalidInputError):
        dir_path_to_img_batch(path='invalid/path')

    # test valid path
    t = dir_path_to_img_batch(path=imgs_path)
    assert isinstance(t, torch.Tensor)
    assert t.size(dim=0) == len(gm)
    assert t.size(dim=1) == 3


def test_img_to_tensor(tfactory: TempDirFactory) -> None:
    """
    Tests the 'img_to_tensor' function from the utils module.

    Parameters
    ----------
    tfactory : TempDirFactory
        the instance of 'TempDirFactory' initalized as
        a pytest fixture.
    """
    imgs_path = setup_img_dir(tfactory, "test_img_to_tensor")

    gm = GalleryManager(path=imgs_path,
                        hashtype='sha256',
                        show_tqdm=False)
    face2_path = gm[0].path
    face2_width = gm[0].width
    face2_height = gm[0].height
    txt_file_path = tfactory.create_txt_file('test_dirisvalid3', "randomt")

    # test invalid path
    with pytest.raises(InvalidInputError):
        img_path_to_tensor(img_path=True,
                           nsize=None)
    with pytest.raises(InvalidInputError):
        img_path_to_tensor(img_path=txt_file_path,
                           nsize=None)
    # test invalid nsize
    with pytest.raises(InvalidInputError):
        img_path_to_tensor(img_path=face2_path,
                           nsize=True)
    # test with nsize=None
    t1 = img_path_to_tensor(img_path=face2_path,
                            nsize=None)
    assert isinstance(t1, torch.Tensor)
    assert t1.size(dim=0) == 3
    assert t1.size(dim=1) == face2_width
    assert t1.size(dim=2) == face2_height

    t2 = img_path_to_tensor(img_path=face2_path,
                            nsize=(400, 400))
    assert isinstance(t2, torch.Tensor)
    assert t2.size(dim=0) == 3
    assert t2.size(dim=1) == 400
    assert t2.size(dim=2) == 400


def test_info_dict_2_pandas(tfactory: TempDirFactory) -> None:
    """
    Tests the 'InfoDict2Pandas' and
    'split_matched' functions from the utils module.

    Parameters
    ----------
    tfactory : TempDirFactory
        the instance of 'TempDirFactory' initalized as
        a pytest fixture.
    """
    imgs_path = setup_img_dir(tfactory, "test_infodict2pandas")
    empty_path1 = tfactory.new_temp("test_testinfodict2pandas2")
    empty_path2 = tfactory.new_temp("test_testinfodict2pandas3")
    # Getting info_dict
    gm = GalleryManager(path=imgs_path,
                        hashtype='sha256',
                        show_tqdm=False)
    face1_path = gm[0].path
    fr = FaceRecognizer(path=imgs_path)
    (gm1, info_dict1) = fr.filter_images_without_specific_face(face1_path,
                                                               empty_path1,
                                                               None,
                                                               20,
                                                               0.6,
                                                               'vggface2',
                                                               'cosine',
                                                               True)
    (gm2, info_dict2) = fr.filter_images_without_face(output_dir=empty_path2,
                                                      min_face_size=20,
                                                      prob_threshold=0.8,
                                                      return_info=True)

    # Test format errors
    # type errors
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(True)
    # dict format errors
    wid1 = {'key1': True, 'key2': True}
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(wid1)
    wid2 = {'info_dict_lst': True}
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(wid2)
    wid3 = {'info_dict_lst': [True, {}]}
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(wid3)
    wid4 = {'info_dict_lst': [{'path': None,
                               'boxes': None,
                               'probs': None,
                               'error': None}]}
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(wid4)
    # list format errors
    wid5 = [True, False]
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(wid5)
    wid6 = [{'path': None,
             'boxes': None,
             'probs': None,
             'error': None}]
    with pytest.raises(InfoDictFormatError):
        InfoDict2Pandas(wid6)

    # test correct format
    out1 = InfoDict2Pandas(info_dict1)
    assert isinstance(out1, dict)
    assert isinstance(out1['matched_ref_df'], pd.DataFrame)
    out2 = InfoDict2Pandas(info_dict2)
    assert isinstance(out1, dict)
    assert isinstance(out2['info_df'], pd.DataFrame)

    # test split_matched
    out3 = split_matched(info_dict1)
    assert isinstance(out3, dict)
    assert isinstance(out3['info_df'], dict)
    assert 'matched' in out3['info_df'].keys()
    out4 = split_matched(info_dict2)
    assert isinstance(out4, dict)
    assert isinstance(out4['info_df'], dict)
    assert 'matched' in out4['info_df'].keys()
