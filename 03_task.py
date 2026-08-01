def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.split()

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": " ".join(message)
    }

def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        return [parse_log_line(line) for line in file.readlines()]

def filter_logs_by_level(logs: list, level: str | None) -> list:

    if level is None:
        return logs
    
    return list(filter(lambda log: log["level"] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    levels = ["DEBUG", "INFO", "WARNING", "ERROR"]

    counts = {level: 0 for level in levels}

    for log in logs:
        counts[log["level"]] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")  
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main(path, level = None):
    logs = load_logs(path)
    filtered_logs = filter_logs_by_level(logs, level)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered_logs:  
            print(f"{log['date']} {log['time']} - {log['message']}")

main("assets/log-file.txt")