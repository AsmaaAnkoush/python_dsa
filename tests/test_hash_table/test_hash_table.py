from src.hash_table.hash_table import Node, HashTable

def test_put():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")

    assert hash_table.size == 3

def test_get():
    hash_table: HashTable = HashTable()
    hash_table.put("name", "Asmaa")
    hash_table.put("age", 25)
    hash_table.put("university", "Birzeit")
    
    
    assert hash_table.get("age") == 25
    assert hash_table.get("name") == "Asmaa"

