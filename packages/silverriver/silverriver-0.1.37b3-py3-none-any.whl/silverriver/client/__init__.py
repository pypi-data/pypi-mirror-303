from silverriver.client.http_client import HTTPCruxClient
from silverriver.interfaces import SubTransition, AgentAction, NOOP_ACTION, SupportedModes
from silverriver.interfaces.chat import AgentChatInterface
from silverriver.interfaces.data_models import BrowserObservation, Observation
from silverriver.utils.execution import execute_python_code

API_HOST = "crux.silverstream.ai"
API_PORT = 31337
API_SERVER_URL = f"http://{API_HOST}:{API_PORT}"

class BrowserSession:
    """
    Represents a browser session in the cloud for the agent to interact with.

    This class manages interactions with a remote browser session,
    code execution, and observation retrieval.
    """

    def __init__(self, client: HTTPCruxClient, chat_module: AgentChatInterface):
        self._client = client
        self.remote_page = None
        self.chat_module = chat_module

    def reset(self, start_url: str) -> SubTransition:
        """
        Reset the browser session with a new starting URL.

        Args:
            start_url (str): The URL to start the session with.

        Returns:
            SubTransition: The initial state of the browser after reset.
        """
        setup = self._client.env_setup(start_url=start_url)
        self.remote_page = setup.exec_context["page"]
        return self._client.internal_step(NOOP_ACTION)

    def execute(self, code: str) -> BrowserObservation:
        """
        Execute Python code in the context of the browser session.

        This method runs the provided code, posts the action to the client,
        and returns the resulting browser observation.

        Args:
            code (str): The Python code to execute.

        Returns:
            BrowserObservation: The observation after executing the code.
        """
        execute_python_code(
            code, execution_context={
                "page": self.remote_page,
                "chat": self.chat_module,
            })

        action = AgentAction(code=code)
        ret = self._client.internal_step(action)
        return BrowserObservation(**dict(ret.obs))


class Crux:
    """
    Main client for interacting with the Crux API.

    This class provides methods to create browser sessions and retrieve agent actions.
    """

    def __init__(self, api_key: str, base_url: str = API_SERVER_URL):
        self._client = HTTPCruxClient(api_key=api_key, base_url=base_url)

    def create_browser_session(self, start_url: str, chat) -> tuple[BrowserSession, BrowserObservation, dict]:
        """
        Create a new browser session.

        Args:
            start_url (str): The URL to start the session with.
            chat: The chat interface for agent-user communication.

        Returns:
            tuple: A tuple containing the BrowserSession, initial BrowserObservation, and additional info.
                session: is the BrowserSession to control the browser remotely, BrowserObservation contains all the
                relevant information for decision making, while info contains metadata which is likely not interesting
                to the agent.
        """
        session = BrowserSession(client=self._client, chat_module=chat)
        transition = session.reset(start_url=start_url)
        return session, BrowserObservation(**transition.obs), transition.info

    def get_action(self, obs: Observation, mode: SupportedModes) -> str:
        """
        Get the next action from the agent based on the current observation.

        Args:
            obs (Observation): The current observation of the environment.
            mode (SupportedModes): The mode to use for generating the action. See SupportedModes for available options.

        Returns:
            str: The code representing the next action to take.
        """
        if isinstance(obs, BrowserObservation) and not isinstance(obs, Observation):
            raise ValueError("The agent needs to be informed of the chat messages, use Observation instead.")
        action = self._client.agent_get_action(obs, mode)
        return action.code

    def upload_trace(self, prefix: str, filename: str) -> bool:
        """
        Upload a trace file to the Crux API.

        Args:
            prefix (str): The destination path for the uploaded trace file.
            filename (str): The full path to the trace file to upload.

        Returns:
            success (bool) : The response from the API after uploading the trace.
        """
        return self._client.upload_trace(prefix, filename)

    def close(self):
        self._client.env_close()
        self._client.agent_close()
