from manim import AddTextLetterByLetter, Write, DrawBorderThenFill, ApplyWave, FadeIn
from random import randrange


# TODO: Maybe this method below is unnecessary
def simple_play_animation(self, animation, object, duration: float = 1):
    WAITING = duration * 0.05
    ANIMATION_DURATION = duration - 2 * WAITING

    self.wait(WAITING)
    self.play(animation(object), run_time = ANIMATION_DURATION)
    self.wait(WAITING)

# TODO: I think this method below doesn't fit here
def RandomTextAnimation():
    """
    Returns a random text animation to be applied with text.
    """
    random_animations = [AddTextLetterByLetter, Write, DrawBorderThenFill, ApplyWave, FadeIn]

    return random_animations[randrange(len(random_animations))]