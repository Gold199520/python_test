def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


class Notification:
    def __init__(self, message="", recipients=None):
        self.message = message
        self.recipients = recipients if recipients else []
        self.sent = False

    def notification(self):
        """Отправляет уведомление"""
        if not self.message:
            print("Сообщение не может быть пустым")
            return False

        if not self.recipients:
            print("Нет получателей для отправки")
            return False

        # Здесь может быть реальная логика отправки (email, SMS, push и т.д.)
        print(f"Отправка уведомления: '{self.message}'")
        print(f"Получатели: {', '.join(self.recipients)}")

        # Сохраняем в файл для примера
        log_content = f"Уведомление: {self.message}\n"
        log_content += f"Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        log_content += f"Получатели: {self.recipients}\n"

        write_to_file("notification_log.txt", log_content)

        self.sent = True
        return True


class Schedule:
    def __init__(self):
        self.tasks = []

    def schedule(self, notification: Notification, delay_seconds=0):
        """Планирует уведомление с задержкой"""
        import time
        from datetime import datetime

        if delay_seconds > 0:
            scheduled_time = datetime.now().timestamp() + delay_seconds
            self.tasks.append({
                'notification': notification,
                'scheduled_time': scheduled_time,
                'executed': False
            })
            print(f"Уведомление запланировано на {delay_seconds} секунд")
            return True
        else:
            # Немедленное выполнение
            return notification.notification()

    def run_pending(self):
        """Выполняет запланированные задачи"""
        import time
        current_time = time.time()
        executed_count = 0

        for task in self.tasks:
            if not task['executed'] and current_time >= task['scheduled_time']:
                print(f"Выполнение запланированного уведомления...")
                task['notification'].notification()
                task['executed'] = True
                executed_count += 1

        # Удаляем выполненные задачи
        self.tasks = [task for task in self.tasks if not task['executed']]

        return executed_count


# Пример использования
if __name__ == "__main__":
    from datetime import datetime

    # Создаем уведомление
    notification1 = Notification(
        message="Совещание через 15 минут",
        recipients=["ivan@example.com", "anna@example.com"]
    )

    notification2 = Notification(
        message="Дедлайн проекта завтра",
        recipients=["team@example.com"]
    )

    # Создаем планировщик
    scheduler = Schedule()

    # Планируем уведомления
    scheduler.schedule(notification1, delay_seconds=5)  # через 5 секунд
    scheduler.schedule(notification2, delay_seconds=10)  # через 10 секунд

    print("Планировщик запущен. Ожидайте выполнения задач...")

    # Запускаем проверку запланированных задач
    import time

    for i in range(15):
        print(f"Проверка... ({i + 1})")
        scheduler.run_pending()
        time.sleep(1)

    print("Все задачи выполнены.")

    # Читаем лог из файла
    try:
        log_content = read_from_file("notification_log.txt")
        print("\nСодержимое лога:")
        print(log_content)
    except FileNotFoundError:
        print("Файл лога не найден")