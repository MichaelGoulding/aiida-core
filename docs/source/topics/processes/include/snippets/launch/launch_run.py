from aiida import orm, plugins
from aiida.engine import run

ArithmeticAddCalculation = plugins.CalculationFactory('core.arithmetic.add')
result = run(ArithmeticAddCalculation, x=orm.Int(1), y=orm.Int(2))
