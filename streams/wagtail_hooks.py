
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.core import hooks


# @hooks.register("register_rich_text_features")
# def register_code_styling(features):
#     """Add <code> to the richtext editor."""

#     feature_name = "code"
#     type_ = "CODE"
#     tag = "code"

#     control = {
#         "type": type_,
#         "label": "</>",
#         "description": "Code",
#     }

#     features.register_editor_plugin(
#         "draftail", feature_name, draftail_features.InlineStyleFeature(control)
#     )

#     db_conversion = {
#         "from_database_format": {tag: InlineStyleElementHandler(type_)},
#         "to_database_format": {"style_map": {type_: {"element": tag}}},
#     }

#     features.register_converter_rule("contentstate", feature_name, db_conversion)

#     features.default_features.append(feature_name)


@hooks.register("register_rich_text_features")
def register_centertext_feature(features):
    """Adds centered textore to the richtext editor"""

    feature_name = "center"
    type_ = "CENTERTEXT"
    tag = "div"

    control = {
        "type": type_,
        "label": "Center",
        "description": "Center Text",
        "style": {
            "display": "block",
            "text-align": "center",
        }
    }

    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "class": "text-center"
                    }
                }
            }
        },
    }

    features.register_converter_rule("contentstate", feature_name, db_conversion)

    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def enable_blockquote_feature(features):
    features.default_features.append('blockquote')