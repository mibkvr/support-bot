import json
import os


class TicketConfig:
    support_message_id = 0
    support_category_id = 0
    team_role_id = 0

    support_channel_message_text = "Wilkommen im Support Bereich. Reagiere mit ❓ um ein Support Ticket zu erstellen"
    ticket_channel_message_text = "Dein Ticket wurde erstellt. \n Schildere hier bitte dein Problem"

    defaultConfig = {
        "user_ticket_list": {},
        "global_stats": 0,
        "support_message_id": 0,
        "support_category_id": 0,
        "team_role_id": 0
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
            self.support_message_id = json_data["support_message_id"]
            self.support_category_id = json_data["support_category_id"]
            self.team_role_id = json_data["team_role_id"]
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
                "global_stats": self.global_stats,
                "support_message_id": self.support_message_id,
                "support_category_id": self.support_category_id,
                "team_role_id": self.team_role_id
            }, f)
