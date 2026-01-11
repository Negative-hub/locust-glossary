"""
Нагрузочное тестирование REST API глоссария
Полностью самодостаточный файл - не требует дополнительных файлов
"""

from locust import HttpUser, task, between
import random
import time

class GlossaryUser(HttpUser):
    """
    Пользователь REST API глоссария.
    Тестируем 4 метода (2 легких, 1 средней сложности, 1 тяжелый)
    """
    
    wait_time = between(0.5, 2.5)  # Случайная пауза между запросами
    host = "http://localhost:8000"
    
    def on_start(self):
        """Действия при старте пользователя"""
        self.term_ids = list(range(1, 19))  # ID существующих терминов
        # Простые тестовые данные в коде
        self.test_terms = [
            {
                "name": "Test Term " + str(random.randint(1000, 9999)),
                "definition": "Тестовое определение для нагрузочного тестирования",
                "category": random.choice(["CI/CD", "Тестирование", "Инструменты"]),
                "source": "Load Test",
                "related_terms": ["термин1", "термин2"]
            }
        ]
    
    @task(4)  # 40% вероятность - легкий запрос
    def get_all_terms(self):
        """GET /api/v1/terms - получение всех терминов (легкий)"""
        params = {
            "skip": random.randint(0, 5),
            "limit": random.randint(5, 20),
        }
        with self.client.get("/api/v1/terms", params=params, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status {response.status_code}")
    
    @task(3)  # 30% вероятность - легкий запрос
    def get_term_by_id(self):
        """GET /api/v1/terms/{id} - получение термина по ID (легкий)"""
        if self.term_ids:
            term_id = random.choice(self.term_ids)
            with self.client.get(f"/api/v1/terms/{term_id}", catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Status {response.status_code}")
    
    @task(2)  # 20% вероятность - средний запрос
    def search_terms(self):
        """GET /api/v1/search - поиск терминов (средней сложности)"""
        search_queries = ["docker", "test", "автомат", "deploy", "code"]
        query = random.choice(search_queries)
        with self.client.get(f"/api/v1/search?q={query}", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status {response.status_code}")
    
    @task(1)  # 10% вероятность - тяжелый запрос
    def create_term(self):
        """POST /api/v1/terms - создание термина (тяжелый)"""
        term_data = {
            "name": f"Load Test Term {int(time.time())}{random.randint(1, 1000)}",
            "definition": "Термин созданный во время нагрузочного тестирования",
            "category": random.choice(["CI/CD", "DevOps", "Testing"]),
            "source": "Locust Load Test",
            "related_terms": []
        }
        
        headers = {"Content-Type": "application/json"}
        with self.client.post("/api/v1/terms", 
                             json=term_data, 
                             headers=headers, 
                             catch_response=True) as response:
            if response.status_code in [200, 201]:
                response.success()
                # Сохраняем ID созданного термина для последующих запросов
                try:
                    resp_data = response.json()
                    if "id" in resp_data:
                        self.term_ids.append(resp_data["id"])
                except:
                    pass
            else:
                response.failure(f"Status {response.status_code}")