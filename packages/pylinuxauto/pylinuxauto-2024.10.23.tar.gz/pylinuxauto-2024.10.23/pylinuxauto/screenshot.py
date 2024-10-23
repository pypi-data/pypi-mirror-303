import os

from nocmd import Cmd

from pylinuxauto.config import config


def _screenshot_cmd():
    return "dbus-send --session --print-reply=literal --dest=org.kde.KWin /Screenshot org.kde.kwin.Screenshot"

def insert_path():
    os.environ['XDG_RUNTIME_DIR'] = f'/run/user/{os.getuid()}'
    os.environ['DBUS_SESSION_BUS_ADDRESS'] = f"unix:path={os.environ['XDG_RUNTIME_DIR']}/bus"

def check_kwin_dbus_useful(screen_path):
    if "Error org.freedesktop.DBus" in screen_path:
        return False
    return True

def install_pyscreenshot():
    os.system("pip3 install pyscreenshot")
    if config.SYS_ARCH in ["x86_64", "aarch64"]:
        os.system(f"pip3 install pillow -i {config.PYPI_MIRROR}")
    else:
        Cmd.sudo_run("apt install python3-pil -y")

def screenshot_full():
    insert_path()
    fullscreen_path = os.popen(f"{_screenshot_cmd()}.screenshotFullscreen").read().strip().strip("\n")
    if check_kwin_dbus_useful(fullscreen_path) is False:
        install_pyscreenshot()
        import pyscreenshot
        import easyprocess
        fullscreen_path = config.SCREEN_CACHE
        try:
            pyscreenshot.grab().save(os.path.expanduser(fullscreen_path))
        except easyprocess.EasyProcessError:
            ...
    return fullscreen_path


def screenshot_area(x, y, w, h):
    insert_path()
    screen_path =  (
        os.popen(f"{_screenshot_cmd()}.screenshotArea int32:{x} int32:{y} int32:{w} int32:{h}")
        .read()
        .strip()
        .strip("\n")
    )
    if check_kwin_dbus_useful(screen_path) is False:
        install_pyscreenshot()
        import pyscreenshot
        import easyprocess
        screen_path = config.SCREEN_CACHE
        try:
            pyscreenshot.grab(bbox=(x, y, w, h)).save(os.path.expanduser(screen_path))
        except easyprocess.EasyProcessError:
            ...
    return screen_path

if __name__ == '__main__':
    print(screenshot_full())