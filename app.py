tasks = []

def add_task(task_name):
    tasks.append(task_name)
    print(f"Đã thêm công việc: {task_name}")
def list_tasks():
    print("\nDanh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    list_tasks()
def add_task(task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Đã thêm công việc: {task_name}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"✅ Đã hoàn thành: {tasks[index]['name']}")
    else:
        print("❌ Chỉ số không hợp lệ.")

def list_tasks():
    print("\nDanh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['name']}")

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    complete_task(0)
    list_tasks()
  def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ Đã xóa công việc: {removed['name']}")
    else:
        print("❌ Chỉ số không hợp lệ.")

