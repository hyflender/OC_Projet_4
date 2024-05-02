from views.menu import PlayerView
from controllers.controller_player import PlayerController


def main():
    # Create the view instance
    view = PlayerView()

    # Create the model, which in this simple case is just a list of Player objects
    model = []

    # Initialize the controller with the view and model
    controller = PlayerController(view, model)

    # Run the application
    controller.run()


if __name__ == "__main__":
    main()
