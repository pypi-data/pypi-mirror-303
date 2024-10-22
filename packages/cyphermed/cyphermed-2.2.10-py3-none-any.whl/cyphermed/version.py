import os


BUILD_LABEL = os.getenv("BUILD_LABEL", None)
BUILD_LABEL = BUILD_LABEL if BUILD_LABEL else ""

VERSION = "2.2.10" + BUILD_LABEL

if __name__ == "__main__":
    # Output version number for use in shell scripts
    print(VERSION)
