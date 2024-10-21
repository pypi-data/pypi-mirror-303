from googletrans import Translator
from blikon_sdk.v2.models.sdk_configuration_model import SDKConfiguration
from blikon_sdk.v2.core.core import Core
from blikon_sdk.v2.services.log_service import LogService


def msg(text: str) -> str:
    sdk_configuration: SDKConfiguration = Core.get_sdk_configuration()
    log_service: LogService = Core.get_log_service()
    translator = Translator()
    app_language = sdk_configuration.sdk_settings.client_application_language
    traduccion: str = text
    try:
        # Detect the language automatically
        detected_language = translator.detect(text).lang

        log_service.info(
            f"Starting translation from language '{detected_language}' to '{app_language}'",
            text_to_translate=text,
            source="blikon_sdk",
            file_name="msg_helper.py",
            function_name="msg"
        )

        # Log if detection failed
        if detected_language is None:
            log_service.error(
                "Language detection failed",
                text_to_translate=text,
                source="blikon_sdk",
                file_name="msg_helper.py",
                function_name="msg"
            )
            return traduccion

        # Translate only if detected language differs from app client language
        if detected_language != app_language:
            result = translator.translate(
                text=text, src=detected_language, dest=app_language
            )
            traduccion = result.text

    except Exception as e:
        log_service.error(
            f"Unable to translate to '{app_language}' language",
            error_message=str(e),
            text_to_translate=text,
            source="blikon_sdk",
            file_name="msg_helper.py",
            function_name="msg"
        )
    return traduccion
