from yta_multimedia.video.edition.effect.moviepy.position.utils import get_center_x, get_center_y
from random import randrange, choice as randomchoice
from enum import Enum


class ScreenPosition(Enum):
    OUT_TOP_LEFT = 'out_top_left'
    """
    Out of the screen, on the top left corner, just one pixel
    out of bounds.
    """
    IN_EDGE_TOP_LEFT = 'in_edge_top_left'
    """
    The center of the video is on the top left corner, so only
    the bottom left quarter part of the video is shown (inside
    the screen).
    """
    TOP_LEFT = 'top_left'
    """
    The video is completely visible, just at the top left 
    corner of the screen.
    """
    OUT_TOP = 'out_top'
    IN_EDGE_TOP = 'in_edge_top'
    TOP = 'top'
    OUT_TOP_RIGHT = 'out_top_right'
    IN_EDGE_TOP_RIGHT = 'in_edge_top_right'
    TOP_RIGHT = 'top_right'
    CENTER = 'center'
    OUT_RIGHT = 'out_right'
    IN_EDGE_RIGHT = 'in_edge_right'
    RIGHT = 'right'
    OUT_BOTTOM_RIGHT = 'out_bottom_right'
    IN_EDGE_BOTTOM_RIGHT = 'in_edge_bottom_right'
    BOTTOM_RIGHT = 'bottom_right'
    OUT_BOTTOM = 'out_bottom'
    IN_EDGE_BOTTOM = 'in_edge_bottom'
    BOTTOM = 'bottom'
    OUT_BOTTOM_LEFT = 'out_bottom_left'
    IN_EDGE_BOTTOM_LEFT = 'in_edge_bottom_left'
    BOTTOM_LEFT = 'bottom_left'
    OUT_LEFT = 'out_left'
    IN_EDGE_LEFT = 'in_edge_left'
    LEFT = 'left'

    HALF_TOP = 'half_top'
    HALF_TOP_RIGHT = 'half_top_right'
    HALF_RIGHT = 'half_right'
    HALF_BOTTOM_RIGHT = 'half_bottom_right'
    HALF_BOTTOM = 'half_bottom'
    HALF_BOTTOM_LEFT = 'half_bottom_left'
    HALF_LEFT = 'half_left'
    HALF_TOP_LEFT = 'half_top_left'

    QUADRANT_1_TOP_RIGHT_CORNER = 'quadrant_1_top_right_corner'
    QUADRANT_1_BOTTOM_RIGHT_CORNER = 'quadrant_1_bottom_right_corner'
    QUADRANT_1_BOTTOM_LEFT_CORNER = 'quadrant_1_bottom_left_corner'
    QUADRANT_2_TOP_LEFT_CORNER = 'quadrant_2_top_left_corner'
    QUADRANT_2_BOTTOM_RIGHT_CORNER = 'quadrant_2_bottom_right_corner'
    QUADRANT_2_BOTTOM_LEFT_CORNER = 'quadrant_2_bottom_left_corner'
    QUADRANT_3_TOP_RIGHT_CORNER = 'quadrant_3_top_right_corner'
    QUADRANT_3_TOP_LEFT_CORNER = 'quadrant_3_top_left_corner'
    QUADRANT_3_BOTTOM_LEFT_CORNER = 'quadrant_3_bottom_left_corner'
    QUADRANT_4_TOP_RIGHT_CORNER = 'quadrant_4_top_right_corner'
    QUADRANT_4_TOP_LEFT_CORNER = 'quadrant_4_top_left_corner'
    QUADRANT_4_BOTTOM_RIGHT_CORNER = 'quadrant_4_bottom_right_corner'

    RANDOM_INSIDE = 'random_inside'
    """
    A random position inside the screen with no pixels out of bounds.
    """
    RANDOM_OUTSIDE = 'random_outside'
    """
    A random position out of the screen. It is randomly chosen from 
    the 8 'OUT_...' options we have registered.
    """
    @classmethod
    def out_positions_as_list(cls):
        """
        Returns all the existing options out of the edges.
        """
        return [cls.OUT_TOP, cls.OUT_TOP_RIGHT, cls.OUT_RIGHT, cls.OUT_BOTTOM_RIGHT, cls.OUT_BOTTOM, cls.OUT_BOTTOM_LEFT, cls.OUT_LEFT, cls.TOP_LEFT]
    
    @classmethod
    def in_and_out_positions_as_list(cls):
        """
        Returns a list of 2 elements containing the out edge from which
        the video will come into the screen, and the opposite edge to get
        out of the screen. This has been created to animate a random slide
        transition effect. The possibilities are horizontal, diagonal and
        vertical linear sliding transitions. The first element in the list
        is the initial position and the second one, the final position. 
        """
        positions = [ScreenPosition.OUT_LEFT, ScreenPosition.OUT_RIGHT]
        rnd = randrange(0, 7)
        if rnd == 0:
            positions = [ScreenPosition.OUT_RIGHT, ScreenPosition.OUT_LEFT]
        elif rnd == 1:
            positions = [ScreenPosition.OUT_TOP, ScreenPosition.OUT_BOTTOM]
        elif rnd == 2:
            positions = [ScreenPosition.OUT_BOTTOM, ScreenPosition.OUT_TOP]
        elif rnd == 3:
            positions = [ScreenPosition.OUT_TOP_LEFT, ScreenPosition.OUT_BOTTOM_RIGHT] 
        elif rnd == 4:
            positions = [ScreenPosition.OUT_TOP_RIGHT, ScreenPosition.OUT_BOTTOM_LEFT]
        elif rnd == 5:
            positions = [ScreenPosition.OUT_BOTTOM_LEFT, ScreenPosition.OUT_TOP_RIGHT]
        elif rnd == 6:
            positions = [ScreenPosition.OUT_BOTTOM_RIGHT, ScreenPosition.OUT_TOP_LEFT]

        return positions

    def get_moviepy_position(self, video, background_video):
        """
        This method will calculate the (x, y) tuple position for the provided
        'video' over the also provided 'background_video' that would be,
        hypothetically, a 1920x1080 black color background static image. The
        provided 'position' will be transformed into the (x, y) tuple according
        to our own definitions.
        """
        # TODO: Do 'video' and 'background_video' checkings
        position_tuple = None

        if self == ScreenPosition.CENTER:
            position_tuple = (get_center_x(video, background_video), get_center_y(video, background_video))

        #           Edges below
        # TOP
        elif self == ScreenPosition.OUT_TOP:
            position_tuple = ((background_video.w / 2) - (video.w / 2), -video.h)
        elif self == ScreenPosition.IN_EDGE_TOP:
            position_tuple = ((background_video.w / 2) - (video.w / 2), -(video.h / 2))
        elif self == ScreenPosition.TOP:
            position_tuple = ((background_video.w / 2) - (video.w / 2), 0)
        # TOP RIGHT
        elif self == ScreenPosition.OUT_TOP_RIGHT:
            position_tuple = (background_video.w, -video.h)
        elif self == ScreenPosition.IN_EDGE_TOP_RIGHT:
            position_tuple = (background_video.w - (video.w / 2), -(video.h / 2))
        elif self == ScreenPosition.TOP_RIGHT:
            position_tuple = (background_video.w - video.w, 0)
        # RIGHT
        elif self == ScreenPosition.OUT_RIGHT:
            position_tuple = (background_video.w, (background_video.h / 2) - (video.h / 2))
        elif self == ScreenPosition.IN_EDGE_RIGHT:
            position_tuple = (background_video.w - (video.w / 2), (background_video.h / 2) - (video.h / 2))
        elif self == ScreenPosition.RIGHT:
            position_tuple = (background_video.w - video.w, (background_video.h / 2) - (video.h / 2))
        # BOTTOM RIGHT
        elif self == ScreenPosition.OUT_BOTTOM_RIGHT:
            position_tuple = (background_video.w, background_video.h)
        elif self == ScreenPosition.IN_EDGE_BOTTOM_RIGHT:
            position_tuple = (background_video.w - (video.w / 2), background_video.h - (video.h / 2))
        elif self == ScreenPosition.BOTTOM_RIGHT:
            position_tuple = (background_video.w - video.w, background_video.h - video.h)
        # BOTTOM
        elif self == ScreenPosition.OUT_BOTTOM:
            position_tuple = ((background_video.w / 2) - (video.w / 2), background_video.h)
        elif self == ScreenPosition.IN_EDGE_BOTTOM:
            position_tuple = ((background_video.w / 2) - (video.w / 2), background_video.h - (video.h / 2))
        elif self == ScreenPosition.BOTTOM:
            position_tuple = ((background_video.w / 2) - (video.w / 2), background_video.h - video.h)
        # BOTTOM LEFT
        elif self == ScreenPosition.OUT_BOTTOM_LEFT:
            position_tuple = (-video.w, background_video.h)
        elif self == ScreenPosition.IN_EDGE_BOTTOM_LEFT:
            position_tuple = (-(video.w / 2), background_video.h - (video.h / 2))
        elif self == ScreenPosition.BOTTOM_LEFT:
            position_tuple = (0, background_video.h - video.h)
        # LEFT
        elif self == ScreenPosition.OUT_LEFT:
            position_tuple = (-video.w, (background_video.h / 2) - (video.h / 2))
        elif self == ScreenPosition.IN_EDGE_LEFT:
            position_tuple = (-(video.w / 2), (background_video.h / 2) - (video.h / 2))
        elif self == ScreenPosition.LEFT:
            position_tuple = (0, (background_video.h / 2) - (video.h / 2))
        # TOP LEFT
        elif self == ScreenPosition.OUT_TOP_LEFT:
            position_tuple = (-video.w, -video.h)
        elif self == ScreenPosition.IN_EDGE_TOP_LEFT:
            position_tuple = (-(video.w / 2), -(video.h / 2))
        elif self == ScreenPosition.TOP_LEFT:
            position_tuple = (0, 0)

        # HALF POSITIONS
        elif self == ScreenPosition.HALF_TOP:
            position_tuple = (background_video.w / 2 - video.w / 2, background_video.h / 4 - video.h / 2)
        elif self == ScreenPosition.HALF_RIGHT:
            position_tuple = (3 * background_video.w / 4 - video.w / 2, background_video.h / 2 - video.h / 2)
        elif self == ScreenPosition.HALF_BOTTOM:
            position_tuple = (background_video.w / 2 - video.w / 2, 3 * background_video.h / 4 - video.h / 2)
        elif self == ScreenPosition.HALF_LEFT:
            position_tuple = (background_video.w / 4 - video.w / 2, background_video.h / 2 - video.h / 2)
        elif self == ScreenPosition.HALF_TOP_RIGHT:
            position_tuple = (3 * background_video.w / 4 - video.w / 2, background_video.h / 4 - video.h / 2)
        elif self == ScreenPosition.HALF_BOTTOM_RIGHT:
            position_tuple = (3 * background_video.w / 4 - video.w / 2, 3 * background_video.h / 4 - video.h / 2)
        elif self == ScreenPosition.HALF_BOTTOM_LEFT:
            position_tuple = (background_video.w / 4 - video.w / 2, 3 * background_video.h / 4 - video.h / 2)
        elif self == ScreenPosition.HALF_TOP_LEFT:
            position_tuple = (background_video.w / 4 - video.w / 2, background_video.h / 4 - video.h / 2)

        # QUADRANT CORNERS
        elif self == ScreenPosition.QUADRANT_1_TOP_RIGHT_CORNER:
            position_tuple = (background_video.w / 2 - video.w, 0)
        elif self == ScreenPosition.QUADRANT_1_BOTTOM_LEFT_CORNER:
            position_tuple = (0, background_video.h / 2 - video.h)
        elif self == ScreenPosition.QUADRANT_1_BOTTOM_RIGHT_CORNER:
            position_tuple = (background_video.w / 2 - video.w, background_video.h / 2 - video.h)
        elif self == ScreenPosition.QUADRANT_2_BOTTOM_LEFT_CORNER:
            position_tuple = (background_video.w / 2, background_video.h / 2 - video.h)
        elif self == ScreenPosition.QUADRANT_2_BOTTOM_RIGHT_CORNER:
            position_tuple = (background_video.w - video.w, background_video.h / 2 - video.h)
        elif self == ScreenPosition.QUADRANT_2_TOP_LEFT_CORNER:
            position_tuple = (background_video.w / 2, 0)
        elif self == ScreenPosition.QUADRANT_3_BOTTOM_LEFT_CORNER:
            position_tuple = (background_video.w / 2, background_video.h - video.h)
        elif self == ScreenPosition.QUADRANT_3_TOP_LEFT_CORNER:
            position_tuple = (background_video.w / 2, background_video.h / 2)
        elif self == ScreenPosition.QUADRANT_3_TOP_RIGHT_CORNER:
            position_tuple = (background_video.w - video.w, background_video.h / 2)
        elif self == ScreenPosition.QUADRANT_4_BOTTOM_RIGHT_CORNER:
            position_tuple = (background_video.w / 2 - video.w, background_video.h - video.h)
        elif self == ScreenPosition.QUADRANT_4_TOP_LEFT_CORNER:
            position_tuple = (0, background_video.h / 2)
        elif self == ScreenPosition.QUADRANT_4_TOP_RIGHT_CORNER:
            position_tuple = (background_video.w / 2 - video.w, background_video.h / 2)

        # RANDOMs
        elif self == ScreenPosition.RANDOM_INSIDE:
            lower_limit = ScreenPosition.TOP_LEFT.get_moviepy_position(video, background_video)
            upper_limit = ScreenPosition.BOTTOM_RIGHT.get_moviepy_position(video, background_video)
            position_tuple = (randrange(lower_limit[0], upper_limit[0]), randrange(lower_limit[1], upper_limit[1]))
        elif self == ScreenPosition.RANDOM_OUTSIDE:
            # By now I'm choosing one of the 'OUT' available options
            position_tuple = randomchoice(ScreenPosition.out_positions_as_list())

        return position_tuple