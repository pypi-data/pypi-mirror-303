import re
import random
import time
from datetime import datetime, timedelta
from datetime import datetime, timezone, tzinfo


class Crontab:
    STEP = timedelta(seconds=1)

    def __init__(self, **specs):
        self.t0 = None
        self.specs = specs

    def now(self):
        now = datetime.now(tz=timezone.utc).replace(microsecond=0)
        return now

    def check(self, now=None):
        "Fires all time that matches from last call"
        now = now or self.now()
        if self.t0:
            # TODO: OPTIMIZE: when now and self.t0 are too far each other
            while self.t0 <= now:
                self.t0 += self.STEP
                for key, pattern in self.specs.items():
                    value = getattr(self.t0, key, None)
                    if value is not None:
                        if not isinstance(value, int):
                            value = value()  # method
                        if not re.match(f"{pattern}$", f"{value}"):
                            break
                else:
                    # all specs (if any) matches
                    return self.t0
        else:
            self.t0 = now.replace(microsecond=0)


if __name__ == "__main__":
    cron = Crontab(second='0', minute='0|15|30|45')
    while True:
        while not (t := cron.check()):
            time.sleep(random.randint(1, 10))
        print(f"match at: {t}")
