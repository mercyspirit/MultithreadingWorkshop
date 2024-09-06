import time
from request_service import get
from json_service import write_to_file

if __name__ == '__main__':
    print("Program start")
    start = time.time()

    # body = get('https://data.wa.gov/api/views/f6w7-q2d2/rows.json?accessType=DOWNLOAD')
    # data = body["data"]
    # # 10 location

    # print(len(data))
    
    
    end = time.time()
    difference = end - start
    print(f"Time elapsed: {difference}")