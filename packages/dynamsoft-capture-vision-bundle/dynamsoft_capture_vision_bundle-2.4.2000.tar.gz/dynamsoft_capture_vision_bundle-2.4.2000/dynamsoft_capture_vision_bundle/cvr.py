__version__ = "2.4.20"

if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftCaptureVisionRouter
else:
    import _DynamsoftCaptureVisionRouter

from abc import ABC, abstractmethod
from enum import Enum, IntEnum
from typing import Tuple, List


class EnumPresetTemplate(Enum):
    PT_DEFAULT = _DynamsoftCaptureVisionRouter.getPT_DEFAULT()
    PT_READ_BARCODES = _DynamsoftCaptureVisionRouter.getPT_READ_BARCODES()
    PT_RECOGNIZE_TEXT_LINES = _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_TEXT_LINES()
    PT_DETECT_DOCUMENT_BOUNDARIES = (
        _DynamsoftCaptureVisionRouter.getPT_DETECT_DOCUMENT_BOUNDARIES()
    )
    PT_DETECT_AND_NORMALIZE_DOCUMENT = (
        _DynamsoftCaptureVisionRouter.getPT_DETECT_AND_NORMALIZE_DOCUMENT()
    )
    PT_NORMALIZE_DOCUMENT = _DynamsoftCaptureVisionRouter.getPT_NORMALIZE_DOCUMENT()
    PT_READ_BARCODES_SPEED_FIRST = (
        _DynamsoftCaptureVisionRouter.getPT_READ_BARCODES_SPEED_FIRST()
    )
    PT_READ_BARCODES_READ_RATE_FIRST = (
        _DynamsoftCaptureVisionRouter.getPT_READ_BARCODES_READ_RATE_FIRST()
    )
    PT_READ_SINGLE_BARCODE = _DynamsoftCaptureVisionRouter.getPT_READ_SINGLE_BARCODE()
    PT_RECOGNIZE_NUMBERS = _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_NUMBERS()
    PT_RECOGNIZE_LETTERS = _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_LETTERS()
    PT_RECOGNIZE_NUMBERS_AND_LETTERS = (
        _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_NUMBERS_AND_LETTERS()
    )
    PT_RECOGNIZE_NUMBERS_AND_UPPERCASE_LETTERS = (
        _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_NUMBERS_AND_UPPERCASE_LETTERS()
    )
    PT_RECOGNIZE_UPPERCASE_LETTERS = (
        _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_UPPERCASE_LETTERS()
    )


class EnumCaptureState(IntEnum):
    CS_STARTED = _DynamsoftCaptureVisionRouter.CS_STARTED
    CS_STOPPED = _DynamsoftCaptureVisionRouter.CS_STOPPED
    CS_PAUSED = _DynamsoftCaptureVisionRouter.CS_PAUSED
    CS_RESUMED = _DynamsoftCaptureVisionRouter.CS_RESUMED


class EnumImageSourceState(IntEnum):
    ISS_BUFFER_EMPTY = _DynamsoftCaptureVisionRouter.ISS_BUFFER_EMPTY
    ISS_EXHAUSTED = _DynamsoftCaptureVisionRouter.ISS_EXHAUSTED

class SimplifiedCaptureVisionSettings(object):
    """
    The SimplifiedCaptureVisionSettings class contains settings for capturing and recognizing images with the CaptureVisionRouter class.

    Attributes:
        captured_result_item_types (int): Specifies the type(s) of captured result item(s) that will be captured.
        roi (Quadrilateral): Specifies the region of interest (ROI) where the image capture and recognition will take place.
        roi_measured_in_percentage (int): Specifies whether the ROI is measured in pixels or as a percentage of the image size.
        max_parallel_tasks (int): Specifies the maximum number of parallel tasks that can be used for image capture and recognition.
        timeout (int): Specifies the maximum time (in milliseconds) allowed for image capture and recognition.
        barcode_settings (SimplifiedBarcodeReaderSettings): Specifies the settings for barcode recognition.
        label_settings (SimplifiedLabelRecognizerSettings): Specifies the settings for label recognition.
        document_settings (SimplifiedDocumentNormalizerSettings): Specifies the settings for document normalization.
        min_image_capture_interval (int): Specifies the minimum time interval (in milliseconds) allowed between consecutive image captures.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    captured_result_item_types: int = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_capturedResultItemTypes_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_capturedResultItemTypes_set,
        doc="Specifies the type(s) of captured result item(s) that will be captured. It is a bitwise OR combination of one or more values from the EnumCapturedResultItemType enumeration."
    )
    roi: Quadrilateral = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roi_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roi_set,
        doc="Specifies the region of interest (ROI) where the image capture and recognition will take place."
    )
    roi_measured_in_percentage: int = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roiMeasuredInPercentage_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roiMeasuredInPercentage_set,
        doc="Specifies whether the ROI is measured in pixels or as a percentage of the image size. Values: 0 the ROI is measured in pixels. 1 the ROI is measured as a percentage of the image size."
    )
    max_parallel_tasks: int = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_maxParallelTasks_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_maxParallelTasks_set,
        doc="Specifies the maximum number of parallel tasks that can be used for image capture and recognition."
    )
    timeout: int = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_timeout_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_timeout_set,
        doc="Specifies the maximum time (in milliseconds) allowed for image capture and recognition."
    )
    barcode_settings: "SimplifiedBarcodeReaderSettings" = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_barcodeSettings_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_barcodeSettings_set,
        doc="Specifies the settings for barcode recognition."
    )
    label_settings: "SimplifiedLabelRecognizerSettings" = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_labelSettings_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_labelSettings_set,
        doc="Specifies the settings for label recognition."
    )
    min_image_capture_interval: int = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_minImageCaptureInterval_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_minImageCaptureInterval_set,
        doc="""
            Specifies the minimum time interval (in milliseconds) allowed between consecutive image captures.
            This property represents the minimum time interval (in milliseconds) that must elapse before the next image capture operation can be initiated.
            Setting a larger value for this property will introduce a delay between image captures, while setting a smaller value allows for more frequent captures.
            It can be used to reduce the computational frequency, which can effectively lower energy consumption.
            Please note that the actual time interval between captures may be longer than the specified minimum interval due to various factors, such as image processing time and hardware limitations.
            """
    )
    document_settings: "SimplifiedDocumentNormalizerSettings" = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_documentSettings_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_documentSettings_set,
        doc="Specifies the settings for document normalization."
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_init(
            self, _DynamsoftCaptureVisionRouter.new_SimplifiedCaptureVisionSettings()
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_SimplifiedCaptureVisionSettings


_DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_register(
    SimplifiedCaptureVisionSettings
)

class CapturedResult(object):
    """
    The CapturedResult class represents the result of a capture operation on an image.
    Internally, CaptureResult stores an array that contains multiple items, each of which may be a barcode, text line, detected quad, normalized image, original image, parsed item, etc.

    Methods:
        get_original_image_hash_id(self) -> str: Gets the hash ID of the original image.
        get_original_image_tag(self) -> ImageTag: Gets the tag of the original image.
        get_items(self) -> List[CapturedResultItem]: Gets all items in the captured result.
        get_rotation_transform_matrix(self) -> List[float]: Gets the 3x3 rotation transformation matrix of the original image relative to the rotated image.
        get_error_code(self) -> int: Gets the error code of the capture operation.
        get_error_string(self) -> str: Gets the error message of the capture operation.
        get_decoded_barcodes_result(self) -> DecodedBarcodesResult: Gets the decoded barcode items from the CapturedResult.
        get_recognized_text_lines_result(self) -> RecognizedTextLinesResult: Gets the recognized text line items from the CapturedResult.
        get_detected_quads_result(self) -> DetectedQuadsResult: Gets the detected quads items from the CapturedResult.
        get_normalized_images_result(self) -> NormalizedImagesResult: Gets the normalized images items from the CapturedResult.
        get_parsed_result(self) -> ParsedResult: Gets the parsed result items from the CapturedResult.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftCaptureVisionRouter.CCapturedResult_Release

    def get_original_image_hash_id(self) -> str:
        """
        Gets the hash ID of the original image.

        Returns:
            The hash ID of the original image as a string.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetOriginalImageHashId(
            self
        )

    def get_original_image_tag(self) -> ImageTag:
        """
        Gets the tag of the original image.

        Returns:
            An ImageTag object containing the tag of the original image.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetOriginalImageTag(self)

    def get_rotation_transform_matrix(self) -> List[float]:
        """
        Gets the 3x3 rotation transformation matrix of the original image relative to the rotated image.

        Returns:
            A float list of length 9 which represents a 3x3 rotation matrix.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetRotationTransformMatrix(
            self
        )

    def get_items(self) -> List[CapturedResultItem]:
        """
        Gets all items in the captured result.

        Returns:
            A list of CapturedResultItem objects with all items in the captured result.
        """
        list = []
        count = _DynamsoftCaptureVisionRouter.CCapturedResult_GetItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftCaptureVisionRouter.CCapturedResult_GetItem(self, i))
        return list

    def __getitem__(self, index: int) -> CapturedResultItem:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetItem(self, index)

    def get_error_code(self) -> int:
        """
        Gets the error code of the capture operation.

        Returns:
            The error code of the capture operation.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetErrorCode(self)

    def get_error_string(self) -> str:
        """
        Gets the error message of the capture operation.

        Returns:
            The error message of the capture operation as a string.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetErrorString(self)

    def get_decoded_barcodes_result(self) -> "DecodedBarcodesResult":
        """
        Gets the decoded barcode items from the CapturedResult.

        Returns:
            A DecodedBarcodesResult object containing the decoded barcode items.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetDecodedBarcodesResult(
            self
        )

    def get_recognized_text_lines_result(self) -> "RecognizedTextLinesResult":
        """
        Gets the recognized text line items from the CapturedResult.

        Returns:
            A RecognizedTextLinesResult object containing the recognized text line items.
        """
        return (
            _DynamsoftCaptureVisionRouter.CCapturedResult_GetRecognizedTextLinesResult(
                self
            )
        )

    def get_detected_quads_result(self) -> "DetectedQuadsResult":
        """
        Gets the detected quads items from the CapturedResult.

        Returns:
            A DetectedQuadsResult object containing the detected quads items.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetDetectedQuadsResult(
            self
        )

    def get_normalized_images_result(self) -> "NormalizedImagesResult":
        """
        Gets the normalized images items from the CapturedResult.

        Returns:
            A NormalizedImagesResult object containing the normalized images items.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetNormalizedImagesResult(
            self
        )

    def get_parsed_result(self) -> "ParsedResult":
        """
        Gets the parsed result items from the CapturedResult.

        Returns:
            A ParsedResult object containing the parsed result items.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetParsedResult(self)


_DynamsoftCaptureVisionRouter.CCapturedResult_register(CapturedResult)

class CapturedResultReceiver(object):
    """
    The CapturedResultReceiver class is responsible for receiving captured results.
    It contains several callback functions for different types of results, including original image, decoded barcodes, recognized text lines, detected quads, normalized images, and parsed results.

    Methods:
        get_name(self) -> str: Gets the name of the captured result receiver.
        set_name(self, name: str) -> None: Sets the name of the captured result receiver.
        on_captured_result_received(self, captured_result: CapturedResult) -> None: Callback function triggered after processing each image and returns all captured results.
        on_original_image_result_received(self, original_image_result: OriginalImageResultItem) -> None: Callback function triggered when start processing each image and returns the original image result.
        on_decoded_barcodes_received(self, decoded_barcodes_result: DecodedBarcodesResult) -> None: Callback function triggered after processing each image and returns all decoded barcodes results.
        on_recognized_text_lines_received(self, recognized_text_lines_result: RecognizedTextLinesResult) -> None: Callback function triggered after processing each image and returns all recognized text lines results.
        on_detected_quads_received(self, detected_quads_result: DetectedQuadsResult) -> None: Callback function triggered after processing each image and returns all detected quads results.
        on_normalized_images_received(self, normalized_images_result: NormalizedImagesResult) -> None: Callback function triggered after processing each image and returns all normalized images results.
        on_parsed_results_received(self, parsed_result: ParsedResult) -> None: Callback function triggered after processing each image and returns all parsed results.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
         if type(self) is CapturedResultReceiver:
            raise TypeError("Cannot create an instance of an abstract class.")
         else:
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
                self, _DynamsoftCaptureVisionRouter.new_CCapturedResultReceiver(self)
            )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCapturedResultReceiver
    def get_name(self) -> str:
        """
        Gets the name of the captured result receiver.

        Returns:
            The name of the captured result receiver.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_GetName(self)

    def set_name(self, name: str) -> None:
        """
        Sets the name of the captured result receiver.

        Args:
            name(str): The name of the captured result receiver.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_SetName(self, name)

    def on_captured_result_received(self, result: CapturedResult) -> None:
        """
        Callback function triggered after processing each image and returns all captured results.

        Args:
            result(CapturedResult): The captured result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnCapturedResultReceived(
            self, result
        )

    def on_original_image_result_received(
        self, result: OriginalImageResultItem
    ) -> None:
        """
        Callback function triggered when start processing each image and returns the original image result.
        For the callback to be triggered, it is essential that the parameter `OutputOriginalImage` is set to value `1`.

        Args:
            result(OriginalImageResultItem): The original image result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnOriginalImageResultReceived(
            self, result
        )

    def on_decoded_barcodes_received(self, result: "DecodedBarcodesResult") -> None:
        """
        Callback function triggered after processing each image and returns all decoded barcodes.
        For the callback to be triggered, it is essential that the `BarcodeReaderTask` is properly configured.

        Args:
            result(DecodedBarcodesResult): The decoded barcodes result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnDecodedBarcodesReceived(
            self, result
        )

    def on_recognized_text_lines_received(
        self, result: "RecognizedTextLinesResult"
    ) -> None:
        """
        Callback function triggered after processing each image and returns all recognized text lines.
        For the callback to be triggered, it is essential that the `LabelRecognizerTask` is properly configured.

        Args:
            result(RecognizedTextLinesResult): The recognized text lines result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnRecognizedTextLinesReceived(
            self, result
        )

    def on_detected_quads_received(self, result: "DetectedQuadsResult") -> None:
        """
        Callback function triggered after processing each image and returns all detected quads.
        For the callback to be triggered, it is essential that the `DocumentNormalizerTask` is properly configured.

        Args:
            result(DetectedQuadsResult): The detected quads result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnDetectedQuadsReceived(
            self, result
        )

    def on_normalized_images_received(self, result: "NormalizedImagesResult") -> None:
        """
        Callback function triggered after processing each image and returns all normalized images.
        For the callback to be triggered, it is essential that the `DocumentNormalizerTask` is properly configured.

        Args:
            result(NormalizedImagesResult): The normalized images result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnNormalizedImagesReceived(
            self, result
        )

    def on_parsed_results_received(self, result: "ParsedResult") -> None:
        """
        Callback function triggered after processing each image and returns all parsed results.
        For the callback to be triggered, it is essential that the `CodeParserTask` is properly configured.

        Args:
            result(ParsedResult): The parsed result.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnParsedResultsReceived(
            self, result
        )


_DynamsoftCaptureVisionRouter.CCapturedResultReceiver_register(CapturedResultReceiver)

class CapturedResultFilter(object):
    """
    The CapturedResultFilter class is responsible for filtering captured results.
    It contains several callback functions for different types of results, including original image, decoded barcodes, recognized text lines, detected quads, normalized images, and parsed results.

    Methods:
        get_name(self): Gets the name of the captured result filter.
        set_name(self, name: str): Sets the name of the captured result filter.        
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        if type(self) is CapturedResultFilter:
            raise TypeError("Cannot create an instance of an abstract class.")
        else:
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
                self, _DynamsoftCaptureVisionRouter.new_CCapturedResultFilter(self)
            )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCapturedResultFilter

    def get_name(self) -> str:
        """
        Gets the name of the captured result filter.

        Returns:
            str: The name of the captured result filter.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_GetName(self)

    def set_name(self, name: str) -> None:
        """
        Sets the name of the captured result filter.

        Args:
            name(str): The name of the captured result filter.
        """
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_SetName(self, name)

    def on_original_image_result_received(
        self, result: OriginalImageResultItem
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnOriginalImageResultReceived(
            self, result
        )

    def on_decoded_barcodes_received(self, result: "DecodedBarcodesResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnDecodedBarcodesReceived(
            self, result
        )

    def on_recognized_text_lines_received(
        self, result: "RecognizedTextLinesResult"
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnRecognizedTextLinesReceived(
            self, result
        )

    def on_detected_quads_received(self, result: "DetectedQuadsResult") -> None:
        return (
            _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnDetectedQuadsReceived(
                self, result
            )
        )

    def on_normalized_images_received(self, result: "NormalizedImagesResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnNormalizedImagesReceived(
            self, result
        )

    def on_parsed_results_received(self, result: "ParsedResult") -> None:
        return (
            _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnParsedResultsReceived(
                self, result
            )
        )


_DynamsoftCaptureVisionRouter.CCapturedResultFilter_register(CapturedResultFilter)

class CaptureStateListener(ABC):
    """
    Defines a listener for capture state changes.

    Methods:
        on_capture_state_changed(self, state: int) -> None: Called when the capture state changes.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
            self, _DynamsoftCaptureVisionRouter.new_CCaptureStateListener(self)
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCaptureStateListener

    @abstractmethod
    def on_capture_state_changed(self, state: int) -> None:
        """
        Called when the capture state changes.

        Args:
            state (int): The new capture state. It is one of the values of the EnumCaptureState enumeration.
        """
        pass


_DynamsoftCaptureVisionRouter.CCaptureStateListener_register(CaptureStateListener)

class ImageSourceStateListener(ABC):
    """
    Defines a listener for image source state changes.

    Methods:
        on_image_source_state_received(self, state: int) -> None: This method is called when the state of the image source changes.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
            self, _DynamsoftCaptureVisionRouter.new_CImageSourceStateListener(self)
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CImageSourceStateListener

    @abstractmethod
    def on_image_source_state_received(self, state: int) -> None:
        """
        This method is called when the state of the image source changes.

        Args:
            state (int): The state of the image source. It is one of the values of the EnumImageSourceState enumeration.
        """
        pass


_DynamsoftCaptureVisionRouter.CImageSourceStateListener_register(
    ImageSourceStateListener
)

class BufferedItemsManager:
    """
    Defines a listener for image source state changes.

    Methods:
        set_max_buffered_items_count(self, count: int) -> None: Sets the maximum number of buffered items.
        get_max_buffered_items_count(self) -> int: Gets the maximum number of buffered items.
        get_buffered_character_item_set(self) -> "BufferedCharacterItemSet": Gets the buffered recognized character items.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        """
        Initializes a new instance of the BufferedItemsManager class.

        Raises:
            AttributeError: No constructor defined - class is abstract.
        """
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CBufferedItemsManager

    def set_max_buffered_items_count(self, count: int) -> None:
        """
        Sets the maximum number of buffered items.

        Args:
            count (int): The maximum number of buffered items.
        """
        return _DynamsoftCaptureVisionRouter.CBufferedItemsManager_SetMaxBufferedItems(
            self, count
        )

    def get_max_buffered_items_count(self) -> int:
        """
        Gets the maximum number of buffered items.

        Returns:
            int: The maximum number of buffered items.
        """
        return _DynamsoftCaptureVisionRouter.CBufferedItemsManager_GetMaxBufferedItems(
            self
        )

    def get_buffered_character_item_set(self) -> "BufferedCharacterItemSet":
        """
        Gets the buffered recognized character items.

        Returns:
            BufferedCharacterItemSet: The buffered recognized character items.
        """
        return _DynamsoftCaptureVisionRouter.CBufferedItemsManager_GetBufferedCharacterItemSet(
            self
        )
        
_DynamsoftCaptureVisionRouter.CBufferedItemsManager_register(BufferedItemsManager)


class CaptureVisionRouter(object):
    """
    The CaptureVisionRouter class is what a user uses to interact with image-processing and semantic-processing products in their applications.
    It accepts an image source and returns processing results which may contain Final results.

    Methods:
        init_settings(self, content: str) -> Tuple[int, str]: Loads and initializes a template from a string.
        init_settings_from_file(self, file_path: str) -> Tuple[int, str]: Loads and initializes a template from a file.
        output_settings(self, template_name: str) -> Tuple[int, str, str]: Exports a specific template to a string.
        output_settings_to_file(self, template_name: str, file_path: str) -> Tuple[int, str]: Exports a specific template to a file.
        get_simplified_settings(self, template_name: str) -> Tuple[int, str, SimplifiedCaptureVisionSettings]: Retrieves a simplified version of the capture settings for a specific template.
        update_settings(self, template_name: str, settings: SimplifiedCaptureVisionSettings) -> Tuple[int, str]: Updates a template with simplified capture settings.
        reset_settings(self) -> Tuple[int, str]: Resets all templates to factory settings.
        capture(self, *args) -> CapturedResult: Process an image or file to derive important information. It can optionally use a specified template for the capture.
        set_input(self, adapter: ImageSourceAdapter) -> Tuple[int, str]: Sets an image source to provide images for consecutive process.
        get_input(self) -> ImageSourceAdapter: Gets the attached image source adapter object of the capture vision router.
        add_image_source_state_listener(self, listener: ImageSourceStateListener) -> Tuple[int, str]: Adds an object that listens to state changes of the image source.
        remove_image_source_state_listener(self, listener: ImageSourceStateListener) -> Tuple[int, str]: Removes an object which listens to state changes of the image source.
        add_result_receiver(self, receiver: CapturedResultReceiver) -> Tuple[int, str]: Adds an object as the receiver of captured results.
        remove_result_receiver(self, receiver: CapturedResultReceiver) -> Tuple[int, str]: Removes an object which was added as a receiver of captured results.
        add_result_filter(self, filter: CapturedResultFilter) -> Tuple[int, str]: Adds an object as the filter of captured results.
        remove_result_filter(self, filter: CapturedResultFilter) -> Tuple[int, str]: Removes an object which was added as a filter of captured results.
        add_capture_state_listener(self, listener: CaptureStateListener) -> Tuple[int, str]: Adds an object that listens to the state changes of the capture process.
        remove_capture_state_listener(self, listener: CaptureStateListener) -> Tuple[int, str]: Removes an object which listens to the state changes of the capture process.
        start_capturing(self, template_name: str = "", wait_for_thread_exit: bool = False) -> Tuple[int, str]: Starts to process images consecutively.
        stop_capturing(self, wait_for_remaining_tasks: bool = True, wait_for_thread_exit: bool = True) -> None: Stops the multiple-file processing.
        pause_capturing(self) -> None: Pauses the capture process. The current thread will be blocked until the capture process is resumed.
        resume_capturing(self) -> None: Resumes the capture process. The current thread will be unblocked after the capture process is resumed.
        get_buffered_items_manager(self) -> BufferedItemsManager: Gets a BufferedItemsManager object.
    """

    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_init(
            self, _DynamsoftCaptureVisionRouter.new_CCaptureVisionRouter()
        )
        self._input = None

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCaptureVisionRouter

    def init_settings(self, content: str) -> Tuple[int, str]:
        """
        Loads and initializes a template from a string.

        Args:
            content (str): The string containing the template.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_InitSettings(
            self, content
        )

    def init_settings_from_file(self, file_path: str) -> Tuple[int, str]:
        """
        Loads and initializes a template from a file.

        Args:
            file_path (str): The path to the file containing the template.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_InitSettingsFromFile(
            self, file_path
        )

    def output_settings(self, template_name: str) -> Tuple[int, str, str]:
        """
        Exports a specific template to a string.
        It is supported to export all loaded templates by specifying the template_name as '*'.

        Args:
            template_name (str): The name of the template to be exported.

        Returns:
            A tuple containing an error code, error message, and a string containing the exported template.   
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_OutputSettings(
            self, template_name
        )

    def output_settings_to_file(
        self, template_name: str, file_path: str
    ) -> Tuple[int, str]:
        """
        Exports a specific template to a file.
        It is supported to export all loaded templates by specifying the template_name as '*'.

        Args:
            template_name (str): The name of the template to be exported.
            file_path (str): The path to the output file.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_OutputSettingsToFile(
            self, template_name, file_path
        )

    def get_simplified_settings(
        self, template_name: str
    ) -> Tuple[int, str, SimplifiedCaptureVisionSettings]:
        """
        Retrieves a simplified version of the capture settings for a specific template.

        Args:
            template_name (str): The name of the template.

        Returns:
            A tuple containing an error code, error message, and a SimplifiedCaptureVisionSettings object.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_GetSimplifiedSettings(
            self, template_name
        )
    
    def update_settings(
        self, template_name: str, settings: SimplifiedCaptureVisionSettings
    ) -> Tuple[int, str]:
        """
        Updates a template with simplified capture settings.

        Args:
            template_name (str): The name of the template to update.
            settings (SimplifiedCaptureVisionSettings): A pointer to a SimplifiedCaptureVisionSettings object.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_UpdateSettings(
            self, template_name, settings
        )
    
    def reset_settings(self) -> Tuple[int, str]:
        """
        Resets all templates to factory settings.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_ResetSettings(self)

    def capture(self, *args) -> CapturedResult:
        """
        Process an image or file to derive important information. It can optionally use a specified template for the capture.

        Args:
            A variable-length argument list. Can be one of the following:
            - file_path (str), template_name (str, optional): Specifies the path of the file to process and the template to use for capturing.
            - file_bytes (bytes), template_name (str, optional): Specifies the image file bytes in memory to process and the template to use for capturing.
            - image_data (ImageData), template_name (str, optional): Specifies the image data to process and the template to use for capturing.

        Returns:
            A CapturedResult object containing the captured items.
        """
        ret = _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_Capture(self, *args)
        return ret

    def set_input(self, adapter: ImageSourceAdapter) -> Tuple[int, str]:
        """
        Sets an image source to provide images for consecutive process.

        Args:
            adapter (ImageSourceAdapter): Specifies an object which has implemented the ImageSourceAdapter Class.
        
        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        ret = _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_SetInput(self, adapter)
        if ret[0] == 0:
            self._input = adapter
        return ret

    def get_input(self) -> ImageSourceAdapter:
        """
        Gets the attached image source adapter object of the capture vision router.

        Returns:
            The attached image source adapter object of the capture vision router.
        """
        return self._input

    def add_image_source_state_listener(
        self, listener: ImageSourceStateListener
    ) -> Tuple[int, str]:
        """
        Adds an object that listens to state changes of the image source.

        Args:
            listener (ImageSourceStateListener): Specifies a listening object of the type ImageSourceStateListener.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddImageSourceStateListener(
            self, listener
        )

    def remove_image_source_state_listener(
        self, listener: ImageSourceStateListener
    ) -> Tuple[int, str]:
        """
        Removes an object which listens to state changes of the image source.

        Args:
            listener (ImageSourceStateListener): Specifies a listening object of the type ImageSourceStateListener.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveImageSourceStateListener(
            self, listener
        )

    def add_result_receiver(self, receiver: CapturedResultReceiver) -> Tuple[int, str]:
        """
        Adds an object as the receiver of captured results.

        Args:
            receiver (CapturedResultReceiver): Specifies a receiver object of the type CapturedResultReceiver.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddResultReceiver(
            self, receiver
        )

    def remove_result_receiver(
        self, receiver: CapturedResultReceiver
    ) -> Tuple[int, str]:
        """
        Removes an object which was added as a receiver of captured results.

        Args:
            receiver (CapturedResultReceiver): Specifies a receiver object of the type CapturedResultReceiver.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveResultReceiver(
            self, receiver
        )

    def add_result_filter(self, filter: CapturedResultFilter) -> Tuple[int, str]:
        """
        Adds an object as the filter of captured results.

        Args:
            filter (CapturedResultFilter): Specifies a filter object of the type CapturedResultFilter.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddResultFilter(
            self, filter
        )

    def remove_result_filter(self, filter: CapturedResultFilter) -> Tuple[int, str]:
        """
        Removes an object which was added as a filter of captured results.

        Args:
            filter (CapturedResultFilter): Specifies a filter object of the type CapturedResultFilter.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveResultFilter(
            self, filter
        )
    def add_capture_state_listener(
        self, listener: CaptureStateListener
    ) -> Tuple[int, str]:
        """
        Adds an object that listens to the state changes of the capture process.

        Args:
            listener (CaptureStateListener): Specifies a listening object of the type CaptureStateListener.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return (
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddCaptureStateListener(
                self, listener
            )
        )
    def remove_capture_state_listener(
        self, listener: CaptureStateListener
    ) -> Tuple[int, str]:
        """
        Removes an object which listens to the state changes of the capture process.

        Args:
            listener (CaptureStateListener): Specifies a listening object of the type CaptureStateListener.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveCaptureStateListener(
            self, listener
        )

    def start_capturing(
        self, template_name: str = "", wait_for_thread_exit: bool = False
    ) -> Tuple[int, str]:
        """
        Starts to process images consecutively.

        Args:
            template_name (str): Specifies a template to use for capturing. Setting an empty string means the factory default template.
            wait_for_thread_exit (bool): Indicates whether to wait for the capture process to complete before returning. The default value is False.

        Returns:
            A tuple containing following elements:
            - error_code <int>: The error code indicating the status of the operation.
            - error_message <str>: A descriptive message explaining the error.
        """
        ret = _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_StartCapturing(
            self, template_name, wait_for_thread_exit
        )
        return ret

    def stop_capturing(
        self, wait_for_remaining_tasks: bool = True, wait_for_thread_exit: bool = True
    ) -> None:
        """
        Stops the multiple-file processing.

        Args:
            wait_for_remaining_tasks (bool): Indicates whether to wait for the remaining tasks to complete before returning. The default value is True.
            wait_for_thread_exit (bool): Indicates whether to wait for the capture process to complete before returning. The default value is True.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_StopCapturing(
            self, wait_for_remaining_tasks, wait_for_thread_exit
        )

    def pause_capturing(self) -> None:
        """
        Pauses the capture process. The current thread will be blocked until the capture process is resumed.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_PauseCapturing(self)

    def resume_capturing(self) -> None:
        """
        Resumes the capture process. The current thread will be unblocked after the capture process is resumed.
        """
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_ResumeCapturing(self)

    def get_buffered_items_manager(self) -> BufferedItemsManager:
        """
        Gets a BufferedItemsManager object.

        Returns:
            A BufferedItemsManager object.
        """
        return (
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_GetBufferedItemsManager(
                self
            )
        )


_DynamsoftCaptureVisionRouter.CCaptureVisionRouter_register(CaptureVisionRouter)


class CaptureVisionRouterModule(object):
    """
    The CaptureVisionRouterModule class defines general functions in the capture vision router module.

    Methods:
        get_version() -> str: Returns the version of the capture vision router module.
    """
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        """
        Returns the version of the capture vision router module.

        Returns:
            A string representing the version of the capture vision router module.
        """
        return __version__ + " (Algotithm " + _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_GetVersion() + ")"

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
            self, _DynamsoftCaptureVisionRouter.new_CCaptureVisionRouterModule()
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCaptureVisionRouterModule


_DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_register(
    CaptureVisionRouterModule
)
