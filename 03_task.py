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

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    for log in logs:
        if log["level"] == level.upper():
            filtered_logs.append(log)
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    levels = ["DEBUG", "INFO", "WARNING", "ERROR"]

    counts = {level: 0 for level in levels}

    for log in logs:
        if log["level"] == levels[0]:
            counts["DEBUG"] += 1
        elif log["level"] == levels[1]:
            counts["INFO"] += 1
        elif log["level"] == levels[2]:
            counts["WARNING"] += 1
        elif log["level"] == levels[3]:
            counts["ERROR"] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")  
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main(path, level):
    logs = load_logs(path)
    filtered_logs = filter_logs_by_level(logs, level)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    print(f"\nДеталі логів для рівня '{level}':")
    for log in filtered_logs:  
        print(f"{log['date']} {log['time']} - {log['message']}")

main("assets/log-file.txt", "ERROR")