import array
import math
import pygame

SOUNDS = {
    "ok": [(660,880,0.07,0.35),(800,1175,0.11,0.35)],
    "bad": [(220,140,0.25,0.40)],
    "die": [(440,60,0.50,0.45)],
    "win": [(523,523,0.10,0.35), (659,659,0.10,0.35),
            (784,784,0.10,0.35), (1046,1046,0.35,0.35)],
    "select": [(600,800,0.06,0.30)],
    "start": [(400,800,0.12,0.30)],
}

class Audio:
    def __init__(self):
        self.enabled = False
        self.muted = False
        self.sounds = {}
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            info = pygame.mixer.get_init()
            if info and info[1] == -16:
                rate, _, channels = info
                for name, notes in SOUNDS.items():
                    self.sounds[name] = self._make(notes, rate, channels)
                self.enabled = True
        except (pygame.error, TypeError, ValueError):
            self.enabled = False

    @staticmethod
    def _make(notes,rate,channels):
        buf = array.array("h")
        for f0, f1, dur, vol in notes:
            n= int(rate * dur)
            phase = 0.0
            for i in range(n):
                p = i/n
                phase += 2* math.pi * (f0 + (f1 - f0)* p) / rate
                env = min(1.0, i / (rate * 0.005)) * (1-p) ** 0.7
                v= int(32767 * vol * env * math.sin(phase))
                for _ in range(channels):
                    buf.append(v)
        return pygame.mixer.Sound(buffer=buf.tobytes())

    def play(self,name):
        if self.enabled and not self.muted and name in self.sounds:
            self.sounds[name].play()
    def toggle_mute(self):
        self.muted = not self.muted