from PIL import Image

def load_image(image_path):
   
    return Image.open(image_path)

def save_image(image, output_path):
    
    image.save(output_path)

def encrypt_image(image, key):
    """Encrypt an image using pixel manipulation."""
    encrypted_image = image.copy()
    pixels = encrypted_image.load()
    width, height = encrypted_image.size
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Simple encryption by adding the key to each RGB component
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    
    return encrypted_image

def decrypt_image(encrypted_image, key):
  
    decrypted_image = encrypted_image.copy()
    pixels = decrypted_image.load()
    width, height = decrypted_image.size
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Reverse the encryption by subtracting the key from each RGB component
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    
    return decrypted_image


image_path = 'input_image.jpg'
output_encrypted_path = 'encrypted_image.png'
output_decrypted_path = 'decrypted_image.png'
encryption_key = 50  # Choose a key for encryption


image = load_image(image_path)

# Encrypt the image
encrypted_image = encrypt_image(image, encryption_key)
save_image(encrypted_image, output_encrypted_path)

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, encryption_key)
save_image(decrypted_image, output_decrypted_path)

print("Encryption and decryption completed.")
