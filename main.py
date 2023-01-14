from common.const import PATH_DIR
from common.work_file import create_not_exist_dir
import recipient_main
import sender_main

create_not_exist_dir(PATH_DIR)
recipient_main.root.mainloop()
sender_main.root.mainloop()