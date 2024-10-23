__version__ = "10.4.20"

if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftBarcodeReader
else:
    import _DynamsoftBarcodeReader


from enum import Enum, IntEnum
from typing import List


class EnumBarcodeFormat(Enum):
    BF_NULL = _DynamsoftBarcodeReader.BF_NULL
    BF_ALL = _DynamsoftBarcodeReader.BF_ALL
    BF_DEFAULT = _DynamsoftBarcodeReader.BF_DEFAULT
    BF_ONED = _DynamsoftBarcodeReader.BF_ONED
    BF_GS1_DATABAR = _DynamsoftBarcodeReader.BF_GS1_DATABAR
    BF_CODE_39 = _DynamsoftBarcodeReader.BF_CODE_39
    BF_CODE_128 = _DynamsoftBarcodeReader.BF_CODE_128
    BF_CODE_93 = _DynamsoftBarcodeReader.BF_CODE_93
    BF_CODABAR = _DynamsoftBarcodeReader.BF_CODABAR
    BF_ITF = _DynamsoftBarcodeReader.BF_ITF
    BF_EAN_13 = _DynamsoftBarcodeReader.BF_EAN_13
    BF_EAN_8 = _DynamsoftBarcodeReader.BF_EAN_8
    BF_UPC_A = _DynamsoftBarcodeReader.BF_UPC_A
    BF_UPC_E = _DynamsoftBarcodeReader.BF_UPC_E
    BF_INDUSTRIAL_25 = _DynamsoftBarcodeReader.BF_INDUSTRIAL_25
    BF_CODE_39_EXTENDED = _DynamsoftBarcodeReader.BF_CODE_39_EXTENDED
    BF_GS1_DATABAR_OMNIDIRECTIONAL = (
        _DynamsoftBarcodeReader.BF_GS1_DATABAR_OMNIDIRECTIONAL
    )
    BF_GS1_DATABAR_TRUNCATED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_TRUNCATED
    BF_GS1_DATABAR_STACKED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_STACKED
    BF_GS1_DATABAR_STACKED_OMNIDIRECTIONAL = (
        _DynamsoftBarcodeReader.BF_GS1_DATABAR_STACKED_OMNIDIRECTIONAL
    )
    BF_GS1_DATABAR_EXPANDED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_EXPANDED
    BF_GS1_DATABAR_EXPANDED_STACKED = (
        _DynamsoftBarcodeReader.BF_GS1_DATABAR_EXPANDED_STACKED
    )
    BF_GS1_DATABAR_LIMITED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_LIMITED
    BF_PATCHCODE = _DynamsoftBarcodeReader.BF_PATCHCODE
    BF_CODE_32 = _DynamsoftBarcodeReader.BF_CODE_32
    BF_PDF417 = _DynamsoftBarcodeReader.BF_PDF417
    BF_QR_CODE = _DynamsoftBarcodeReader.BF_QR_CODE
    BF_DATAMATRIX = _DynamsoftBarcodeReader.BF_DATAMATRIX
    BF_AZTEC = _DynamsoftBarcodeReader.BF_AZTEC
    BF_MAXICODE = _DynamsoftBarcodeReader.BF_MAXICODE
    BF_MICRO_QR = _DynamsoftBarcodeReader.BF_MICRO_QR
    BF_MICRO_PDF417 = _DynamsoftBarcodeReader.BF_MICRO_PDF417
    BF_GS1_COMPOSITE = _DynamsoftBarcodeReader.BF_GS1_COMPOSITE
    BF_MSI_CODE = _DynamsoftBarcodeReader.BF_MSI_CODE
    BF_CODE_11 = _DynamsoftBarcodeReader.BF_CODE_11
    BF_TWO_DIGIT_ADD_ON = _DynamsoftBarcodeReader.BF_TWO_DIGIT_ADD_ON
    BF_FIVE_DIGIT_ADD_ON = _DynamsoftBarcodeReader.BF_FIVE_DIGIT_ADD_ON
    BF_MATRIX_25 = _DynamsoftBarcodeReader.BF_MATRIX_25
    BF_POSTALCODE = _DynamsoftBarcodeReader.BF_POSTALCODE
    BF_NONSTANDARD_BARCODE = _DynamsoftBarcodeReader.BF_NONSTANDARD_BARCODE
    BF_USPSINTELLIGENTMAIL = _DynamsoftBarcodeReader.BF_USPSINTELLIGENTMAIL
    BF_POSTNET = _DynamsoftBarcodeReader.BF_POSTNET
    BF_PLANET = _DynamsoftBarcodeReader.BF_PLANET
    BF_AUSTRALIANPOST = _DynamsoftBarcodeReader.BF_AUSTRALIANPOST
    BF_RM4SCC = _DynamsoftBarcodeReader.BF_RM4SCC
    BF_KIX = _DynamsoftBarcodeReader.BF_KIX
    BF_DOTCODE = _DynamsoftBarcodeReader.BF_DOTCODE
    BF_PHARMACODE_ONE_TRACK = _DynamsoftBarcodeReader.BF_PHARMACODE_ONE_TRACK
    BF_PHARMACODE_TWO_TRACK = _DynamsoftBarcodeReader.BF_PHARMACODE_TWO_TRACK
    BF_PHARMACODE = _DynamsoftBarcodeReader.BF_PHARMACODE


class EnumLocalizationMode(IntEnum):
    LM_AUTO = _DynamsoftBarcodeReader.LM_AUTO
    LM_CONNECTED_BLOCKS = _DynamsoftBarcodeReader.LM_CONNECTED_BLOCKS
    LM_STATISTICS = _DynamsoftBarcodeReader.LM_STATISTICS
    LM_LINES = _DynamsoftBarcodeReader.LM_LINES
    LM_SCAN_DIRECTLY = _DynamsoftBarcodeReader.LM_SCAN_DIRECTLY
    LM_STATISTICS_MARKS = _DynamsoftBarcodeReader.LM_STATISTICS_MARKS
    LM_STATISTICS_POSTAL_CODE = _DynamsoftBarcodeReader.LM_STATISTICS_POSTAL_CODE
    LM_CENTRE = _DynamsoftBarcodeReader.LM_CENTRE
    LM_ONED_FAST_SCAN = _DynamsoftBarcodeReader.LM_ONED_FAST_SCAN
    LM_REV = _DynamsoftBarcodeReader.LM_REV
    LM_SKIP = _DynamsoftBarcodeReader.LM_SKIP


class EnumDeblurMode(IntEnum):
    DM_DIRECT_BINARIZATION = _DynamsoftBarcodeReader.DM_DIRECT_BINARIZATION
    DM_THRESHOLD_BINARIZATION = _DynamsoftBarcodeReader.DM_THRESHOLD_BINARIZATION
    DM_GRAY_EQUALIZATION = _DynamsoftBarcodeReader.DM_GRAY_EQUALIZATION
    DM_SMOOTHING = _DynamsoftBarcodeReader.DM_SMOOTHING
    DM_MORPHING = _DynamsoftBarcodeReader.DM_MORPHING
    DM_DEEP_ANALYSIS = _DynamsoftBarcodeReader.DM_DEEP_ANALYSIS
    DM_SHARPENING = _DynamsoftBarcodeReader.DM_SHARPENING
    DM_BASED_ON_LOC_BIN = _DynamsoftBarcodeReader.DM_BASED_ON_LOC_BIN
    DM_SHARPENING_SMOOTHING = _DynamsoftBarcodeReader.DM_SHARPENING_SMOOTHING
    DM_REV = _DynamsoftBarcodeReader.DM_REV
    DM_SKIP = _DynamsoftBarcodeReader.DM_SKIP


class EnumQRCodeErrorCorrectionLevel(IntEnum):
    QRECL_ERROR_CORRECTION_H = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_H
    QRECL_ERROR_CORRECTION_L = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_L
    QRECL_ERROR_CORRECTION_M = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_M
    QRECL_ERROR_CORRECTION_Q = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_Q


class EnumExtendedBarcodeResultType(IntEnum):
    EBRT_STANDARD_RESULT = _DynamsoftBarcodeReader.EBRT_STANDARD_RESULT
    EBRT_CANDIDATE_RESULT = _DynamsoftBarcodeReader.EBRT_CANDIDATE_RESULT
    EBRT_PARTIAL_RESULT = _DynamsoftBarcodeReader.EBRT_PARTIAL_RESULT


class SimplifiedBarcodeReaderSettings(object):
    """
    The SimplifiedBarcodeReaderSettings class contains settings for barcode decoding. It is a sub-parameter of SimplifiedCaptureVisionSettings.

    Attributes:
        barcode_format_ids (int): Specifies the targeting format(s) of the barcode(s) to be decoded.
        expected_barcodes_count (int): Specifies the expected barcode count. The default value is 0.
        grayscale_transformation_modes (List[int]): Specifies how grayscale transformations should be applied, including whether to process inverted grayscale images and the specific transformation mode to use.
        grayscale_enhancement_modes (List[int]): Specifies how to enhance the quality of the grayscale image.
        localization_modes(List[int]): Specifies how to localize barcodes.
        deblur_modes (List[int]): Specifies the mode and priority for deblurring.
        min_result_confidence (int): Specifies the minimum result confidence to filter out the low confidence results. The default value is 30.
        min_barcode_text_length (int): Specifies the minimum barcode text length to filter out the unqualified results.
        barcode_text_regex_pattern (str): Specifies the RegEx pattern of the barcode text to filter out the unqualified results.
        max_threads_in_one_task (int): Specifies the maximum available threads count in one barcode decoding task.
        scale_down_threshold (int): Specifies the threshold for image shrinking.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    barcode_format_ids: int = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeFormatIds_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeFormatIds_set,
        doc="""
            Specifies the targeting format(s) of the barcode(s) to be decoded.
            It is a bitwise OR combination of one or more values from the EnumBarcodeFormat enumeration.
            """
    )
    expected_barcodes_count: int = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_expectedBarcodesCount_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_expectedBarcodesCount_set,
        doc="""
            Specifies the expected barcode count. The default value is 0.
            Set expected_barcodes_count to 0 if the barcode count is unknown. The library will try to find at least 1 barcode.
            Set expected_barcodes_count to 1 to reach the highest speed for processing single barcode.
            Set expected_barcodes_count to "n" if there will be "n" barcodes to process from an image.
            Set expected_barcodes_count to the highest expected value if there exists multiple barcode but the exact count is not confirmed.            
            """,
    )
    grayscale_transformation_modes: List[int] = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleTransformationModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleTransformationModes_set,
        doc="""
            Specifies how grayscale transformations should be applied, including whether to process inverted grayscale images and the specific transformation mode to use.
            It is a list of 8 integers, where each integer represents a mode specified by the EnumGrayscaleTransformationMode enumeration.
            """,
    )
    grayscale_enhancement_modes: List[int] = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleEnhancementModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleEnhancementModes_set,
        doc="""
            Specifies how to enhance the quality of the grayscale image.
            It is a list of 8 integers, where each integer represents a mode specified by the EnumGrayscaleEnhancementMode enumeration.
            """,
    )
    localization_modes: List[int] = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_localizationModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_localizationModes_set,
        doc="""
            Specifies how to localize barcodes.
            It is a list of 8 integers, where each integer represents a mode specified by the EnumLocalizationMode enumeration.
            """,
    )
    deblur_modes: List[int] = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_deblurModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_deblurModes_set,
        doc="""
            Specifies the mode and priority for deblurring.
            It is a list of 8 integers, where each integer represents a mode specified by the EnumDeblurMode enumeration.
            """,
    )
    min_result_confidence: int = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minResultConfidence_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minResultConfidence_set,
        doc="Specifies the minimum result confidence to filter out the low confidence results. The default value is 30.",
    )
    min_barcode_text_length: int = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minBarcodeTextLength_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minBarcodeTextLength_set,
        doc="Specifies the minimum barcode text length to filter out the unqualified results.",
    )
    barcode_text_regex_pattern: str = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeTextRegExPattern_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeTextRegExPattern_set,
        doc="Specifies the RegEx pattern of the barcode text to filter out the unqualified results.",
    )
    max_threads_in_one_task: int = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_maxThreadsInOneTask_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_maxThreadsInOneTask_set,
        doc="""
            Specifies the maximum available threads count in one barcode decoding task.
            The value range is [1, 256]
            The default value is 4
            """,
    )
    scale_down_threshold: int = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_scaleDownThreshold_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_scaleDownThreshold_set,
        doc="""
            Specifies the threshold for image shrinking.
            If the shorter edge size is larger than the given threshold value, the library will calculate the required height and width of the target image and shrink the image to that size before further operation.
            Otherwise, the library will perform operation on the original image.
            The value range is [512, 0x7fffffff]
            The default value is 2300
            """
    )

    def __init__(self):
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_init(
            self, _DynamsoftBarcodeReader.new_SimplifiedBarcodeReaderSettings()
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_SimplifiedBarcodeReaderSettings


_DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_register(
    SimplifiedBarcodeReaderSettings
)


class BarcodeDetails(object):
    """
    The BarcodeDetails class represents the details of a barcode. It is an abstract base class.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    __destroy__ = _DynamsoftBarcodeReader.delete_CBarcodeDetails

    def __init__(self):
        _DynamsoftBarcodeReader.CBarcodeDetails_init(
            self, _DynamsoftBarcodeReader.new_CBarcodeDetails()
        )


_DynamsoftBarcodeReader.CBarcodeDetails_register(BarcodeDetails)

class OneDCodeDetails(BarcodeDetails):
    """
    The OneDCodeDetails class represents detailed information about a one-dimensional barcode. It inherits from the BarcodeDetails class.

    Attributes:
        start_chars_bytes (bytes): The start chars of the one-dimensional barcode in a byte array.
        stop_chars_bytes (bytes): The stop chars of the one-dimensional barcode in a byte array.
        check_digit_bytes (bytes): The check digit chars of the one-dimensional barcode in a byte array.
        start_pattern_range (List[float]): The position of the start pattern relative to the barcode location.
        middle_pattern_range (List[float]): The position of the middle pattern relative to the barcode location.
        end_pattern_range (List[float]): The position of the end pattern relative to the barcode location.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftBarcodeReader.COneDCodeDetails_init(
            self, _DynamsoftBarcodeReader.new_COneDCodeDetails()
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_COneDCodeDetails
    start_chars_bytes: bytes = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_startCharsBytes_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_startCharsBytes_set,
        doc="The start chars of the one-dimensional barcode in a byte array.",
    )
    stop_chars_bytes: bytes = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_stopCharsBytes_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_stopCharsBytes_set,
        doc="The stop chars of the one-dimensional barcode in a byte array.",
    )
    check_digit_bytes: bytes = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_checkDigitBytes_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_checkDigitBytes_set,
        doc="The check digit chars of the one-dimensional barcode in a byte array.",
    )
    start_pattern_range: List[float] = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_startPatternRange_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_startPatternRange_set,
        doc="""
            The position of the start pattern relative to the barcode location.
            The property represents a float list of length 2:
            Index 0: X coordinate of the start position in percentage value.
            Index 1: X coordinate of the end position in percentage value.
            """,
    )
    middle_pattern_range: List[float] = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_middlePatternRange_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_middlePatternRange_set,
        doc="""
            The position of the middle pattern relative to the barcode location.
            The property represents a float list of length 2:
            Index 0: X coordinate of the start position in percentage value.
            Index 1: X coordinate of the end position in percentage value.
            """,
    )
    end_pattern_range: List[float] = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_endPatternRange_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_endPatternRange_set,
        doc="""
            The position of the end pattern relative to the barcode location.
            The property represents a float list of length 2:
            Index 0: X coordinate of the start position in percentage value.
            Index 1: X coordinate of the end position in percentage value.
            """,
    )


_DynamsoftBarcodeReader.COneDCodeDetails_register(OneDCodeDetails)


class QRCodeDetails(BarcodeDetails):
    """
    The QRCodeDetails class represents the details of a QR Code.
    It is derived from the BarcodeDetails class and contains various attributes related to the QR Code.

    Attributes:
        rows (int): The row count of the QR Code.
        columns (int): The column count of the QR Code.
        error_correction_level (int): The error correction level of the QR Code.
        version (int): The version of the QR Code.
        model (int): Number of models of the QR Code.
        mode (int): The first data encoding mode of the QR Code.
        page (int): The position of the particular symbol in the Structured Append format of the QR Code.
        total_page (int): The total number of symbols to be concatenated in the Structured Append format of the QR Code.
        parity_data (int): The Parity Data shall be an 8 bit byte following the Symbol Sequence Indicator. The parity data is a value obtained by XORing byte by byte the ASCII/JIS values of all the original input data before division into symbol blocks.
        data_mask_pattern (int): The data mask pattern reference for QR Code symbols.
        codewords (bytes): The codewords of the QR Code.

    Methods:
        __init__(self, rows: int, columns: int, error_correction_level: int, version: int, model: int, mode: int, page: int, total_page: int, parity_data: int): Initializes a new instance of the QRCodeDetails class.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(
        self,
        rows: int = -1,
        columns: int = -1,
        error_correction_level: int = EnumQRCodeErrorCorrectionLevel.QRECL_ERROR_CORRECTION_H.value,
        version: int = -1,
        model: int = -1,
        mode: int = -1,
        page: int = -1,
        total_page: int = -1,
        parity_data: int = -1,
    ):
        _DynamsoftBarcodeReader.CQRCodeDetails_init(
            self,
            _DynamsoftBarcodeReader.new_CQRCodeDetails(
                rows,
                columns,
                error_correction_level,
                version,
                model,
                mode,
                page,
                total_page,
                parity_data,
            ),
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_CQRCodeDetails
    rows: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_rows_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_rows_set,
    )
    columns: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_columns_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_columns_set,
    )
    error_correction_level: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_errorCorrectionLevel_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_errorCorrectionLevel_set,
    )
    version: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_version_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_version_set,
    )
    model: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_model_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_model_set,
    )
    mode: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_mode_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_mode_set,
    )
    page: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_page_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_page_set,
    )
    total_page: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_totalPage_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_totalPage_set,
    )
    parity_data: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_parityData_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_parityData_set,
    )
    data_mask_pattern: int = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_dataMaskPattern_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_dataMaskPattern_set,
    )
    codewords: bytes = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_codewords_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_codewords_set,
    )


_DynamsoftBarcodeReader.CQRCodeDetails_register(QRCodeDetails)


class PDF417Details(BarcodeDetails):
    """
    The PDF417Details class represents a barcode in PDF417 format.
    It inherits from the BarcodeDetails class and contains information about the row count, column count, and error correction level of the barcode.

    Attributes:
        rows (int): The number of rows in the PDF417 barcode.
        columns (int): The number of columns in the PDF417 barcode.
        error_correction_level (int): The error correction level of PDF417 code.
        has_left_row_indicator (int): Specifies whether the left row indicator of the PDF417 code exists.
        has_right_row_indicator (int): Specifies whether the right row indicator of the PDF417 code exists.

    Methods:
        __init__(self, rows: int = -1, columns: int = -1, level: int = -1, has_left_row_indicator: int = -1, has_right_row_indicator: int = -1): Initializes a new instance of the PDF417Details class.
    """
    thisown = property(
        lambda self: self.this.own(),
        lambda self, v: self.this.own(v),
        doc="The membership flag",
    )

    def __init__(
        self,
        rows: int = -1,
        columns: int = -1,
        level: int = -1,
        has_left_row_indicator: int = -1,
        has_right_row_indicator: int = -1,
    ):
        _DynamsoftBarcodeReader.CPDF417Details_init(
            self,
            _DynamsoftBarcodeReader.new_CPDF417Details(
                rows, columns, level, has_left_row_indicator, has_right_row_indicator
            ),
        )

    rows: int = property(
        _DynamsoftBarcodeReader.CPDF417Details_rows_get,
        _DynamsoftBarcodeReader.CPDF417Details_rows_set,
        doc="The number of rows in the PDF417 barcode.",
    )
    columns: int = property(
        _DynamsoftBarcodeReader.CPDF417Details_columns_get,
        _DynamsoftBarcodeReader.CPDF417Details_columns_set,
        doc="The number of columns in the PDF417 barcode.",
    )
    error_correction_level: int = property(
        _DynamsoftBarcodeReader.CPDF417Details_errorCorrectionLevel_get,
        _DynamsoftBarcodeReader.CPDF417Details_errorCorrectionLevel_set,
        doc="The error correction level of PDF417 code.",
    )
    has_left_row_indicator: int = property(
        _DynamsoftBarcodeReader.CPDF417Details_hasLeftRowIndicator_get,
        _DynamsoftBarcodeReader.CPDF417Details_hasLeftRowIndicator_set,
        doc="Specifies whether the left row indicator of the PDF417 code exists.",  
    )
    has_right_row_indicator: int = property(
        _DynamsoftBarcodeReader.CPDF417Details_hasRightRowIndicator_get,
        _DynamsoftBarcodeReader.CPDF417Details_hasRightRowIndicator_set,
        doc="Specifies whether the right row indicator of the PDF417 code exists.",
    )
    __destroy__ = _DynamsoftBarcodeReader.delete_CPDF417Details


_DynamsoftBarcodeReader.CPDF417Details_register(PDF417Details)


class DataMatrixDetails(BarcodeDetails):
    """
    The DataMatrixDetails class represents the details of a DataMatrix barcode. It is derived from the BarcodeDetails class and contains various attributes related to the DataMatrix barcode.

    Attributes:
        rows (int): The row count of the DataMatrix barcode.
        columns (int): The column count of the DataMatrix barcode.
        data_region_rows (int): The data region row count of the DataMatrix barcode.
        data_region_columns (int): The data region column count of the DataMatrix barcode.
        data_region_number (int): The data region count.

    Methods:
        __init__(self, rows: int = -1, columns: int = -1, data_region_rows: int = -1, data_region_columns: int = -1, data_region_number: int = -1): Initialize a new instance of the CDataMatrixDetails class.
    """
    thisown = property(
        lambda self: self.this.own(),
        lambda self, v: self.this.own(v),
        doc="The membership flag",
    )

    def __init__(
        self,
        rows: int = -1,
        columns: int = -1,
        data_region_rows: int = -1,
        data_region_columns: int = -1,
        data_region_number: int = -1,
    ):
        _DynamsoftBarcodeReader.CDataMatrixDetails_init(
            self,
            _DynamsoftBarcodeReader.new_CDataMatrixDetails(
                rows, columns, data_region_rows, data_region_columns, data_region_number
            ),
        )

    rows: int = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_rows_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_rows_set,
        doc="The row count of the DataMatrix barcode.",
    )
    columns: int = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_columns_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_columns_set,
        doc="The column count of the DataMatrix barcode.",
    )
    data_region_rows: int = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionRows_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionRows_set,
        doc="The data region row count of the DataMatrix barcode.",
    )
    data_region_columns: int = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionColumns_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionColumns_set,
        doc="The data region column count of the DataMatrix barcode.",
    )
    data_region_number: int  = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionNumber_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionNumber_set,
        doc="The data region count.",
    )
    __destroy__ = _DynamsoftBarcodeReader.delete_CDataMatrixDetails


_DynamsoftBarcodeReader.CDataMatrixDetails_register(DataMatrixDetails)

class AztecDetails(BarcodeDetails):
    """
    The AztecDetails class represents a barcode in Aztec format. It inherits from the BarcodeDetails class and contains information about the row count, column count, and layer number of the barcode.

    Attributes:
        rows (int): The number of rows in the Aztec barcode.
        columns (int): The number of columns in the Aztec barcode.
        layer_number (int): Specifies the layer number of the Aztec barcode.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self, rows: int = -1, columns: int = -1, layer_number: int = -1):
        _DynamsoftBarcodeReader.CAztecDetails_init(
            self, _DynamsoftBarcodeReader.new_CAztecDetails(rows, columns, layer_number)
        )

    rows: int = property(
        _DynamsoftBarcodeReader.CAztecDetails_rows_get,
        _DynamsoftBarcodeReader.CAztecDetails_rows_set,
        doc="The number of rows in the Aztec barcode.",
    )
    columns: int = property(
        _DynamsoftBarcodeReader.CAztecDetails_columns_get,
        _DynamsoftBarcodeReader.CAztecDetails_columns_set,
        doc="The number of columns in the Aztec barcode.",
    )
    layer_number: int = property(
        _DynamsoftBarcodeReader.CAztecDetails_layerNumber_get,
        _DynamsoftBarcodeReader.CAztecDetails_layerNumber_set,
        doc="Specifies the layer number of the Aztec barcode. A negative number (-1, -2, -3, -4) specifies a compact Aztec code. A positive number (1, 2, .. 32) specifies a normal (full-range) Aztec code.",
    )
    __destroy__ = _DynamsoftBarcodeReader.delete_CAztecDetails


_DynamsoftBarcodeReader.CAztecDetails_register(AztecDetails)

class BarcodeResultItem(CapturedResultItem):
    """
    The BarcodeResultItem class represents a barcode result item decoded by barcode reader engine. It is derived from CapturedResultItem.

    Methods:
        get_format(self) -> int: Gets the format of the decoded barcode result.
        get_format_string(self) -> str: Gets the format string of the decoded barcode result.
        get_text(self) -> str: Gets the text result of the decoded barcode.
        get_bytes(self) -> bytes: Gets the text bytes of the decoded barcode result.
        get_location(self) -> Quadrilateral: Gets the location of the decoded barcode in a quadrilateral.
        get_confidence(self) -> int: Gets the confidence of the decoded barcode result.
        get_angle(self) -> int: Gets the angle of the decoded barcode result.
        get_module_size(self) -> int: Gets the module size of the decoded barcode result.
        get_details(self) -> BarcodeDetails: Gets the details of the decoded barcode result.
        is_dpm(self) -> bool: Gets whether the decoded barcode is a DPM code.
        is_mirrored(self) -> bool: Gets whether the decoded barcode is mirrored.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_format(self) -> int:
        """
        Gets the format of the decoded barcode result.

        Returns:
            The format of the decoded barcode result which is a value of the EnumBarcodeFormat enumeration.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetFormat(self)

    def get_format_string(self) -> str:
        """
        Gets the format string of the decoded barcode result.

        Returns:
            The format string of the decoded barcode result.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetFormatString(self)

    def get_text(self) -> str:
        """
        Gets the text result of the decoded barcode.

        Returns:
            The text result of the decoded barcode.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetText(self)

    def get_bytes(self) -> bytes:
        """
        Gets the text bytes of the decoded barcode result.

        Returns:
            The text bytes of the decoded barcode result.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetBytes(self)

    def get_location(self) -> Quadrilateral:
        """
        Gets the location of the decoded barcode in a quadrilateral.

        Returns:
            The location of the decoded barcode in a quadrilateral.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetLocation(self)

    def get_confidence(self) -> int:
        """
        Gets the confidence of the decoded barcode result.

        Returns:
            The confidence of the decoded barcode result.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetConfidence(self)

    def get_angle(self) -> int:
        """
        Gets the angle of the decoded barcode result.

        Returns:
            The angle of the decoded barcode result.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetAngle(self)

    def get_module_size(self) -> int:
        """
        Gets the module size of the decoded barcode result.

        Returns:
            The module size of the decoded barcode result.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetModuleSize(self)

    def get_details(self) -> BarcodeDetails:
        """
        Gets the details of the decoded barcode result.

        Returns:
            The details of the decoded barcode result.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetDetails(self)

    def is_dpm(self) -> bool:
        """
        Gets whether the decoded barcode is a DPM code.

        Returns:
            Whether the decoded barcode is a DPM code.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_IsDPM(self)

    def is_mirrored(self) -> bool:
        """
        Gets whether the decoded barcode is mirrored.

        Returns:
            Whether the decoded barcode is mirrored.
        """
        return _DynamsoftBarcodeReader.CBarcodeResultItem_IsMirrored(self)


_DynamsoftBarcodeReader.CBarcodeResultItem_register(BarcodeResultItem)

class DecodedBarcodesResult(object):
    """
    The DecodedBarcodesResult class represents the result of a barcode reading process.
    It provides access to information about the decoded barcodes, the source image, and any errors that occurred during the barcode reading process.

    Methods:
        get_error_code(self) -> int: Gets the error code of the barcode reading result, if an error occurred.
        get_error_string(self) -> str: Gets the error message of the barcode reading result, if an error occurred.
        get_items(self) -> List[BarcodeResultItem]: Gets all the decoded barcode result items.
        get_original_image_hash_id(self) -> str: Gets the hash ID of the source image.
        get_original_image_tag(self) -> ImageTag: Gets the tag of the source image.
        get_rotation_transform_matrix(self) -> List[float]: Gets the 3x3 rotation transformation matrix of the original image relative to the rotated image.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftBarcodeReader.CDecodedBarcodesResult_Release

    def get_original_image_hash_id(self) -> str:
        """
        Gets the hash ID of the source image.

        Returns:
            The hash ID of the source image as a string.
        """
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetOriginalImageHashId(
            self
        )

    def get_original_image_tag(self) -> ImageTag:
        """
        Gets the tag of the source image.

        Returns:
            An ImageTag object containing the tag of the source image.
        """
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetOriginalImageTag(self)

    def get_rotation_transform_matrix(self) -> List[float]:
        """
        Gets the 3x3 rotation transformation matrix of the original image relative to the rotated image.

        Returns:
            A float list of length 9 which represents a 3x3 rotation matrix.
        """
        return (
            _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetRotationTransformMatrix(
                self
            )
        )

    def get_items(self) -> List[BarcodeResultItem]:
        """
        Gets all the decoded barcode result items.

        Returns:
            A list of BarcodeResultItem objects with all the decoded barcode result items.
        """
        list = []
        count = _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftBarcodeReader.CDecodedBarcodesResult_GetItem(self, i))
        return list

    def get_error_code(self) -> int:
        """
        Gets the error code of the barcode reading result, if an error occurred.

        Returns:
            The error code of the barcode reading result, or 0 if no error occurred.
        """
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetErrorCode(self)

    def get_error_string(self) -> str:
        """
        Gets the error message of the barcode reading result, if an error occurred.

        Returns:
            A string containing the error message of the barcode reading result, or an empty string if no error occurred.
        """
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetErrorString(self)


_DynamsoftBarcodeReader.CDecodedBarcodesResult_register(DecodedBarcodesResult)


class BarcodeReaderModule(object):
    """
    The BarcodeReaderModule class defines general functions in the barcode reader module.

    Methods:
        get_version() -> str: Returns the version of the barcode reader module.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns the version of the barcode reader module.

        Returns:
            A string representing the version of the barcode reader module.
        """
        return __version__ + " (Algotithm " + _DynamsoftBarcodeReader.CBarcodeReaderModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftBarcodeReader.CBarcodeReaderModule_init(
            self, _DynamsoftBarcodeReader.new_CBarcodeReaderModule()
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_CBarcodeReaderModule


_DynamsoftBarcodeReader.CBarcodeReaderModule_register(BarcodeReaderModule)
