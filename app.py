# todo-list-app
Một ứng dụng To-Do List đơn giản bằng Python.
 # Hàm thêm công việc mới

def add_task(task_name):
    """
    Thêm một công việc mới vào danh sách.
    Mỗi công việc gồm: tên và trạng thái hoàn thành (False mặc định).
    """
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f" Đã thêm công việc: {task_name}")

# Hàm liệt kê công việc
def list_tasks():
    """
    Hiển thị tất cả công việc trong danh sách.
    Nếu chưa có công việc nào, in thông báo tương ứng.
    """
    if not tasks:
        print(" Danh sách công việc trống.")
        return

    print("\Danh sách công việc:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")
    print()  # dòng trống cuối

# Hàm đánh dấu hoàn thành
# 
def complete_task(task_index):
    """
    Đánh dấu một công việc là đã hoàn thành.
    task_index: chỉ số (bắt đầu từ 1).
    """
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print(f" Đã hoàn thành: {tasks[task_index - 1]['name']}")
    else:
        print(" Chỉ số công việc không hợp lệ!")

# Hàm xóa công việc

def delete_task(task_index):
    """
    Xóa công việc khỏi danh sách theo chỉ số.
    task_index: chỉ số (bắt đầu từ 1).
    """
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f" Đã xóa công việc: {removed_task['name']}")
    else:
        print(" Chỉ số công việc không hợp lệ!")
# Chương trình chính
if __name__ == "__main__":
    print("=== TO-DO LIST APP ===")
    add_task("Học bài Git")
    add_task("Làm bài tập Thực hành 6")
    add_task("Tạo Pull Request trên GitHub")

    list_tasks()

    complete_task(1)
    list_tasks()

    delete_task(2)
    list_tasks()
