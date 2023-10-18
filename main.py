import time
from pynput.mouse import Controller
from pynput.mouse import Button
from pynput.mouse import Listener
import sys
from pynput import mouse


def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    if pressed:
        print("Kliknięto {0} na pozycji ({1}, {2})".format(button, x, y))


def on_scroll(x, y, dx, dy):
    pass


def simulate_mouse_movement():
    mouse_controller = Controller()

    distance = 200
    duration = 1
    simulation_duration = 3600  # 1 godzina w sekundach

    start_x, start_y = mouse_controller.position

    start_time = time.time()
    while time.time() - start_time < simulation_duration:
        for i in range(distance):
            mouse_controller.position = (start_x, start_y - i)
            time.sleep(duration / distance)

        for i in range(distance):
            mouse_controller.position = (start_x, start_y - distance + i)
            time.sleep(duration / distance)


def main():
    run_simulation = True

    while run_simulation:
        simulate_mouse_movement()
        response = input("Czy chcesz uruchomić symulację ponownie? (T/N): ").strip().lower()
        run_simulation = response == "t"

    print("Mam nadzieję, że symulator był przydatny.")
    print("To rzekła Anarchy Foxy")


if __name__ == "__main__":
    main()
