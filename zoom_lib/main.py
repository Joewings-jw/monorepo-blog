def process_image(filter_type: str = "none", brightness: int = 0, contrast: int = 0) -> str:
    return (f"Image processed with filter: {filter_type}, "
            f"brightness adjustment: {brightness}, "
            f"contrast adjustment: {contrast}!")
