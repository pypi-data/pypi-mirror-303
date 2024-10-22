import ast
from typing import List

from flake8_plugin_utils import Error

from custom_otello_linter.abstract_checkers import StepsChecker
from custom_otello_linter.errors import MultipleScreenshotsError
from custom_otello_linter.visitors.scenario_visitor import Context, ScenarioVisitor


@ScenarioVisitor.register_steps_checker
class MakeScreenshotChecker(StepsChecker):

    def check_steps(self, context: Context, config) -> List[Error]:
        errors = []

        # Проверяем каждый шаг в сценарии
        for step in context.steps:
            if (
                    step.name.startswith('then')
                    or step.name.startswith('and')
                    or step.name.startswith('but')
            ):
                screenshot_calls = 0

                # Проходим через каждый элемент в теле функции (step.body)
                for stmt in step.body:
                    # Применяем ast.walk к каждому выражению в теле функции
                    for node in ast.walk(stmt):
                        if isinstance(node, ast.Call):
                            func_name = self._get_full_func_name(node.func)

                            # Проверяем вызов функции make_screenshot_for_comparison
                            if func_name.endswith('make_screenshot_for_comparison'):
                                screenshot_calls += 1

                                # Если вызовов функции больше одного, добавляем ошибку
                                if screenshot_calls > 1:
                                    errors.append(MultipleScreenshotsError(
                                        lineno=node.lineno,
                                        col_offset=node.col_offset,
                                        step_name=step.name
                                    ))
                                    # Прерываем проверку текущего шага после обнаружения ошибки
                                    break

        # Возвращаем собранные ошибки после завершения всех шагов
        return errors

    def _get_full_func_name(self, func_node) -> str:
        """
        Извлекает полное имя функции из узла ast.Call.func.
        Для прямых вызовов (make_screenshot_for_comparison) возвращает 'make_screenshot_for_comparison'.
        Для вызовов через атрибуты (self.page.make_screenshot_for_comparison) возвращает 'self.page.make_screenshot_for_comparison'.
        """
        if isinstance(func_node, ast.Name):
            return func_node.id
        elif isinstance(func_node, ast.Attribute):
            return self._get_full_func_name(func_node.value) + '.' + func_node.attr
        return ""
