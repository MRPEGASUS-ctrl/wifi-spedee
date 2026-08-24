#!/usr/bin/env python3
import time
import os
import sys
import psutil

def format_bytes(bytes_num):
    """Format bytes ke KB/s atau MB/s."""
    kb = bytes_num / 1024
    if kb >= 1024:
        return f"{kb / 1024:.2f} MB/s"
    return f"{kb:.2f} KB/s"

def draw_bar(speed_bytes, max_speed=10 * 1024 * 1024):
    """Membuat grafik bar sederhana."""
    length = 20
    fraction = min(speed_bytes / max_speed, 1.0)
    filled = int(length * fraction)
    return "█" * filled + "-" * (length - filled)

def main():
    print("\033[92m======================================")
    print("        WIFI SPEDEE - MONITOR        ")
    print("======================================\033[0m")
    print("Tekan Ctrl+C untuk menghentikan.\n")

    last_net = psutil.net_io_counters()
    last_time = time.time()

    try:
        while True:
            time.sleep(1)
            current_time = time.time()
            current_net = psutil.net_io_counters()

            elapsed = current_time - last_time
            bytes_sent = current_net.bytes_sent - last_net.bytes_sent
            bytes_recv = current_net.bytes_recv - last_net.bytes_recv

            speed_up = bytes_sent / elapsed
            speed_down = bytes_recv / elapsed

            sys.stdout.write("\033[K")
            print(f" ⬇ DOWNLOAD : {format_bytes(speed_down):<10} [{draw_bar(speed_down)}]")
            sys.stdout.write("\033[K")
            print(f" ⬆ UPLOAD   : {format_bytes(speed_up):<10} [{draw_bar(speed_up)}]")
            
            sys.stdout.write("\033[F\033[F")
            sys.stdout.flush()

            last_net = current_net
            last_time = current_time

    except KeyboardInterrupt:
        print("\n\n\033[91m[!] wifi spedee dihentikan.\033[0m")
        sys.exit()

if __name__ == "__main__":
    main()

