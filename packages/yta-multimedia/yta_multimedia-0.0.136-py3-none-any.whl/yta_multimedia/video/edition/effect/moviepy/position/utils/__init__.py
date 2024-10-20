def get_center_x(video, background_video):
    """
    Returns the 'x' coord in which the 'video' will be centered
    according to the 'background_video' in which it will be
    overlayed.
    """
    # TODO: Ensure 'video' and 'background_video' are valid videos
    return background_video.w / 2 - video.w / 2

def get_center_y(video, background_video):
    """
    Returns the 'y' coord in which the 'clip' will be centered
    according to the 'background_video' in which it will be
    overlayed.
    """
    # TODO: Ensure 'video' and 'background_video' are valid videos
    return background_video.h / 2 - video.h / 2


"""
        This below is a remaning that I want to check only
        and then, when everything is clear, remove it.
"""
# """
# I copied all these files from the "software" project in which
# I initially created them, just to preserve and adapt the ones
# we weant to keep in the code.
# """
# from yta_multimedia.video.edition.effect.moviepy.testing.position_effect import PositionEffect
# from moviepy.editor import CompositeVideoClip, ColorClip

# def clip_with_effect(clip, effect: PositionEffect, **kwargs):
#     """
#     This method will create a black background clip and will put
#     as an overlay the provided 'clip' with the also provided
#     'effect' applied on it.

#     This method will use the kwargs['time'] as the effect time if provided,
#     or will use the 'destination_clip' duration if no time provided. This
#     method will also crop the 'time' if provided to, as maximum, the
#     'destination_clip' duration.

#     Pay atenttion to the parameters of the PositionEffect you are trying
#     to use.

#     This method will return a CompositeVideoClip that includes the 
#     'destination_clip' and the effect applied over it.
#     """
#     background_clip = ColorClip(clip.size, [0, 0, 0], duration = clip.duration)

#     return __add_clip_with_effect(clip, effect = effect, destination_clip = background_clip, **kwargs)

# def add_clip_with_effect(clip, effect: PositionEffect, destination_clip, **kwargs):
#     """
#     Adds the provided 'clip' with the also provided 'effect' over the
#     'destination_clip'. The provided 'clip' is the clip that will be used 
#     in the effect. For example, an ImageClip that contains an emoji that 
#     is going to be slided in and out.

#     This method will use the kwargs['time'] as the effect time if provided,
#     or will use the 'destination_clip' duration if no time provided. This
#     method will also crop the 'time' if provided to, as maximum, the
#     'destination_clip' duration.

#     Pay atenttion to the parameters of the PositionEffect you are trying
#     to use.

#     This method will return a CompositeVideoClip that includes the 
#     'destination_clip' and the effect applied over it.
#     """
#     return __add_clip_with_effect(clip, effect = effect, destination_clip = destination_clip, **kwargs)

# def __add_clip_with_effect(clip, effect: PositionEffect, destination_clip, **kwargs):
#     """
#     This method is to avoid duplicating the code. Only for internal use.
#     """
#     if not 'time' in kwargs:
#         kwargs['time'] = destination_clip.duration

#     if kwargs.get('time') > destination_clip.duration:
#         kwargs['time'] = destination_clip.duration

#     if kwargs.get('time') < clip.duration:
#         return CompositeVideoClip([
#             destination_clip,
#             *effect(clip.subclip(0, kwargs['time']), **kwargs),
#             clip.subclip(kwargs['time'], clip.duration).set_start(kwargs['time'])
#         ])

#     return CompositeVideoClip([
#         destination_clip,
#         *effect(clip, **kwargs)
#     ])