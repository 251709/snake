from pathlib import Path


class HighScore:
    """Отвечает за загрузку и сохранение лучшего результата."""

    def __init__(self, file_path="highscore.txt"):
        """Создаёт хранилище рекорда."""
        self.file_path = Path(file_path)

    def load(self):
        """Загружает рекорд из файла."""
        try:
            return int(self.file_path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0

    def save(self, score):
        """Сохраняет новый рекорд в файл."""
        self.file_path.write_text(str(score), encoding="utf-8")

    def update(self, score):
        """Обновляет рекорд, если текущий результат больше."""
        current_record = self.load()

        if score > current_record:
            self.save(score)
            return score

        return current_record
