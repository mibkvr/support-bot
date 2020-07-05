import json
import os


class TicketConfig:
    support_channel = ""
    support_message = 729327466287464458
    support_category = 729327631551561791

    support_channel_message_text = "Hello World. Use .close_ticket to close the Ticket"
    team_role_id = 729337237879128064

    defaultConfig = {
        "user_ticket_list": {},
        "global_stats": 0
    }
    user_ticket_list = {}
    global_stats = 0

    config_file_path = "./config/config.json"
    config_folder_path = "./config"

    def __init__(self):
        self.read_config()

    def read_config(self):
        if os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'r') as f:
                data = f.read()
            json_data = json.loads(data)

            self.user_ticket_list = json_data["user_ticket_list"]
            self.global_stats = json_data["global_stats"]

        else:
            self.create_default_config_file()

    def create_default_config_file(self):
        if not os.path.exists(self.config_folder_path):
            os.mkdir(self.config_folder_path)
        if not os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'w') as f:
                json.dump(self.defaultConfig, f)
                f.flush()
                f.close()

    def add_support_stats(self, user_id):
        if user_id in self.user_ticket_list.keys():
            self.user_ticket_list[user_id] = self.user_ticket_list[user_id] + 1
            self.global_stats = self.global_stats + 1
        else:
            self.user_ticket_list[user_id] = 1
            self.global_stats = self.global_stats + 1
        self.updateConfig()

    def updateConfig(self):
        with open(self.config_file_path, 'w') as f:
            json.dump({
                "user_ticket_list": self.user_ticket_list,
                "global_stats": self.global_stats
            }, f)
