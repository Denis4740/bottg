import requests
import logging

logger = logging.getLogger(__name__)

CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
DOG_API_URL = 'https://api.thedogapi.com/v1/images/search'

def get_new_image():
    try:
        response = requests.get(CAT_API_URL)
        response.raise_for_status()
        image_url = response.json()[0].get('url')
        logger.info(f"Кот получен: {image_url}")
        return image_url
    except Exception as e:
        logger.error(f"Ошибка API котов: {e}", exc_info=True)
        try:
            response = requests.get(DOG_API_URL)
            response.raise_for_status()
            image_url = response.json()[0].get('url')
            logger.info(f"Собака вместо кота: {image_url}")
            return image_url
        except Exception as e2:
            logger.critical(f"Полный провал: {e2}", exc_info=True)
            return None
