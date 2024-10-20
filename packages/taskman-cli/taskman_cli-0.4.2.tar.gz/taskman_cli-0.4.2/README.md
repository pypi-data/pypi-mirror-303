# TaskMan CLI
## 📝 Description

TaskMan CLI is a powerful and user-friendly task management application built with Python. It offers a seamless command-line interface for efficiently managing your daily tasks, helping you boost productivity and stay organized.  
**Important Note: This project is for learning purposes and is based on the original script by me. The original repository can be found at [TaskMan CLI](https://github.com/tahadnan/TaskMan-CLI.git) repo.**

## ✨ Features

- 📌 **Add Tasks**: Easily add new tasks to your to-do list
- 🗑️ **Remove Tasks**: Remove tasks from your to-do list
- ✅ **Mark Tasks as Completed**: Move tasks to a "done" list when completed
- 👀 **View Current State**: See all your tasks, both pending and completed
- 🧹 **Clear Lists**: Clean up your to-do and done lists with a single command
- 💾 **Data Persistence**: Your tasks are saved automatically, so you never lose your progress
- 📊 **Generate Reports**: Create daily task reports to track your productivity

## 🚀 Installation

You can install TaskMan CLI using pip:

```bash
pip install taskman-cli
```

## 🛠️ Usage

After installation, you can start TaskMan CLI by running:

```bash
taskman
```

Once launched, you'll see the TaskMan welcome screen. Type `help` to see available commands:

```
TaskMan > help
```

Use the various commands to manage your tasks. Here are some examples:

```
TaskMan > add Buy groceries | Call mom | Finish report
TaskMan > list-todo
TaskMan > mark-as-done Buy groceries
TaskMan > list-both
```

## 📚 Available Commands

- `add [task1] | [task2] | ...`: Add one or more tasks
- `remove [task1] | [task2] | ...`: Remove one or more tasks
- `mark-as-done / mad [task1]...`: Mark one or more tasks as completed
- `list-both / lb`: Show all tasks (to-do and done)
- `list-todo / ltd`: Show pending tasks
- `list-done / ld`: Show completed tasks
- `clear-todo / cltd`: Clear all pending tasks
- `clear-done / cld`: Clear all completed tasks
- `reset`: Clear all tasks (both to-do and done)
- `report [name]`: Generate a report (optional custom name)
- `save`: Save current state to file
- `help`: Show the help message
- `clear / Ctrl+l`: Clear the screen
- `exit`: Exit the program

## 💡 Tips

- Use the up and down arrow keys to navigate through your command history.
- TaskMan supports auto-completion. Start typing a command and press Tab to complete it.
- Your tasks can be saved, so you can safely exit with saving the current state and resume your work later.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the ZTM Python course by Andrei Neagoie
- Built with love using Python and prompt_toolkit

## 📞 Contact

If you have any questions, feel free to reach out:

- Gmail - taha.y.adnan@gmail.com
- Project Link: [TaskMan-CLI-PyPi](https://github.com/tahadnan/TaskMan-CLI-PyPi.git)

---

<div align="center">

Made with ❤️ by [Taha Yasser Adnan](https://github.com/tahadnan)

</div>
