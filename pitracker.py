# PiTracker Main App (pitracker.py) 
# Offline Maps, Waypoints, GPS Trace, Route Navigation, Voice Prompts

import os
import time
import gpsd
import pygame
from datetime import datetime
from pathlib import Path
from PIL import Image
import pyttsx3
import math

# Init GPS and voice engine
gpsd.connect()
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Init Pygame UI
pygame.init()
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("PiTracker")
font = pygame.font.SysFont(None, 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)

# UI Buttons
start_button = pygame.Rect(20, 260, 100, 40)
stop_button = pygame.Rect(360, 260, 100, 40)
zoom_in_button = pygame.Rect(200, 260, 30, 30)
zoom_out_button = pygame.Rect(240, 260, 30, 30)

# GPX Logging
is_logging = False
gpx_file = None
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

# Map Tiles Grid
TILE_SIZE = 256
tile_folder = "tiles"
def get_tile(x, y):
    tile_path = f"{tile_folder}/{x}_{y}.png"
    if os.path.exists(tile_path):
        return pygame.image.load(tile_path)
    return pygame.Surface((TILE_SIZE, TILE_SIZE))

zoom = 1.0

# Trace history
gps_trace = []
max_trace_length = 1000

# Waypoints (lat, lon)
waypoints = [(28.6139, 77.2090), (28.6129, 77.2180)]

# Navigation route (list of lat/lon pairs)
route = waypoints[:]
current_nav_index = 0
announced_wp = set()

# Projection base for Delhi
base_lat, base_lon = 28.6139, 77.2090

def draw_tiles():
    for x in range(0, 480, TILE_SIZE):
        for y in range(0, 320, TILE_SIZE):
            tile = get_tile(0, 0)  # Example single tile, extend to GPS-based indexing
            tile = pygame.transform.scale(tile, (int(TILE_SIZE * zoom), int(TILE_SIZE * zoom)))
            screen.blit(tile, (x, y))

def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def create_gpx_file():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    gpx_filename = log_path / f"track_{timestamp}.gpx"
    f = open(gpx_filename, "w")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    f.write("<gpx version=\"1.1\" creator=\"PiTracker\">\n")
    f.write("  <trk><name>PiTrack Log</name><trkseg>\n")
    return f

def close_gpx_file(f):
    f.write("  </trkseg></trk>\n</gpx>")
    f.close()

def log_position(f, lat, lon):
    timestamp = datetime.utcnow().isoformat() + "Z"
    f.write(f"    <trkpt lat=\"{lat}\" lon=\"{lon}\">\n")
    f.write(f"      <time>{timestamp}</time>\n")
    f.write("    </trkpt>\n")

def latlon_to_screen(lat, lon):
    scale = 10000 * zoom
    x = int((lon - base_lon) * scale + 240)
    y = int((base_lat - lat) * scale + 160)
    return x, y

def draw_waypoints():
    for wp in waypoints:
        x, y = latlon_to_screen(wp[0], wp[1])
        pygame.draw.circle(screen, RED, (x, y), 6)

def draw_marker(lat, lon):
    x, y = latlon_to_screen(lat, lon)
    pygame.draw.circle(screen, BLUE, (x, y), 7)

def draw_trace():
    if len(gps_trace) > 1:
        points = [latlon_to_screen(lat, lon) for lat, lon in gps_trace]
        pygame.draw.lines(screen, YELLOW, False, points, 3)

def get_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2) * 111000

def check_navigation(lat, lon):
    global current_nav_index
    if current_nav_index < len(route):
        wp = route[current_nav_index]
        dist = get_distance(lat, lon, wp[0], wp[1])
        if dist < 30 and wp not in announced_wp:
            engine.say(f"Reached waypoint {current_nav_index + 1}")
            engine.runAndWait()
            announced_wp.add(wp)
            current_nav_index += 1

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)
    draw_tiles()

    pygame.draw.rect(screen, GREEN if is_logging else BLACK, start_button)
    pygame.draw.rect(screen, RED if is_logging else BLACK, stop_button)
    pygame.draw.rect(screen, WHITE, zoom_in_button, 2)
    pygame.draw.rect(screen, WHITE, zoom_out_button, 2)

    draw_text("+", 207, 265)
    draw_text("-", 247, 265)
    draw_text("Start", 35, 270, WHITE)
    draw_text("Stop", 385, 270, WHITE)

    draw_waypoints()
    draw_trace()

    try:
        packet = gpsd.get_current()
        if packet.mode >= 2:
            lat, lon = packet.lat, packet.lon
            draw_marker(lat, lon)
            draw_text(f"Lat: {lat:.6f}", 10, 10)
            draw_text(f"Lon: {lon:.6f}", 10, 35)
            gps_trace.append((lat, lon))
            if len(gps_trace) > max_trace_length:
                gps_trace.pop(0)
            if is_logging:
                log_position(gpx_file, lat, lon)
            check_navigation(lat, lon)
        else:
            draw_text("Waiting for GPS fix...", 10, 10)
    except Exception as e:
        draw_text(f"GPS error: {e}", 10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if is_logging:
                close_gpx_file(gpx_file)
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos) and not is_logging:
                gpx_file = create_gpx_file()
                is_logging = True
            elif stop_button.collidepoint(event.pos) and is_logging:
                close_gpx_file(gpx_file)
                is_logging = False
            elif zoom_in_button.collidepoint(event.pos):
                zoom = min(zoom + 0.1, 2.0)
            elif zoom_out_button.collidepoint(event.pos):
                zoom = max(zoom - 0.1, 0.5)

    pygame.display.update()
    clock.tick(1)
