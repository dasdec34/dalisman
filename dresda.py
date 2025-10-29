from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'

with SB(uc=True, test=True,locale=f"{language_code.upper()}") as benbe:
    benbe.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    benbe.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    url = "https://twitch.tv/brutalles"
    benbe.uc_open_with_reconnect(url, 4)
    benbe.sleep(43)
    benbe.uc_gui_click_captcha()
    benbe.sleep(1)
    benbe.uc_gui_handle_captcha()
    benbe.sleep(4)
    if benbe.is_element_present("#live-channel-stream-information"):
      url = "https://www.twitch.tv/brutalles"
      benbe.uc_open_with_reconnect(url, 5)
      if benbe.is_element_present('button:contains("Accept")'):
          benbe.uc_click('button:contains("Accept")', reconnect_time=4)
      if True:
          benbe2 = benbe.get_new_driver(undetectable=True)
          benbe2.uc_open_with_reconnect(url, 5)
          benbe.sleep(10)
          if benbe2.is_element_present('button:contains("Accept")'):
              benbe2.uc_click('button:contains("Accept")', reconnect_time=4)
          while benbe.is_element_present("#live-channel-stream-information"):
              benbe.sleep(150)
          benbe.quit_extra_driver()
    benbe.sleep(1)
