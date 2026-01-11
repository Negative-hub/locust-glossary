"""
Нагрузочное тестирование gRPC сервиса глоссария
Полностью самодостаточный файл
"""

import grpc
from locust import User, task, between, events
import random
import time

# Импортируем сгенерированный код gRPC
try:
    from generated import glossary_pb2, glossary_pb2_grpc
except ImportError:
    # Если generated нет, создаем заглушки для тестирования
    print("WARNING: Generated gRPC code not found. Using dummy classes.")
    
    class DummyProto:
        class GetAllTermsRequest:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
        
        class GetTermByIdRequest:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
        
        class SearchTermsRequest:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
        
        class CreateTermRequest:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)
    
    glossary_pb2 = DummyProto()

class GrpcGlossaryUser(User):
    """
    Пользователь gRPC сервиса глоссария.
    Тестируем 4 метода (2 легких, 1 средней сложности, 1 тяжелый)
    """
    
    wait_time = between(0.5, 2.5)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Создаем gRPC клиент
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = glossary_pb2_grpc.GlossaryServiceStub(self.channel)
        self.term_ids = list(range(1, 19))
    
    @task(4)  # 40% вероятность
    def get_all_terms(self):
        """GetAllTerms - получение всех терминов (легкий)"""
        request = glossary_pb2.GetAllTermsRequest(
            skip=random.randint(0, 5),
            limit=random.randint(5, 20),
            category=""
        )
        self._call_grpc_method("GetAllTerms", request)
    
    @task(3)  # 30% вероятность
    def get_term_by_id(self):
        """GetTermById - получение термина по ID (легкий)"""
        if self.term_ids:
            term_id = random.choice(self.term_ids)
            request = glossary_pb2.GetTermByIdRequest(id=term_id)
            self._call_grpc_method("GetTermById", request)
    
    @task(2)  # 20% вероятность
    def search_terms(self):
        """SearchTerms - поиск терминов (средней сложности)"""
        search_queries = ["kubernetes", "test", "monitor", "deploy", "code"]
        query = random.choice(search_queries)
        request = glossary_pb2.SearchTermsRequest(query=query)
        self._call_grpc_method("SearchTerms", request)
    
    @task(1)  # 10% вероятность
    def create_term(self):
        """CreateTerm - создание термина (тяжелый)"""
        request = glossary_pb2.CreateTermRequest(
            name=f"Grpc Test Term {int(time.time())}{random.randint(1, 1000)}",
            definition="Термин созданный во время нагрузочного тестирования gRPC",
            category=random.choice(["CI/CD", "gRPC", "Testing"]),
            source="Locust gRPC Load Test",
            related_terms=["test1", "test2"]
        )
        
        # Вызываем метод и обрабатываем ответ
        response = self._call_grpc_method("CreateTerm", request)
        if response and hasattr(response, 'term') and hasattr(response.term, 'id'):
            self.term_ids.append(response.term.id)
    
    def _call_grpc_method(self, method_name, request):
        """Обертка для вызова gRPC методов с измерением времени."""
        start_time = time.time()
        
        try:
            method = getattr(self.stub, method_name)
            response = method(request)
            
            total_time = int((time.time() - start_time) * 1000)
            
            # Отправляем метрику в Locust
            events.request.fire(
                request_type="grpc",
                name=method_name,
                response_time=total_time,
                response_length=0,
                exception=None,
                context={}
            )
            
            return response
            
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            
            events.request.fire(
                request_type="grpc",
                name=method_name,
                response_time=total_time,
                response_length=0,
                exception=e,
                context={}
            )
            
            raise e
    
    def on_stop(self):
        """Очистка при завершении"""
        self.channel.close()