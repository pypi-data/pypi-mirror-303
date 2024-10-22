from flake8_plugin_utils import Error


class DecoratorVedroParams(Error):
    code = 'OCS101'
    message = 'decorator @vedro.params should not be presented'


class MultipleScreenshotsError(Error):
    code = 'OCS300'
    message = 'step "{step_name}" make_screenshot_for_comparison more once'
