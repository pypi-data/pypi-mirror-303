__version__ = "3.4.20"

if __package__ or "." in __name__:
    from . import _DynamsoftCore
else:
    import _DynamsoftCore

from typing import List
from enum import Enum, IntEnum
from abc import ABC, abstractmethod

class EnumErrorCode(IntEnum):
    EC_OK = _DynamsoftCore.EC_OK
    EC_UNKNOWN = _DynamsoftCore.EC_UNKNOWN
    EC_NO_MEMORY = _DynamsoftCore.EC_NO_MEMORY
    EC_NULL_POINTER = _DynamsoftCore.EC_NULL_POINTER
    EC_LICENSE_INVALID = _DynamsoftCore.EC_LICENSE_INVALID
    EC_LICENSE_EXPIRED = _DynamsoftCore.EC_LICENSE_EXPIRED
    EC_FILE_NOT_FOUND = _DynamsoftCore.EC_FILE_NOT_FOUND
    EC_FILE_TYPE_NOT_SUPPORTED = _DynamsoftCore.EC_FILE_TYPE_NOT_SUPPORTED
    EC_BPP_NOT_SUPPORTED = _DynamsoftCore.EC_BPP_NOT_SUPPORTED
    EC_INDEX_INVALID = _DynamsoftCore.EC_INDEX_INVALID
    EC_CUSTOM_REGION_INVALID = _DynamsoftCore.EC_CUSTOM_REGION_INVALID
    EC_IMAGE_READ_FAILED = _DynamsoftCore.EC_IMAGE_READ_FAILED
    EC_TIFF_READ_FAILED = _DynamsoftCore.EC_TIFF_READ_FAILED
    EC_DIB_BUFFER_INVALID = _DynamsoftCore.EC_DIB_BUFFER_INVALID
    EC_PDF_READ_FAILED = _DynamsoftCore.EC_PDF_READ_FAILED
    EC_PDF_DLL_MISSING = _DynamsoftCore.EC_PDF_DLL_MISSING
    EC_PAGE_NUMBER_INVALID = _DynamsoftCore.EC_PAGE_NUMBER_INVALID
    EC_CUSTOM_SIZE_INVALID = _DynamsoftCore.EC_CUSTOM_SIZE_INVALID
    EC_TIMEOUT = _DynamsoftCore.EC_TIMEOUT
    EC_JSON_PARSE_FAILED = _DynamsoftCore.EC_JSON_PARSE_FAILED
    EC_JSON_TYPE_INVALID = _DynamsoftCore.EC_JSON_TYPE_INVALID
    EC_JSON_KEY_INVALID = _DynamsoftCore.EC_JSON_KEY_INVALID
    EC_JSON_VALUE_INVALID = _DynamsoftCore.EC_JSON_VALUE_INVALID
    EC_JSON_NAME_KEY_MISSING = _DynamsoftCore.EC_JSON_NAME_KEY_MISSING
    EC_JSON_NAME_VALUE_DUPLICATED = _DynamsoftCore.EC_JSON_NAME_VALUE_DUPLICATED
    EC_TEMPLATE_NAME_INVALID = _DynamsoftCore.EC_TEMPLATE_NAME_INVALID
    EC_JSON_NAME_REFERENCE_INVALID = _DynamsoftCore.EC_JSON_NAME_REFERENCE_INVALID
    EC_PARAMETER_VALUE_INVALID = _DynamsoftCore.EC_PARAMETER_VALUE_INVALID
    EC_DOMAIN_NOT_MATCH = _DynamsoftCore.EC_DOMAIN_NOT_MATCH
    EC_RESERVED_INFO_NOT_MATCH = _DynamsoftCore.EC_RESERVED_INFO_NOT_MATCH
    EC_LICENSE_KEY_NOT_MATCH = _DynamsoftCore.EC_LICENSE_KEY_NOT_MATCH
    EC_REQUEST_FAILED = _DynamsoftCore.EC_REQUEST_FAILED
    EC_LICENSE_INIT_FAILED = _DynamsoftCore.EC_LICENSE_INIT_FAILED
    EC_SET_MODE_ARGUMENT_ERROR = _DynamsoftCore.EC_SET_MODE_ARGUMENT_ERROR
    EC_LICENSE_CONTENT_INVALID = _DynamsoftCore.EC_LICENSE_CONTENT_INVALID
    EC_LICENSE_KEY_INVALID = _DynamsoftCore.EC_LICENSE_KEY_INVALID
    EC_LICENSE_DEVICE_RUNS_OUT = _DynamsoftCore.EC_LICENSE_DEVICE_RUNS_OUT
    EC_GET_MODE_ARGUMENT_ERROR = _DynamsoftCore.EC_GET_MODE_ARGUMENT_ERROR
    EC_IRT_LICENSE_INVALID = _DynamsoftCore.EC_IRT_LICENSE_INVALID
    EC_FILE_SAVE_FAILED = _DynamsoftCore.EC_FILE_SAVE_FAILED
    EC_STAGE_TYPE_INVALID = _DynamsoftCore.EC_STAGE_TYPE_INVALID
    EC_IMAGE_ORIENTATION_INVALID = _DynamsoftCore.EC_IMAGE_ORIENTATION_INVALID
    EC_CONVERT_COMPLEX_TEMPLATE_ERROR = _DynamsoftCore.EC_CONVERT_COMPLEX_TEMPLATE_ERROR
    EC_CALL_REJECTED_WHEN_CAPTURING = _DynamsoftCore.EC_CALL_REJECTED_WHEN_CAPTURING
    EC_NO_IMAGE_SOURCE = _DynamsoftCore.EC_NO_IMAGE_SOURCE
    EC_READ_DIRECTORY_FAILED = _DynamsoftCore.EC_READ_DIRECTORY_FAILED
    EC_MODULE_NOT_FOUND = _DynamsoftCore.EC_MODULE_NOT_FOUND
    EC_MULTI_PAGES_NOT_SUPPORTED = _DynamsoftCore.EC_MULTI_PAGES_NOT_SUPPORTED
    EC_FILE_ALREADY_EXISTS = _DynamsoftCore.EC_FILE_ALREADY_EXISTS
    EC_CREATE_FILE_FAILED = _DynamsoftCore.EC_CREATE_FILE_FAILED
    EC_IMAGE_DATA_INVALID = _DynamsoftCore.EC_IMAGE_DATA_INVALID
    EC_IMAGE_SIZE_NOT_MATCH = _DynamsoftCore.EC_IMAGE_SIZE_NOT_MATCH
    EC_IMAGE_PIXEL_FORMAT_NOT_MATCH = _DynamsoftCore.EC_IMAGE_PIXEL_FORMAT_NOT_MATCH
    EC_SECTION_LEVEL_RESULT_IRREPLACEABLE = (
        _DynamsoftCore.EC_SECTION_LEVEL_RESULT_IRREPLACEABLE
    )
    EC_AXIS_DEFINITION_INCORRECT = _DynamsoftCore.EC_AXIS_DEFINITION_INCORRECT
    EC_RESULT_TYPE_MISMATCH_IRREPLACEABLE = (
        _DynamsoftCore.EC_RESULT_TYPE_MISMATCH_IRREPLACEABLE
    )
    EC_PDF_LIBRARY_LOAD_FAILED = _DynamsoftCore.EC_PDF_LIBRARY_LOAD_FAILED
    EC_LICENSE_WARNING = _DynamsoftCore.EC_LICENSE_WARNING
    EC_NO_LICENSE = _DynamsoftCore.EC_NO_LICENSE
    EC_HANDSHAKE_CODE_INVALID = _DynamsoftCore.EC_HANDSHAKE_CODE_INVALID
    EC_LICENSE_BUFFER_FAILED = _DynamsoftCore.EC_LICENSE_BUFFER_FAILED
    EC_LICENSE_SYNC_FAILED = _DynamsoftCore.EC_LICENSE_SYNC_FAILED
    EC_DEVICE_NOT_MATCH = _DynamsoftCore.EC_DEVICE_NOT_MATCH
    EC_BIND_DEVICE_FAILED = _DynamsoftCore.EC_BIND_DEVICE_FAILED
    EC_LICENSE_CLIENT_DLL_MISSING = _DynamsoftCore.EC_LICENSE_CLIENT_DLL_MISSING
    EC_INSTANCE_COUNT_OVER_LIMIT = _DynamsoftCore.EC_INSTANCE_COUNT_OVER_LIMIT
    EC_LICENSE_INIT_SEQUENCE_FAILED = _DynamsoftCore.EC_LICENSE_INIT_SEQUENCE_FAILED
    EC_TRIAL_LICENSE = _DynamsoftCore.EC_TRIAL_LICENSE
    EC_LICENSE_VERSION_NOT_MATCH = _DynamsoftCore.EC_LICENSE_VERSION_NOT_MATCH
    EC_LICENSE_CACHE_USED = _DynamsoftCore.EC_LICENSE_CACHE_USED
    EC_FAILED_TO_REACH_DLS = _DynamsoftCore.EC_FAILED_TO_REACH_DLS
    EC_BARCODE_FORMAT_INVALID = _DynamsoftCore.EC_BARCODE_FORMAT_INVALID
    EC_QR_LICENSE_INVALID = _DynamsoftCore.EC_QR_LICENSE_INVALID
    EC_1D_LICENSE_INVALID = _DynamsoftCore.EC_1D_LICENSE_INVALID
    EC_PDF417_LICENSE_INVALID = _DynamsoftCore.EC_PDF417_LICENSE_INVALID
    EC_DATAMATRIX_LICENSE_INVALID = _DynamsoftCore.EC_DATAMATRIX_LICENSE_INVALID
    EC_CUSTOM_MODULESIZE_INVALID = _DynamsoftCore.EC_CUSTOM_MODULESIZE_INVALID
    EC_AZTEC_LICENSE_INVALID = _DynamsoftCore.EC_AZTEC_LICENSE_INVALID
    EC_PATCHCODE_LICENSE_INVALID = _DynamsoftCore.EC_PATCHCODE_LICENSE_INVALID
    EC_POSTALCODE_LICENSE_INVALID = _DynamsoftCore.EC_POSTALCODE_LICENSE_INVALID
    EC_DPM_LICENSE_INVALID = _DynamsoftCore.EC_DPM_LICENSE_INVALID
    EC_FRAME_DECODING_THREAD_EXISTS = _DynamsoftCore.EC_FRAME_DECODING_THREAD_EXISTS
    EC_STOP_DECODING_THREAD_FAILED = _DynamsoftCore.EC_STOP_DECODING_THREAD_FAILED
    EC_MAXICODE_LICENSE_INVALID = _DynamsoftCore.EC_MAXICODE_LICENSE_INVALID
    EC_GS1_DATABAR_LICENSE_INVALID = _DynamsoftCore.EC_GS1_DATABAR_LICENSE_INVALID
    EC_GS1_COMPOSITE_LICENSE_INVALID = _DynamsoftCore.EC_GS1_COMPOSITE_LICENSE_INVALID
    EC_DOTCODE_LICENSE_INVALID = _DynamsoftCore.EC_DOTCODE_LICENSE_INVALID
    EC_PHARMACODE_LICENSE_INVALID = _DynamsoftCore.EC_PHARMACODE_LICENSE_INVALID
    EC_BARCODE_READER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_BARCODE_READER_LICENSE_NOT_FOUND
    EC_CHARACTER_MODEL_FILE_NOT_FOUND = _DynamsoftCore.EC_CHARACTER_MODEL_FILE_NOT_FOUND
    EC_TEXT_LINE_GROUP_LAYOUT_CONFLICT = (
        _DynamsoftCore.EC_TEXT_LINE_GROUP_LAYOUT_CONFLICT
    )
    EC_TEXT_LINE_GROUP_REGEX_CONFLICT = _DynamsoftCore.EC_TEXT_LINE_GROUP_REGEX_CONFLICT
    EC_LABEL_RECOGNIZER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_LABEL_RECOGNIZER_LICENSE_NOT_FOUND
    EC_QUADRILATERAL_INVALID = _DynamsoftCore.EC_QUADRILATERAL_INVALID
    EC_DOCUMENT_NORMALIZER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_DOCUMENT_NORMALIZER_LICENSE_NOT_FOUND
    EC_PANORAMA_LICENSE_INVALID = _DynamsoftCore.EC_PANORAMA_LICENSE_INVALID
    EC_RESOURCE_PATH_NOT_EXIST = _DynamsoftCore.EC_RESOURCE_PATH_NOT_EXIST
    EC_RESOURCE_LOAD_FAILED = _DynamsoftCore.EC_RESOURCE_LOAD_FAILED
    EC_CODE_SPECIFICATION_NOT_FOUND = _DynamsoftCore.EC_CODE_SPECIFICATION_NOT_FOUND
    EC_FULL_CODE_EMPTY = _DynamsoftCore.EC_FULL_CODE_EMPTY
    EC_FULL_CODE_PREPROCESS_FAILED = _DynamsoftCore.EC_FULL_CODE_PREPROCESS_FAILED
    EC_ZA_DL_LICENSE_INVALID = _DynamsoftCore.EC_ZA_DL_LICENSE_INVALID
    EC_AAMVA_DL_ID_LICENSE_INVALID = _DynamsoftCore.EC_AAMVA_DL_ID_LICENSE_INVALID
    EC_AADHAAR_LICENSE_INVALID = _DynamsoftCore.EC_AADHAAR_LICENSE_INVALID
    EC_MRTD_LICENSE_INVALID = _DynamsoftCore.EC_MRTD_LICENSE_INVALID
    EC_VIN_LICENSE_INVALID = _DynamsoftCore.EC_VIN_LICENSE_INVALID
    EC_CUSTOMIZED_CODE_TYPE_LICENSE_INVALID = (
        _DynamsoftCore.EC_CUSTOMIZED_CODE_TYPE_LICENSE_INVALID
    )
    EC_CODE_PARSER_LICENSE_NOT_FOUND = _DynamsoftCore.EC_CODE_PARSER_LICENSE_NOT_FOUND


class EnumImagePixelFormat(IntEnum):
    IPF_BINARY = _DynamsoftCore.IPF_BINARY
    IPF_BINARYINVERTED = _DynamsoftCore.IPF_BINARYINVERTED
    IPF_GRAYSCALED = _DynamsoftCore.IPF_GRAYSCALED
    IPF_NV21 = _DynamsoftCore.IPF_NV21
    IPF_RGB_565 = _DynamsoftCore.IPF_RGB_565
    IPF_RGB_555 = _DynamsoftCore.IPF_RGB_555
    IPF_RGB_888 = _DynamsoftCore.IPF_RGB_888
    IPF_ARGB_8888 = _DynamsoftCore.IPF_ARGB_8888
    IPF_RGB_161616 = _DynamsoftCore.IPF_RGB_161616
    IPF_ARGB_16161616 = _DynamsoftCore.IPF_ARGB_16161616
    IPF_ABGR_8888 = _DynamsoftCore.IPF_ABGR_8888
    IPF_ABGR_16161616 = _DynamsoftCore.IPF_ABGR_16161616
    IPF_BGR_888 = _DynamsoftCore.IPF_BGR_888
    IPF_BINARY_8 = _DynamsoftCore.IPF_BINARY_8
    IPF_NV12 = _DynamsoftCore.IPF_NV12
    IPF_BINARY_8_INVERTED = _DynamsoftCore.IPF_BINARY_8_INVERTED


class EnumGrayscaleTransformationMode(IntEnum):
    GTM_INVERTED = _DynamsoftCore.GTM_INVERTED
    GTM_ORIGINAL = _DynamsoftCore.GTM_ORIGINAL
    GTM_AUTO = _DynamsoftCore.GTM_AUTO
    GTM_REV = _DynamsoftCore.GTM_REV
    GTM_SKIP = _DynamsoftCore.GTM_SKIP


class EnumGrayscaleEnhancementMode(IntEnum):
    GEM_AUTO = _DynamsoftCore.GEM_AUTO
    GEM_GENERAL = _DynamsoftCore.GEM_GENERAL
    GEM_GRAY_EQUALIZE = _DynamsoftCore.GEM_GRAY_EQUALIZE
    GEM_GRAY_SMOOTH = _DynamsoftCore.GEM_GRAY_SMOOTH
    GEM_SHARPEN_SMOOTH = _DynamsoftCore.GEM_SHARPEN_SMOOTH
    GEM_REV = _DynamsoftCore.GEM_REV
    GEM_SKIP = _DynamsoftCore.GEM_SKIP


class EnumPDFReadingMode(IntEnum):
    PDFRM_VECTOR = _DynamsoftCore.PDFRM_VECTOR
    PDFRM_RASTER = _DynamsoftCore.PDFRM_RASTER
    PDFRM_REV = _DynamsoftCore.PDFRM_REV


class EnumRasterDataSource(IntEnum):
    RDS_RASTERIZED_PAGES = _DynamsoftCore.RDS_RASTERIZED_PAGES
    RDS_EXTRACTED_IMAGES = _DynamsoftCore.RDS_EXTRACTED_IMAGES


class EnumCapturedResultItemType(IntEnum):
    CRIT_ORIGINAL_IMAGE = _DynamsoftCore.CRIT_ORIGINAL_IMAGE
    CRIT_BARCODE = _DynamsoftCore.CRIT_BARCODE
    CRIT_TEXT_LINE = _DynamsoftCore.CRIT_TEXT_LINE
    CRIT_DETECTED_QUAD = _DynamsoftCore.CRIT_DETECTED_QUAD
    CRIT_NORMALIZED_IMAGE = _DynamsoftCore.CRIT_NORMALIZED_IMAGE
    CRIT_PARSED_RESULT = _DynamsoftCore.CRIT_PARSED_RESULT


class EnumBufferOverflowProtectionMode(IntEnum):
    BOPM_BLOCK = _DynamsoftCore.BOPM_BLOCK
    BOPM_UPDATE = _DynamsoftCore.BOPM_UPDATE


class EnumImageTagType(IntEnum):
    ITT_FILE_IMAGE = _DynamsoftCore.ITT_FILE_IMAGE
    ITT_VIDEO_FRAME = _DynamsoftCore.ITT_VIDEO_FRAME


class EnumVideoFrameQuality(IntEnum):
    VFQ_HIGH = _DynamsoftCore.VFQ_HIGH
    VFQ_LOW = _DynamsoftCore.VFQ_LOW
    VFQ_UNKNOWN = _DynamsoftCore.VFQ_UNKNOWN


class EnumImageCaptureDistanceMode(IntEnum):
    ICDM_NEAR = _DynamsoftCore.ICDM_NEAR
    ICDM_FAR = _DynamsoftCore.ICDM_FAR


class EnumColourChannelUsageType(IntEnum):
    CCUT_AUTO = _DynamsoftCore.CCUT_AUTO
    CCUT_FULL_CHANNEL = _DynamsoftCore.CCUT_FULL_CHANNEL
    CCUT_Y_CHANNEL_ONLY = _DynamsoftCore.CCUT_Y_CHANNEL_ONLY
    CCUT_RGB_R_CHANNEL_ONLY = _DynamsoftCore.CCUT_RGB_R_CHANNEL_ONLY
    CCUT_RGB_G_CHANNEL_ONLY = _DynamsoftCore.CCUT_RGB_G_CHANNEL_ONLY
    CCUT_RGB_B_CHANNEL_ONLY = _DynamsoftCore.CCUT_RGB_B_CHANNEL_ONLY

class CoreModule(object):
    """
    The CoreModule class defines general functions in the core module.

    Methods:
        get_version() -> str: Returns a string representing the version of the core module.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns a string representing the version of the core module.

        Returns:
            str: A string representing the version of the core module.
        """
        return __version__ + " (Algotithm " + _DynamsoftCore.CCoreModule_GetVersion() + ")"


    def __init__(self):
        _DynamsoftCore.CCoreModule_init(self, _DynamsoftCore.new_CCoreModule())

    __destroy__ = _DynamsoftCore.delete_CCoreModule


_DynamsoftCore.CCoreModule_register(CoreModule)


class Point(object):
    """
    A class representing a point in 2D space.

    Attributes:
        x (int): The x coordinate of the point.
        y (int): The y coordinate of the point.

    Methods:
        distance_to(self, pt: 'Point') -> float: Calculates the distance between the current point and the specified target point.
        transform_coordinates(original_point: 'Point', transformation_matrix: List[float]) -> 'Point': Transforms the coordinates of a point using a given transformation matrix.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    x: int = property(_DynamsoftCore.CPoint_Getx, _DynamsoftCore.CPoint_Setx)
    y: int = property(_DynamsoftCore.CPoint_Gety, _DynamsoftCore.CPoint_Sety)

    def __init__(self, x: int = 0, y: int = 0):
        """
        Constructs a Point object.

        Args:
            x (int, optional): The x coordinate of the point. Defaults to 0.
            y (int, optional): The y coordinate of the point. Defaults to 0.
        """
        _DynamsoftCore.CPoint_init(self, _DynamsoftCore.new_CPoint(x,y))

    __destroy__ = _DynamsoftCore.delete_CPoint

    def distance_to(self, pt: "Point") -> float:
        """
        Calculates the distance between the current point and the specified target point.

        Args:
            pt: The target point to which the distance is calculated.

        Returns:
            A value representing the distance between the current point and the specified target point.
        """
        return _DynamsoftCore.CPoint_DistanceTo(self, pt)

    @staticmethod
    def transform_coordinates(original_point: "Point", transformation_matrix: List[float]) -> "Point":
        """
        Transforms the coordinates of a point using a given transformation matrix.

        Args:
            original_point: The original point to transform.
            transformation_matrix: The transformation matrix to apply to the coordinates.

        Returns:
            A new Point object with the transformed coordinates.
        """
        return _DynamsoftCore.CPoint_TransformCoordinates(
            original_point, transformation_matrix
        )


_DynamsoftCore.CPoint_register(Point)

class Quadrilateral(object):
    """
    A quadrilateral.

    Attributes:
        points: A Point list of length 4 that define the quadrilateral.

    Methods:
        contains(self, point: 'Point') -> bool: Determines whether a point is inside the quadrilateral.
        get_area(self) -> int: Gets the area of the quadrilateral.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    points: List[Point] = property(
        _DynamsoftCore.CQuadrilateral_points_get,
        _DynamsoftCore.CQuadrilateral_points_set,
    )

    def contains(self, point: "Point") -> bool:
        """
        Determines whether a point is inside the quadrilateral.

        Args:
            point: The point to test.

        Returns:
            True if the point inside the quadrilateral, False otherwise.
        """
        return _DynamsoftCore.CQuadrilateral_Contains(self, point)

    def get_area(self) -> int:
        """
        Gets the area of the quadrilateral.

        Returns:
            The area of the quadrilateral.
        """
        return _DynamsoftCore.CQuadrilateral_GetArea(self)

    def __init__(self):
        """
        Initializes a new instance of the Quadrilateral class with default values.
        """
        _DynamsoftCore.CQuadrilateral_init(self, _DynamsoftCore.new_CQuadrilateral())

    __destroy__ = _DynamsoftCore.delete_CQuadrilateral

_DynamsoftCore.CQuadrilateral_register(Quadrilateral)


class Rect(object):
    """
    The Rect class represents a rectangle in 2D space.

    Attributes:
        top (int): The top coordinate of the rectangle.
        left (int): The left coordinate of the rectangle.
        right (int): The right coordinate of the rectangle.
        bottom (int): The bottom coordinate of the rectangle.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    top: int = property(_DynamsoftCore.CRect_top_get, _DynamsoftCore.CRect_top_set)
    left: int = property(_DynamsoftCore.CRect_left_get, _DynamsoftCore.CRect_left_set)
    right: int = property(_DynamsoftCore.CRect_right_get, _DynamsoftCore.CRect_right_set)
    bottom: int = property(_DynamsoftCore.CRect_bottom_get, _DynamsoftCore.CRect_bottom_set)

    def __init__(self):
        _DynamsoftCore.CRect_init(self, _DynamsoftCore.new_CRect())

    __destroy__ = _DynamsoftCore.delete_CRect


_DynamsoftCore.CRect_register(Rect)

class ImageTag(ABC):
    """
    ImageTag represents an image tag that can be attached to an image in a system.
    It contains information about the image, such as the image ID and the image capture distance mode.

    Methods:
        __init__(self): Initializes a new instance of the ImageTag class.
        get_type(self) -> int: Gets the type of the image tag.
        clone(self) -> ImageTag: Creates a copy of the image tag.
        get_image_id(self) -> int: Gets the ID of the image.
        set_image_id(self, imgId: int) -> None: Sets the ID of the image.
        get_image_capture_distance_mode(self) -> int: Gets the capture distance mode of the image.
        set_image_capture_distance_mode(self, mode: int) -> None: Sets the capture distance mode of the image.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        """
        Initializes a new instance of the ImageTag class.
        """

        _DynamsoftCore.CRect_init(self, _DynamsoftCore.new_CImageTag(self))

    __destroy__ = _DynamsoftCore.delete_CImageTag

    @abstractmethod
    def get_type(self) -> int:
        """
        Gets the type of the image tag.

        Returns:
            int: The type of the image tag.
        """
        pass
        return _DynamsoftCore.CImageTag_GetType(self)

    @abstractmethod
    def clone(self) -> "ImageTag":
        """
        Creates a copy of the image tag.

        Returns:
            ImageTag: A copy of the ImageTag object.
        """
        pass
        return _DynamsoftCore.CImageTag_Clone(self)

    def get_image_id(self) -> int:
        """
        Gets the ID of the image.

        Returns:
            int: The ID of the image.
        """
        return _DynamsoftCore.CImageTag_GetImageId(self)

    def set_image_id(self, imgId: int) -> None:
        """
        Sets the ID of the image.

        Args:
            imgId (int): The ID of the image.
        """
        return _DynamsoftCore.CImageTag_SetImageId(self, imgId)

    def get_image_capture_distance_mode(self) -> int:
        """
        Gets the capture distance mode of the image.

        Returns:
            int: The capture distance mode of the image.
        """
        return _DynamsoftCore.CImageTag_GetImageCaptureDistanceMode(self)

    def set_image_capture_distance_mode(self, mode: int) -> None:
        """
        Sets the capture distance mode of the image.

        Args:
            mode (int): The capture distance mode of the image.
        """
        return _DynamsoftCore.CImageTag_SetImageCaptureDistanceMode(self, mode)

_DynamsoftCore.CImageTag_register(ImageTag)

class FileImageTag(ImageTag):
    """
    FileImageTag represents an image tag that is associated with a file.
    It inherits from the ImageTag class and adds two attributes, a file path and a page number.

    Methods:
        __init__(file_path: str, page_number: int, total_pages: int):Initializes a new instance of the FileImageTag class.
        get_type(self) -> int: Gets the type of the image tag.
        clone(self) -> FileImageTag: Creates a copy of the image tag.
        get_file_path(self) -> str: Gets the file path of the image.
        get_page_number(self) -> int: Gets the page number of the current image in the Multi-Page image file.
        get_total_pages(self) -> int: Gets the total page number of the Multi-Page image file.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self, file_path: str, page_number: int, total_pages: int):
        """
        Initializes a new instance of the FileImageTag class.

        Args:
            file_path (str): The file path.
            page_number (int): The page number of the file image.
            total_pages (int): The total pages of the file image.
        """
        _DynamsoftCore.CFileImageTag_init(
            self, _DynamsoftCore.new_CFileImageTag(file_path, page_number, total_pages)
        )

    __destroy__ = _DynamsoftCore.delete_CFileImageTag

    def get_type(self) -> int:
        """
        Gets the type of the image tag.

        Returns:
            int: The type of the image tag.
        """
        return _DynamsoftCore.CFileImageTag_GetType(self)

    def clone(self) -> "FileImageTag":
        """
        Creates a copy of the image tag.

        Returns:
            FileImageTag: A copy of the FileImageTag object.
        """
        return _DynamsoftCore.CFileImageTag_Clone(self)

    def get_file_path(self) -> str:
        """
        Gets the file path of the image.

        Returns:
            str: The file path of the image.
        """
        return _DynamsoftCore.CFileImageTag_GetFilePath(self)

    def get_page_number(self) -> int:
        """
        Gets the page number of the current image in the Multi-Page image file.

        Returns:
            int: The page number of the current image in the Multi-Page image file.
        """
        return _DynamsoftCore.CFileImageTag_GetPageNumber(self)

    def get_total_pages(self) -> int:
        """
        Gets the total page number of the Multi-Page image file.

        Returns:
            int: The total page number of the Multi-Page image file.
        """
        return _DynamsoftCore.CFileImageTag_GetTotalPages(self)

_DynamsoftCore.CFileImageTag_register(FileImageTag)

class VideoFrameTag(ImageTag):
    """
    VideoFrameTag represents a video frame tag, which is a type of image tag that is used to store additional information about a video frame.

    Methods:
        __init__(self, quality: int, is_cropped: bool, crop_region: Rect, original_width: int, original_height: int): Initializes a new instance of the VideoFrameTag class.
        get_video_frame_quality(self) -> int: Gets the quality of the video frame.
        is_cropped(self) -> bool: Determines whether the video frame is cropped.
        get_crop_region(self) -> Rect: Gets the crop region of the video frame.
        get_original_width(self) -> int: Gets the original width of the video frame.
        get_original_height(self) -> int: Gets the original height of the video frame.
        get_type(self) -> int: Gets the type of the image tag.
        clone(self) -> VideoFrameTag: Creates a copy of the image tag.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def get_video_frame_quality(self) -> int:
        """
        Gets the quality of the video frame.

        Returns:
            The quality of the video frame.
        """
        return _DynamsoftCore.CVideoFrameTag_GetVideoFrameQuality(self)

    def is_cropped(self) -> bool:
        """
        Determines whether the video frame is cropped.

        Returns:
            True if the video frame is cropped, False otherwise.
        """
        return _DynamsoftCore.CVideoFrameTag_IsCropped(self)

    def get_crop_region(self) -> Rect:
        """
        Gets the crop region of the video frame.

        Returns:
            A Rect object that represents the crop region of the video frame. It may be null.
        """
        return _DynamsoftCore.CVideoFrameTag_GetCropRegion(self)

    def get_original_width(self) -> int:
        """
        Gets the original width of the video frame.

        Returns:
            The original width of the video frame.
        """
        return _DynamsoftCore.CVideoFrameTag_GetOriginalWidth(self)

    def get_original_height(self) -> int:
        """
        Gets the original height of the video frame.

        Returns:
            The original height of the video frame.
        """
        return _DynamsoftCore.CVideoFrameTag_GetOriginalHeight(self)

    def get_type(self) -> int:
        """
        Gets the type of the image tag.

        Returns:
            The type of the image tag.
        """
        return _DynamsoftCore.CVideoFrameTag_GetType(self)

    def clone(self) -> "VideoFrameTag":
        """
        Creates a copy of the image tag.

        Returns:
            A copy of the VideoFrameTag object.
        """
        return _DynamsoftCore.CVideoFrameTag_Clone(self)

    def __init__(
        self,
        quality: int,
        is_cropped: bool,
        crop_region: Rect,
        original_width: int,
        original_height: int,
    ):
        """
        Initializes a new instance of the VideoFrameTag class.

        Args:
            quality (int): The quality of the video frame.
            is_cropped (bool): A boolean value indicating whether the video frame is cropped.
            crop_region (Rect): A Rect object that represents the crop region of the video frame.
            original_width (int): The original width of the video frame.
            original_height (int): The original height of the video frame.
        """
        _DynamsoftCore.CVideoFrameTag_init(
            self,
            _DynamsoftCore.new_CVideoFrameTag(
                self, quality, is_cropped, crop_region, original_width, original_height
            ),
        )

    __destroy__ = _DynamsoftCore.delete_CVideoFrameTag


_DynamsoftCore.CVideoFrameTag_register(VideoFrameTag)

class ImageData(object):
    """
    This class represents image data, which contains the image bytes, width, height, stride, pixel format, orientation, and a tag.

    Methods:
        __init__(self, bytes: bytes, width: int, height: int, stride: int, format: int, orientation: int = 0, tag: ImageTag = None): Initializes an ImageData object.
        get_bytes(self) -> bytes: Returns the image bytes.
        get_width(self) -> int: Returns the width of the image.
        get_height(self) -> int: Returns the height of the image.
        get_stride(self) -> int: Returns the stride of the image.
        get_format(self) -> int: Returns the pixel format of the image.
        get_orientation(self) -> int: Returns the orientation of the image.
        get_tag(self) -> ImageTag: Returns the tag of the image.
        set_tag(self, tag: ImageTag): Sets the tag of the image.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(
        self,
        bytes: bytes,
        width: int,
        height: int,
        stride: int,
        format: int,
        orientation: int = 0,
        tag: ImageTag = None,
    ):
        """
        Initializes an ImageData object.

        Args:
            bytes: The image byte array.
            width: The width of the image.
            height: The height of the image.
            stride: The stride of the image.
            format: The pixel format of the image.
            orientation: The orientation of the image.
            tag: The tag of the image.
        """
        _DynamsoftCore.CImageData_init(
            self,
            _DynamsoftCore.new_CImageData(
                bytes, width, height, stride, format, orientation, tag
            ),
        )

    __destroy__ = _DynamsoftCore.delete_CImageData

    def get_bytes(self) -> bytes:
        """
        Gets the image byte array.

        Returns:
            The image byte array.
        """
        return _DynamsoftCore.CImageData_GetBytes(self)

    def get_width(self) -> int:
        """
        Gets the width of the image.

        Returns:
            The width of the image.
        """
        return _DynamsoftCore.CImageData_GetWidth(self)

    def get_height(self) -> int:
        """
        Gets the height of the image.

        Returns:
            The height of the image.
        """
        return _DynamsoftCore.CImageData_GetHeight(self)

    def get_stride(self) -> int:
        """
        Gets the stride of the image.

        Returns:
            The stride of the image.
        """
        return _DynamsoftCore.CImageData_GetStride(self)

    def get_image_pixel_format(self) -> int:
        """
        Gets the pixel format of the image.

        Returns:
            The pixel format of the image.
        """
        return _DynamsoftCore.CImageData_GetImagePixelFormat(self)

    def get_orientation(self) -> int:
        """
        Gets the orientation of the image.

        Returns:
            The orientation of the image.
        """
        return _DynamsoftCore.CImageData_GetOrientation(self)

    def get_image_tag(self) -> ImageTag:
        """
        Gets the tag of the image.

        Returns:
            The tag of the image.
        """
        return _DynamsoftCore.CImageData_GetImageTag(self)

    def set_image_tag(self, tag: ImageTag) -> None:
        """
        Sets the tag of the image.

        Args:
            tag: The tag of the image.
        """
        return _DynamsoftCore.CImageData_SetImageTag(self, tag)

_DynamsoftCore.CImageData_register(ImageData)

class CapturedResultItem(object):
    """
    The CapturedResultItem class represents an item in a captured result.
    It is an abstract base class with multiple subclasses, each representing a different type of captured item such as barcode, text line, detected quad, normalized image, raw image, parsed item, etc.

    Methods:
    get_type(self): Gets the type of the captured result item.
    get_reference_item(self): Gets the referenced item in the captured result item.
    get_target_roi_def_name(self): Gets the name of the target ROI definition.
    get_task_name(self): Gets the name of the task.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        """
        Initializes an instance of the CapturedResultItem class.

        Raises:
            AttributeError: If the constructor is called directly.
        """
        raise AttributeError("No constructor defined - class is abstract")

    def get_type(self) -> int:
        """
        Gets the type of the captured result item.

        Returns:
            int: The type of the captured result item.
        """
        return _DynamsoftCore.CCapturedResultItem_GetType(self)

    def get_reference_item(self) -> "CapturedResultItem":
        """
        Gets the referenced item in the captured result item.

        Returns:
            CapturedResultItem: The referenced item in the captured result item.
        """
        return _DynamsoftCore.CCapturedResultItem_GetReferenceItem(self)

    def get_target_roi_def_name(self) -> str:
        """
        Gets the name of the target ROI definition.

        Returns:
            str: The name of the target ROI definition.
        """
        return _DynamsoftCore.CCapturedResultItem_GetTargetROIDefName(self)

    def get_task_name(self) -> str:
        """
        Gets the name of the task.

        Returns:
            str: The name of the task.
        """
        return _DynamsoftCore.CCapturedResultItem_GetTaskName(self)


_DynamsoftCore.CCapturedResultItem_register(CapturedResultItem)

class OriginalImageResultItem(CapturedResultItem):
    """
    The OriginalImageResultItem class represents a captured original image result item. It is a derived class of CapturedResultItem and provides a class to get the image data.

    Methods:
    get_image_data(self): Gets the image data for the OriginalImageResultItem.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )
    __destroy__ = _DynamsoftCore.COriginalImageResultItem_Release

    def __init__(self):
        """
        Initializes a new instance of the OriginalImageResultItem class.

        Raises:
            AttributeError: If the constructor is called.
        """
        raise AttributeError("No constructor defined - class is abstract")

    def get_image_data(self) -> ImageData:
        """
        Gets the image data for the OriginalImageResultItem.

        Returns:
            ImageData: The ImageData object that contains the image data for the OriginalImageResultItem.
        """
        return _DynamsoftCore.COriginalImageResultItem_GetImageData(self)


_DynamsoftCore.COriginalImageResultItem_register(OriginalImageResultItem)


class ImageSourceErrorListener(ABC):
    """
    The ImageSourceErrorListener class defines a listener for receiving error notifications from an image source.

    Methods:
        on_error_received(self, error_code: int, error_message: str) -> None: Called when an error is received.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCore.CPDFReadingParameter_init(
            self, _DynamsoftCore.new_CImageSourceErrorListener(self)
        )

    @abstractmethod
    def on_error_received(self, error_code: int, error_message: str) -> None:
        """
        Called when an error is received from the image source.

        Args:
            error_code (int): The integer error code indicating the type of error.
            error_message(str): A string containing the error message providing additional information about the error.
        """

        pass

    __destroy__ = _DynamsoftCore.delete_CImageSourceErrorListener


_DynamsoftCore.CImageSourceErrorListener_register(ImageSourceErrorListener)


class ImageSourceAdapter(ABC):
    """
    This class provides an interface for fetching and buffering images.
    It is an abstract class that needs to be implemented by a concrete class to provide actual functionality.

    Methods:
        add_image_to_buffer(self, image: ImageData) -> None: Adds an image to the buffer.
        has_next_image_to_fetch(self) -> bool: Checks if there is the next image to fetch.
        start_fetching(self) -> None: Starts fetching images.
        stop_fetching(self) -> None: Stops fetching images.
        get_image(self) -> ImageData: Gets an image from the buffer.
        set_max_image_count(self, count: int) -> None: Sets the maximum count of images in the buffer.
        get_max_image_count(self) -> int: Gets the maximum count of images in the buffer.
        set_buffer_overflow_protection_mode(self, mode: int) -> None: Sets the mode of buffer overflow protection.
        get_buffer_overflow_protection_mode(self) -> int: Gets the mode of buffer overflow protection.
        has_image(self, image_id: int) -> bool: Checks if there is an image with the specified ID in the buffer.
        set_next_image_to_return(self, image_id: int, keep_in_buffer: bool = True) -> bool: Sets the next image to return and optionally keeps it in the buffer.
        get_image_count(self) -> int: Gets the number of images in the buffer.
        is_buffer_empty(self) -> bool: Checks if the buffer is empty.
        clear_buffer(self) -> None: Clears the buffer.
        set_colour_channel_usage_type(self, type: int) -> None: Sets the usage type of a color channel in images.
        get_colour_channel_usage_type(self) -> int: Gets the usage type of a color channel in images.
        set_error_listener(self, listener: ImageSourceErrorListener) -> None: Sets an error listener object that will receive notifications when errors occur during image source operations.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCore.CPDFReadingParameter_init(
            self, _DynamsoftCore.new_CImageSourceAdapter(self)
        )

    __destroy__ = _DynamsoftCore.delete_CImageSourceAdapter

    def add_image_to_buffer(self, image: ImageData) -> None:
        """
        Adds an image to the buffer.

        Args:
            image (ImageData): The image to be added.
        """
        return _DynamsoftCore.CImageSourceAdapter_AddImageToBuffer(self, image)

    @abstractmethod
    def has_next_image_to_fetch(self) -> bool:
        """
        Checks if there is the next image to fetch.

        Returns:
            bool: True if there is the next image to fetch, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_HasNextImageToFetch(self)

    def start_fetching(self) -> None:
        """
        Starts fetching images.
        """
        return _DynamsoftCore.CImageSourceAdapter_StartFetching(self)

    def stop_fetching(self) -> None:
        """
        Stops fetching images.
        """
        return _DynamsoftCore.CImageSourceAdapter_StopFetching(self)

    def get_image(self) -> ImageData:
        """
        Gets an image from the buffer.

        Returns:
            ImageData: The image from the buffer.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetImage(self)

    def set_max_image_count(self, count: int) -> None:
        """
        Sets the maximum count of images in the buffer.

        Args:
            count (int): The maximum count of images.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetMaxImageCount(self, count)

    def get_max_image_count(self) -> int:
        """
        Gets the maximum count of images in the buffer.

        Returns:
            int: The maximum count of images.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetMaxImageCount(self)

    def set_buffer_overflow_protection_mode(self, mode: int) -> None:
        """
        Sets the mode of buffer overflow protection.

        Args:
            mode (int): The mode of buffer overflow protection.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetBufferOverflowProtectionMode(
            self, mode
        )

    def get_buffer_overflow_protection_mode(self) -> int:
        """
        Gets the mode of buffer overflow protection.

        Returns:
            int: The mode of buffer overflow protection.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetBufferOverflowProtectionMode(self)

    def has_image(self, image_id: int) -> bool:
        """
        Checks if there is an image with the specified ID in the buffer.

        Args:
            image_id (int): The ID of the image to check.

        Returns:
            bool: True if there is the image with the specified ID, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_HasImage(self, image_id)

    def set_next_image_to_return(
        self, image_id: int, keep_in_buffer: bool = True
    ) -> bool:
        """
        Sets the next image to return and optionally keeps it in the buffer.

        Args:
            image_id (int): The ID of the image to set as the next image to return.
            keep_in_buffer (bool, optional): Whether to keep the image in the buffer. Defaults to True.

        Returns:
            bool: True if the image is set as the next image to return, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetNextImageToReturn(
            self, image_id, keep_in_buffer
        )

    def get_image_count(self) -> int:
        """
        Gets the number of images in the buffer.

        Returns:
            int: The number of images in the buffer.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetImageCount(self)

    def is_buffer_empty(self) -> bool:
        """
        Checks if the buffer is empty.

        Returns:
            bool: True if the buffer is empty, False otherwise.
        """
        return _DynamsoftCore.CImageSourceAdapter_IsBufferEmpty(self)

    def clear_buffer(self) -> None:
        """
        Clears the buffer.
        """
        return _DynamsoftCore.CImageSourceAdapter_ClearBuffer(self)

    def set_colour_channel_usage_type(self, type: int) -> None:
        """
        Sets the usage type of a color channel in images.

        Args:
            type (int): The usage type of a color channel in images.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetColourChannelUsageType(self, type)

    def get_colour_channel_usage_type(self) -> int:
        """
        Gets the usage type of a color channel in images.

        Returns:
            int: The usage type of a color channel in images.
        """
        return _DynamsoftCore.CImageSourceAdapter_GetColourChannelUsageType(self)

    def set_error_listener(self, listener: ImageSourceErrorListener) -> None:
        """
        Sets an error listener object that will receive notifications when errors occur during image source operations.

        Args:
            listener (ImageSourceErrorListener): The listening object of the type ImageSourceErrorListener that will handle error notifications.
        """
        return _DynamsoftCore.CImageSourceAdapter_SetErrorListener(self, listener)


_DynamsoftCore.CImageSourceAdapter_register(ImageSourceAdapter)


class PDFReadingParameter(object):
    """
    The PDFReadingParameter class represents the parameters for reading a PDF file.
    It contains the mode of PDF reading, the DPI (dots per inch) value, and the raster data source type.

    Attributes:
        mode (int): The mode used for PDF reading. This is one of the values of the EnumPDFReadingMode enumeration.
        dpi (int): The DPI (dots per inch) value.
        raster_data_source (int): The raster data source type. This is one of the values of the EnumRasterDataSource enumeration.
    Methods:
        __init__(self): Initializes a new instance of the PDFReadingParameter class.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    mode: int = property(
        _DynamsoftCore.CPDFReadingParameter_mode_get,
        _DynamsoftCore.CPDFReadingParameter_mode_set,
    )
    dpi: int = property(
        _DynamsoftCore.CPDFReadingParameter_dpi_get,
        _DynamsoftCore.CPDFReadingParameter_dpi_set,
    )
    raster_data_source: int = property(
        _DynamsoftCore.CPDFReadingParameter_rasterDataSource_get,
        _DynamsoftCore.CPDFReadingParameter_rasterDataSource_set,
    )

    def __init__(self):
        """
        Initializes a new instance of the PDFReadingParameter class.

        This constructor initializes the properties with default values:
        mode: 2 (EnumPDFReadingMode.PDFRM_RASTER.value)
        dpi: 300
        raster_data_source: 0 (EnumRasterDataSource.RDS_RASTERIZED_PAGES.value)
        """
        _DynamsoftCore.CPDFReadingParameter_init(
            self, _DynamsoftCore.new_CPDFReadingParameter()
        )

    __destroy__ = _DynamsoftCore.delete_CPDFReadingParameter


_DynamsoftCore.CPDFReadingParameter_register(PDFReadingParameter)
