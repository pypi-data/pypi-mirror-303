import numpy as np
from skimage.transform import resize

def resize_image(image: np.ndarray, proportion: float) -> np.ndarray:
    """
    Redimensiona a imagem de acordo com a proporção fornecida.

    :param image: Imagem a ser redimensionada (np.ndarray).
    :param proportion: Proporção para redimensionamento (float entre 0 e 1).
    :return: Imagem redimensionada (np.ndarray).
    """
    if not isinstance(image, np.ndarray):
        raise TypeError("A imagem deve ser um objeto numpy.ndarray.")
    
    if not (0 <= proportion <= 1):
        raise ValueError("Especifique uma proporção válida entre 0 e 1.")
    
    if proportion == 0:
        return np.empty((0, 0, image.shape[2]), dtype=image.dtype)

    if proportion == 1:
        return image 
    
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    
    try:
        image_resized = resize(image, (height, width), anti_aliasing=True)
    except Exception as e:
        raise RuntimeError(f"Erro ao redimensionar a imagem: {e}")
    
    return image_resized
