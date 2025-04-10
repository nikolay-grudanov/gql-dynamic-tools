from typing import cast

from graphql import (
    DirectiveLocation,
    GraphQLArgument,
    GraphQLBoolean,
    GraphQLDirective,
    GraphQLEnumType,
    GraphQLEnumValue,
    GraphQLField,
    GraphQLFloat,
    GraphQLID,
    GraphQLInputField,
    GraphQLInputObjectType,
    GraphQLInt,
    GraphQLList,
    GraphQLNonNull,
    GraphQLObjectType,
    GraphQLScalarType,
    GraphQLSchema,
    GraphQLString,
    Undefined,
)
from graphql.type.schema import TypeMap

type_map: TypeMap = {
    "AdminDirection": GraphQLObjectType(
        name="AdminDirection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "color": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "icons": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Icon"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idPwc": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "marks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["AdminMark"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "year": GraphQLField(
                cast(GraphQLObjectType, type_map["Year"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "yearId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "AdminMark": GraphQLObjectType(
        name="AdminMark",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createdAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "dataSource": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "dataSourceEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "dataYear": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "direction": GraphQLField(
                cast(GraphQLObjectType, type_map["AdminDirection"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "directionId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "hasSmarteks": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idPwc": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "markType": GraphQLField(
                cast(GraphQLEnumType, type_map["MarkType"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "oesr": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "priority": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "published": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "ru": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "smartekCode": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "smarteks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["Smartek"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "unit": GraphQLField(
                cast(GraphQLObjectType, type_map["Unit"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "weight": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "year": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Year"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "yearId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Agglomeration": GraphQLObjectType(
        name="Agglomeration",
        description=None,
        interfaces=[],
        fields=lambda: {
            "agglomerationMarks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["AgglomerationMark"])
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "photos": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "secondaryPhotos": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AgglomerationData": GraphQLObjectType(
        name="AgglomerationData",
        description=None,
        interfaces=[],
        fields=lambda: {
            "directionsData": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["JSON"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "marksData": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["JSON"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "AgglomerationMark": GraphQLObjectType(
        name="AgglomerationMark",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "mark": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["AdminMark"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "markId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "AttachFile": GraphQLObjectType(
        name="AttachFile",
        description=None,
        interfaces=[],
        fields=lambda: {
            "contentType": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "extension": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "filename": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "size": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "title": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "titleEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "url": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "AttachText": GraphQLObjectType(
        name="AttachText",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "text": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "textEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Banner": GraphQLObjectType(
        name="Banner",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "link": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "City": GraphQLObjectType(
        name="City",
        description=None,
        interfaces=[],
        fields=lambda: {
            "centerLat": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "centerLng": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "cityType": GraphQLField(
                cast(GraphQLObjectType, type_map["CityType"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "cluster": GraphQLField(
                cast(GraphQLObjectType, type_map["Cluster"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "clusterId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionIkp": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionIkpEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idPwc": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "isRus": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "photos": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "subject": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "subjectCode": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CityData": GraphQLObjectType(
        name="CityData",
        description=None,
        interfaces=[],
        fields=lambda: {
            "directionsData": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["JSON"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "marksData": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["JSON"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "marksPointData": GraphQLField(
                cast(GraphQLScalarType, type_map["JSON"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CityStats": GraphQLObjectType(
        name="CityStats",
        description=None,
        interfaces=[],
        fields=lambda: {
            "directions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["MarkValue"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLNonNull(GraphQLFloat),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CityType": GraphQLObjectType(
        name="CityType",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cities": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["City"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Cluster": GraphQLObjectType(
        name="Cluster",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cities": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["City"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "creativeName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "creativeNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "ClusterStats": GraphQLObjectType(
        name="ClusterStats",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cities": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["CityStats"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "directions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["MarkValue"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Content": GraphQLObjectType(
        name="Content",
        description=None,
        interfaces=[],
        fields=lambda: {
            "citiesDesc": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "citiesDescEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "databaseDesc": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "databaseDescEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "mapDesc": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "mapDescEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "metodologyDesc": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "metodologyDescEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "metodologyDescOne": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "metodologyDescOneEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "metodologyDescTwo": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "metodologyDescTwoEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "platformDesc": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "platformDescEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "platformTaskDesc": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "platformTaskDescEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreativeDirection": GraphQLObjectType(
        name="CreativeDirection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "average": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "color": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "creativeMarks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["CreativeMark"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "icons": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Icon"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreativeMark": GraphQLObjectType(
        name="CreativeMark",
        description=None,
        interfaces=[],
        fields=lambda: {
            "averageClusters": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["MarkValue"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "creativeDirection": GraphQLField(
                cast(GraphQLObjectType, type_map["CreativeDirection"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "creativeDirectionId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "directionColor": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "unit": GraphQLField(
                cast(GraphQLObjectType, type_map["Unit"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "unitShort": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "unitShortEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "zeroMax": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "CreativeMarkValue": GraphQLObjectType(
        name="CreativeMarkValue",
        description=None,
        interfaces=[],
        fields=lambda: {
            "absValue": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "unitShort": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "unitShortEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "CreativePage": GraphQLObjectType(
        name="CreativePage",
        description=None,
        interfaces=[],
        fields=lambda: {
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "materialBlocks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["MaterialBlock"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "publish": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "title": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "titleEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Direction": GraphQLObjectType(
        name="Direction",
        description=None,
        interfaces=[],
        fields=lambda: {
            "color": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "icons": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Icon"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idPwc": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "marks": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Mark"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "year": GraphQLField(
                cast(GraphQLObjectType, type_map["Year"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "yearId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "DirectionMultiplierInput": GraphQLInputObjectType(
        name="DirectionMultiplierInput",
        description=None,
        fields=lambda: {
            "directionId": GraphQLInputField(
                GraphQLNonNull(GraphQLID),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "multiplier": GraphQLInputField(
                GraphQLNonNull(GraphQLInt),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EsgCity": GraphQLObjectType(
        name="EsgCity",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "descriptionEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "esgCluster": GraphQLField(
                cast(GraphQLObjectType, type_map["EsgCluster"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "esgCompanies": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgCompany"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idEsg": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "nameEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EsgCluster": GraphQLObjectType(
        name="EsgCluster",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "descriptionEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idEsg": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "nameEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EsgCompany": GraphQLObjectType(
        name="EsgCompany",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createdAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "link": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "nameEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "photos": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EsgContent": GraphQLObjectType(
        name="EsgContent",
        description=None,
        interfaces=[],
        fields=lambda: {
            "description": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "descriptionEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "logo": GraphQLField(
                cast(GraphQLObjectType, type_map["Icon"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "logoEng": GraphQLField(
                cast(GraphQLObjectType, type_map["Icon"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "researchFile": GraphQLField(
                cast(GraphQLObjectType, type_map["AttachFile"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "researchFileEng": GraphQLField(
                cast(GraphQLObjectType, type_map["AttachFile"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "title": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "titleEng": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EsgDirection": GraphQLObjectType(
        name="EsgDirection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "color": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "esgMarks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgMark"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idEsg": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "EsgMark": GraphQLObjectType(
        name="EsgMark",
        description=None,
        interfaces=[],
        fields=lambda: {
            "dataSource": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "dataSourceEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "dataYear": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "esgDirection": GraphQLField(
                cast(GraphQLObjectType, type_map["EsgDirection"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "esgDirectionColor": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "esgDirectionId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idEsg": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "markType": GraphQLField(
                cast(GraphQLEnumType, type_map["MarkType"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "priority": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "published": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "unit": GraphQLField(
                cast(GraphQLObjectType, type_map["Unit"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "unitShort": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "unitShortEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Feedback": GraphQLObjectType(
        name="Feedback",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createdAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "files": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["AttachFile"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "fromUser": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "fullname": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "status": GraphQLField(
                cast(GraphQLEnumType, type_map["FeedbackStatus"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "text": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "userId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "FeedbackCreateInput": GraphQLInputObjectType(
        name="FeedbackCreateInput",
        description=None,
        fields=lambda: {
            "id": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "status": GraphQLInputField(
                cast(GraphQLEnumType, type_map["FeedbackStatus"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "userId": GraphQLInputField(
                GraphQLID,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fullname": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "text": GraphQLInputField(
                GraphQLString,
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "fileIds": GraphQLInputField(
                GraphQLList(GraphQLNonNull(GraphQLID)),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "FeedbackStatus": GraphQLEnumType(
        name="FeedbackStatus",
        description=None,
        values={
            "OPENED": GraphQLEnumValue(
                value="OPENED", description=None, deprecation_reason=None
            ),
            "CLOSED": GraphQLEnumValue(
                value="CLOSED", description=None, deprecation_reason=None
            ),
            "REJECTED": GraphQLEnumValue(
                value="REJECTED", description=None, deprecation_reason=None
            ),
        },
    ),
    "FileCreateInput": GraphQLInputObjectType(
        name="FileCreateInput",
        description=None,
        fields=lambda: {
            "file": GraphQLInputField(
                cast(GraphQLScalarType, type_map["Upload"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            )
        },
    ),
    "Icon": GraphQLObjectType(
        name="Icon",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "resizedUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "thumbUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "url": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "vignetteResizedUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "vignetteUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "JSON": GraphQLScalarType(name="JSON", description=None, specified_by_url=None),
    "Link": GraphQLObjectType(
        name="Link",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "link": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "title": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "titleEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "MapCitySelection": GraphQLObjectType(
        name="MapCitySelection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "averageClusterValue": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "averageValue": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "centerLat": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "centerLng": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "clusterId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "clusterName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "clusterNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "transparencyPercent": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Mark": GraphQLObjectType(
        name="Mark",
        description=None,
        interfaces=[],
        fields=lambda: {
            "dataSource": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "dataSourceEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "dataYear": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "direction": GraphQLField(
                cast(GraphQLObjectType, type_map["Direction"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "directionColor": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "directionId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "hasSmarteks": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "idPwc": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "markType": GraphQLField(
                cast(GraphQLEnumType, type_map["MarkType"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "oesr": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "priority": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "published": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "ru": GraphQLField(
                GraphQLNonNull(GraphQLBoolean),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "smartekCode": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "smarteks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["Smartek"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "unit": GraphQLField(
                cast(GraphQLObjectType, type_map["Unit"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "unitShort": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "unitShortEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "weight": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "year": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Year"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "yearId": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "MarkType": GraphQLEnumType(
        name="MarkType",
        description=None,
        values={
            "STRAIGHT": GraphQLEnumValue(
                value="STRAIGHT", description=None, deprecation_reason=None
            ),
            "REVERSED": GraphQLEnumValue(
                value="REVERSED", description=None, deprecation_reason=None
            ),
        },
    ),
    "MarkValue": GraphQLObjectType(
        name="MarkValue",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "MaterialBlock": GraphQLObjectType(
        name="MaterialBlock",
        description=None,
        interfaces=[],
        fields=lambda: {
            "files": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["AttachFile"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "links": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Link"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "texts": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["AttachText"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "width": GraphQLField(
                cast(GraphQLEnumType, type_map["Width"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Mutation": GraphQLObjectType(
        name="Mutation",
        description=None,
        interfaces=[],
        fields=lambda: {
            "authorizedFeedbackCreate": GraphQLField(
                cast(GraphQLObjectType, type_map["Feedback"]),
                args={
                    "input": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType, type_map["FeedbackCreateInput"]
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "feedbackCreate": GraphQLField(
                cast(GraphQLObjectType, type_map["Feedback"]),
                args={
                    "input": GraphQLArgument(
                        GraphQLNonNull(
                            cast(
                                GraphQLInputObjectType, type_map["FeedbackCreateInput"]
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "fileCreate": GraphQLField(
                cast(GraphQLObjectType, type_map["AttachFile"]),
                args={
                    "input": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["FileCreateInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "fileDestroy": GraphQLField(
                GraphQLBoolean,
                args={
                    "id": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "fileUpdate": GraphQLField(
                cast(GraphQLObjectType, type_map["AttachFile"]),
                args={
                    "id": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "input": GraphQLArgument(
                        GraphQLNonNull(
                            cast(GraphQLInputObjectType, type_map["FileCreateInput"])
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "sessionCreate": GraphQLField(
                cast(GraphQLObjectType, type_map["Session"]),
                args={
                    "email": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "password": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "sessionDestroy": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "sessionRefresh": GraphQLField(
                cast(GraphQLObjectType, type_map["Session"]),
                args={
                    "refreshToken": GraphQLArgument(
                        GraphQLNonNull(GraphQLString),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "News": GraphQLObjectType(
        name="News",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "materialBlocks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["MaterialBlock"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "publish": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "publishTime": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "tags": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Tag"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "text": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "textEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "title": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "titleEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "OrderDir": GraphQLEnumType(
        name="OrderDir",
        description=None,
        values={
            "DESC": GraphQLEnumValue(
                value="DESC", description=None, deprecation_reason=None
            ),
            "ASC": GraphQLEnumValue(
                value="ASC", description=None, deprecation_reason=None
            ),
        },
    ),
    "OrderInput": GraphQLInputObjectType(
        name="OrderInput",
        description=None,
        fields=lambda: {
            "type": GraphQLInputField(
                cast(GraphQLEnumType, type_map["OrderType"]),
                default_value=Undefined,
                description=None,
                deprecation_reason=None,
            ),
            "dir": GraphQLInputField(
                cast(GraphQLEnumType, type_map["OrderDir"]),
                default_value="DESC",
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "OrderType": GraphQLEnumType(
        name="OrderType",
        description=None,
        values={
            "NAME": GraphQLEnumValue(
                value="NAME", description=None, deprecation_reason=None
            ),
            "CREATED_AT": GraphQLEnumValue(
                value="CREATED_AT", description=None, deprecation_reason=None
            ),
        },
    ),
    "Partner": GraphQLObjectType(
        name="Partner",
        description=None,
        interfaces=[],
        fields=lambda: {
            "engPhotos": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "link": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "photos": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Photo": GraphQLObjectType(
        name="Photo",
        description=None,
        interfaces=[],
        fields=lambda: {
            "engResizedUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "engThumbUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "engUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "resizedUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "thumbUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "url": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "vignetteResizedUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "vignetteUrl": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Query": GraphQLObjectType(
        name="Query",
        description=None,
        interfaces=[],
        fields=lambda: {
            "agglomerations": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["Agglomeration"])
                        )
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "transliteratedTitles": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "banners": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Banner"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "cities": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["City"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "transliteratedTitles": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "isRus": GraphQLArgument(
                        GraphQLBoolean,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityTypeId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "cityMarkDataYear": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={
                    "markId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "cityTypes": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["CityType"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "clusters": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Cluster"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "contents": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["Content"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "creativeDirections": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["CreativeDirection"])
                        )
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "creativeDirectionsData": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["MarkValue"]))
                    )
                ),
                args={
                    "creativeDirectionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "creativeMarks": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["CreativeMark"])
                        )
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "zeroMax": GraphQLArgument(
                        GraphQLBoolean,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "creativeMarksData": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["CreativeMarkValue"])
                        )
                    )
                ),
                args={
                    "creativeMarkId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "creativePages": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["CreativePage"])
                        )
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "transliteratedTitles": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "directions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Direction"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "yearId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "downloadAgglomeration": GraphQLField(
                GraphQLString,
                args={
                    "agglomerationId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "yearId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "downloadCity": GraphQLField(
                GraphQLString,
                args={
                    "cityId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "yearId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "esgCities": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgCity"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "companyIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "esgClusters": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgCluster"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "esgCompanies": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgCompany"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "esgContents": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgContent"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "esgDirections": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["EsgDirection"])
                        )
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "esgMarks": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["EsgMark"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getAgglomerationsDbData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["AgglomerationData"])),
                args={
                    "markIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "directionIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "agglomerationIds": GraphQLArgument(
                        GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLID))),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getClustersRatingData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["RatingStats"])),
                args={
                    "directionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "getCreativeClustersRatingData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["RatingStats"])),
                args={
                    "creativeDirectionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "getCreativeDbData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CityData"])),
                args={
                    "creativeMarkIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "creativeDirectionIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityIds": GraphQLArgument(
                        GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLID))),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getCreativeRatingData": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["MarkValue"]))
                    )
                ),
                args={
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "getDbData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CityData"])),
                args={
                    "markIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "directionIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityIds": GraphQLArgument(
                        GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLID))),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "includeOesr": GraphQLArgument(
                        GraphQLBoolean,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getDirectionDynamic": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["ValueByYears"]))
                ),
                args={
                    "directionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getEsgDbData": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["CityData"])),
                args={
                    "markIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "directionIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityIds": GraphQLArgument(
                        GraphQLNonNull(GraphQLList(GraphQLNonNull(GraphQLID))),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getLogs": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["UserLog"]))
                    )
                ),
                args={
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "action": GraphQLArgument(
                        cast(GraphQLEnumType, type_map["UserLogAction"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getMapCitiesByDirection": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["MapCitySelection"])
                    )
                ),
                args={
                    "directionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getMapCitiesByMark": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["MapCitySelection"])
                    )
                ),
                args={
                    "markId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getMarkDynamic": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["ValueByYears"]))
                ),
                args={
                    "markId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getParamsRank": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["RankCitySelection"])
                    )
                ),
                args={
                    "multipliers": GraphQLArgument(
                        GraphQLNonNull(
                            GraphQLList(
                                GraphQLNonNull(
                                    cast(
                                        GraphQLInputObjectType,
                                        type_map["DirectionMultiplierInput"],
                                    )
                                )
                            )
                        ),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "cityTypeIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getProfile": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["User"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "getRatingData": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["JSON"])),
                args={
                    "directionId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "getTopCitiesByDirection": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["TopCitySelection"])
                    )
                ),
                args={
                    "directionId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "getTopCitiesByMark": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(
                        cast(GraphQLObjectType, type_map["TopCitySelection"])
                    )
                ),
                args={
                    "markId": GraphQLArgument(
                        GraphQLNonNull(GraphQLID),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "clusterIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "marks": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Mark"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "published": GraphQLArgument(
                        GraphQLBoolean,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "order": GraphQLArgument(
                        cast(GraphQLInputObjectType, type_map["OrderInput"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "ru": GraphQLArgument(
                        GraphQLBoolean,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "oesr": GraphQLArgument(
                        GraphQLBoolean,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "yearId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "directionId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "news": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["News"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "transliteratedTitles": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "search": GraphQLArgument(
                        GraphQLString,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "tags": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "oesrCities": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["City"]))),
                args={
                    "markIds": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    )
                },
                description=None,
                deprecation_reason=None,
            ),
            "partners": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Partner"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "researches": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Research"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "transliteratedTitles": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "subindices": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Subindex"]))
                    )
                ),
                args={
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "transliteratedTitles": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLString)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
            "tags": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Tag"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "years": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["Year"]))
                    )
                ),
                args={
                    "id": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "ids": GraphQLArgument(
                        GraphQLList(GraphQLNonNull(GraphQLID)),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "limit": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "offset": GraphQLArgument(
                        GraphQLInt,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "updatedAfter": GraphQLArgument(
                        cast(GraphQLScalarType, type_map["Timestamp"]),
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                    "lastId": GraphQLArgument(
                        GraphQLID,
                        default_value=Undefined,
                        description=None,
                        deprecation_reason=None,
                    ),
                },
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "RankCitySelection": GraphQLObjectType(
        name="RankCitySelection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cityId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "cityName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "cityNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "cityTypeId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "cityTypeName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "cityTypeNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "clusterId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "clusterName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "clusterNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "percent": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "resultSum": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "RatingStats": GraphQLObjectType(
        name="RatingStats",
        description=None,
        interfaces=[],
        fields=lambda: {
            "clusters": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(
                            cast(GraphQLObjectType, type_map["ClusterStats"])
                        )
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "directions": GraphQLField(
                GraphQLNonNull(
                    GraphQLList(
                        GraphQLNonNull(cast(GraphQLObjectType, type_map["MarkValue"]))
                    )
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Research": GraphQLObjectType(
        name="Research",
        description=None,
        interfaces=[],
        fields=lambda: {
            "color": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "icons": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Icon"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "materialBlocks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["MaterialBlock"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "researchKeys": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["ResearchKey"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "ResearchKey": GraphQLObjectType(
        name="ResearchKey",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Session": GraphQLObjectType(
        name="Session",
        description=None,
        interfaces=[],
        fields=lambda: {
            "accessToken": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "expiresIn": GraphQLField(
                GraphQLNonNull(cast(GraphQLScalarType, type_map["Timestamp"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "refreshToken": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "user": GraphQLField(
                GraphQLNonNull(cast(GraphQLObjectType, type_map["User"])),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Smartek": GraphQLObjectType(
        name="Smartek",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "result": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "slug": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "task": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "url": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Subindex": GraphQLObjectType(
        name="Subindex",
        description=None,
        interfaces=[],
        fields=lambda: {
            "buttonName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "buttonNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "link": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "subindexPage": GraphQLField(
                cast(GraphQLObjectType, type_map["SubindexPage"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "SubindexPage": GraphQLObjectType(
        name="SubindexPage",
        description=None,
        interfaces=[],
        fields=lambda: {
            "description": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "descriptionEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "files": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["AttachFile"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "materialBlocks": GraphQLField(
                GraphQLList(
                    GraphQLNonNull(cast(GraphQLObjectType, type_map["MaterialBlock"]))
                ),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Tag": GraphQLObjectType(
        name="Tag",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Timestamp": GraphQLScalarType(
        name="Timestamp", description=None, specified_by_url=None
    ),
    "TopCitySelection": GraphQLObjectType(
        name="TopCitySelection",
        description=None,
        interfaces=[],
        fields=lambda: {
            "cityTypeName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "cityTypeNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "clusterName": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "clusterNameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "placeNum": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "transliteratedTitle": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Unit": GraphQLObjectType(
        name="Unit",
        description=None,
        interfaces=[],
        fields=lambda: {
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "nameEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "short": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "shortEng": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
        },
    ),
    "Upload": GraphQLScalarType(name="Upload", description=None, specified_by_url=None),
    "User": GraphQLObjectType(
        name="User",
        description=None,
        interfaces=[],
        fields=lambda: {
            "apiKey": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "appointment": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "createdAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "email": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "firstName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLNonNull(GraphQLID),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "images": GraphQLField(
                GraphQLList(GraphQLNonNull(cast(GraphQLObjectType, type_map["Photo"]))),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "lastName": GraphQLField(
                GraphQLNonNull(GraphQLString),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "organisation": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "patronymic": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "UserLog": GraphQLObjectType(
        name="UserLog",
        description=None,
        interfaces=[],
        fields=lambda: {
            "action": GraphQLField(
                cast(GraphQLEnumType, type_map["UserLogAction"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "createdAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "ipAddress": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "userId": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "UserLogAction": GraphQLEnumType(
        name="UserLogAction",
        description=None,
        values={
            "LOGIN": GraphQLEnumValue(
                value="LOGIN", description=None, deprecation_reason=None
            ),
            "LOGOUT": GraphQLEnumValue(
                value="LOGOUT", description=None, deprecation_reason=None
            ),
        },
    ),
    "ValueByYears": GraphQLObjectType(
        name="ValueByYears",
        description=None,
        interfaces=[],
        fields=lambda: {
            "name": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
            "refValue": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "value": GraphQLField(
                GraphQLFloat, args={}, description=None, deprecation_reason=None
            ),
            "year": GraphQLField(
                GraphQLString, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "Width": GraphQLEnumType(
        name="Width",
        description=None,
        values={
            "CENTER": GraphQLEnumValue(
                value="CENTER", description=None, deprecation_reason=None
            ),
            "FILL": GraphQLEnumValue(
                value="FILL", description=None, deprecation_reason=None
            ),
        },
    ),
    "Year": GraphQLObjectType(
        name="Year",
        description=None,
        interfaces=[],
        fields=lambda: {
            "createdAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "defaultSelected": GraphQLField(
                GraphQLBoolean, args={}, description=None, deprecation_reason=None
            ),
            "id": GraphQLField(
                GraphQLID, args={}, description=None, deprecation_reason=None
            ),
            "position": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
            "status": GraphQLField(
                cast(GraphQLEnumType, type_map["YearStatus"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "updatedAt": GraphQLField(
                cast(GraphQLScalarType, type_map["Timestamp"]),
                args={},
                description=None,
                deprecation_reason=None,
            ),
            "year": GraphQLField(
                GraphQLInt, args={}, description=None, deprecation_reason=None
            ),
        },
    ),
    "YearStatus": GraphQLEnumType(
        name="YearStatus",
        description=None,
        values={
            "PREPARATION": GraphQLEnumValue(
                value="PREPARATION", description=None, deprecation_reason=None
            ),
            "PUBLISHED": GraphQLEnumValue(
                value="PUBLISHED", description=None, deprecation_reason=None
            ),
            "ARCHIVE": GraphQLEnumValue(
                value="ARCHIVE", description=None, deprecation_reason=None
            ),
        },
    ),
}
schema: GraphQLSchema = GraphQLSchema(
    query=cast(GraphQLObjectType, type_map["Query"]),
    mutation=cast(GraphQLObjectType, type_map["Mutation"]),
    subscription=None,
    types=type_map.values(),
    directives=[
        GraphQLDirective(
            name="include",
            description="Directs the executor to include this field or fragment only when the `if` argument is true.",
            is_repeatable=False,
            locations=(
                DirectiveLocation.FIELD,
                DirectiveLocation.FRAGMENT_SPREAD,
                DirectiveLocation.INLINE_FRAGMENT,
            ),
            args={
                "if": GraphQLArgument(
                    GraphQLNonNull(GraphQLBoolean),
                    default_value=Undefined,
                    description="Included when true.",
                    deprecation_reason=None,
                )
            },
        ),
        GraphQLDirective(
            name="skip",
            description="Directs the executor to skip this field or fragment when the `if` argument is true.",
            is_repeatable=False,
            locations=(
                DirectiveLocation.FIELD,
                DirectiveLocation.FRAGMENT_SPREAD,
                DirectiveLocation.INLINE_FRAGMENT,
            ),
            args={
                "if": GraphQLArgument(
                    GraphQLNonNull(GraphQLBoolean),
                    default_value=Undefined,
                    description="Skipped when true.",
                    deprecation_reason=None,
                )
            },
        ),
        GraphQLDirective(
            name="deprecated",
            description="Marks an element of a GraphQL schema as no longer supported.",
            is_repeatable=False,
            locations=(
                DirectiveLocation.FIELD_DEFINITION,
                DirectiveLocation.ARGUMENT_DEFINITION,
                DirectiveLocation.INPUT_FIELD_DEFINITION,
                DirectiveLocation.ENUM_VALUE,
            ),
            args={
                "reason": GraphQLArgument(
                    GraphQLString,
                    default_value="No longer supported",
                    description="Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax, as specified by [CommonMark](https://commonmark.org/).",
                    deprecation_reason=None,
                )
            },
        ),
        GraphQLDirective(
            name="specifiedBy",
            description="Exposes a URL that specifies the behaviour of this scalar.",
            is_repeatable=False,
            locations=(DirectiveLocation.SCALAR,),
            args={
                "url": GraphQLArgument(
                    GraphQLNonNull(GraphQLString),
                    default_value=Undefined,
                    description="The URL that specifies the behaviour of this scalar.",
                    deprecation_reason=None,
                )
            },
        ),
    ],
    description=None,
)
