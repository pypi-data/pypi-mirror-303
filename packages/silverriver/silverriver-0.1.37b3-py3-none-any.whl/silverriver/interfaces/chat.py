import abc


class AgentChatInterface(abc.ABC):
    @abc.abstractmethod
    def send_message_to_user(self, message):
        pass

    @abc.abstractmethod
    def wait_for_user_message(self):
        pass
