import ast
from typing import List

from flake8_plugin_utils import Error

from custom_otello_linter.abstract_checkers import ScenarioChecker
from custom_otello_linter.errors import DecoratorVedroParams
from custom_otello_linter.visitors.scenario_visitor import Context, ScenarioVisitor


@ScenarioVisitor.register_scenario_checker
class VedroParamsChecker(ScenarioChecker):

    def check_scenario(self, context: Context, *args) -> List[Error]:
        # Проходим по всем шагам в контексте
        for step in context.steps:
            # Проходим по списку декораторов каждого шага
            for decorator in step.decorator_list:
                # Проверяем, является ли декоратор вызовом функции (ast.Call)
                if isinstance(decorator, ast.Call):
                    # Проверяем, является ли функция атрибутом (например, vedro.params)
                    if (
                            isinstance(decorator.func, ast.Attribute)
                            and decorator.func.value.id == 'vedro'
                            and decorator.func.attr == 'params'
                    ):
                        # Возвращаем ошибку, если найден декоратор vedro.params
                        return [DecoratorVedroParams(decorator.lineno, decorator.col_offset)]

        return []
