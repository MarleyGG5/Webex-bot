class Poll:
    def __init__(self, name, description, room_id, author):
        self.name = name
        self.description = description
        self.room_id = room_id
        self.author = author
        self.options = {}
        self.votes = {}
        self.voted_users = set()  # Track users who have voted
        self._last_option_index_added = 1
        self.started = False

    def add_option(self, option):
        self.options[self._last_option_index_added] = option
        self.votes[self._last_option_index_added] = 0
        self._last_option_index_added += 1

    def vote(self, option_num, user_email):
        if user_email in self.voted_users:
            return False # if the user has already voted not allow for another to go through
        self.votes[option_num] += 1
        self.voted_users.add(user_email)
        return True
    
    def list_options(self):
        return self.options
    
    def collate_results(self):
        results = {}
        for value, option in self.options.items():
            results[option] = self.votes[value]
        return results