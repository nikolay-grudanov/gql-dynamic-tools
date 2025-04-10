import json
import asyncio
import os
import time
import logging
import traceback

from gql_utils.dynamic_query_builder import DynamicQueryBuilder

GQL_URL = "https://citylifeindex.ru/api/graphql"
GRAPHQL_SCHEMA_PATH = 'schemas/schema.graphql'

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("parser.log"),
        logging.StreamHandler()
    ]
)

async def main():
    # Инициализация клиента
    builder = DynamicQueryBuilder(GQL_URL, GRAPHQL_SCHEMA_PATH)
    
    # Получение списка всех доступных сущностей
    try:
        entities = builder.explorer.get_all_entities()
        logging.info(f"Найдено {len(entities)} сущностей для обработки")
    except Exception as e:
        logging.error(f"Ошибка при получении списка сущностей: {str(e)}")
        entities = ["City", "Cluster", "Direction", "Mark", "Agglomeration", "CityType"]
        logging.info(f"Используем предопределенный список сущностей: {entities}")
    
    # Создание директорий для результатов
    os.makedirs("data", exist_ok=True)
    os.makedirs("queries", exist_ok=True)
    os.makedirs("errors", exist_ok=True)
    
    # Статистика обработки
    total_start_time = time.time()
    processed = 0
    success = 0
    failed = 0
    
    # Обход всех сущностей
    for entity in entities:
        entity_start_time = time.time()
        logging.info(f"Обработка сущности: {entity}")
        
        # Попытка с разными глубинами
        for depth in range(3, 0, -1):
            try:
                # Генерация запроса
                query = builder.build_query(entity, depth=depth)
                
                # Сохраняем запрос в файл
                query_file = f"queries/{entity}_depth{depth}.graphql"
                with open(query_file, 'w', encoding='utf-8') as f:
                    f.write(query)
                logging.info(f"Запрос для {entity} с глубиной {depth} сохранен")
                
                # Выполнение запроса
                query_start = time.time()
                data = await builder.execute_paginated_query(query)
                query_time = time.time() - query_start
                
                # Сохранение результатов
                data_file = f"data/{entity}_depth{depth}.json"
                with open(data_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                logging.info(f"Успешно получены данные для {entity} (глубина {depth}) за {query_time:.2f}с")
                success += 1
                break  # Если успешно, прекращаем попытки с меньшей глубиной
                
            except Exception as e:
                # Сохраняем информацию об ошибке
                error_file = f"errors/{entity}_depth{depth}_error.txt"
                with open(error_file, 'w', encoding='utf-8') as f:
                    f.write(f"Ошибка при обработке {entity} с глубиной {depth}:\n")
                    f.write(str(e) + "\n\n")
                    f.write(traceback.format_exc())
                
                if depth == 1:  # Если не удалось даже с минимальной глубиной
                    logging.error(f"Не удалось обработать сущность {entity}: {str(e)}")
                    failed += 1
                else:
                    logging.warning(f"Ошибка при глубине {depth} для {entity}, пробуем меньшую глубину")
        
        processed += 1
        entity_time = time.time() - entity_start_time
        logging.info(f"Обработка {entity} завершена за {entity_time:.2f}с")
        
        # Вывод промежуточной статистики
        if processed % 5 == 0:
            logging.info(f"Прогресс: {processed}/{len(entities)} сущностей, успешно: {success}, ошибок: {failed}")
    
    # Итоговая статистика
    total_time = time.time() - total_start_time
    logging.info(f"Парсинг завершен за {total_time:.2f}с")
    logging.info(f"Всего обработано: {processed}, успешно: {success}, с ошибками: {failed}")

if __name__ == "__main__":
    asyncio.run(main())
