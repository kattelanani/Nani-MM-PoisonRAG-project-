
from pathlib import Path
from PIL import Image
import json


class ImageRetriever:

    def __init__(self, image_folder="data/images"):
        self.image_folder = Path(image_folder)

    def load_images(self):
        supported = {".jpg", ".jpeg", ".png"}
        images = []

        if not self.image_folder.exists():
            print("Image folder does not exist.")
            return images

        for path in self.image_folder.iterdir():
            if path.suffix.lower() in supported:
                try:
                    with Image.open(path) as image:
                        width, height = image.size

                    images.append({
                        "filename": path.name,
                        "path": str(path),
                        "width": width,
                        "height": height
                    })

                except Exception as error:
                    print("Could not load:", path.name, error)

        return images

    def search(self, keyword):
        images = self.load_images()
        keyword = keyword.lower().strip()

        results = [
            image for image in images
            if keyword in image["filename"].lower()
        ]

        return results


if __name__ == "__main__":
    retriever = ImageRetriever()

    print("Available images:")
    for image in retriever.load_images():
        print(image)

    query = input("\nSearch image by filename: ")

    results = retriever.search(query)

    print("\nMatching images:")

    if results:
        for result in results:
            print(result)
    else:
        print("No matching images found.")
