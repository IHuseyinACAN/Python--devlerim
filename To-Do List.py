import os

# Görev Sınıfı
class Task:
    def __init__(self, name, is_completed=False):
        self.name = name
        self.is_completed = is_completed

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "✓" if self.is_completed else "✗"
        return f"{self.name} [{status}]"

# Görev Yöneticisi Sınıfı
class TaskManager:
    def __init__(self, file_name="tasks.txt"):
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def add_task(self, name):
        self.tasks.append(Task(name))
        print(f"'{name}' görevi eklendi.")

    def complete_task(self, index):
        try:
            self.tasks[index].mark_completed()
            print(f"'{self.tasks[index].name}' görevi tamamlandı olarak işaretlendi.")
        except IndexError:
            print("Geçersiz görev numarası!")

    def delete_task(self, index):
        try:
            task = self.tasks.pop(index)
            print(f"'{task.name}' görevi silindi.")
        except IndexError:
            print("Geçersiz görev numarası!")

    def list_tasks(self):
        print("\nYapılacaklar Listesi:")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")
        print()

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.is_completed}\n")
        print("Görevler kaydedildi.")

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                for line in file:
                    name, is_completed = line.strip().split("|")
                    self.tasks.append(Task(name, is_completed == "True"))
            print("Görevler yüklendi.")
        else:
            print("Görev dosyası bulunamadı. Yeni bir liste oluşturuldu.")

# Ana Program
def main():
    manager = TaskManager()
    while True:
        print("\n1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görev Tamamla")
        print("4. Görev Sil")
        print("5. Çıkış ve Kaydet")
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            name = input("Görev adı: ")
            manager.add_task(name)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            index = int(input("Tamamlanacak görev numarası: "))
            manager.complete_task(index)
        elif choice == "4":
            manager.list_tasks()
            index = int(input("Silinecek görev numarası: "))
            manager.delete_task(index)
        elif choice == "5":
            manager.save_tasks()
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    main()
