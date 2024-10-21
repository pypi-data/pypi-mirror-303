import os
import numpy as np  
from skimage.io import imread, imsave

def read_image(path: str, as_gray: bool = False):
    """Lê uma imagem do caminho fornecido."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"O caminho fornecido não existe: {path}")
    
    try:
        image = imread(path, as_gray=as_gray)
    except ValueError as e:
        raise ValueError(f"Erro ao ler a imagem. Verifique se o arquivo está em um formato suportado: {e}")
    
    return image

def save_image(image, path: str):
    """Salva a imagem no caminho fornecido."""
    if image is None or (not isinstance(image, np.ndarray) or image.size == 0):
        raise ValueError("Imagem inválida. O objeto de imagem não pode ser nulo ou vazio.")

    if image.dtype == np.float64:
        image = (image * 255).astype(np.uint8)  

    try:
        imsave(path, image)
    except ValueError as e:
        raise ValueError(f"Erro ao salvar a imagem. Verifique se o formato de destino é suportado: {e}")
