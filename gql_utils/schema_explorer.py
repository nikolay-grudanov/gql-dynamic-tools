from typing import Dict, Any, Optional
from graphql import GraphQLObjectType, GraphQLList, GraphQLNonNull
from graphql.type.schema import TypeMap

class SchemaExplorer:
    def __init__(self, type_map: TypeMap):
        """
        Инициализация SchemaExplorer.

        Args:
        type_map (TypeMap): Карта типов GraphQL.
        """
        self.visited_types = set()
        self.current_path = []  # Добавляем трекинг пути
        self.type_map = type_map # Добавляем атрибут для хранения мапы

        
    def get_all_entities(self) -> list:
        """Получение списка всех сущностей"""
        return [
            name for name, type_def in self.type_map.items()
            if isinstance(type_def, GraphQLObjectType)
            and not name.startswith("__")  # Исключаем внутренние типы GraphQL
            and name not in ["Query", "Mutation"]  # Исключаем корневые типы
        ]


    def get_type_definition(self, type_name: str) -> Optional[GraphQLObjectType]:
        """Получение определения типа по имени"""
        type_def = self.type_map.get(type_name)
        if isinstance(type_def, GraphQLObjectType):
            return type_def
        return None


    def explore_type(self, type_name: str, depth: int = 3, parent_field=None) -> Dict[str, Any]:
        """Рекурсивный обход типа схемы"""
        if depth <= 0 or (type_name, parent_field) in self.current_path: 
            return {}
            
        type_def = self.get_type_definition(type_name)
        if not isinstance(type_def, GraphQLObjectType):
            return {}

        self.current_path.append((type_name, parent_field))  # Фиксируем путь
        result = {}

        for field_name, field in type_def.fields.items():
            # Пропускаем служебные поля
            if field_name.startswith("_"):
                continue

            # Проверяем наличие соответствующего ID-поля
            id_field = f"{field_name}Id"
            current_type_fields = list(type_def.fields.keys())
            
            if id_field in current_type_fields and parent_field != id_field:
                result[id_field] = "ID"
                continue # Пропускаем вложенное поле, если есть Id

            field_type = self.unwrap_field_type(field.type)
            result[field_name] = self.process_field(field_type, depth - 1, field_name)

        self.current_path.pop()  # Удаляем путь после обработки
        return result



    def unwrap_field_type(self, gql_type):
        """Распаковка сложных типов поля"""
        while isinstance(gql_type, (GraphQLList, GraphQLNonNull)):
            gql_type = gql_type.of_type
        return gql_type

    def process_field(self, field_type, depth: int, current_field: str) -> Any:
        """Обработка поля с учетом его типа"""
        if isinstance(field_type, GraphQLObjectType):
            return self.explore_type(field_type.name, depth, current_field)
        elif isinstance(field_type, GraphQLObjectType):
            return self.map_scalar_type(field_type.name)
        return str(field_type)

    def map_scalar_type(self, type_name: str) -> str:
        """Сопоставление скалярных типов"""
        scalar_map = {
            'String': 'string',
            'Int': 'integer',
            'Float': 'float',
            'Boolean': 'boolean',
            'Timestamp': 'datetime',
            'JSON': 'json',
            'ID': 'ID'
        }
        return scalar_map.get(type_name, type_name)
