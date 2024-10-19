import importlib.util
import os
import tempfile

BROWSERSTREAM_TEMP_DIR: str = os.path.join(tempfile.gettempdir(), 'browserstream')



def execute_python_code(code: str, execution_context: dict):
    """
    Execute Python code in a temporary module with a provided execution context.

    This approach allows for better debugging capabilities by creating a
    named temporary file instead of executing the code directly.

    Args:
        code (str): The Python code to be executed.
        execution_context (dict): Variables to be made available in the agent's global namespace.
    """
    os.makedirs(BROWSERSTREAM_TEMP_DIR, exist_ok=True)
    with tempfile.NamedTemporaryFile(
            dir=BROWSERSTREAM_TEMP_DIR,
            mode='w',
            suffix='.py',
            # The WebBrowserEnv will report the file at close() time, so we need to keep it around
            delete=False,
    ) as temp_file:
        temp_file.write(code)
        temp_file.flush()

        spec = importlib.util.spec_from_file_location("temp_module", temp_file.name)
        module = importlib.util.module_from_spec(spec)

        # Populate the module's global namespace with the execution context
        for k, v in execution_context.items():
            setattr(module, k, v)
        spec.loader.exec_module(module)
