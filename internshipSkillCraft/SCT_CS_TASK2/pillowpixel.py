from PIL import Image
import os

def encrypt_image(image_path, method):
    try:
        image = Image.open(image_path)
        pixels = image.load()
        width, height = image.size

        if method == 'swap':
            print("🔄 Swapping pixels horizontally...")
            for y in range(height):
                for x in range(width // 2):
                    left = pixels[x, y]
                    right = pixels[width - 1 - x, y]
                    pixels[x, y], pixels[width - 1 - x, y] = right, left

        elif method == 'invert':
            print("🎨 Inverting pixel colors...")
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (255 - r, 255 - g, 255 - b)

        else:
            print("❌ Unknown method selected.")
            return

        # Save the encrypted image
        new_filename = f'encrypted_{method}.png'
        image.save(new_filename)
        print(f"✅ All done! Your encrypted image is saved as: {new_filename}")

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")

def main():
    print("🔐 Welcome to the Simple Image Encryption Tool!")
    print("This tool lets you 'hide' your image using fun pixel manipulation.\n")

    image_path = input("📁 Enter the path to your image (e.g., 'photo.jpg'): ").strip()

    if not os.path.isfile(image_path):
        print("❌ Hmm, that file doesn’t seem to exist. Try again with a valid path.")
        return

    print("\n✨ Choose how you’d like to encrypt your image:")
    print("1️⃣ Swap pixels horizontally")
    print("2️⃣ Invert each pixel’s color")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == '1':
        encrypt_image(image_path, 'swap')
    elif choice == '2':
        encrypt_image(image_path, 'invert')
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
