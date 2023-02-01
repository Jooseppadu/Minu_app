import Model

# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

    def get_task(self):
        self.model.generate_task()
        return self.model.task


