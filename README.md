# Multithreading Workshop

## Requirements
Please install docker on your system.

Windows (Either WSL or Hyper-V work) - https://docs.docker.com/desktop/install/windows-install/

Mac - https://docs.docker.com/desktop/install/mac-install/
Setup

Linux - https://docs.docker.com/desktop/install/linux-install/

Ubuntu - https://docs.docker.com/engine/install/ubuntu/

docker build -t my-python-app .
docker run -it --rm --name my-running-app my-python-app
docker run -v /$(pwd)/output:/usr/src/app/output -it --rm --name my-running-app my-python-app