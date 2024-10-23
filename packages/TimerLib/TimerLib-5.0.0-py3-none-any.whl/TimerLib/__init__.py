from logging import basicConfig, DEBUG, getLogger

basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = getLogger(__name__)
logger.setLevel(DEBUG)  # Установка уровня логирования