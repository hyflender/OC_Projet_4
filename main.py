from controllers import GlobalController
from utils import Logger


def main():

    Logger.info("Initialize the global controller")
    controller = GlobalController()

    Logger.info("Run the application")
    controller.run()


if __name__ == "__main__":
    main()
