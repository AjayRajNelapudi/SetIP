import time
import click
import navigator

@click.command("setip")
@click.argument("profile")
def set_ip_profile(profile):
    ip_nav = navigator.Navigate(images_path="/Users/ajayraj/Documents/SetIP/")

    ip_nav.open_network_preferences()
    time.sleep(0.5)

    ip_nav.open_advanced_panel()
    ip_nav.goto_tcp_ip()
    if profile.lower() == "home":
        ip_nav.set_home_ip()
    else:
        ip_nav.set_college_ip()
    time.sleep(0.2)

    ip_nav.apply_and_close()

if __name__ == "__main__":
    set_ip_profile()