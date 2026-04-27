import threading
import time

def tarefa(thread_id, tempo_execucao):
 print(f"Thread {thread_id} iniciada (tempo {tempo_execucao})")
 time.sleep(tempo_execucao)
 print(f"Thread {thread_id} finalizada")
 
tempos = [5, 1, 3]
threads = []

for i, tempo in enumerate(tempos):
 t = threading.Thread(target=tarefa, args=(i+1, tempo))
 threads.append(t)
 t.start()
 
 for t in threads:
  t.join()
 
print("Simulação concluída")
