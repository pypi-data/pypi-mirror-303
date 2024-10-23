#!/bin/bash
rye publish \
    --repository testpypi \
    --repository-url https://test.pypi.org/legacy/ \
    --username mitszo \
    --token $TESTPYPI_PASSWORD \
    --yes
