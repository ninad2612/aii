import multiprocessing  # Importing the multiprocessing module to handle processes and communication

# Function representing the child process
def child_process(conn):
    message = "Hello from child process!"  # Message to send to parent
    conn.send(message)  # Send the message through the connection (to the parent process)
    conn.close()  # Close the connection once the message is sent

# Function representing the parent process
def parent_process():
    # Create a two-way pipe for communication between parent and child processes
    parent_conn, child_conn = multiprocessing.Pipe()  # parent_conn is used by the parent process, and child_conn is used by the child process

    # Create a new process that will run the child_process function and pass the child_conn to it
    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()  # Start the child process

    # Receive the message from the child process through the parent_conn
    message = parent_conn.recv()  # Blocking call, waits until the child sends a message
    print(f"Parent received: {message}")  # Print the received message from the child process

    # Wait for the child process to finish execution before proceeding
    process.join()

# Entry point for the program
if __name__ == "__main__":
    parent_process()  # Call the parent_process function to execute the code
