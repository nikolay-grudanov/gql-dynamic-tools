from gql_utils.schema_explorer import SchemaExplorer
from typing import Dict, Any, Optional
from graphql import  print_ast, parse, validate, build_schema
from graphql.type.schema import TypeMap
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from pathlib import Path

from schema import type_map  # Импорт сгенерированных схем

class DynamicQueryBuilder:
    def __init__(self, endpoint_url: str, graphql_schema_path: str):
        """
        Инициализация DynamicQueryBuilder.

        Args:
        endpoint_url (str): URL конечной точки GraphQL.
        graphql_schema_path (str): Путь к файлу схемы GraphQL.
        """
        self.transport = AIOHTTPTransport(
            url=endpoint_url,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )
        # Загрузка схемы из файла
        schema_path = Path(graphql_schema_path)
        with schema_path.open() as f:
            schema_sdl = f.read()
        self.schema = build_schema(schema_sdl)

        # Создание клиента с явной передачей схемы
        self.client = Client(
            transport=self.transport,
            schema=self.schema,
            fetch_schema_from_transport=False  # Отключаем авто-интроспекцию
        )

        self.explorer = SchemaExplorer(type_map)
        

    def build_query(self, root_type: str, depth: int = 2) -> str:
        """Генерация GraphQL-запроса"""
        fields = self.explorer.explore_type(root_type, depth)
        query_fields = self.format_fields(self.__clean_fields(fields))
        query_str = (f'''
            query {root_type}Query {{
                {root_type.lower()}s {{
                    {query_fields}
                }}
            }}
        ''')
        self.__validate_query(query_str)
        query = gql(query_str)
        return print_ast(query)


    def format_fields(self, fields: Dict[str, Any], indent: int = 4) -> str:
        """Форматирование полей для запроса"""
        lines = []
        for name, value in fields.items():
            if isinstance(value, dict):
                nested = self.format_fields(value, indent + 2)
                lines.append(f'{name} {{\n{nested}\n{" " * indent}}}')
            else:
                lines.append(name)
        return '\n'.join([f'{" " * indent}{line}' for line in lines])

    async def execute_paginated_query(self, query: str, variables: Optional[dict] = None) -> dict:
        """Выполнение пагинационного запроса"""
        document = parse(query)
        result = await self.client.execute_async(document, variable_values=variables or {})
        return result

    def __validate_query(self, query: str):
        """Валидация запроса"""
        print("Validating query...")
        print("query:\n", query)
        try:
            document = parse(query)
            schema = self.client.schema
            if schema is None:
                raise ValueError(f"Schema is empty")
            if errors := validate(schema, document):
                raise ValueError(f"Invalid query: {errors}")
        except Exception as e:
            raise ValueError(f"Invalid query: {str(e)}")

    def __clean_fields(self, fields: Dict) -> Dict:
        """Рекурсивная очистка пустых значений"""
        return {
            k: self.__clean_fields(v) if isinstance(v, dict) else v
            for k, v in fields.items()
            if v is not None and (v or not isinstance(v, dict))
        }
