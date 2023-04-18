"""StreamFields live in here."""

from ctypes import alignment
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from bs4 import BeautifulSoup


class RichTextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Rich Text Block"

class ImageBlock(blocks.StructBlock):
    """Image block with options."""

    image = ImageChooserBlock(required=True)
    image_caption = blocks.CharBlock(required=False)

    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Block Image"

class ImageBlockExtra(blocks.StructBlock):
    """Image block with extra options."""

    image = ImageChooserBlock(required=True)
    image_caption = blocks.CharBlock(required=False)
    alignment = blocks.ChoiceBlock(
        choices=[
            ("start", "Left"),
            ("center", "Center"),
            ("end", "Right"),
        ],
        blank=False,
        default="Left",
    )
    width = blocks.ChoiceBlock(
        choices=[
            ("10", "10%"),
            ("20", "20%"),
            ("30", "30%"),
            ("40", "40%"),
            ("50", "50%"),
            ("60", "60%"),
            ("70", "70%"),
            ("80", "80%"),
            ("90", "90%"),
            ("100", "100%"),
        ],
        blank=False,
        default="80%",
    )

    class Meta:
        template = "streams/image_block_extra.html"
        icon = "image"
        label = "Block Image w/ Options"

# class HTMLStructValue(blocks.StructValue):
#     """Additional logic for HTML Block."""

#     def raw_html(self):
#         input_html = self.get("input_html")
#         html_soup = BeautifulSoup(input_html, 'html.parser')
#         hide_caption = self.get("hide_caption")
#         if hide_caption:
#             # try:
#             html_soup.find('p').decompose()
#             print(type(input_html))
#             return html_soup
#             # except:
#             #     return input_html
#         else:
#             return input_html
        

class GIFEmbedBlock(blocks.StructBlock):
    """Image block with extra options."""

    input_html = blocks.RawHTMLBlock()
    # hide_caption = blocks.BooleanBlock(required=False)
    alignment = blocks.ChoiceBlock(
        choices=[
            ("start", "Left"),
            ("center", "Center"),
            ("end", "Right"),
        ],
        blank=False,
        default="Center",
    )
    width = blocks.ChoiceBlock(
        choices=[
            ("10", "10%"),
            ("20", "20%"),
            ("30", "30%"),
            ("40", "40%"),
            ("50", "50%"),
            ("60", "60%"),
            ("70", "70%"),
            ("80", "80%"),
            ("90", "90%"),
            ("100", "100%"),
        ],
        blank=False,
        default="80%",
    )



    class Meta:
        template = "streams/gif_embed_block.html"
        icon = "code"
        label = "GIF Embed Block"
        # value_class = HTMLStructValue

class ImageRowBlock(blocks.StructBlock):
    """Row of four images."""

    image_1 = ImageChooserBlock(required=True)
    image_1_caption = blocks.CharBlock(required=False)
    image_2 = ImageChooserBlock(required=True)
    image_2_caption = blocks.CharBlock(required=False)
    image_3 = ImageChooserBlock(required=True)
    image_3_caption = blocks.CharBlock(required=False)
    image_4 = ImageChooserBlock(required=True)
    image_4_caption = blocks.CharBlock(required=False)

    class Meta:
        template = "streams/image_row_block.html"
        icon = "image"
        label = "Image Row"

class ImageCarouselBlock(blocks.StructBlock):
    """Image carousel with options."""

    slides = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("caption", blocks.CharBlock(required=False, max_length=100)),
            ]
        )
    )

    show_download_links = blocks.BooleanBlock(required=True, default=False)

    class Meta:
        template = "streams/image_carousel_block.html"
        icon = "image"
        label = "Image Carousel"

class LeftImageBlock(blocks.StructBlock):
    """2 column image block with options."""

    image = ImageChooserBlock(required=True)
    image_caption = blocks.CharBlock(required=False)

    content = blocks.RichTextBlock(required=False)

    class Meta:
        template = "streams/left_image_block.html"
        icon = "image"
        label = "Left Image"

class ButtonStructValue(blocks.StructValue):
    """Additional logic for buttons."""

    def url(self):
        button_page = self.get("button_page")
        button_url = self.get("button_url")
        
        if button_page:
            return button_page.url
        elif button_url:
            return button_url
        return None

class ButtonBlock(blocks.StructBlock):
    """An external or internal URL."""

    button_text = blocks.CharBlock(required=True)
    button_style = blocks.ChoiceBlock(
        choices=[
            ("btn", "Standard"),
            ("btn-outline", "Outline"),
        ],
        blank=False,
        default="Outline",
    )
    button_page = blocks.PageChooserBlock(required=False, help_text="Page overrides URL if one is chosen.")
    button_url = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/button_block.html"
        icon = "link"
        label = "Single Button"
        value_class = ButtonStructValue

class HeadlineBlock(blocks.StructBlock):
    """Styled headline."""

    headline_text = blocks.CharBlock(required=True)

    class Meta:
        template = "streams/headline_block.html"
        icon = "link"
        label = "Headline Block"