import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:  
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        list_of_items = os.listdir(target_dir)
        records = []
        for item in list_of_items:
            full_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            record = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            records.append(record)
        return "\n".join(records)

    except Exception as e:
        return f"Error: {e}"

