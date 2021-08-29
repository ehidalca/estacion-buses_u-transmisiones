import multiprocessing as mp
from Negocio.Pistolas import Pistolas

class Number:
    def __init__(self, n):
        self.number = n
        
    def power(self):
        self.number = self.number**2
        return self.number

def run_power(n, out_queue):  
    print(n)  

    out_queue.put((n.id))
    
if __name__ == '__main__':
    n1 = Number(1)
    n2 = Number(2)
    numbers = dict()
    numbers[1] = n1
    numbers[2] = n2
    pistolas = Pistolas().Listar()
    out_queue = mp.Queue()
    workers = [mp.Process(target=run_power, args=(n, out_queue)) for n in pistolas]
    for work in workers:
        work.start()
    for work in workers:
        work.join()
    results = []
    for j in range(len(workers)):
        results.append(out_queue.get())
    for r in results:
        print(r[0], '-->', r[1])