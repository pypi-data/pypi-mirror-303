from PIL import Image


def pixelate_image_file(image_filename: str, i_size, output_filename: str):
    """
    Pixelates the provided 'image_filename' and saves it as the 'output_filename'.
    The 'i_size' is the pixelating square. The smaller it is, the less pixelated 
    its.

    'i_size' must be a tuple such as (8, 8) or (16, 16).
    """
    if not image_filename:
        return None
    
    # TODO: Handle 'i_size' format and check
    
    if not output_filename:
        return None

    img = Image.open(image_filename)

    # Convert to small image
    small_img = img.resize(i_size,Image.BILINEAR)

    # Resize to output size
    res = small_img.resize(img.size, Image.NEAREST)

    res.save(output_filename)