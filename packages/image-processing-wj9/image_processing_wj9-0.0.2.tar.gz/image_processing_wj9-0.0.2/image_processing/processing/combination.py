import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1: np.ndarray, image2: np.ndarray) -> (np.ndarray, float):
    """
    Encontra a diferença entre duas imagens.

    Parâmetros:
        image1 (np.ndarray): Primeira imagem (RGB).
        image2 (np.ndarray): Segunda imagem (RGB).

    Retorna:
        (np.ndarray, float): Imagem de diferença normalizada entre 0 e 1 e a similaridade.
    
    Levanta:
        ValueError: Se as imagens não tiverem a mesma forma ou não forem válidas.
    """
    if not isinstance(image1, np.ndarray) or not isinstance(image2, np.ndarray):
        raise ValueError("Ambas as entradas devem ser arrays NumPy.")
    if image1.shape != image2.shape:
        raise ValueError("As imagens devem ter a mesma forma.")
    
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    data_range = gray_image1.max() - gray_image1.min()  

    score, difference_image = structural_similarity(gray_image1, gray_image2, full=True, data_range=data_range)
    
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    
    return normalized_difference_image, score 


def transfer_histogram(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """
    Transfere o histograma de image2 para image1.

    Parâmetros:
        image1 (np.ndarray): A imagem da qual o histograma será transferido.
        image2 (np.ndarray): A imagem cuja distribuição de intensidade será aplicada a image1.

    Retorna:
        np.ndarray: A imagem com o histograma transferido.

    Levanta:
        ValueError: Se image1 ou image2 não forem válidos.
    """
    if image1 is None or image2 is None:
        raise ValueError("Ambas as imagens devem ser fornecidas e não podem ser None.")
    if not isinstance(image1, np.ndarray) or not isinstance(image2, np.ndarray):
        raise ValueError("Ambas as entradas devem ser arrays numpy.")

    matched_image = match_histograms(image1, image2)  
    return matched_image
