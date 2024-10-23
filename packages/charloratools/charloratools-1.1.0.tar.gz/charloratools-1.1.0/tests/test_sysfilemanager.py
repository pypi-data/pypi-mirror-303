import pytest
from pathlib import Path
import re
from PIL import Image
from imagehash import ImageHash, ImageMultiHash
from charloratools.SysFileManager import ImgManager
from charloratools.SysFileManager import GalleryManager
from charloratools.SysFileManager import TmpManager
from charloratools.errors import InvalidPathError
from charloratools.errors import OperationNotSupportedError
from charloratools.errors import OperationResultsInEmptyDirectoryError
from charloratools.errors import InvalidInputError
from charloratools.errors import ImageTypeNotSupportedError
from charloratools.errors import ImgHashNotSupportedError
from charloratools.errors import ImageIsDeletedError
hashtype_lst = ['sha256', 'phash', 'dhash', 'avg_hash', 'crop_resistant']

# -------------- Test ImgManager


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_img_manager(hashtype: str, tfactory):
    """
    Tests basic functionality of the ImgManager class,
    specifically the methods: [__init__,
    __str__,__repr__,__bool__,__hash__,
    __eq__,arr_equals and to_hash]

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """

    t_path = tfactory.new_temp('test_imanager_init')
    ipath = tfactory.create_random_image('test_imanager_init', 'random')
    txt_path = tfactory.create_txt_file('test_imanager_init', 'randomt')
    # Test unsupported hashtype
    with pytest.raises(ImgHashNotSupportedError):
        ImgManager(path=ipath,
                   hashtype='invalid_hash')
    # Test when path is Path
    im = ImgManager(path=ipath,
                    hashtype=hashtype)
    assert isinstance(im, ImgManager)
    # Test when path is string
    im2 = ImgManager(path=str(ipath),
                     hashtype=hashtype)
    assert isinstance(im2, ImgManager)
    # Test when path is invalid
    with pytest.raises(InvalidPathError):
        ImgManager(path='invalid/path',
                   hashtype=hashtype)
    # Test when path is not a file
    with pytest.raises(InvalidInputError):
        ImgManager(path=t_path,
                   hashtype=hashtype)

    # Test when path type is not supported
    with pytest.raises(InvalidInputError):
        ImgManager(path=True,
                   hashtype=hashtype)

    # Test when img type is not supported
    with pytest.raises(ImageTypeNotSupportedError):
        ImgManager(path=txt_path,
                   hashtype=hashtype)

    # Test str
    p = f"Path:{im.path};"
    s = f"Size:{im.dim[0]}x{im.dim[1]};"
    d = f"Deleted:{im.deleted};"
    h = f"Hash:{str(im.hash)};"
    es = f"ImgManager[{p} {s} {d} {h}]"
    assert str(im) == es

    # Test repr
    er = f"ImgManager(path={im.path},hashtype={im.hashtype})"
    assert im.__repr__() == er

    # Test bool
    assert im.__bool__()
    im.delete()
    assert not im.__bool__()

    # Test Img Operation on deleted
    with pytest.raises(ImageIsDeletedError):
        im.to_hash(hashtype=hashtype)

    # Test hash, arr_equals and __eq__
    ipath2 = tfactory.create_random_image('test_imanager_init', 'random2')
    ipath3 = tfactory.create_random_image('test_imanager_init', 'random3')
    im_h = ImgManager(path=ipath2,
                      hashtype=hashtype)
    im_h2 = ImgManager(path=ipath2,
                       hashtype=hashtype)
    im_h3 = ImgManager(path=ipath3,
                       hashtype=hashtype)
    # __eq__
    assert im_h != im_h3
    assert im_h == im_h2
    # arr_equals
    arr2 = im_h2.array
    arr3 = im_h3.array
    assert im_h.arr_equals(arr2)
    assert not im_h.arr_equals(arr3)
    # arr equals when other is not numpy array
    with pytest.raises(InvalidInputError):
        im_h.arr_equals(True)
    # hash
    assert isinstance(im_h.__hash__(), int)
    assert im_h.__hash__() == im_h2.__hash__()
    assert im_h.__hash__() != im_h3.__hash__()


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_img_copy_to(hashtype, tfactory):
    """
    Tests the 'copy_to' method of the ImgManager instance.
    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    tfactory.new_temp('test_copy_to')
    ipath1 = tfactory.create_random_image('test_copy_to', 'random')
    ipath2 = tfactory.create_random_image('test_copy_to', 'random2')
    im1 = ImgManager(path=ipath1,
                     hashtype=hashtype)
    im2 = ImgManager(path=ipath2,
                     hashtype=hashtype)
    t_path2 = tfactory.new_temp('test_copy_to2')

    # Test invalid path input
    with pytest.raises(InvalidInputError):
        im1.copy_to(path=True,
                    name=None)
    # Test path is not directory
    with pytest.raises(InvalidInputError):
        im1.copy_to(path=ipath2,
                    name=None)
    # Test path is invalid
    with pytest.raises(InvalidInputError):
        im1.copy_to(path='invalid/path',
                    name=None)
    # Test with name not being a string
    with pytest.raises(InvalidInputError):
        im1.copy_to(path=t_path2,
                    name=True)
    # Test with name
    im1.copy_to(path=t_path2,
                name="im1_copy")
    assert (t_path2 / "im1_copy.jpg").exists()
    # Test without name
    im2.copy_to(path=t_path2,
                name=None)
    assert (t_path2 / "random2.jpg").exists()
    # Test copy when image name already exists
    im2.copy_to(path=t_path2,
                name=None)
    p = r'random2_\d+\.jpg'
    regex = re.compile(p)
    blst = []
    for path in t_path2.iterdir():
        if path.is_file() and regex.match(path.name):
            blst.append(True)
        else:
            blst.append(False)
    assert any(blst)


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_resize_img(hashtype, tfactory):
    """
    Tests the 'resize' method of the ImgManager instance.
    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    tfactory.new_temp('test_resize_img')
    ipath1 = tfactory.create_random_image('test_resize_img', 'random')
    ipath2 = tfactory.create_random_image('test_resize_img', 'random2')
    im1 = ImgManager(path=ipath1,
                     hashtype=hashtype)
    im2 = ImgManager(path=ipath2,
                     hashtype=hashtype)
    t_path2 = tfactory.new_temp('test_resize_img2')

    # Test inplace is False and output_dir is None
    with pytest.raises(InvalidInputError):
        im1.resize(max_size=300,
                   keep_aspect_ratio=True,
                   size=None,
                   inplace=False,
                   output_dir=None)
    # Test aspect_ratio is False and size is None
    with pytest.raises(InvalidInputError):
        im1.resize(max_size=300,
                   keep_aspect_ratio=False,
                   size=None,
                   inplace=True,
                   output_dir=None)

    # Test path is invalid
    with pytest.raises(InvalidInputError):
        im1.resize(max_size=300,
                   keep_aspect_ratio=True,
                   size=None,
                   inplace=False,
                   output_dir='invalid/path')
    # Test path is not str or path
    with pytest.raises(InvalidInputError):
        im1.resize(max_size=300,
                   keep_aspect_ratio=True,
                   size=None,
                   inplace=False,
                   output_dir=True)
    # Test path is not dir
    with pytest.raises(InvalidInputError):
        im1.resize(max_size=300,
                   keep_aspect_ratio=True,
                   size=None,
                   inplace=False,
                   output_dir=ipath2)
    # Test inplace is true
    im1.resize(max_size=300,
               keep_aspect_ratio=True,
               size=None,
               inplace=True,
               output_dir=None)
    with Image.open(im1.path) as rim1:
        assert rim1.height == 300 or rim1.width == 300
    assert im1.height == 300 or im1.width == 300
    # Test inplace is false
    nipath = im1.resize(max_size=300,
                        keep_aspect_ratio=True,
                        size=None,
                        inplace=False,
                        output_dir=t_path2)
    rim1 = ImgManager(path=nipath,
                      hashtype=hashtype)
    with Image.open(nipath) as prim1:
        assert prim1.height == 300 or prim1.width == 300
    assert rim1.height == 300 or rim1.width == 300
    # Repeat tests with aspect_ratio = False
    # Test inplace is true
    im2.resize(max_size=300,
               keep_aspect_ratio=False,
               size=(300, 300),
               inplace=True,
               output_dir=None)
    with Image.open(im2.path) as rim2:
        assert rim2.height == 300 and rim2.width == 300
    assert im2.height == 300 and im2.width == 300
    # Test inplace is false
    nipath2 = im2.resize(max_size=300,
                         keep_aspect_ratio=False,
                         size=(300, 300),
                         inplace=False,
                         output_dir=t_path2)
    rim2 = ImgManager(path=nipath2,
                      hashtype=hashtype)
    with Image.open(nipath) as prim2:
        assert prim2.height == 300 and prim2.width == 300
    assert rim2.height == 300 and rim2.width == 300


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_delete_image(hashtype: str, tfactory):
    """
    Tests the 'delete' method of the ImgManager instance.
    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    tfactory.new_temp('test_imanager_delete')
    ipath = tfactory.create_random_image('test_imanager_delete', 'random')
    im = ImgManager(path=ipath,
                    hashtype=hashtype)
    assert im
    im.delete()
    assert not ipath.exists()
    assert not im


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_to_hash(hashtype: str, tfactory):
    """
    Tests 'to_hash' method of ImgManager.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    tfactory.new_temp('test_to_hash')
    ipath = tfactory.create_random_image('test_to_hash', 'random')
    im1 = ImgManager(path=ipath,
                     hashtype=hashtype)
    _hash = im1.to_hash(hashtype=hashtype)
    if hashtype == 'sha256':
        assert isinstance(_hash, str)
    elif hashtype == 'crop_resistant':
        assert isinstance(_hash, ImageMultiHash)
    else:
        assert isinstance(_hash, ImageHash)


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_base64(hashtype: str, tfactory):
    """
    Tests 'to_hash' method of ImgManager.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    tfactory.new_temp('test_base64')
    ipath = tfactory.create_random_image('test_base64', 'random')
    im1 = ImgManager(path=ipath,
                     hashtype=hashtype)
    # Test with no html tag
    b64 = im1.to_html_base64(no_html_tag=True)
    assert isinstance(b64, str)
    # Test with html tag
    htmlb64 = im1.to_html_base64()
    assert isinstance(b64, str)
    assert '<img' in htmlb64
# --------------
# -------------- Test Refresh Decorator


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_refresh_decorator(hashtype: str, tfactory):
    """
    Tests the refresh decorator function to update
    the GalleryManager instance after methods.
    """
    t_path = tfactory.new_temp('test_refresh_dec')
    tfactory.create_random_image('test_refresh_dec', 'random')
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype,
                        show_tqdm=False)
    tfactory.create_random_image('test_refresh_dec', 'random2')
    assert isinstance(gm[1], ImgManager)
    assert len(gm) == 2

# --------------
# -------------- Test GalleryManager


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_init(hashtype: str, tfactory) -> None:
    """
    Tests instance initialization of a GalleryManager instance.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    show_tqdm : bool
                Wether or not to show tqdm progress bars during image
                operations.
    """
    t_path = tfactory.new_temp('test_init_path')
    tfactory.create_random_image('test_init_path', 'random')
    # provided path is pathlib.Path object
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype,
                        show_tqdm=False)
    assert isinstance(gm, GalleryManager)
    # provided path is str
    t_path2 = tfactory.new_temp('test_init_str')
    tfactory.create_random_image('test_init_str', 'random')
    gm_str = GalleryManager(path=str(t_path2),
                            hashtype=hashtype,
                            show_tqdm=False)
    assert isinstance(gm_str, GalleryManager) and isinstance(gm_str.path, Path)

    # provided path is unsupported type
    with pytest.raises(InvalidPathError):
        GalleryManager(path=True,
                       hashtype=hashtype,
                       show_tqdm=False)

    # Repeat with showing tqdm on

    t_path3 = tfactory.new_temp('test_init_path2')
    tfactory.create_random_image('test_init_path2', 'random')
    # provided path is pathlib.Path object
    gm2 = GalleryManager(path=t_path3,
                         hashtype=hashtype,
                         show_tqdm=True)
    assert isinstance(gm2, GalleryManager)
    # provided path is str
    t_path4 = tfactory.new_temp('test_init_str2')
    tfactory.create_random_image('test_init_str2', 'random')
    gm_str2 = GalleryManager(path=str(t_path4),
                             hashtype=hashtype,
                             show_tqdm=True)
    assert isinstance(gm_str2, GalleryManager)
    assert isinstance(gm_str2.path, Path)

    # provided path is unsupported type
    with pytest.raises(InvalidPathError):
        GalleryManager(path=True,
                       hashtype=hashtype,
                       show_tqdm=True)


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_change_hashtype(hashtype: str, tfactory) -> None:
    """
    Tests changing hashtype of GalleryManager instance.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_change_hashtype')
    tfactory.create_random_image('test_change_hashtype', 'random')
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype)
    assert gm.hashtype == hashtype


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_str(hashtype: str, tfactory) -> None:
    """
    Tests the str and repr representations of the GalleryManager instance.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_str')
    tfactory.create_random_image('test_str', 'random')
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype)
    cstr = f"GalleryManager[hash = {gm.hashtype}, imgs = {len(gm)}]"
    assert gm.__str__() == cstr
    # repr
    cr = f"GalleryManager(path={t_path}, hashtype={hashtype}, show_tqdm=False)"
    assert gm.__repr__() == cr


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_len(hashtype: str, tfactory) -> None:
    """
    Tests the length operation of the GalleryManager instance.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_len')
    tfactory.create_random_image('test_len', 'random')
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype)
    assert len(gm) == 1


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_gm_getitem(hashtype: str, tfactory) -> None:
    """
    Tests the overloading of the index operator in the GalleryManager instance.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_getitem')
    tfactory.create_random_image('test_getitem', 'random')
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype)
    # Indexing with int
    im1 = gm[0]
    # Indexing with ImgManager object
    im1_1 = gm[im1]
    # Indexing with path object
    im1_2 = gm[im1.path]
    # Indexing with string
    im1_3 = gm[str(im1.path)]

    assert isinstance(im1, ImgManager)
    assert im1 == im1_1 == im1_2 == im1_3

    # Invalid indexing
    with pytest.raises(KeyError):
        gm[2]


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_gm_setitem(hashtype: str, tfactory) -> None:
    """
    Tests the overloading of the index operator when setting an item
    index with a new value in the GalleryManager instance.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_setitem')
    tfactory.create_random_image('test_setitem', 'random')
    nimg = tfactory.create_random_image('test_setitem', 'random2')
    nimanager = ImgManager(path=nimg,
                           hashtype=hashtype)
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype)

    # Setting new value to path
    gm[0] = nimg
    assert gm[0] == nimanager

    # new value to ImgManager
    gm[0] = nimanager
    assert gm[0] == nimanager

    # new value to string
    gm[0] = str(nimg)
    assert gm[0] == nimanager

    # Invalid indexing
    with pytest.raises(KeyError):
        gm[2] = nimanager

    # Invalid type for value
    with pytest.raises(OperationNotSupportedError):
        gm[0] = True

    # setting to invalid path str
    with pytest.raises(InvalidPathError):
        gm[0] = "invalid/path"


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_gm_iterator(hashtype: str, tfactory) -> None:
    """
    Tests the GalleryManager iterator.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_iterator')
    tfactory.create_random_image('test_iterator', 'random')
    tfactory.create_random_image('test_iterator', 'random2')
    tfactory.create_random_image('test_iterator', 'random3')
    gm = GalleryManager(path=t_path,
                        hashtype=hashtype)

    for imanager in gm:
        assert isinstance(imanager, ImgManager)


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_gm_contains(hashtype: str, tfactory) -> None:
    """
    Tests GalleryManager's overloading of __contains__ method
    ('in' operator).

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_contains_1')
    ri1 = tfactory.create_random_image('test_contains_1', 'random')
    ri2 = tfactory.create_random_image('test_contains_1', 'random2')
    tfactory.create_random_image('test_contains_1', 'random3')
    t_path2 = tfactory.new_temp('test_contains_2')

    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)

    im2 = ImgManager(path=ri2,
                     hashtype=hashtype)
    # Indirectly test 'copy_to' operator for ImgManager
    im1.copy_to(t_path2)
    im2.copy_to(t_path2)

    gm2 = GalleryManager(path=t_path2,
                         hashtype=hashtype)
    # ImgManager test
    assert im1 in gm1
    # GalleryManager test
    assert gm2 in gm1
    # string test
    assert str(ri1) in gm1
    # list of strings test
    assert [str(ri1), str(ri2)] in gm1
    # list of ImgManager test
    assert [im1, im2] in gm1
    # list of ImgManager and strings test
    assert [im1, ri2] in gm1
    # invalid path test
    with pytest.raises(InvalidPathError):
        'invalid/path' in gm1
    with pytest.raises(InvalidPathError):
        ['invalid/path', 'invalid/path/2'] in gm1
    # Operation not supported test
    with pytest.raises(OperationNotSupportedError):
        True in gm1


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_equality(hashtype: str, tfactory) -> None:
    """
    Tests GalleryManager's equality operator along
    with some minor overloading implementations
    of length associated operators

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_eq_1')
    tfactory.create_random_image('test_eq_1', 'random')
    tfactory.create_random_image('test_eq_1', 'random2')
    tfactory.create_random_image('test_eq_1', 'random3')
    tfactory.create_random_image('test_eq_1', 'random4')
    t_path2 = tfactory.new_temp('test_eq_2')
    tfactory.create_random_image('test_eq_2', 'random')
    tfactory.create_random_image('test_eq_2', 'random2')
    tfactory.create_random_image('test_eq_2', 'random3')

    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)
    gm2 = GalleryManager(path=t_path2,
                         hashtype=hashtype)

    # Test __eq__ overloading (__ne__ implicitly calls __eq__)
    assert gm1 != gm2
    # Test greater than
    assert gm1 > gm2
    # Test less than
    assert gm2 < gm1


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_ix_ops(hashtype: str, tfactory) -> None:
    """
    tests GalleryManager's overloading of __iadd__ and
    __isub__ operators ('+=' and '-=').

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_ix1')
    ri1 = tfactory.create_random_image('test_ix1', 'random')
    ri2 = tfactory.create_random_image('test_ix1', 'random2')
    ri3 = tfactory.create_random_image('test_ix1', 'random3')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)
    im2 = ImgManager(path=ri2,
                     hashtype=hashtype)
    im3 = ImgManager(path=ri3,
                     hashtype=hashtype)
    t_path2 = tfactory.new_temp('test_ix2')
    t_path3 = tfactory.new_temp('test_ix3')
    t_path4 = tfactory.new_temp('test_ix4')

    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    # Indirectly tests 'copy_to' method of ImgManager
    im1.copy_to(t_path2)
    im2.copy_to(t_path2)
    im1.copy_to(t_path3)
    im2.copy_to(t_path3)
    im3.copy_to(t_path3)
    im1.copy_to(t_path4)
    im2.copy_to(t_path4)
    im3.copy_to(t_path4)

    gm2 = GalleryManager(path=t_path2,
                         hashtype=hashtype)

    gm3 = GalleryManager(path=t_path3,
                         hashtype=hashtype)

    gm4 = GalleryManager(path=t_path4,
                         hashtype=hashtype)

    # Test with ImgManager
    gm2 += im3
    assert im3 in gm2
    gm2 -= im3
    assert im3 not in gm2
    # Test with str
    gm2 += str(ri3)
    assert im3 in gm2
    gm2 -= str(ri3)
    assert im3 not in gm2
    # Test with GalleryManager
    gm2 += gm1
    assert im3 in gm2
    # Should duplicate already existing images so
    # gm2 has now 2 images and gm1 has 3
    assert len(gm2) == 5
    # Test error when operation would result in empty dir
    with pytest.raises(OperationResultsInEmptyDirectoryError):
        gm1 -= im1
        gm1 -= im2
        gm1 -= im3
    with pytest.raises(OperationResultsInEmptyDirectoryError):
        gm3 -= gm4

    # Test OperationNotSupported
    with pytest.raises(OperationNotSupportedError):
        gm1 += True
    with pytest.raises(OperationNotSupportedError):
        gm1 -= True

    # Test invalid path error
    with pytest.raises(InvalidPathError):
        gm1 += 'invalid/path'
    with pytest.raises(InvalidPathError):
        gm1 -= 'invalid/path/2'


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_gm_add(hashtype: str, tfactory):
    """
    Tests GalleryManager's overloading of the addition operator.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_add1')
    ri1 = tfactory.create_random_image('test_add1', 'random')
    ri2 = tfactory.create_random_image('test_add1', 'random2')
    ri3 = tfactory.create_random_image('test_add1', 'random3')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)
    im2 = ImgManager(path=ri2,
                     hashtype=hashtype)
    im3 = ImgManager(path=ri3,
                     hashtype=hashtype)
    t_path2 = tfactory.new_temp('test_add2')
    t_path3 = tfactory.new_temp('test_add3')
    t_path4 = tfactory.new_temp('test_add4')
    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    # Indirectly tests 'copy_to' method of ImgManager
    im1.copy_to(t_path2)
    im2.copy_to(t_path2)
    im1.copy_to(t_path3)
    im2.copy_to(t_path3)
    im3.copy_to(t_path3)
    im1.copy_to(t_path4)
    im2.copy_to(t_path4)
    im3.copy_to(t_path4)

    gm2 = GalleryManager(path=t_path2,
                         hashtype=hashtype)

    gm3 = GalleryManager(path=t_path3,
                         hashtype=hashtype)

    gm4 = GalleryManager(path=t_path4,
                         hashtype=hashtype)
    # Test adding ImgManager
    ext_dir = gm1.ext_dir
    gm_add1 = gm1 + im1
    assert gm_add1.ext_dir == ext_dir
    assert len(gm_add1) == len(gm1) + 1

    # Test adding str
    ext_dir = gm2.ext_dir
    gm_add2 = gm2 + str(ri3)
    assert gm_add2.ext_dir == ext_dir
    assert gm_add2 == gm3
    assert len(gm_add2) == len(gm2) + 1

    # Test adding GalleryManager
    ext_dir = gm3.ext_dir
    gm_add3 = gm3 + gm4
    assert gm_add3.ext_dir == ext_dir
    assert len(gm_add3) == len(gm3) + len(gm4)

    # Test adding invalid type
    with pytest.raises(OperationNotSupportedError):
        gm2 + True

    # Test Invalid path error
    with pytest.raises(InvalidPathError):
        gm2 + 'invalid/path'


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_gm_sub(hashtype: str, tfactory):
    """
    Tests GalleryManager's overloading of the addition operator.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_sub1')
    ri1 = tfactory.create_random_image('test_sub1', 'random')
    ri2 = tfactory.create_random_image('test_sub1', 'random2')
    ri3 = tfactory.create_random_image('test_sub1', 'random3')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)
    im2 = ImgManager(path=ri2,
                     hashtype=hashtype)
    im3 = ImgManager(path=ri3,
                     hashtype=hashtype)
    t_path2 = tfactory.new_temp('test_sub2')
    t_path3 = tfactory.new_temp('test_sub3')
    t_path4 = tfactory.new_temp('test_sub4')
    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    # Indirectly tests 'copy_to' method of ImgManager
    im1.copy_to(t_path2)
    im2.copy_to(t_path2)
    im1.copy_to(t_path3)
    im2.copy_to(t_path3)
    im3.copy_to(t_path3)
    im1.copy_to(t_path4)
    im2.copy_to(t_path4)
    im3.copy_to(t_path4)

    gm2 = GalleryManager(path=t_path2,
                         hashtype=hashtype)

    gm3 = GalleryManager(path=t_path3,
                         hashtype=hashtype)

    gm4 = GalleryManager(path=t_path4,
                         hashtype=hashtype)
    # Test subtracting ImgManager
    ext_dir = gm1.ext_dir
    gm_sub1 = gm1 - im3
    assert gm_sub1.ext_dir == ext_dir
    assert len(gm_sub1) == len(gm1) - 1
    assert im3 not in gm_sub1

    # Test subtracting str
    ext_dir = gm3.ext_dir
    gm_sub2 = gm2 - str(ri2)
    assert gm_sub2.ext_dir == ext_dir
    assert len(gm_sub2) == len(gm2) - 1
    assert im3 not in gm_sub2

    # Test subtracting GalleryManager
    t_sub_gm = tfactory.new_temp("sub_gm")
    subr1 = tfactory.create_random_image('sub_gm', 'random')
    tfactory.create_random_image('sub_gm', 'random2')
    t_sub_gm2 = tfactory.new_temp('sub_gm2')

    subgm1 = GalleryManager(path=t_sub_gm,
                            hashtype=hashtype)
    subim1 = ImgManager(path=subr1,
                        hashtype=hashtype)
    subim1.copy_to(t_sub_gm2)
    subgm2 = GalleryManager(path=t_sub_gm2,
                            hashtype=hashtype)
    ext_dir = subgm1.ext_dir
    gm_sub3 = subgm1 - subgm2
    assert gm_sub3.ext_dir == ext_dir
    assert len(gm_sub3) == len(subgm1) - len(subgm2)
    assert subim1 not in gm_sub3

    # Test subtracting resulting in empty dir
    with pytest.raises(OperationResultsInEmptyDirectoryError):
        gm3 - gm4

    # Test Operation not supported
    with pytest.raises(OperationNotSupportedError):
        gm1 - True

    # Test invalid path
    with pytest.raises(InvalidPathError):
        gm1 - 'invalid/path'


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_html_gallery(hashtype: str, tfactory):
    """
    Tests the 'to_html_img_gallery' method of GalleryManager.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_html1')
    tfactory.create_random_image('test_html1', 'random')
    t_path2 = tfactory.new_temp('test_html2')
    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    # Test saving file
    save_path, fstr = gm1.to_html_img_gallery(str(t_path2),
                                              separate_elements=False)
    assert save_path.exists()
    assert save_path.is_file()
    assert isinstance(fstr, str)

    # Test returning elements
    html_head, html_body = gm1.to_html_img_gallery(str(t_path2),
                                                   separate_elements=True)
    assert isinstance(html_head, str)
    assert isinstance(html_body, str)


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_duplicates(hashtype: str, tfactory):
    """
    Tests the 'delete_duplicates' method of GalleryManager.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_duplicates')
    ri1 = tfactory.create_random_image('test_duplicates', 'random')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)

    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    gm1 += im1
    # Test deleting one duplicate
    gm1.delete_duplicates()
    assert len(gm1) == 1
    assert im1 in gm1

    # Test deleting multiple duplicates
    gm1 += im1
    gm1 += im1
    gm1.delete_duplicates()
    assert len(gm1) == 1
    assert im1 in gm1


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_resize(hashtype: str, tfactory):
    """
    Tests the 'resize_all' method of GalleryManager.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_resize')
    ri1 = tfactory.create_random_image('test_resize', 'random')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)
    init_size = im1.dim
    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)

    t_path2 = tfactory.new_temp('test_resize2')
    t_path3 = tfactory.new_temp('test_resize3')

    # Test with inplace being False
    gm2 = gm1.resize_all(max_size=100,
                         keep_aspect_ratio=False,
                         size=(300, 300),
                         inplace=False,
                         output_dir=t_path2)
    assert isinstance(gm2, GalleryManager)
    assert gm2[0].dim == (300, 300)
    assert init_size == (100, 100)

    # Aspect Ratio
    gm3 = gm1.resize_all(max_size=300,
                         keep_aspect_ratio=True,
                         size=None,
                         inplace=False,
                         output_dir=t_path3)
    assert isinstance(gm3, GalleryManager)
    assert gm3[0].width == 300 or gm3[0].heigh == 300
    assert init_size == (100, 100)

    # Test with inplace being true
    gm1.resize_all(max_size=300,
                   keep_aspect_ratio=False,
                   size=(300, 300),
                   inplace=True,
                   output_dir=None)

    assert gm1[0].dim == (300, 300)
    assert init_size == (100, 100)

    # Aspect Ratio
    gm1.resize_all(max_size=400,
                   keep_aspect_ratio=True,
                   size=None,
                   inplace=True,
                   output_dir=None)

    assert gm1[0].width == 400 or gm1[0].height == 400


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_imanager_index(hashtype: str, tfactory):
    """
    Tests the 'get_img_manager_index' method of GalleryManager.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    t_path = tfactory.new_temp('test_managerindex')
    ri1 = tfactory.create_random_image('test_managerindex', 'random')
    ri2 = tfactory.create_random_image('test_managerindex', 'random2')
    tfactory.new_temp('test_managerindex2')
    ri3 = tfactory.create_random_image('test_managerindex2', 'random4')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)
    im2 = ImgManager(path=ri2,
                     hashtype=hashtype)
    im3 = ImgManager(path=ri3,
                     hashtype=hashtype)
    gm1 = GalleryManager(path=t_path,
                         hashtype=hashtype)
    imanagers = gm1.img_managers

    # Test normal functioning
    res1 = gm1.get_img_manager_index(im1)
    res2 = gm1.get_img_manager_index(im2)
    assert res1 == 0
    assert res2 == 1
    assert gm1[res1] == im1 == imanagers[res1]
    assert gm1[res2] == im2 == imanagers[res2]

    # Test Key Error
    with pytest.raises(KeyError):
        gm1.get_img_manager_index(im3)

# --------------
# -------------- Test TmpManager


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_tmp_manager(hashtype: str, tfactory):
    """
    Tests initalization of the TmpManager class.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    # Test with output dir
    tfactory.new_temp('test_tmpmanager')
    ri1 = tfactory.create_random_image('test_tmpmanager', 'random')
    t_path2 = tfactory.new_temp('test_tmpmanager2')
    im1 = ImgManager(path=ri1,
                     hashtype=hashtype)
    tmp_p = []
    with TmpManager(hashtype=hashtype,
                    save_content_on_deletion=True,
                    output_dir=t_path2) as tmp:
        assert tmp.tmp_path.exists()
        tmp += im1
        assert im1 in tmp
        tmp_p.append(tmp.tmp_path)
    assert not tmp_p[0].exists()
    gm = GalleryManager(path=t_path2,
                        hashtype=hashtype)
    assert im1 in gm and len(gm) == 1
    # Test with no output dir
    with TmpManager(hashtype=hashtype,
                    save_content_on_deletion=False) as tmp:
        assert tmp.tmp_path.exists()
        tmp_p.append(tmp.tmp_path)
        tmp += im1
        assert im1 in tmp
    assert not tmp_p[1].exists()

    # Test with invalid output dir
    with pytest.raises(InvalidInputError):
        with TmpManager(hashtype=hashtype,
                        save_content_on_deletion=True,
                        output_dir='invalid/path') as tmp:
            tmp += im1


@pytest.mark.parametrize("hashtype", hashtype_lst)
def test_tmp_cleanup(hashtype: str):
    """
    Tests cleanup of the TmpManager class when using the deletion operator,
    also tests TmpManager's overloading of the str and repr methods.

    Parameters
    ----------
    hashtype : str
               What type of hashing function the instance will use.
    """
    tmp_manager = TmpManager(hashtype=hashtype,
                             save_content_on_deletion=False)
    p = f"Path:{tmp_manager.tmp_path};"
    o = f"Opened:{tmp_manager.is_open}"
    es1 = f"TmpManager[{p} {o}]"
    assert str(tmp_manager) == es1
    sc = 'save_content_on_deletion=False'
    assert f"TmpManager(hashtype={hashtype},{sc},output_dir=None)"
    tmp_manager.__enter__()
    tmp_path = tmp_manager.tmp_path
    assert tmp_path.exists()
    p = f"Path:{tmp_manager.tmp_path};"
    o = f"Opened:{tmp_manager.is_open}"
    es2 = f"TmpManager[{p} {o}]"
    assert str(tmp_manager) == es2
    assert f"TmpManager(hashtype={hashtype},{sc},output_dir=None)"
    del tmp_manager
    assert not tmp_path.exists()

# --------------
