from main import capture_image

def test_capture_image():
    assert capture_image() == "Image captured with resolution 1080p in JPEG format!"
    assert capture_image("720p", "PNG") == "Image captured with resolution 720p in PNG format!"
    assert capture_image("4K", "BMP") == "Image captured with resolution 4K in BMP format!"