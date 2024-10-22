#!/usr/bin/env -S rye run python

import os

from lastmile import Lastmile

client = Lastmile(
    # This is the default and can be omitted
    bearer_token=os.environ.get("BEARER_TOKEN"),
)

model = client.models.retrieve(
    model_id={"value": "value"},
)
print(model.model)
