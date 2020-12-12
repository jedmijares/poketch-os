import wasp

# import icons
import fonts.pokeClock as digits

DIGITS = (
        digits.d0, digits.d1, digits.d2, digits.d3,
        digits.d4, digits.d5, digits.d6, digits.d7,
        digits.d8, digits.d9
)

# MONTH = 'JanFebMarAprMayJunJulAugSepOctNovDec'

class PokeClockApp():
    NAME = 'Clock'
    # ICON = icons.clock

    def foreground(self):
        wasp.system.bar.clock = False
        wasp.system.bar.meter = False
        wasp.system.bar.notif = False
        self._draw(True)
        wasp.system.request_tick(1000)

    def sleep(self):
        return True

    def wake(self):
        self._draw()

    def tick(self, ticks):
        self._draw()

    def _draw(self, redraw=False):
        draw = wasp.watch.drawable
        draw.set_color(0x3AC7, 0x6D4D) # dark and light green
        if redraw:
            now = wasp.watch.rtc.get_localtime()
            draw.fill()
            draw.blit(digits.colon, x=2*48, y=80)
            draw.blit(digits.biggerPikachu, x = 0, y = 180)
            # wasp.system.bar.draw()
        else:
            now = wasp.system.bar.update()
            now = wasp.watch.rtc.get_localtime()
            if not now or self._min == now[4]:
                return
        # month = now[1] - 1
        # month = MONTH[month*3:(month+1)*3]
        draw.blit(DIGITS[now[4]  % 10], x = 4*48, y = 80)
        draw.blit(DIGITS[now[4] // 10], x = 3*48, y = 80)
        draw.blit(DIGITS[now[3]  % 10], x = 1*48, y = 80)
        draw.blit(DIGITS[now[3] // 10], x = 0*48, y = 80)
        # draw.string('green?', 0, 108, width=240)
        # draw.string('{} {} {}'.format(now[2], month, now[0]),
                # 0, 180, width=240)
        self._min = now[4]
