from conftest import TempDirFactory
from conftest import CLOUDFARE_ACC_HASH
from pathlib import Path
from charloratools.FilterAI import FaceRecognizer


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


def test_face_recognizer(tfactory: TempDirFactory) -> None:
    """
    Tests initialization and basic functionality of the FaceRecognizer instance
    such as the __str__ and __repr__ methods.
    """
    t_path = setup_img_dir(tfactory, 'test_fr_init')
    fr = FaceRecognizer(path=t_path)
    assert isinstance(fr, FaceRecognizer)
    # Test str
    p = f"Path:{fr.path};"
    i = f"Images:{len(fr.gallery)};"
    d = f"Torch Device:{fr.device};"
    es = f"FaceRecognizer[{p} {i} {d}]"
    assert str(fr) == es

    # Test repr
    er = f"FaceRecognizer(path={t_path})"
    assert fr.__repr__() == er


def test_filter_without_face(tfactory: TempDirFactory) -> None:
    """
    Tests the 'filter_images_without_face' method of
    FaceRecognizer
    """
    t_path = setup_img_dir(tfactory, 'test_filter_without_face')
    t_path2 = tfactory.new_temp('test_filter_without_face2')

    fr = FaceRecognizer(t_path)

    gm = fr.filter_images_without_face(output_dir=t_path2,
                                       min_face_size=20,
                                       prob_threshold=0.8,
                                       return_info=False)

    assert len(gm) == 3

    # Repeat tests for return_info=True
    (gm, info_dict) = fr.filter_images_without_face(output_dir=t_path2,
                                                    min_face_size=20,
                                                    prob_threshold=0.8,
                                                    return_info=True)

    assert len(gm) == 3
    assert isinstance(info_dict, dict)
    assert 'info_dict_lst' in info_dict.keys()


def test_filter_multiple_face(tfactory: TempDirFactory) -> None:
    """
    Tests the 'filter_images_with_multiple_faces' method of
    FaceRecognizer
    """
    t_path = setup_img_dir(tfactory, 'test_filter_multiple_face')
    t_path2 = tfactory.new_temp('test_filter_multiple_face2')

    fr = FaceRecognizer(t_path)

    gm = fr.filter_images_with_multiple_faces(output_dir=t_path2,
                                              min_face_size=20,
                                              prob_threshold=0.9,
                                              return_info=False)

    assert len(gm) == 2

    # Repeat tests for return_info=True
    (gm, info_dict) = fr.filter_images_without_face(output_dir=t_path2,
                                                    min_face_size=20,
                                                    prob_threshold=0.9,
                                                    return_info=True)

    assert len(gm) == 2
    assert isinstance(info_dict, dict)
    assert 'info_dict_lst' in info_dict.keys()


def test_filter_ref(tfactory: TempDirFactory) -> None:
    """
    Tests the 'filter_images_without_specific_face' method of
    FaceRecognizer
    """
    t_path = setup_img_dir(tfactory, 'test_filter_ref_face')
    t_path2 = tfactory.new_temp('test_filter_ref_face2')
    face1_path = t_path / 'test_face1.jpg'

    fr = FaceRecognizer(t_path)
    pm = 'vggface2'
    gm = fr.filter_images_without_specific_face(face1_path,
                                                t_path2,
                                                None,
                                                20,
                                                0.6,
                                                pm,
                                                'cosine',
                                                False)

    assert len(gm) == 1

    # Repeat tests for return_info=True
    (gm, info_dict) = fr.filter_images_without_specific_face(face1_path,
                                                             t_path2,
                                                             None,
                                                             20,
                                                             0.6,
                                                             pm,
                                                             'cosine',
                                                             True)

    assert len(gm) == 1
    assert isinstance(info_dict, dict)
    assert 'info_dict_lst' in info_dict.keys()


def test_save_images_with_detection_box(tfactory: TempDirFactory) -> None:
    """
    Tests the 'save_images_with_detection_box' method of
    FaceRecognizer
    """
    t_path = setup_img_dir(tfactory, 'test_detection_box')
    t_path2 = tfactory.new_temp('test_detection_box2')
    t_path3 = tfactory.new_temp('test_detection_box3')
    fr = FaceRecognizer(t_path)
    (gm, info_dict) = fr.filter_images_without_face(output_dir=t_path2,
                                                    min_face_size=20,
                                                    prob_threshold=0.8,
                                                    return_info=True)
    idlst = info_dict['info_dict_lst']
    # save_only_matched=False
    gm2 = fr.save_images_with_detection_box(idlst,
                                            t_path2,
                                            False)
    assert len(gm2) == 4

    # save_only_matched=True
    gm3 = fr.save_images_with_detection_box(idlst,
                                            t_path3,
                                            True)
    assert len(gm3) == 3
