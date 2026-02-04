class calculator:
    
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = (x * y for x, y in zip(V1, V2))
        result = sum(result)
        print(f"Dot product is: {result}")
        
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add vector is: {result}")
        
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous vector is: {result}")

