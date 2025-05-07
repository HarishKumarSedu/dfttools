import EasyMCP2221
from PIL import Image, ImageDraw, ImageFont
import time
import keyboard  # For capturing arrow keys

# OLED parameters
OLED_WIDTH = 128
OLED_HEIGHT = 64
OLED_I2C_ADDR = 0x3C
CELL_SIZE = 8  # Each snake segment is 8x8 pixels
GRID_WIDTH = OLED_WIDTH // CELL_SIZE  # 16
GRID_HEIGHT = OLED_HEIGHT // CELL_SIZE  # 8

# Initialize MCP2221 device
mcp = EasyMCP2221.Device()

def send_command(cmd):
    mcp.I2C_write(OLED_I2C_ADDR, [0x00, cmd])

def send_commands(cmds):
    for cmd in cmds:
        send_command(cmd)

def send_data(data):
    chunk_size = 60
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        mcp.I2C_write(OLED_I2C_ADDR, [0x40] + list(chunk))

def oled_init():
    cmds = [
        0xAE, 0x20, 0x00, 0xB0, 0xC8,
        0x00, 0x10, 0x40, 0x81, 0x7F,
        0xA1, 0xA6, 0xA8, 0x3F, 0xA4,
        0xD3, 0x00, 0xD5, 0x80, 0xD9,
        0xF1, 0xDA, 0x12, 0xDB, 0x40,
        0x8D, 0x14, 0xAF
    ]
    send_commands(cmds)

def clear_display():
    for page in range(8):
        send_command(0xB0 + page)
        send_command(0x00)
        send_command(0x10)
        send_data([0x00] * OLED_WIDTH)

def display_image(image):
    bw_image = image.convert('1')
    buffer = bytearray(OLED_WIDTH * OLED_HEIGHT // 8)
    pixels = bw_image.load()

    for x in range(OLED_WIDTH):
        for page in range(OLED_HEIGHT // 8):
            byte = 0
            for bit in range(8):
                y = page * 8 + bit
                if pixels[x, y] == 255:
                    byte |= (1 << bit)
            buffer[x + page * OLED_WIDTH] = byte

    for page in range(8):
        send_command(0xB0 + page)
        send_command(0x00)
        send_command(0x10)
        start = page * OLED_WIDTH
        end = start + OLED_WIDTH
        send_data(buffer[start:end])

# Game logic

class SnakeGame:
    def __init__(self):
        self.snake = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.direction = (1, 0)  # Moving right initially
        self.spawn_food()
        self.game_over = False
        self.score = 0

    def spawn_food(self):
        import random
        while True:
            self.food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if self.food not in self.snake:
                break

    def change_direction(self, new_dir):
        # Prevent snake from reversing
        if (new_dir[0] == -self.direction[0] and new_dir[1] == -self.direction[1]):
            return
        self.direction = new_dir

    def update(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Check collisions with walls
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            self.game_over = True
            return

        # Check collisions with self
        if new_head in self.snake:
            self.game_over = True
            return

        # Move snake
        self.snake.insert(0, new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()  # Remove tail

    def draw(self):
        image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))
        draw = ImageDraw.Draw(image)

        # Draw food
        fx, fy = self.food
        draw.rectangle([fx*CELL_SIZE, fy*CELL_SIZE, 
                        fx*CELL_SIZE + CELL_SIZE - 1, fy*CELL_SIZE + CELL_SIZE - 1], fill=255)

        # Draw snake
        for x, y in self.snake:
            draw.rectangle([x*CELL_SIZE, y*CELL_SIZE, 
                            x*CELL_SIZE + CELL_SIZE - 1, y*CELL_SIZE + CELL_SIZE - 1], fill=255)

        display_image(image)

# Global game instance to be accessed in keyboard callbacks
game = None

def on_key_event(event):
    if game is None or game.game_over:
        return

    if event.name == 'up':
        game.change_direction((0, -1))
    elif event.name == 'down':
        game.change_direction((0, 1))
    elif event.name == 'left':
        game.change_direction((-1, 0))
    elif event.name == 'right':
        game.change_direction((1, 0))
    elif event.name == 'esc':
        print("Game exited by user.")
        exit()

def main():
    global game
    oled_init()
    clear_display()

    game = SnakeGame()

    print("Use arrow keys to control the snake. Press ESC to quit.")

    # Register keyboard event handler
    keyboard.on_press(on_key_event)

    last_update = time.time()
    update_interval = 0.15  # seconds per snake move

    while not game.game_over:
        now = time.time()
        if now - last_update >= update_interval:
            game.update()
            game.draw()
            last_update = now
        time.sleep(0.01)  # Small delay to reduce CPU usage

    print(f"Game Over! Your score: {game.score}")

    # Display "Game Over" message
    image = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text = "GAME OVER"
    w = draw.textlength(text, font=font)
    h = font.size
    x = (OLED_WIDTH - w) // 2
    y = (OLED_HEIGHT - h) // 2
    draw.text((x, y), text, font=font, fill=255)
    display_image(image)

if __name__ == "__main__":
    main()
