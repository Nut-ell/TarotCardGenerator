import random
from PIL import Image

# Dictionary linking card names to image file names
card_images = {
    "0 The Fool": "card_images/0_the_fool.png",
    "1 The Magician": "card_images/1_the_magician.png"
    # ... add the rest of the cards as you go
}

# Randomly select a Major Arcana card from the available ones
card_name = random.choice(list(card_images.keys()))
image_path = card_images[card_name]

# Display the card's name
print(f"Your card is: {card_name}")

# Open and display the card image
card_image = Image.open(image_path)
card_image.show()

