from controllers import GlobalController
from utils import Log


def main():
    Log.debug("Initialize the global controller")
    controller = GlobalController()

    Log.debug("Run the application")
    controller.run()


if __name__ == "__main__":
    main()
