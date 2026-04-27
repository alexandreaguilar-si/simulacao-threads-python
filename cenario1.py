import threading
import time

def tarefa(thread_id, tempo_execucao):
    print("Thread", thread_id, "iniciada")
    time.sleep(tempo_execucao)
    print("Thread", thread_id, "finalizada")

tempos = [2, 4, 1]
threads = []

for i, tempo in enumerate(tempos):
    t = threading.Thread(target=tarefa, args=(i+1, tempo))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
print("Fim da simulação")
