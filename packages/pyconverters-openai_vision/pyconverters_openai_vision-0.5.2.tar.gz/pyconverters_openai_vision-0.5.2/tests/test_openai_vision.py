from pathlib import Path
from typing import List

import pytest
from pymultirole_plugins.v1.schema import Document
from starlette.datastructures import UploadFile

from pyconverters_openai_vision.openai_vision import (
    OpenAIVisionConverter,
    OpenAIVisionParameters, DeepInfraOpenAIVisionParameters, DeepInfraOpenAIVisionConverter
)


def test_openai_vision_basic():
    model = OpenAIVisionConverter.get_model()
    model_class = model.construct().__class__
    assert model_class == OpenAIVisionParameters


@pytest.mark.skip(reason="Not a test")
def test_openai():
    converter = OpenAIVisionConverter()
    parameters = OpenAIVisionParameters()
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/colducoq.jpg')
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(UploadFile(source.name, fin, 'image/jpeg'), parameters)
        assert len(docs) == 1
        doc0 = docs[0]
        assert 'dent de crolles' in doc0.text.lower()

    source = Path(testdir, 'data/webinar.png')
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(UploadFile(source.name, fin, 'image/png'), parameters)
        assert len(docs) == 1
        doc0 = docs[0]
        assert 'kairntech' in doc0.text.lower()


@pytest.mark.skip(reason="Not a test")
def test_deepinfra():
    converter = DeepInfraOpenAIVisionConverter()
    parameters = DeepInfraOpenAIVisionParameters(model="meta-llama/Llama-3.2-11B-Vision-Instruct")
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/colducoq.jpg')
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(UploadFile(source.name, fin, 'image/jpeg'), parameters)
        assert len(docs) == 1
        doc0 = docs[0]
        assert 'dent de crolles' in doc0.text.lower()

    source = Path(testdir, 'data/webinar.png')
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(UploadFile(source.name, fin, 'image/png'), parameters)
        assert len(docs) == 1
        doc0 = docs[0]
        assert 'generative ai' in doc0.text.lower()
