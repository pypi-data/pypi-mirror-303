from typing import Dict, List, Literal, Optional, Union

from api_schemas.base import BaseInputModel
from docarray import BaseDoc, DocList
from docarray.base_doc.doc import BaseDocWithoutId
from docarray.typing import NdArray
from docarray.typing.bytes import ImageBytes
from docarray.typing.url import AnyUrl
from docarray.utils._internal.pydantic import bytes_validator
from pydantic import BaseModel, Field, root_validator


class ExecutorUsage(BaseDoc):
    """The usage of the embedding services to report, e.g. number of tokens in case of text input"""  # noqa

    total_tokens: int = Field(
        description='The number of tokens used to embed the input text'
    )


# EXECUTOR MODELS
## Model to be imported by the Executor and used by the Universal API
class TextDoc(BaseDoc):
    """Document containing a text field"""

    text: str


class ChunkedTextDoc(BaseDoc):
    """Document containing chunk text fields"""

    texts: List[str]


# class TextDocWithTruncationFlag(TextDoc):
#     """Document containing a text field and a flag to know if it needs to be truncated"""  # noqa
#
#     truncate: Optional[bool] = Field(
#         description='Flag to determine if the text needs to be truncated when exceeding the maximum token length', # noqa
#         default=None,
#     )


class SerializeImageBytes(ImageBytes):
    @classmethod
    def _docarray_validate(
        cls,
        value,
    ):
        if isinstance(value, str):
            import base64

            return cls(base64.b64decode(value))
        else:
            value = bytes_validator(value)
            return cls(value)

    def _docarray_to_json_compatible(self):
        """
        Convert itself into a json compatible object
        """
        import base64

        encoded_str = base64.b64encode(self).decode('utf-8')
        return encoded_str


class Url(AnyUrl):
    @classmethod
    def _docarray_validate(
        cls,
        value,
    ):
        import urllib.parse

        if isinstance(value, str):
            if urllib.parse.urlparse(value).scheme not in {'http', 'https'}:
                raise ValueError(
                    'This does not have a valid URL schema ("http" or "https")'
                )

        return cls(value)

    @classmethod
    def is_extension_allowed(cls, value) -> bool:
        """Returns a list of allowed file extensions for the class
        that are not covered by the mimetypes library."""
        import urllib.parse

        if isinstance(value, str):
            if urllib.parse.urlparse(value).scheme in {'http', 'https'}:
                return True
            else:
                return False

        return True


class ImageDoc(BaseDoc):
    """ImageDoc with fields"""

    url: Optional[Url] = Field(
        description='URL of an image file',
        default=None,
    )
    bytes: Optional[SerializeImageBytes] = Field(
        description='base64 representation of the Image.',
        default=None,
    )
    image: Optional[Union[Url, SerializeImageBytes]] = Field(
        description='Image representation that can hold URL of an image or a base64 representation',  # noqa
        default=None,
    )

    @root_validator(pre=False)
    def validate_all_input(cls, value):
        if (
            value.get('image', None) is None
            and value.get('url', None) is None
            and value.get('bytes', None) is None
        ):
            raise ValueError('image, URL or bytes need to be provided')
        if value.get('image', None) is not None:
            image = value.get('image')
            if isinstance(image, SerializeImageBytes):
                value['bytes'] = image
                value['image'] = None
            elif isinstance(image, AnyUrl):
                value['url'] = image
                value['image'] = None
            else:
                raise ValueError(
                    'image must be a valid URL or base64 image representation'
                )
        return value


## Model to be imported by the Executor and used by the Universal API
class EmbeddingDoc(BaseDoc):
    """Document to be returned by the embedding backend, containing the embedding
    vector and the token usage for the corresponding input texts"""

    embedding: NdArray = Field(description='The embedding of the texts', default=[])
    usage: ExecutorUsage
    # truncated: Optional[bool] = Field(
    #     description='Flag to inform that the embedding is computed ', default=None
    # )


# UNIVERSAL API MODELS (mimic OpenAI API)
class TextEmbeddingInput(BaseDocWithoutId):
    """The input to the API for text embedding. OpenAI compatible"""

    model: str = Field(
        description='The identifier of the model.\n'
        '\nAvailable models and corresponding param size and dimension:\n'
        '- `jina-clip-v1`,\t223M,\t768\n'
        '- `jina-embeddings-v2-base-en`,\t137M,\t768\n'
        '- `jina-embeddings-v2-base-es`,\t161M,\t768\n'
        '- `jina-embeddings-v2-base-de`,\t161M,\t768\n'
        '- `jina-embeddings-v2-base-zh`,\t161M,\t768\n'
        '- `jina-embeddings-v2-base-code`,\t137M,\t768\n'
        '- `jina-embeddings-v3`,\t570M,\t1024\n'
        '\nFor more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224).\n',  # noqa
    )

    input: Union[List[Optional[str]], Optional[str], List[TextDoc], TextDoc] = Field(
        description='List of texts to embed',
    )
    encoding_type: Optional[
        Union[
            Literal['float', 'base64', 'binary', 'ubinary'],
            List[Literal['float', 'base64', 'binary', 'ubinary']],
        ]
    ] = Field(
        description='The format in which you want the embeddings to be returned.'
        'Possible value are `float`, `base64`, `binary`, `ubinary` or a list '
        'containing any of them. Defaults to `float`',
        alias='embedding_type',
    )
    task: Optional[
        Literal[
            "retrieval.query",
            "retrieval.passage",
            "text-matching",
            "classification",
            "separation",
        ]
    ] = Field(
        description='Used to convey intended downstream application to help the model produce better embeddings. Must be one of the following values:\n'  # noqa
        '- "retrieval.query": Specifies the given text is a query in a search or retrieval setting.\n'  # noqa
        '- "retrieval.passage": Specifies the given text is a document in a search or retrieval setting.\n'  # noqa
        '- "text-matching": Specifies the given text is used for Semantic Textual Similarity.\n'  # noqa
        '- "classification": Specifies that the embedding is used for classification.\n'
        '- "separation": Specifies that the embedding is used for clustering.\n',
        default=None,
    )
    dimensions: Optional[int] = Field(
        description='Used to specify output embedding size. If set, output embeddings will be truncated to the size specified.',  # noqa
        default=None,
    )
    normalized: Optional[bool] = Field(
        description='Flag to determine if the embeddings should be normalized to have a unit L2 norm',  # noqa
        default=None,
    )
    late_chunking: Optional[bool] = Field(
        description='Flag to determine if late chunking is applied. If True, all the sentences in inputs will be concatenated and used as input for late chunking.',  # noqa
        default=None,
    )

    # truncate: Optional[bool] = Field(
    #     description='Flag to determine if the text needs to be truncated when exceeding the maximum token length',  # noqa
    #     default=None,
    # )

    @classmethod
    def validate(
        cls,
        value,
    ):
        if 'input' not in value:
            raise ValueError('"input" field missing')
        if 'model' not in value:
            raise ValueError('you must provide a model parameter')

        return super().validate(value)

    class Config(BaseDoc.Config):
        extra = 'forbid'
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "model": "jina-embeddings-v3",
                "input": ["Hello, world!"],
            },
        }


class ImageEmbeddingInput(BaseDocWithoutId):
    """The input to the API for text embedding. OpenAI compatible"""

    model: str = Field(
        description='The identifier of the model.\n'
        '\nAvailable models and corresponding param size and dimension:\n'
        '- `jina-clip-v1`,\t223M,\t768\n'
        '\nFor more information, please checkout our [technical blog](https://arxiv.org/abs/2405.20204).\n',  # noqa
    )

    input: Union[ImageDoc, List[ImageDoc]] = Field(
        description='List of images to embed',
    )
    encoding_type: Optional[
        Union[
            Literal['float', 'base64', 'binary', 'ubinary'],
            List[Literal['float', 'base64', 'binary', 'ubinary']],
        ]
    ] = Field(
        description='The format in which you want the embeddings to be returned.'
        'Possible value are `float`, `base64`, `binary`, `ubinary` or a list '
        'containing any of them. Defaults to `float`',
        alias='embedding_type',
    )
    normalized: Optional[bool] = Field(
        description='Flag to determine if the embeddings should be normalized to have a unit L2 norm',  # noqa
        default=None,
    )

    @classmethod
    def validate(
        cls,
        value,
    ):
        if 'input' not in value:
            raise ValueError('"input" field missing')
        if 'model' not in value:
            raise ValueError('you must provide a model parameter')
        return super().validate(value)

    class Config(BaseDoc.Config):
        extra = 'forbid'
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "model": "jina-clip-v1",
                "input": ["bytes or URL"],
            },
        }


class MixedEmbeddingInput(BaseDocWithoutId):
    """The input to the API for text embedding. OpenAI compatible"""

    model: str = Field(
        description='The identifier of the model.\n'
        '\nAvailable models and corresponding param size and dimension:\n'
        '- `jina-clip-v1`,\t223M,\t768\n'
        '\nFor more information, please checkout our [technical blog](https://arxiv.org/abs/2405.20204).\n',  # noqa
    )

    input: List[Union[ImageDoc, TextDoc, str]] = Field(
        description='List of text and images to embed',
    )
    encoding_type: Optional[
        Union[
            Literal['float', 'base64', 'binary', 'ubinary'],
            List[Literal['float', 'base64', 'binary', 'ubinary']],
        ]
    ] = Field(
        description='The format in which you want the embeddings to be returned.'
        'Possible value are `float`, `base64`, `binary`, `ubinary` or a list '
        'containing any of them. Defaults to `float`',
        alias='embedding_type',
    )
    normalized: Optional[bool] = Field(
        description='Flag to determine if the embeddings should be normalized to have a unit L2 norm',  # noqa
        default=None,
    )

    @classmethod
    def validate(
        cls,
        value,
    ):
        if 'input' not in value:
            raise ValueError('"input" field missing')
        if 'model' not in value:
            raise ValueError('you must provide a model parameter')
        return super().validate(value)

    class Config(BaseDoc.Config):
        extra = 'forbid'
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "model": "jina-clip-v1",
                "input": ["bytes or URL"],
            },
        }


class EmbeddingObject(BaseDocWithoutId):
    """Embedding object. OpenAI compatible"""

    object: str = 'embedding'
    index: int = Field(
        description='The index of the embedding output, corresponding to the index in the list of inputs'  # noqa
    )
    embedding: Union[NdArray, bytes, Dict[str, Union[NdArray, bytes]]] = Field(
        description='The embedding of the texts. It may come as the base64 '
        'encoded of the embeddings tensor '
        'if "encoding_type" is "base64". It can be rebuilt in the '
        'client as `np.frombuffer(base64.b64decode(embeddings), '
        'dtype=np.float32)`. In case of multiple "encoding_type" are requested, they will be returned in a '  # noqa
        'dictionary where the key is the encoding format.',
        default=[],
    )

    # truncated: Optional[bool] = Field(
    #     description='Flag to inform that the embedding is computed ', default=None
    # )

    class Config(BaseDocWithoutId.Config):
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "object": "embedding",
                "index": 0,
                "embedding": [0.1, 0.2, 0.3],
            }
        }


class Usage(BaseModel):
    total_tokens: int = Field(
        description='The number of tokens used by all the texts in the input'
    )
    prompt_tokens: int = Field(
        description='The number of tokens used by all the texts in the input'
    )


class ModelEmbeddingOutput(BaseInputModel):
    """Output of the embedding service"""

    object: str = 'list'
    data: DocList[EmbeddingObject] = Field(
        description='A list of Embedding Objects returned by the embedding service'
    )
    usage: Usage = Field(
        description='Total usage of the request. Sums up the usage from each individual input'  # noqa
    )

    class Config(BaseInputModel.Config):
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "data": [
                    {"index": 0, "embedding": [0.1, 0.2, 0.3], "object": "embedding"},
                    {"index": 1, "embedding": [0.3, 0.2, 0.1], "object": "embedding"},
                ],
                "usage": {"total_tokens": 15},
            }
        }
