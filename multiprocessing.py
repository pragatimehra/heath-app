import os
import multiprocessing
import subprocess

# Function to run an app.py file in a separate process
def run_app(app_file):
    subprocess.call(["python", app_file])

# Function to recursively find all app.py files in subdirectories
def find_app_files(root_dir):
    app_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "app.py":
                app_files.append(os.path.join(root, file))
    return app_files

if __name__ == "__main__":
    # Get the path of the directory containing this script
    main_folder = os.path.dirname(os.path.abspath(__file__))

    # Find all app.py files in subdirectories
    app_files = find_app_files(main_folder)

    # Create a process for each app.py file
    processes = []
    for app_file in app_files:
        process = multiprocessing.Process(target=run_app, args=(app_file,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
