
class Game:
    frames_remaining = 0
    roll_number = 0
    score = 0
    pins_remaining = 10
    spare = False
    strike = 0
    bonus_rolls = False

    def __init__(self, frames):
        self.frames_remaining = frames

    def roll(self, pins):
        try:
            self.check_game_over()
            self.update_roll_number()
            self.remove_pins(pins)
            self.add_score(pins)
            self.check_strike()
            self.check_spare()
            self.check_reset_frame()
        except Exception as e:
            print(e)

    def check_game_over(self):
        if self.frames_remaining < 1:
            raise Exception("Game over!")

    def update_roll_number(self):
        self.roll_number += 1

    def remove_pins(self, pins):
        self.pins_remaining -= pins

    def add_score(self, pins):
        # print(self.strike)
        if not self.bonus_rolls:
            self.score += pins
        if self.spare:
            self.score += pins
            self.spare = False
        elif self.is_double_strike():
            self.score += pins * 2
            self.strike -= 2
        elif self.is_single_strike():
            self.score += pins
            self.strike -= 1
        # print(self.score)
        # print("pins", self.pins_remaining)

    def is_single_strike(self):
        return self.strike > 0

    def is_double_strike(self):
        return self.strike > 2

    def check_strike(self):
        if self.roll_number == 1 and self.pins_remaining == 0:
            self.strike += 2
            if self.is_tenth_frame():
                self.bonus_rolls = True

    def is_tenth_frame(self):
        return self.frames_remaining == 1

    def check_spare(self):
        if self.roll_number == 2 and self.pins_remaining < 1:
            self.spare = True
            if self.is_tenth_frame():
                self.bonus_rolls = True

    # The frame is not reset for the bonus rolls in the tenth frame
    def check_reset_frame(self):
        if self.roll_number >= 3:
            self.reset_frame()
        elif (self.roll_number >= 2 or self.pins_remaining < 1) and not self.bonus_rolls:
            self.reset_frame()

    def reset_frame(self):
        self.frames_remaining -= 1
        self.roll_number = 0
        self.pins_remaining = 10
