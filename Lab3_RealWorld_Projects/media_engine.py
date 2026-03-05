# media_engine.py

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper


def play_count_stream(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2


@monitor
def process_stream(limit):
    total = 0
    count = 0
    
    for play in play_count_stream(limit):
        print("Generated Play Count:", play)
        total += play
        count += 1
    
    return total, count