from ttask_manager.ttask_manager import TaskManager
import os
import platformdirs
from prompt_toolkit import prompt, HTML
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import confirm
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.history import FileHistory  
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.document import Document 
def main():
    def get_necessary_files():
        app_data_root = platformdirs.user_data_dir(appname="TaskMan-CLI", appauthor='TYA')
        if not os.path.exists(app_data_root):
            os.makedirs(app_data_root)
        report_dir = os.path.join(app_data_root, 'Reports')
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        json_data_file = os.path.join(app_data_root, 'data.json')
        history_file = FileHistory(os.path.join(app_data_root, '.hist'))
        return report_dir, json_data_file, history_file
    def print_welcome_message():
        print(HTML("""<ansiyellow>
        ╔═══════════════════════════════════════════════════════════════════════════╗
        ║                                                                           ║
        ║   ████████╗ █████╗ ███████╗██╗  ██╗    ███╗   ███╗ █████╗ ███╗   ██╗      ║
        ║   ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔══██╗████╗  ██║      ║
        ║      ██║   ███████║███████╗█████╔╝     ██╔████╔██║███████║██╔██╗ ██║      ║
        ║      ██║   ██╔══██║╚════██║██╔═██╗     ██║╚██╔╝██║██╔══██║██║╚██╗██║      ║
        ║      ██║   ██║  ██║███████║██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║      ║
        ║      ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝      ║
        ║                                                                           ║
        ║              Welcome to TaskMan - Your Personal Task Manager!             ║
        ║                                                                           ║
        ║        Manage your tasks efficiently with simple CLI commands.            ║
        ║        Type 'help' to see available commands or 'exit' to quit.           ║
        ║                                                                           ║
        ║                     Let's boost your productivity!                        ║
        ╚═══════════════════════════════════════════════════════════════════════════╝
        </ansiyellow>
        """))

    def print_help_message():
        print(HTML("""<ansiyellow>
        ╔════════════════════════════════════════════════════════════════════════════════╗
        ║                              TaskMan CLI Commands                              ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║  add [task1] | [task2] | ...    : Add one or more tasks                        ║
        ║    - Format: task:priority      : Add task with specific priority              ║
        ║  remove [task1] | [task2] | ... : Remove one or more tasks                     ║
        ║  mark-as-done / mad [task1]...  : Mark one or more tasks as completed          ║
        ║  list-both / lb                 : Show all tasks (to-do and done)              ║
        ║  list-todo / ltd                : Show pending tasks                           ║
        ║  list-done / ld                 : Show completed tasks                         ║
        ║  clear-todo / cltd              : Clear all pending tasks                      ║
        ║  clear-done / cld               : Clear all completed tasks                    ║
        ║  reset                          : Clear all tasks (both to-do and done)        ║
        ║  report [name]                  : Generate a report (optional custom name)     ║
        ║  save                           : Save current state to file                   ║
        ║  help                           : Show this help message                       ║
        ║  clear / Ctrl+l                 : Clear the screen                             ║
        ║  exit                           : Exit the program                             ║
        ╠════════════════════════════════════════════════════════════════════════════════╣
        ║  Notes:                                                                        ║
        ║  - Use '|' to separate multiple tasks in 'add', 'remove', or 'mad' commands.   ║
        ║  - Tasks are automatically saved on exit and loaded on startup.                ║
        ║  - Priority levels: high, medium, low (default: medium)                        ║
        ╚════════════════════════════════════════════════════════════════════════════════╝
        </ansiyellow>
        """))

    def clear_screen():
        # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
        # For Mac and Linux                 
        else:
            _ = os.system('clear')
    binding = KeyBindings()
    @binding.add('c-l')
    def _(event):
        clear_screen()
    report_dir, json_data_file, history_file = get_necessary_files()     
    def save():
        save = confirm(HTML("<ansicyan>Wanna save the current state: </ansicyan>"),suffix="[y/N]" )
        if save:    
            print(to_do_list.save_current_state(json_data_file))
        else:
            print('Data not saved.')        
    print_welcome_message()
    commands = ['add','remove','mark-as-done','mad','list-both','lb','list-todo','ltd','list done','ld','clear-todo','cltd','clear-done','cld','reset','report','save','help','clear','exit']
    completer = WordCompleter(commands  , ignore_case=True)
    stylesheet = Style.from_dict({
        'positive' : '#4CAF50',
        'negative' : '#FF3333',
        'message'  : '#008080'
    })
    to_do_list = TaskManager()
    print(to_do_list.load_state(json_data_file))
    while True:
        try:
            command = prompt(HTML("<b fg='#FFA500'><i>TaskMan > </i></b>"), completer=completer, history=history_file, auto_suggest=AutoSuggestFromHistory()).strip()            
            if not command:
                print(HTML("<negative>Invalid option,the input cannot be blank,try 'help' to get more info on how to use this CLI.</negative>"), style=stylesheet)

            elif command.lower() == 'clear' :
                clear_screen()
                continue

            elif command.lower() == 'help':
                print_help_message()

            elif command.lower() == 'exit':
                save()
                break
                
            elif command.lower() == 'save':
                print(to_do_list.save_current_state(json_data_file))

            elif command.lower().startswith('add'):
                tasks_input = command.split(maxsplit=1)[1].split('|')
                tasks = []

                for task_str in tasks_input:
                    task_str = task_str.strip()
                    if not task_str:
                        continue

                    if ':' in task_str:
                        task, priority = map(str.strip, task_str.split(':',1))
                        tasks.append((task,priority))
                    else:
                        tasks.append(task_str)
                print(to_do_list.add_task(*tasks))

            elif command.lower().startswith('remove') :
                tasks_tobe_removed = [task.strip() for task in command.split(maxsplit=1)[1].split('|') if task.strip()]
                print(to_do_list.remove_task(*tasks_tobe_removed))

            elif command.lower().startswith('mark-as-done') or command.lower().startswith('mad'):
                tasks_tobe_mad = [task.strip() for task in command.split(maxsplit=1)[1].split('|') if task.strip()]
                print(to_do_list.task_done(*tasks_tobe_mad))

            elif command.lower().startswith('list-both') or command.lower().startswith('lb'):
                print(to_do_list.current_state('both'))

            elif command.lower().startswith('list-todo') or command.lower().startswith('ltd'):
                print(to_do_list.current_state('to-do'))

            elif command.lower().startswith('list-done') or command.lower().startswith('ld') :
                print(to_do_list.current_state('done'))

            elif command.lower().startswith('clear-todo') or command.lower().startswith('cltd'):
                print(to_do_list.clear('todo'))

            elif command.lower().startswith('clear-done') or command.lower().startswith('cld'):
                print(to_do_list.clear('done'))

            elif command.lower().startswith('report'):
                report_name = command[len('report'):].strip()
                if report_name and '\n' not in report_name:
                    print(to_do_list.report(report_dir,f"{report_name}.txt",report_content='all'))
                else:
                    print(to_do_list.report(report_dir))

            elif command.lower().startswith('reset'):
                print(to_do_list.clear('both'))
            else:
                print(HTML("<negative>Invalid option, try 'help' to get more info on how to use this CLI.</negative>"),style=stylesheet)

        except KeyboardInterrupt:
            print(HTML("<negative>\nKeyboardInterrupt detected.Exiting... </negative>"),style=stylesheet)
            save()
            break   
            
        except EOFError:
            print(HTML("<negative>\nEOF detected. Exiting...</negative>"), style=stylesheet)
            save()
            break

        except Exception as e:
            print(HTML(f"<negative>An unexpected error occurred: {e}</negative>"), style=stylesheet)
            print(HTML("<message>Please try again or type 'help' to see available commands or 'exit' to quit.</message>"),style=stylesheet)     

    print(HTML("<ansigreen>Thank you for using TaskMan CLI. Goodbye!</ansigreen>"))

if __name__ == '__main__':
    main()
