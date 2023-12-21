from aiida.engine import submit
from aiida.orm import Int

builder = AddAndMultiplyWorkChain.get_builder()  # noqa: F821
builder.a = Int(1)
builder.b = Int(2)
builder.c = Int(3)

node = submit(builder)
