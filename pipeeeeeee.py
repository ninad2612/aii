import multiprocessing
import multiprocessing.process

def child_process(conn):
    msg = 'hiiii'
    conn.send(msg)
    conn.close()

def parent_process():
    parent_conn,child_conn = multiprocessing.Pipe()
    process = multiprocessing.Process(target=child_process,args=(child_conn,))
    process.start()
    msg = parent_conn.recv()
    print(f"Parent received: {msg}")
    process.join()

if __name__ == '__main__' :
    parent_process()
