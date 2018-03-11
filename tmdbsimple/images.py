from .base import TMDB

class Images(TMDB):
    """
    Movies functionality.

    See: https://developers.themoviedb.org/3/configuration
    """
    BASE_PATH = 'movie'
    URLS = {
        'image': '{size}{image_path}',
    }

    def __init__(self, image_base_uri=None, image_path=None):
        super(Images, self).__init__()
        self.image_path = image_path
        self.image_base_uri = image_base_uri

    def blob(self, **kwargs):
        """
        Get the binary image.

        Args:
          size: Size of the image to get.

        Returns:
          A JPG image from the API.
        """
        path = self.image_base_uri + self.URLS['image'].format(size=kwargs['size'], image_path=self.image_path)

        return self._GET_BINARY(path, kwargs)
