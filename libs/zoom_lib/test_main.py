from main import process_image

def test_process_image():
    assert process_image() == "Image processed with filter: none, brightness adjustment: 0, contrast adjustment: 0!"
    assert process_image("blur", 20, 10) == "Image processed with filter: blur, brightness adjustment: 20, contrast adjustment: 10!"
    assert process_image("sharpen", -5, 10) == "Image processed with filter: sharpen, brightness adjustment: -5, contrast adjustment: 10!"
