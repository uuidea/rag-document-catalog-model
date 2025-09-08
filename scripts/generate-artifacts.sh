Run
#!/bin/bash

poetry run python -m linkml_asciidoc_generator.main \
    "model/catalog-model.yaml" \
    "artifacts/documentation/modules/schema" \
    --diagrams


antora antora-playbook.yml    


gen-pydantic --meta NONE model/catalog-model.yaml > model/schemas/catalog-model-pydantic.py