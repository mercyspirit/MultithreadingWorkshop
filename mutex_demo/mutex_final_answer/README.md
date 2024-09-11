docker build -t python-multithread-race-condition .

docker run --cpus="1" --memory="256m" python-multithread-race-condition